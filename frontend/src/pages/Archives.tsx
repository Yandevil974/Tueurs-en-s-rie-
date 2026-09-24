import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { Bi_, Empty, ErrorState, Loading, PageTitle, Reliability, useLang } from "../components/ui";

export default function Archives() {
  const lang = useLang();
  const [kind, setKind] = useState("");
  const [rel, setRel] = useState("");
  const [q, setQ] = useState("");
  const { data, loading, error, reload } = useApi<Any>(endpoints.archives(), [],);
  const items: Any[] = useMemo(() => (data?.items || []).filter((x: Any) => (!kind || x.kind === kind) && (!rel || x.reliability === rel) && (!q || `${pick(x.title, lang)} ${x.author} ${x.publisher} ${x.kind}`.toLowerCase().includes(q.toLowerCase()))), [data, kind, rel, q, lang]);
  return (
    <>
      <PageTitle eyebrow="🗂" title={tr(lang, "nav.archives")}>
        <p className="lede" style={{ margin: 0 }}>{lang === "fr" ? "Une bibliothèque de pièces documentaires : source, date, auteur, type, lien, fiabilité." : "A library of documentary records: source, date, author, type, link, reliability."}</p>
      </PageTitle>
      {data?.policy && <div className="disclaimer" style={{ marginBottom: 13 }}>{pick(data.policy, lang)}</div>}
      <div className="stack" style={{ gap: 8, marginBottom: 12 }}>
        <div className="field"><span>🔎</span><input value={q} onChange={(e) => setQ(e.target.value)} placeholder={lang === "fr" ? "Chercher dans les archives…" : "Search archives…"} /></div>
        <div className="tabs"><button className={`chip ${!kind ? "on" : ""}`} onClick={() => setKind("")}>{tr(lang, "common.all")}</button>{(data?.kinds || []).map((x: string) => <button key={x} className={`chip ${kind === x ? "on" : ""}`} onClick={() => setKind(x)}>{x}</button>)}</div>
        <div className="tabs"><button className={`chip ${!rel ? "on" : ""}`} onClick={() => setRel("")}>{tr(lang, "common.reliability")}</button>{(data?.levels || []).map((x: Any) => <button key={x.key} className={`chip ${rel === x.key ? "on" : ""}`} onClick={() => setRel(x.key)}><span className="dot" style={{ display: "inline-block", background: x.color }} />{pick(x.label, lang)}</button>)}</div>
      </div>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && <><div className="tiny" style={{ marginBottom: 9 }}>{items.length} / {data.count}</div><div className="stack">{items.map((x) => <article className="card" key={x.id}><div className="between"><div style={{ minWidth: 0 }}><div className="eyebrow blood">{x.kind} {x.case ? `· ${x.case}` : ""}</div><h2 className="h2" style={{ fontSize: 15, marginTop: 4 }}><Bi_ v={x.title} /></h2></div><Reliability level={x.reliability} /></div><div className="kv" style={{ marginTop: 9 }}><dt>{lang === "fr" ? "Auteur" : "Author"}</dt><dd>{x.author || "—"}</dd><dt>{lang === "fr" ? "Éditeur" : "Publisher"}</dt><dd>{x.publisher || "—"}</dd><dt>{tr(lang, "common.date")}</dt><dd className="mono">{x.date || "—"}</dd><dt>{tr(lang, "common.verified")}</dt><dd className="mono">{x.verified_at || "—"}</dd></div>{x.note && <div className="small" style={{ marginTop: 9 }}><Bi_ v={x.note} /></div>}{x.url && <a className="btn sm ghost" href={x.url} target="_blank" rel="noreferrer noopener" style={{ marginTop: 10 }}>{tr(lang, "common.link")} ↗</a>}{x.case && <Link className="tiny" style={{ display: "block", marginTop: 8, textDecoration: "underline" }} to={`/dossiers/${x.case}`}>{lang === "fr" ? "Ouvrir le dossier" : "Open dossier"} →</Link>}</article>)}{!items.length && <Empty />}</div></>}
    </>
  );
}
