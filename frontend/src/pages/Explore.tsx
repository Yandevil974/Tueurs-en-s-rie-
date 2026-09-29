import { useState } from "react";
import { Link, useParams } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi, useLocal } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import CaseCard from "../components/CaseCard";
import WorldCaseMap from "../components/WorldCaseMap";
import { Bi_, Empty, ErrorState, Loading, PageTitle, StatusBadge, useLang } from "../components/ui";

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
export function CaseMap() {
  const lang = useLang();
  const casesRequest = useApi<Any>(endpoints.cases());
  const worldRequest = useApi<Any>(endpoints.world());
  const loading = casesRequest.loading || worldRequest.loading;

  return (
    <>
      <PageTitle eyebrow="🗺" title={tr(lang, "explore.map")}>
        <Link className="tiny" to="/explorer">← {tr(lang, "nav.explore")}</Link>
      </PageTitle>
      {(casesRequest.error || worldRequest.error) && (
        <ErrorState
          message={casesRequest.error || worldRequest.error || undefined}
          onRetry={() => { casesRequest.reload(); worldRequest.reload(); }}
        />
      )}
      <WorldCaseMap
        cases={casesRequest.data?.cases || []}
        continents={worldRequest.data?.continents || []}
        loading={loading}
      />
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
