import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { api, endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import CaseCard from "../components/CaseCard";
import { Bi_, ErrorState, Loading, PageTitle, TierBadge, useLang } from "../components/ui";

const OFFLINE_KEY = "yanisx.offline";

function readOffline(): Record<string, Any> {
  try {
    return JSON.parse(localStorage.getItem(OFFLINE_KEY) || "{}");
  } catch {
    return {};
  }
}

export default function Library() {
  const lang = useLang();
  const meta = useApp((s) => s.meta);
  const tier = useApp((s) => s.tier);
  const favourites = useApp((s) => s.favourites);
  const [filters, setFilters] = useState({ status: "", type: "", country: "", tag: "", sort: "editorial", q: "" });
  const [offline, setOffline] = useState<Record<string, Any>>(readOffline());
  const [busy, setBusy] = useState<string | null>(null);
  const { data, loading, error, reload } = useApi<Any>(endpoints.cases());

  const all: Any[] = data?.cases || [];
  const tags: string[] = data?.filters?.tags || [];

  const filtered = useMemo(() => {
    let rows = [...all];
    if (filters.status) rows = rows.filter((c) => c.status === filters.status);
    if (filters.type) rows = rows.filter((c) => c.type === filters.type);
    if (filters.country) rows = rows.filter((c) => c.country === filters.country);
    if (filters.tag) rows = rows.filter((c) => (c.tags || []).includes(filters.tag));
    if (filters.q) {
      const n = filters.q.toLowerCase();
      rows = rows.filter((c) => `${pick(c.title, "fr")} ${pick(c.title, "en")} ${c.region} ${c.city}`.toLowerCase().includes(n));
    }
    if (filters.sort === "recent") rows.sort((a, b) => (b.year_start || 0) - (a.year_start || 0));
    if (filters.sort === "oldest") rows.sort((a, b) => (a.year_start || 9999) - (b.year_start || 9999));
    if (filters.sort === "title") rows.sort((a, b) => pick(a.title, lang).localeCompare(pick(b.title, lang)));
    return rows;
  }, [all, filters, lang]);

  const favCases = all.filter((c) => favourites.includes(c.slug));

  const download = async (ep: Any) => {
    if (tier !== "PREMIUM") return;
    setBusy(String(ep.id));
    try {
      const full = await api.get<Any>(endpoints.episode(ep.id));
      const next = { ...readOffline(), [ep.id]: { id: ep.id, case_id: full.case_id, title: full.title, saved_at: new Date().toISOString(), payload: full } };
      localStorage.setItem(OFFLINE_KEY, JSON.stringify(next));
      setOffline(next);
    } finally {
      setBusy(null);
    }
  };

  const removeOffline = (id: string) => {
    const next = { ...readOffline() };
    delete next[id];
    localStorage.setItem(OFFLINE_KEY, JSON.stringify(next));
    setOffline(next);
  };

  const episodes: Any[] = data ? (data.cases || []).flatMap((c: Any) => []) : [];
  const { data: epData } = useApi<Any>(endpoints.episodes());

  useEffect(() => {
    /* rien à synchroniser : la liste des épisodes arrive par epData */
  }, [epData]);

  return (
    <>
      <PageTitle eyebrow="📚" title={tr(lang, "nav.library")}>
        <p className="small" style={{ marginTop: 0 }}>
          {lang === "fr"
            ? "Tous les dossiers, filtres, favoris et téléchargements hors ligne."
            : "All dossiers, filters, favourites and offline downloads."}
        </p>
      </PageTitle>

      {favCases.length > 0 && (
        <section className="block-sec">
          <h2 className="h3" style={{ marginBottom: 8 }}>★ {lang === "fr" ? "Mes favoris" : "My favourites"}</h2>
          <div className="stack">
            {favCases.map((c) => (
              <CaseCard key={c.slug} c={c} compact />
            ))}
          </div>
        </section>
      )}

      <section className="block-sec">
        <h2 className="h3" style={{ marginBottom: 8 }}>
          ⬇ {lang === "fr" ? "Hors ligne" : "Offline"}
        </h2>
        {tier !== "PREMIUM" ? (
          <div className="locked">
            <div style={{ fontSize: 22 }}>🔒</div>
            <div className="h2" style={{ fontSize: 14, margin: "8px 0 5px" }}>
              {lang === "fr" ? "Téléchargement réservé à l'abonnement" : "Download reserved for subscribers"}
            </div>
            <div className="small" style={{ marginBottom: 12 }}>
              {lang === "fr"
                ? "La mémoire des victimes, les chronologies et les sources restent en accès libre."
                : "Victim memory, chronologies and sources remain free."}
            </div>
            <Link className="btn sm primary" to="/compte">
              {tr(lang, "nav.account")} →
            </Link>
          </div>
        ) : Object.keys(offline).length === 0 ? (
          <div className="empty">{lang === "fr" ? "Aucun épisode téléchargé." : "No downloaded episode."}</div>
        ) : (
          <div className="stack">
            {Object.values(offline).map((o: Any) => (
              <div key={o.id} className="card tight">
                <div className="between">
                  <div style={{ minWidth: 0 }}>
                    <div className="h2" style={{ fontSize: 13.5 }}>
                      <Bi_ v={o.title} />
                    </div>
                    <div className="tiny mono">
                      {o.case_id} · {new Date(o.saved_at).toLocaleDateString(lang === "fr" ? "fr-FR" : "en-GB")}
                    </div>
                  </div>
                  <div className="row" style={{ gap: 6 }}>
                    <Link className="btn sm ghost" to={`/podcasts/${o.id}`}>
                      {tr(lang, "common.open")}
                    </Link>
                    <button className="iconbtn" style={{ width: 34, height: 34 }} onClick={() => removeOffline(String(o.id))} aria-label={lang === "fr" ? "Supprimer" : "Remove"}>
                      🗑
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {tier === "PREMIUM" && (
          <div className="stack" style={{ marginTop: 10 }}>
            {(epData?.episodes || []).map((ep: Any) => (
              <div key={ep.id} className="card tight">
                <div className="between">
                  <div style={{ minWidth: 0 }}>
                    <div className="h2" style={{ fontSize: 13 }}>
                      <Bi_ v={ep.title} />
                    </div>
                    <div className="tiny">{ep.case_id}</div>
                  </div>
                  <button className="btn sm" disabled={busy === String(ep.id) || Boolean(offline[ep.id])} onClick={() => download(ep)}>
                    {offline[ep.id] ? "✓" : busy === String(ep.id) ? "…" : "⬇"}
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      <hr className="rule" />

      <div className="stack" style={{ gap: 8, marginBottom: 12 }}>
        <div className="field">
          <span>🔎</span>
          <input value={filters.q} onChange={(e) => setFilters({ ...filters, q: e.target.value })} placeholder={lang === "fr" ? "Filtrer les dossiers…" : "Filter dossiers…"} />
        </div>
        <div className="tabs">
          <Chip on={filters.status === ""} onClick={() => setFilters({ ...filters, status: "" })}>{tr(lang, "common.all")}</Chip>
          {(meta?.statuses || []).map((s: Any) => (
            <Chip key={s.key} on={filters.status === s.key} onClick={() => setFilters({ ...filters, status: s.key })}>
              {pick(s.label, lang)}
            </Chip>
          ))}
        </div>
        <div className="tabs">
          <Chip on={filters.type === ""} onClick={() => setFilters({ ...filters, type: "" })}>{lang === "fr" ? "Tous types" : "All types"}</Chip>
          {(meta?.case_types || []).map((s: Any) => (
            <Chip key={s.key} on={filters.type === s.key} onClick={() => setFilters({ ...filters, type: s.key })}>
              {pick(s.label, lang)}
            </Chip>
          ))}
        </div>
        <div className="tabs">
          <Chip on={filters.country === ""} onClick={() => setFilters({ ...filters, country: "" })}>{lang === "fr" ? "Tous pays" : "All countries"}</Chip>
          {Array.from(new Set(all.map((c) => c.country))).map((co: any) => (
            <Chip key={co} on={filters.country === co} onClick={() => setFilters({ ...filters, country: co })}>
              {all.find((c) => c.country === co)?.country_name?.[lang] || co}
            </Chip>
          ))}
        </div>
        <div className="tabs">
          <Chip on={filters.tag === ""} onClick={() => setFilters({ ...filters, tag: "" })}>{lang === "fr" ? "Tous thèmes" : "All themes"}</Chip>
          {tags.map((t) => (
            <Chip key={t} on={filters.tag === t} onClick={() => setFilters({ ...filters, tag: t })}>
              {t.replace(/_/g, " ")}
            </Chip>
          ))}
        </div>
        <div className="tabs">
          <Chip on={filters.sort === "editorial"} onClick={() => setFilters({ ...filters, sort: "editorial" })}>{lang === "fr" ? "Ordre éditorial" : "Editorial order"}</Chip>
          <Chip on={filters.sort === "recent"} onClick={() => setFilters({ ...filters, sort: "recent" })}>{lang === "fr" ? "Plus récentes" : "Most recent"}</Chip>
          <Chip on={filters.sort === "oldest"} onClick={() => setFilters({ ...filters, sort: "oldest" })}>{lang === "fr" ? "Plus anciennes" : "Oldest"}</Chip>
          <Chip on={filters.sort === "title"} onClick={() => setFilters({ ...filters, sort: "title" })}>{lang === "fr" ? "A → Z" : "A → Z"}</Chip>
        </div>
      </div>

      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}

      <div className="stack">
        {filtered.map((c) => (
          <CaseCard key={c.slug} c={c} />
        ))}
        {!loading && filtered.length === 0 && (
          <div className="empty">{lang === "fr" ? "Aucun dossier ne correspond à ces filtres." : "No dossier matches these filters."}</div>
        )}
      </div>
      <div className="tiny" style={{ margin: "14px 0" }}>
        {filtered.length} / {all.length} · <TierBadge />
      </div>
    </>
  );
}

function Chip({ on, onClick, children }: { on: boolean; onClick: () => void; children: React.ReactNode }) {
  return (
    <button className={`chip ${on ? "on" : ""}`} aria-pressed={on} onClick={onClick}>
      {children}
    </button>
  );
}
