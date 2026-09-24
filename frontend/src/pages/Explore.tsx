import { useState } from "react";
import { Link, useParams } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi, useLocal } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import CaseCard from "../components/CaseCard";
import { Bi_, Empty, ErrorState, Loading, PageTitle, Reliability, StatusBadge, useLang } from "../components/ui";

/* ------------------------------------------------------------- 🌍 monde */
export default function Explore() {
  const lang = useLang();
  const meta = useApp((s) => s.meta);
  const { data, loading, error, reload } = useApi<Any>(endpoints.world());
  return (
    <>
      <PageTitle eyebrow="🌍" title={tr(lang, "nav.explore")}>
        <p className="small" style={{ marginTop: 0 }}>
          {pick(meta?.explore?.drilldown, lang) || tr(lang, "explore.drill")}
        </p>
      </PageTitle>

      <div className="row wrap" style={{ gap: 8, marginBottom: 14 }}>
        <Link className="chip" to="/explorer/carte">🗺 {tr(lang, "explore.map")}</Link>
        <Link className="chip" to="/explorer/comparateur">⚖ {tr(lang, "explore.compare")}</Link>
      </div>

      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}

      {data && (
        <>
          <div className="card tight" style={{ marginBottom: 14 }}>
            <div className="between">
              <span className="eyebrow">{lang === "fr" ? "Monde" : "World"}</span>
              <span className="badge blood">{data.total_cases} {lang === "fr" ? "dossiers" : "dossiers"}</span>
            </div>
          </div>
          {data.continents.length === 0 && <Empty />}
          <div className="stack">
            {data.continents.map((c: Any) => (
              <Link key={c.name} to={`/explorer/continent/${encodeURIComponent(c.name)}`} className="card">
                <div className="between">
                  <div>
                    <div className="h2" style={{ fontSize: 15 }}>{c.name}</div>
                    <div className="tiny" style={{ marginTop: 4 }}>
                      {c.countries.map((x: Any) => `${x.flag} ${x.names[lang] || x.names.fr}`).join("  ·  ")}
                    </div>
                  </div>
                  <span className="badge">{c.cases}</span>
                </div>
              </Link>
            ))}
          </div>
        </>
      )}
    </>
  );
}

/* --------------------------------------------------------- continent */
export function ContinentPage() {
  const { continent = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.continent(continent), [continent]);
  return (
    <>
      <PageTitle eyebrow="🌍" title={decodeURIComponent(continent)}>
        <Link className="tiny" to="/explorer">← {tr(lang, "nav.explore")}</Link>
      </PageTitle>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && (
        <div className="stack">
          {data.countries.map((c: Any) => (
            <Link key={c.code} to={`/explorer/pays/${c.code}`} className="card tight">
              <div className="between">
                <span className="h2" style={{ fontSize: 14.5 }}>
                  {c.flag} {c.names[lang] || c.names.fr}
                </span>
                <span className="badge">{c.cases}</span>
              </div>
            </Link>
          ))}
          {data.countries.length === 0 && <Empty />}
        </div>
      )}
    </>
  );
}

/* ------------------------------------------------------------ pays */
export function CountryPage() {
  const { code = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.country(code), [code]);
  return (
    <>
      <PageTitle eyebrow={`🌍 ${data?.country?.continent || ""}`} title={<>{data?.country?.flag} {data?.country?.names?.[lang] || code}</>}>
        <Link className="tiny" to="/explorer">← {tr(lang, "nav.explore")}</Link>
      </PageTitle>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && (
        <>
          {data.regions.length > 0 && (
            <div className="tabs">
              {data.regions.map((r: Any) => (
                <Link key={r.name} className="chip" to={`/explorer/pays/${code}/region/${encodeURIComponent(r.name)}`}>
                  {r.name} ({r.cases})
                </Link>
              ))}
            </div>
          )}
          <div className="stack" style={{ marginTop: 8 }}>
            {data.cases.map((c: Any) => (
              <CaseCard key={c.slug} c={c} />
            ))}
            {data.cases.length === 0 && <Empty />}
          </div>
        </>
      )}
    </>
  );
}

