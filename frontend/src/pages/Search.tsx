import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { tr } from "../lib/i18n";
import CaseCard from "../components/CaseCard";
import { Bi_, Empty, ErrorState, Loading, PageTitle, Reliability, useLang } from "../components/ui";

const TYPES: Record<string, { fr: string; en: string; ico: string }> = {
  case: { fr: "Dossier", en: "Dossier", ico: "📁" },
  victim: { fr: "Victime", en: "Victim", ico: "🕯" },
  timeline: { fr: "Chronologie", en: "Chronology", ico: "🗓" },
  source: { fr: "Source", en: "Source", ico: "📎" },
  glossary: { fr: "Glossaire", en: "Glossary", ico: "📖" },
  course: { fr: "Formation", en: "Course", ico: "🎓" },
  episode: { fr: "Épisode", en: "Episode", ico: "🎧" },
  evidence: { fr: "Indice", en: "Evidence", ico: "🔍" },
  expert: { fr: "Expert", en: "Expert", ico: "🧠" },
};

export default function Search() {
  const lang = useLang();
  const [q, setQ] = useState("");
  const [submitted, setSubmitted] = useState("");
  const [type, setType] = useState<string>("all");
  const { data, loading, error, reload } = useApi<Any>(submitted ? endpoints.search(submitted) : null, [submitted]);

  useEffect(() => {
    const id = setTimeout(() => {
      if (q.trim().length >= 2) setSubmitted(q.trim());
    }, 380);
    return () => clearTimeout(id);
  }, [q]);

  const results: Any[] = (data?.results || []).filter((r: Any) => type === "all" || r.type === type);
  const facets: Any = data?.facets || {};

  return (
    <>
      <PageTitle eyebrow="🔎" title={tr(lang, "nav.search")}>
        <p className="small" style={{ marginTop: 0 }}>
          {lang === "fr"
            ? "Recherche dans les dossiers, les victimes, les chronologies, les sources, les épisodes, les indices, le glossaire et les formations."
            : "Search across dossiers, victims, chronologies, sources, episodes, evidence, glossary and courses."}
        </p>
      </PageTitle>

      <form
        className="field"
        onSubmit={(e) => {
          e.preventDefault();
          setSubmitted(q.trim());
        }}
      >
        <span>🔎</span>
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder={lang === "fr" ? "Nom, lieu, année, notion…" : "Name, place, year, concept…"}
          aria-label={tr(lang, "nav.search")}
          autoFocus
        />
        {q && (
          <button type="button" className="iconbtn" style={{ width: 30, height: 30 }} onClick={() => { setQ(""); setSubmitted(""); }} aria-label={tr(lang, "common.close")}>
            ✕
          </button>
        )}
      </form>

      {data && (
        <div className="tabs" style={{ marginTop: 12 }}>
          <button className={`chip ${type === "all" ? "on" : ""}`} onClick={() => setType("all")} aria-pressed={type === "all"}>
            {tr(lang, "common.all")} ({data.total})
          </button>
          {Object.entries(facets).map(([k, v]) => (
            <button key={k} className={`chip ${type === k ? "on" : ""}`} onClick={() => setType(k)} aria-pressed={type === k}>
              {TYPES[k]?.[lang] || k} ({v})
            </button>
          ))}
        </div>
      )}

      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}

      {data && !loading && (
        <div className="stack" style={{ marginTop: 6 }}>
          {results.length === 0 && <Empty>{lang === "fr" ? "Aucun résultat documenté pour cette recherche." : "No documented result for this search."}</Empty>}

          {results.map((r, i) =>
            r.type === "case" ? (
              <CaseCard key={i} c={r.data} compact />
            ) : (
              <Link key={i} to={r.href} className="card tight">
                <div className="row wrap" style={{ gap: 6, marginBottom: 5 }}>
                  <span className="badge">
                    {TYPES[r.type]?.ico} {TYPES[r.type]?.[lang] || r.type}
                  </span>
                  {r.data?.reliability && <Reliability level={r.data.reliability} />}
                  {r.data?.date && <span className="tiny mono">{r.data.date}</span>}
                </div>
                <div className="h2" style={{ fontSize: 14 }}>
                  <Bi_ v={r.label} />
                </div>
                {r.context && (
                  <div className="small" style={{ marginTop: 3, overflow: "hidden", display: "-webkit-box", WebkitLineClamp: 2, WebkitBoxOrient: "vertical" }}>
                    {typeof r.context === "object" ? <Bi_ v={r.context} /> : String(r.context)}
                  </div>
                )}
                {r.type === "source" && r.data?.url && (
                  <div className="tiny" style={{ marginTop: 6 }}>
                    {r.data.url.replace(/^https?:\/\//, "").slice(0, 58)}…
                  </div>
                )}
              </Link>
            ),
          )}
        </div>
      )}
    </>
  );
}
