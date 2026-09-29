import type { Any } from "./api";

type EmbeddedBundle = {
  api: Record<string, Any>;
  compareRows: Record<string, Any>;
  compareMetadata: Any;
  questionAnswers: Record<string, Any>;
};

let bundlePromise: Promise<EmbeddedBundle> | null = null;

function loadBundle() {
  if (!bundlePromise) {
    bundlePromise = import("../data_embedded/index.json").then((module) => module.default as EmbeddedBundle);
  }
  return bundlePromise;
}

function flatten(value: unknown): string {
  if (value == null) return "";
  if (typeof value === "string" || typeof value === "number") return String(value);
  if (Array.isArray(value)) return value.map(flatten).join(" ");
  if (typeof value === "object") return Object.values(value as Record<string, unknown>).map(flatten).join(" ");
  return String(value);
}

function normalize(value: string) {
  return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

function filtered<T extends Any>(rows: T[], test: (row: T) => boolean) {
  return rows.filter(test);
}

function searchEmbedded(bundle: EmbeddedBundle, query: string) {
  const needle = normalize(query.trim());
  const tokens = needle.match(/[\w'-]{2,}/g) || [];
  const fallbackTokens = tokens.length ? tokens : (needle ? [needle] : []);
  if (!fallbackTokens.length) return { query, count: 0, total: 0, results: [], facets: {} };

  const results: Any[] = [];
  const add = (result: Any, searchable: unknown) => {
    const haystack = normalize(flatten(searchable));
    const score = fallbackTokens.reduce((sum, token) => {
      let occurrences = 0;
      let index = 0;
      while ((index = haystack.indexOf(token, index)) !== -1) {
        occurrences += 1;
        index += token.length;
      }
      return sum + occurrences * 3;
    }, 0);
    if (score) results.push({ ...result, score });
  };

  const cases: Any[] = bundle.api["/cases"]?.cases || [];
  for (const dossier of cases) {
    add({
      type: "case", label: dossier.title, context: dossier.period_label,
      href: `/dossiers/${dossier.slug}`, data: dossier,
    }, [dossier.title, dossier.subtitle, dossier.summary, dossier.region, dossier.city, dossier.tags]);

    const victims: Any[] = bundle.api[`/cases/${dossier.slug}/victims`]?.victims || [];
    for (const victim of victims) {
      const name = `${victim.first_name || ""} ${victim.last_name || ""}`.trim();
      add({
        type: "victim", label: { fr: name, en: name },
        context: victim.life?.fr?.headline || "",
        href: `/dossiers/${dossier.slug}/victimes#${victim.id}`,
        data: { id: victim.id, case: dossier.slug, age: victim.age, reliability: victim.reliability },
      }, [name, victim.life, victim.disappearance, victim.note]);
    }

    const timeline: Any[] = bundle.api[`/cases/${dossier.slug}/timeline`]?.events || [];
    for (const event of timeline) {
      add({
        type: "timeline", label: event.title || { fr: event.date, en: event.date },
        context: { fr: event.date, en: event.date }, href: `/dossiers/${dossier.slug}/chronologie`,
        data: { id: event.id, case: dossier.slug, date: event.date, reliability: event.reliability },
      }, [event.title, event.body]);
    }

    const sourceRows: Any[] = bundle.api[`/cases/${dossier.slug}/sources`]?.sources || [];
    for (const source of sourceRows) {
      add({
        type: "source", label: source.title,
        context: { fr: source.publisher, en: source.publisher },
        href: `/dossiers/${dossier.slug}/sources`,
        data: { id: source.id, url: source.url, reliability: source.reliability, verified_at: source.verified_at },
      }, [source.title, source.publisher, source.author, source.note]);
    }

    const evidenceRows: Any[] = bundle.api[`/cases/${dossier.slug}/evidence`]?.evidence || [];
    for (const evidence of evidenceRows) {
      add({
        type: "evidence", label: evidence.title, context: evidence.description,
        href: `/dossiers/${dossier.slug}/indices`,
        data: { id: evidence.id, kind: evidence.kind, reliability: evidence.reliability },
      }, [evidence.title, evidence.description]);
    }

    const expertRows: Any[] = bundle.api[`/cases/${dossier.slug}/experts`]?.experts || [];
    for (const expert of expertRows) {
      add({
        type: "expert", label: expert.label, context: expert.position,
        href: `/dossiers/${dossier.slug}`, data: { id: expert.id, field: expert.field },
      }, [expert.label, expert.position]);
    }
  }

  for (const entry of bundle.api["/glossary"]?.entries || []) {
    add({
      type: "glossary", label: entry.term, context: entry.simple,
      href: `/formation/glossaire/${entry.slug}`, data: { slug: entry.slug, field: entry.field },
    }, [entry.term, entry.simple, entry.deep]);
  }
  for (const course of bundle.api["/courses"]?.courses || []) {
    add({
      type: "course", label: course.title, context: course.intro,
      href: `/formation/${course.slug}`, data: { slug: course.slug, field: course.field },
    }, [course.title, course.intro, course.lessons]);
  }
  for (const episode of bundle.api["/episodes"]?.episodes || []) {
    add({
      type: "episode", label: episode.title, context: episode.description,
      href: `/podcasts/${episode.id}`,
      data: { id: episode.id, case: episode.case_id, modes: episode.modes, duration_sec: episode.duration_sec },
    }, [episode.title, episode.description, bundle.api[`/episodes/${episode.id}`]?.transcript]);
  }

  results.sort((a, b) => b.score - a.score);
  const limit = 20;
  const facets: Record<string, number> = {};
  for (const result of results) facets[result.type] = (facets[result.type] || 0) + 1;
  return { query, count: Math.min(limit, results.length), total: results.length, results: results.slice(0, limit), facets };
}

export async function getEmbeddedPayload(path: string, init: RequestInit = {}): Promise<Any | undefined> {
  const bundle = await loadBundle();
  const url = new URL(path, "https://yanisx-offline.invalid");
  let pathname: string;
  try {
    pathname = decodeURIComponent(url.pathname);
  } catch {
    pathname = url.pathname;
  }
  const payload = bundle.api[pathname];
  const method = (init.method || "GET").toUpperCase();
  const queryRoutes = new Set(["/cases", "/episodes", "/counterfactuals", "/glossary", "/memory"]);

  if (method === "POST") {
    if (pathname === "/analyst") {
      let body: Any = {};
      try { body = JSON.parse(String(init.body || "{}")); } catch { /* use empty payload */ }
      const meta = bundle.api["/meta"] || {};
      return {
        question: String(body.question || ""),
        answer: meta.disclaimers?.insufficient_data || {
          fr: "Cette information n'est pas suffisamment documentée.",
          en: "This information is not sufficiently documented.",
        },
        documented: false,
        extracts: [],
        levels: meta.reliability || [],
      };
    }
    const answerMatch = pathname.match(/^\/questions\/(\d+)\/answer$/);
    if (answerMatch) {
      const savedByChoice = bundle.questionAnswers[answerMatch[1]];
      if (!savedByChoice) return undefined;
      let body: Any = {};
      try { body = JSON.parse(String(init.body || "{}")); } catch { /* use empty payload */ }
      const choice = String(body.choice || "");
      const saved = savedByChoice[choice];
      return saved ? { ...saved, choice } : undefined;
    }
    return undefined;
  }

  if (method !== "GET") return undefined;
  if (payload !== undefined && (!url.search || !queryRoutes.has(pathname))) return payload;

  const params = url.searchParams;
  if (pathname === "/cases") {
    let rows: Any[] = bundle.api["/cases"]?.cases || [];
    const country = params.get("country")?.toUpperCase();
    const status = params.get("status")?.toUpperCase();
    const type = params.get("type");
    const tag = params.get("tag");
    const decade = Number(params.get("decade") || 0);
    const query = normalize(params.get("q") || "");
    rows = filtered(rows, (row) => {
      if (country && row.country !== country) return false;
      if (status && row.status !== status) return false;
      if (type && row.type !== type) return false;
      if (tag && !(row.tags || []).includes(tag)) return false;
      if (decade && Math.floor(Number(row.year_start || 0) / 10) * 10 !== decade) return false;
      if (query && !normalize(flatten([row.title, row.subtitle, row.summary, row.region, row.city, row.tags])).includes(query)) return false;
      return true;
    });
    return { ...bundle.api["/cases"], count: rows.length, cases: rows };
  }

  if (pathname === "/episodes") {
    let rows: Any[] = bundle.api["/episodes"]?.episodes || [];
    const caseId = params.get("case");
    const mode = params.get("mode");
    rows = filtered(rows, (row) => (!caseId || row.case_id === caseId) && (!mode || (row.modes || []).includes(mode)));
    return { ...bundle.api["/episodes"], count: rows.length, episodes: rows };
  }

  if (pathname === "/counterfactuals") {
    let rows: Any[] = bundle.api["/counterfactuals"]?.items || [];
    const caseId = params.get("case");
    const kind = params.get("kind");
    rows = filtered(rows, (row) => (!caseId || row.case_id === caseId) && (!kind || row.kind === kind));
    return { ...bundle.api["/counterfactuals"], count: rows.length, items: rows };
  }

  if (pathname === "/glossary") {
    let rows: Any[] = bundle.api["/glossary"]?.entries || [];
    const field = params.get("field");
    const query = normalize(params.get("q") || "");
    rows = filtered(rows, (row) => (!field || row.field === field) && (!query || normalize(flatten([row.term, row.simple, row.deep])).includes(query)));
    return { ...bundle.api["/glossary"], count: rows.length, entries: rows };
  }

  if (pathname === "/memory" && params.has("country")) {
    const country = (params.get("country") || "").toUpperCase();
    const groups = filtered(bundle.api["/memory"]?.groups || [], (group) => group.case?.country === country);
    const victims = groups.flatMap((group: Any) => group.victims || []);
    const named = victims.filter((victim: Any) => !victim.anonymised && victim.last_name).length;
    return {
      ...bundle.api["/memory"],
      groups,
      counts: { cases: groups.length, victims: victims.length, named, not_documented: victims.length - named },
    };
  }

  const continentMatch = pathname.match(/^\/explore\/continent\/(.+)$/);
  if (continentMatch) {
    const requested = normalize(continentMatch[1]);
    const continent = (bundle.api["/explore"]?.continents || []).find((row: Any) => normalize(row.name || "") === requested);
    if (!continent) return undefined;
    return { level: "continent", continent: continent.name, countries: continent.countries, next: "/explore/country/{code}" };
  }

  if (pathname === "/explore/compare") {
    const ids = (params.get("ids") || "").split(",").map((id) => id.trim()).filter(Boolean).slice(0, 4);
    const rows = ids.map((id) => bundle.compareRows[id]).filter(Boolean);
    return { cases: rows, ...bundle.compareMetadata };
  }

  if (pathname === "/search") return searchEmbedded(bundle, params.get("q") || "");
  return undefined;
}