/* ---------------------------------------------------------- région */
export function RegionPage() {
  const { code = "", region = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.region(code, region), [code, region]);
  return (
    <>
      <PageTitle eyebrow={`🌍 ${data?.country?.names?.[lang] || code}`} title={decodeURIComponent(region)}>
        <Link className="tiny" to={`/explorer/pays/${code}`}>← {data?.country?.names?.[lang] || code}</Link>
      </PageTitle>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && (
        <>
          {data.cities.length > 0 && (
            <div className="tabs">
              {data.cities.map((c: Any) => (
                <Link key={c.name} className="chip" to={`/explorer/pays/${code}/ville/${encodeURIComponent(c.name)}`}>
                  {c.name} ({c.cases})
                </Link>
              ))}
            </div>
          )}
          <div className="stack" style={{ marginTop: 8 }}>
            {data.cases.map((c: Any) => (
              <CaseCard key={c.slug} c={c} />
            ))}
            {data.cases.length === 0 && <Empty />}
          </div>
        </>
      )}
    </>
  );
}

/* ------------------------------------------------------------ ville */
export function CityPage() {
  const { code = "", city = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.city(code, city), [code, city]);
  return (
    <>
      <PageTitle eyebrow={`🌍 ${data?.country?.names?.[lang] || code}`} title={decodeURIComponent(city)}>
        <Link className="tiny" to={`/explorer/pays/${code}`}>← {data?.country?.names?.[lang] || code}</Link>
      </PageTitle>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && (
        <>
          <div className="note neutral" style={{ marginBottom: 12 }}>{pick(data.no_exact_address, lang)}</div>
          <div className="stack">
            {data.cases.map((c: Any) => (
              <CaseCard key={c.slug} c={c} />
            ))}
            {data.cases.length === 0 && <Empty />}
          </div>
        </>
      )}
    </>
  );
}

/* ------------------------------------------------------- 🗺 carte */
const W = 720;
const H = 360;
const proj = (lat: number, lon: number) => ({ x: ((lon + 180) / 360) * W, y: ((90 - lat) / 180) * H });

export function CaseMap() {
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.map());
  const [sel, setSel] = useState<Any | null>(null);
  const points: Any[] = (data?.case_points || []).filter((p: Any) => p.lat != null && p.lon != null);
  const places: Any[] = data?.locations || [];

  return (
    <>
      <PageTitle eyebrow="🗺" title={tr(lang, "explore.map")}>
        <Link className="tiny" to="/explorer">← {tr(lang, "nav.explore")}</Link>
      </PageTitle>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && (
        <>
          <div className="note neutral" style={{ marginBottom: 12 }}>{pick(data.no_exact_address, lang)}</div>
          <svg className="map" viewBox={`0 0 ${W} ${H}`} role="img" aria-label={tr(lang, "explore.map")}>
            <rect width={W} height={H} fill="#0c0e12" />
            <g stroke="#1c2027" strokeWidth="0.6">
              {Array.from({ length: 13 }).map((_, i) => (
                <line key={`m${i}`} x1={(i * W) / 12} y1="0" x2={(i * W) / 12} y2={H} />
              ))}
              {Array.from({ length: 7 }).map((_, i) => (
                <line key={`p${i}`} x1="0" y1={(i * H) / 6} x2={W} y2={(i * H) / 6} />
              ))}
            </g>
            <line x1="0" y1={H / 2} x2={W} y2={H / 2} stroke="#2b3138" strokeWidth="1" strokeDasharray="4 4" />
            <text x="8" y={H / 2 - 6} fill="#5c636c" fontSize="9" fontFamily="monospace">0°</text>
            {points.map((p) => {
              const { x, y } = proj(p.lat, p.lon);
              const color = p.status === "RESOLVED" ? "#3f9e63" : p.status === "UNSOLVED" ? "#c2603a" : "#c9a227";
              return (
                <g key={p.slug} className="pin" onClick={() => setSel(p)}>
                  <circle cx={x} cy={y} r="10" fill={color} opacity="0.14" />
                  <circle cx={x} cy={y} r="4" fill={color} stroke="#0b0c0e" strokeWidth="1" />
                </g>
              );
            })}
            {places.filter((l) => l.lat != null).map((l, i) => {
              const { x, y } = proj(l.lat, l.lon);
              return <circle key={i} cx={x} cy={y} r="1.8" fill="#e8e4dc" opacity="0.5" />;
            })}
          </svg>
          <div className="tiny" style={{ margin: "8px 0 14px" }}>
            {lang === "fr"
              ? "Projection équirectangulaire schématique. Les points sont les dossiers ; les petites marques, les lieux documentés."
              : "Schematic equirectangular projection. Dots are dossiers; small marks are documented places."}
          </div>

          {sel && (
            <div className="card" style={{ marginBottom: 12 }}>
              <div className="h2" style={{ fontSize: 15, marginBottom: 6 }}>
                <Bi_ v={sel.title} />
              </div>
              <div className="row wrap" style={{ gap: 6 }}>
                <StatusBadge status={sel.status} />
                <span className="badge">{sel.country}</span>
                <span className="tiny mono">
                  {sel.lat?.toFixed(2)}, {sel.lon?.toFixed(2)}
                </span>
              </div>
              <Link className="btn sm primary" style={{ marginTop: 11 }} to={`/dossiers/${sel.slug}`}>
                {tr(lang, "common.open")} →
              </Link>
            </div>
          )}

          <div className="stack">
            {places.map((l) => (
              <div key={l.id} className="card tight">
                <div className="between">
                  <div style={{ minWidth: 0 }}>
                    <div className="h2" style={{ fontSize: 13.5 }}>
                      <Bi_ v={l.names} />
                    </div>
                    <div className="tiny">
                      {l.city} {l.region ? `· ${l.region}` : ""} · {l.country} · {l.kind} · {l.date}
                    </div>
                  </div>
                  <Reliability level={l.reliability} />
                </div>
                {l.note && (l.note.fr || l.note.en) && (
                  <div className="small" style={{ marginTop: 6 }}>
                    <Bi_ v={l.note} />
                  </div>
                )}
                <Link className="tiny" style={{ display: "inline-block", marginTop: 7, textDecoration: "underline" }} to={`/dossiers/${l.case_id}`}>
                  {l.case_id} →
                </Link>
              </div>
            ))}
          </div>
        </>
      )}
    </>
  );
}

