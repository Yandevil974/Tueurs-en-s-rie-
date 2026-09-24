import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { tr } from "../lib/i18n";
import CaseCard from "../components/CaseCard";
import { Bi_, ErrorState, Loading, PageTitle, useLang } from "../components/ui";

export default function Investigations() {
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.cases());
  const cases: Any[] = data?.cases || [];
  return (
    <>
      <PageTitle eyebrow="🔎" title={tr(lang, "nav.investigations")}>
        <p className="lede" style={{ margin: 0 }}>
          {lang === "fr"
            ? "Reconstituer une enquête comme une suite de décisions, de pistes, de preuves et d'erreurs — sans regarder le passé avec les informations du présent."
            : "Reconstruct an investigation as a sequence of decisions, leads, evidence and errors — without looking back with today's information."}
        </p>
      </PageTitle>
      <div className="note neutral" style={{ marginBottom: 14 }}>
        {lang === "fr"
          ? "Le Mode Enquête révèle : disparition → témoignage → premier indice → nouvelle piste → élément scientifique → arrestation. Les étapes verrouillées restent visibles comme telles."
          : "Investigation Mode reveals: disappearance → testimony → first clue → new lead → scientific element → arrest. Locked steps remain visible as locked."}
      </div>
      <div className="row wrap" style={{ gap: 8, marginBottom: 14 }}>
        <Link className="chip" to="/archives">🗂 {tr(lang, "nav.archives")}</Link>
        <Link className="chip" to="/explorer/comparateur">⚖ {tr(lang, "explore.compare")}</Link>
      </div>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && (
        <div className="stack">
          {cases.map((c) => (
            <article key={c.slug}>
              <CaseCard c={c} />
              <Link className="btn sm ghost" style={{ margin: "6px 0 4px 10px" }} to={`/dossiers/${c.slug}/enquete`}>
                🔎 {lang === "fr" ? "Ouvrir le fil de l'enquête" : "Open investigation thread"} →
              </Link>
            </article>
          ))}
        </div>
      )}
      {data && cases.length === 0 && <div className="empty"><Bi_ v={{ fr: "Aucun dossier d'enquête disponible.", en: "No investigation dossier available." }} /></div>}
    </>
  );
}
