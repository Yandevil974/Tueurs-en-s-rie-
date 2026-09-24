import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import CaseCard from "../components/CaseCard";
import { Bi_, ErrorState, Loading, PageTitle, useLang } from "../components/ui";

export default function ColdCases() {
  const lang = useLang();
  const [mode, setMode] = useState<"all" | "unresolved" | "ongoing">("all");
  const { data, loading, error, reload } = useApi<Any>(endpoints.cases());
  const cases: Any[] = data?.cases || [];
  const cold = useMemo(() => {
    const rows = cases.filter((c) => ["UNSOLVED", "ONGOING", "PARTIALLY_RESOLVED"].includes(c.status) || c.tags?.includes("cold_case"));
    if (mode === "unresolved") return rows.filter((c) => c.status === "UNSOLVED");
    if (mode === "ongoing") return rows.filter((c) => ["ONGOING", "PARTIALLY_RESOLVED"].includes(c.status));
    return rows;
  }, [cases, mode]);
  return (
    <>
      <PageTitle eyebrow="❄️" title={tr(lang, "nav.coldcases")}>
        <p className="lede" style={{ margin: 0 }}>
          {lang === "fr"
            ? "Ce que l'on sait, ce qui est probable, ce qui est contesté, ce qui reste inconnu — sans transformer une absence de réponse en récit."
            : "What is known, probable, disputed and unknown — without turning an absence of answers into a story."}
        </p>
      </PageTitle>
      <div className="note neutral" style={{ marginBottom: 13 }}>
        {lang === "fr"
          ? "Chaque dossier peut distinguer : CE QUE L'ON SAIT · PROBABLE · CONTESTÉ · INCONNU · DERNIÈRES AVANCÉES · PISTES · PREUVES · LIMITES."
          : "Each dossier can distinguish: KNOWN · PROBABLE · DISPUTED · UNKNOWN · LATEST DEVELOPMENTS · LEADS · EVIDENCE · LIMITS."}
      </div>
      <div className="tabs">
        <button className={`chip ${mode === "all" ? "on" : ""}`} onClick={() => setMode("all")}>{tr(lang, "common.all")}</button>
        <button className={`chip ${mode === "unresolved" ? "on" : ""}`} onClick={() => setMode("unresolved")}>{lang === "fr" ? "Non résolues" : "Unsolved"}</button>
        <button className={`chip ${mode === "ongoing" ? "on" : ""}`} onClick={() => setMode("ongoing")}>{lang === "fr" ? "En cours / partielles" : "Ongoing / partial"}</button>
      </div>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && (
        <>
          <div className="tiny" style={{ margin: "10px 0" }}>{cold.length} {lang === "fr" ? "dossier(s)" : "dossier(s)"}</div>
          <div className="stack">
            {cold.map((c) => <CaseCard key={c.slug} c={c} />)}
            {!cold.length && <div className="empty">{lang === "fr" ? "Aucun dossier dans ce filtre." : "No dossier in this filter."}</div>}
          </div>
        </>
      )}
      <Link className="card" style={{ display: "block", marginTop: 14 }} to="/archives">
        <div className="eyebrow blood">🗂 {tr(lang, "nav.archives")}</div>
        <div className="h2" style={{ fontSize: 14, marginTop: 5 }}>{lang === "fr" ? "Consulter les pièces et leurs limites" : "Consult the records and their limits"} →</div>
      </Link>
    </>
  );
}