/* ------------------------------------------------- ⚖ comparateur */
export function Comparator() {
  const lang = useLang();
  const [picked, setPicked] = useLocal<string[]>("yanisx.compare", []);
  const cases = useApi<Any>(endpoints.cases());
  const compare = useApi<Any>(picked.length >= 2 ? endpoints.compare(picked) : null, [picked.join(",")]);

  const toggle = (slug: string) =>
    setPicked(picked.includes(slug) ? picked.filter((s) => s !== slug) : picked.length >= 4 ? picked : [...picked, slug]);

  const rows = compare.data?.cases || [];
  const axes: [string, (c: Any) => React.ReactNode][] = [
    ["case.period", (c) => <Bi_ v={c.period} />],
    ["case.country", (c) => <Bi_ v={c.country} />],
    ["case.status", (c) => <StatusBadge status={c.status} />],
    ["victim.count", (c) => c.victims_documented],
    ["victim.named", (c) => c.victims_named],
    ["case.investigation", (c) => c.investigation_steps],
    ["cold.unknowns", (c) => c.cold_case_unknowns],
    ["case.justice", (c) => <Bi_ v={c.sentence_label} />],
    ["common.sources", (c) => c.sources],
    ["case.whatif", (c) => c.counterfactuals],
    ["podcasts", (c) => c.episodes],
    ["case.lessons", (c) => c.lessons],
  ];

  return (
    <>
      <PageTitle eyebrow="⚖" title={tr(lang, "explore.compare")}>
        <Link className="tiny" to="/explorer">← {tr(lang, "nav.explore")}</Link>
        <div className="note warn" style={{ marginTop: 10 }}>
          {lang === "fr"
            ? "Comparaison descriptive uniquement. Aucun classement par dangerosité, intelligence ou nombre de victimes n'est proposé."
            : "Descriptive comparison only. No ranking by dangerousness, intelligence or victim count is offered."}
        </div>
      </PageTitle>

      <div className="tabs">
        {(cases.data?.cases || []).map((c: Any) => (
          <button key={c.slug} className={`chip ${picked.includes(c.slug) ? "on" : ""}`} aria-pressed={picked.includes(c.slug)} onClick={() => toggle(c.slug)}>
            {pick(c.title, lang).slice(0, 34)}
          </button>
        ))}
      </div>
      <div className="tiny" style={{ marginBottom: 12 }}>
        {picked.length}/4 · {lang === "fr" ? "sélectionne au moins deux dossiers" : "select at least two dossiers"}
      </div>

      {compare.loading && <Loading />}
      {compare.error && <ErrorState message={compare.error} onRetry={compare.reload} />}

      {rows.length > 0 && (
        <div className="tablewrap">
          <table className="tbl">
            <thead>
              <tr>
                <th></th>
                {rows.map((c: Any) => (
                  <th key={c.id}>
                    <Link to={`/dossiers/${c.id}`}>{pick(c.title, lang).slice(0, 26)}</Link>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {axes.map(([k, fn]) => (
                <tr key={k}>
                  <td className="eyebrow" style={{ whiteSpace: "nowrap" }}>{tr(lang, k)}</td>
                  {rows.map((c: Any) => (
                    <td key={c.id}>{fn(c)}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </>
  );
}
