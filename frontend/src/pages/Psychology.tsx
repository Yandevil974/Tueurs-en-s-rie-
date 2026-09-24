import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import CaseCard from "../components/CaseCard";
import { Bi_, ErrorState, Loading, PageTitle, useLang } from "../components/ui";

export default function Psychology() {
  const lang = useLang();
  const meta = useApp((s) => s.meta);
  const { data, loading, error, reload } = useApi<Any>(endpoints.cases());
  const types = meta?.case_types || [];
  const cases: Any[] = data?.cases || [];
  return (
    <>
      <PageTitle eyebrow="🧠" title={tr(lang, "nav.psychology")}>
        <p className="lede" style={{ margin: 0 }}>
          {lang === "fr"
            ? "Étudier des comportements documentés, le contexte et les biais d'interprétation. Jamais poser automatiquement un diagnostic."
            : "Study documented behaviour, context and interpretation biases. Never automatically diagnose."}
        </p>
      </PageTitle>
      <div className="disclaimer" style={{ marginBottom: 14 }}>
        {pick(meta?.disclaimers?.psychology, lang) ||
          (lang === "fr"
            ? "Aucune analyse de cette application ne constitue un diagnostic psychiatrique. Les faits, hypothèses, analyses d'experts et inconnues restent séparés."
            : "Nothing in this application constitutes a psychiatric diagnosis. Facts, hypotheses, expert analyses and unknowns remain separate.")}
      </div>
      <section className="card" style={{ marginBottom: 14 }}>
        <div className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "La grille de lecture" : "The reading grid"}</div>
        <div className="grid2">
          {["FAIT", "HYPOTHÈSE", "ANALYSE D'EXPERT", "INCONNU"].map((x, i) => (
            <div key={x} className="card tight">
              <div className="eyebrow blood">{["🟢", "🟡", "🟠", "⚪"][i]} {x}</div>
              <div className="tiny" style={{ marginTop: 5 }}>
                {lang === "fr"
                  ? ["Établi par une source", "Proposition prudente", "Position attribuée et sourcée", "Donnée absente ou insuffisante"][i]
                  : ["Established by a source", "Cautious proposition", "Attributed and sourced position", "Missing or insufficient data"][i]}
              </div>
            </div>
          ))}
        </div>
      </section>
      <div className="row wrap" style={{ gap: 8, marginBottom: 12 }}>
        <Link className="chip" to="/formation/glossaire">📖 {lang === "fr" ? "Glossaire" : "Glossary"}</Link>
        <Link className="chip" to="/formation">🎓 {tr(lang, "nav.training")}</Link>
      </div>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && (
        <>
          <div className="eyebrow" style={{ margin: "14px 0 8px" }}>{lang === "fr" ? "Dossiers comportant une analyse" : "Dossiers with an analysis"}</div>
          <div className="stack">
            {cases.filter((c) => c.tags?.some((t: string) => ["psychology", "behaviour", "profiling", "expert_analysis"].includes(t)) || c.stats?.psychology).map((c) => <CaseCard key={c.slug} c={c} />)}
          </div>
          {cases.length > 0 && cases.every((c) => !c.tags?.some((t: string) => ["psychology", "behaviour", "profiling", "expert_analysis"].includes(t)) && !c.stats?.psychology) && <div className="stack">{cases.slice(0, 4).map((c) => <CaseCard key={c.slug} c={c} />)}</div>}
        </>
      )}
    </>
  );
}
