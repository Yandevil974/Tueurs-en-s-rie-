import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { Bi_, ErrorState, Loading, PageTitle, useLang } from "../components/ui";

export default function Ethics() {
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.ethics());
  return (
    <>
      <PageTitle eyebrow="⚖" title={tr(lang, "nav.ethics")}>
        <p className="lede" style={{ margin: 0 }}>{lang === "fr" ? "La charte qui guide chaque dossier, chaque interface et chaque choix éditorial." : "The charter guiding every dossier, interface and editorial choice."}</p>
      </PageTitle>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && <>
        <div className="card" style={{ marginBottom: 13 }}><div className="eyebrow blood">{pick(data.app?.name, lang)}</div><h2 className="h2" style={{ margin: "7px 0" }}>{pick(data.app?.tagline, lang)}</h2><p className="small" style={{ margin: 0 }}>{pick(data.gamification, lang)}</p></div>
        <div className="stack">{(data.rules || []).map((r: Any, i: number) => <article className="card" key={i}><div className="eyebrow blood">{String(i + 1).padStart(2, "0")}</div><div style={{ marginTop: 6, color: "var(--bone-dim)", fontSize: 15 }}>{typeof r === "object" ? <Bi_ v={r} /> : String(r)}</div></article>)}</div>
        <section className="block-sec"><div className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Disclaimers permanents" : "Permanent disclaimers"}</div><div className="stack"><div className="disclaimer"><Bi_ v={data.disclaimers?.counterfactual} /></div><div className="disclaimer"><Bi_ v={data.disclaimers?.psychology} /></div><div className="disclaimer"><Bi_ v={data.disclaimers?.victimology} /></div></div></section>
        <Link className="card" style={{ display: "block", marginBottom: 14 }} to="/compte"><div className="eyebrow blood">♿ {lang === "fr" ? "Accessibilité" : "Accessibility"}</div><div className="h2" style={{ fontSize: 14, marginTop: 5 }}>{lang === "fr" ? "Taille de texte, contraste, mouvement, transcription" : "Text size, contrast, motion, transcript"} →</div></Link>
      </>}
    </>
  );
}
