import { useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import CaseCard from "../components/CaseCard";
import { Bi_, ErrorState, Empty, Item, Items, Loading, PageTitle, TierBadge, useLang } from "../components/ui";

export default function Training() {
  const lang = useLang();
  const [field, setField] = useState("");
  const { data, loading, error, reload } = useApi<Any>(endpoints.courses());
  const courses: Any[] = (data?.courses || []).filter((c: Any) => !field || c.field === field);
  return (
    <>
      <PageTitle eyebrow="🎓" title={tr(lang, "nav.training")}>
        <p className="lede" style={{ margin: 0 }}>{lang === "fr" ? "Apprendre à regarder les faits : criminologie, victimologie, psychologie criminelle, profilage géographique, biais cognitifs et science forensique." : "Learn to look at facts: criminology, victimology, criminal psychology, geographic profiling, cognitive biases and forensic science."}</p>
      </PageTitle>
      <div className="row wrap" style={{ gap: 8, marginBottom: 13 }}><Link className="chip" to="/formation/glossaire">📖 {lang === "fr" ? "Glossaire" : "Glossary"}</Link><Link className="chip" to="/archives">🗂 {tr(lang, "nav.archives")}</Link></div>
      <div className="tabs"><button className={`chip ${!field ? "on" : ""}`} onClick={() => setField("")}>{tr(lang, "common.all")}</button>{(data?.fields || []).map((x: string) => <button key={x} className={`chip ${field === x ? "on" : ""}`} onClick={() => setField(x)}>{x.replace(/_/g, " ")}</button>)}</div>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && <div className="stack" style={{ marginTop: 10 }}>{courses.map((c) => <Link to={`/formation/${c.slug}`} key={c.slug} className="card"><div className="between"><div><div className="eyebrow blood">{c.field} · {c.level}</div><h2 className="h2" style={{ marginTop: 5 }}><Bi_ v={c.title} /></h2></div><TierBadge tier={c.tier} /></div><p className="small" style={{ margin: "8px 0" }}><Bi_ v={c.intro} /></p><div className="row wrap" style={{ gap: 6 }}><span className="badge">⏱ {c.minutes} min</span><span className="badge">{c.lessons?.length || 0} {lang === "fr" ? "leçons" : "lessons"}</span></div></Link>)}{!courses.length && <Empty />}</div>}
    </>
  );
}

export function GlossaryPage() {
  const lang = useLang();
  const [field, setField] = useState("");
  const [q, setQ] = useState("");
  const { data, loading, error, reload } = useApi<Any>(endpoints.glossary(`${field || q ? `?${field ? `field=${encodeURIComponent(field)}` : ""}${field && q ? "&" : ""}${q ? `q=${encodeURIComponent(q)}` : ""}` : ""}`), [field, q]);
  const entries: Any[] = data?.entries || [];
  return <><PageTitle eyebrow="📖" title={lang === "fr" ? "Glossaire" : "Glossary"}><Link className="tiny" to="/formation">← {tr(lang, "nav.training")}</Link><p className="small" style={{ margin: "8px 0 0" }}>{pick(data?.method, lang)}</p></PageTitle><div className="field"><span>🔎</span><input value={q} onChange={(e) => setQ(e.target.value)} placeholder={lang === "fr" ? "Terme…" : "Term…"} /></div><div className="tabs" style={{ marginTop: 10 }}><button className={`chip ${!field ? "on" : ""}`} onClick={() => setField("")}>{tr(lang, "common.all")}</button>{(data?.fields || []).map((x: string) => <button key={x} className={`chip ${field === x ? "on" : ""}`} onClick={() => setField(x)}>{x}</button>)}</div>{loading && <Loading />}{error && <ErrorState message={error} onRetry={reload} />}{data && <div className="stack" style={{ marginTop: 10 }}>{entries.map((e) => <Link className="card" key={e.slug} to={`/formation/glossaire/${e.slug}`}><div className="eyebrow blood">{e.field}</div><h2 className="h2" style={{ fontSize: 15, marginTop: 4 }}><Bi_ v={e.term} /></h2><p className="small" style={{ margin: "6px 0 0" }}><Bi_ v={e.simple} /></p></Link>)}{!entries.length && <Empty />}</div>}</>;
}

export function GlossaryEntryPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.glossaryEntry(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return <><Link className="tiny" to="/formation/glossaire" style={{ display: "inline-block", padding: "14px 0 6px" }}>← {lang === "fr" ? "Glossaire" : "Glossary"}</Link><PageTitle eyebrow={data.field} title={<Bi_ v={data.term} />}><p className="lede" style={{ margin: 0 }}><Bi_ v={data.simple} /></p></PageTitle><article className="card"><div className="h3" style={{ marginBottom: 7 }}>{lang === "fr" ? "Approfondir" : "Deep dive"}</div><p style={{ margin: 0, color: "var(--bone-dim)", fontSize: 15 }}><Bi_ v={data.deep} /></p></article>{data.cases?.length > 0 && <section className="block-sec"><h2 className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Dans les dossiers" : "In dossiers"}</h2><div className="stack">{data.cases.map((c: Any) => <CaseCard key={c.slug} c={c} />)}</div></section>}</>;
}

export function CoursePage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const award = useApp((s) => s.award);
  const [done, setDone] = useState<number[]>([]);
  const { data, loading, error, reload } = useApi<Any>(endpoints.course(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  const lessons: Any[] = data.lessons || [];
  const toggle = (i: number) => { const next = done.includes(i) ? done.filter((x) => x !== i) : [...done, i]; setDone(next); if (!done.includes(i)) award("course_completed", `${slug}:${i}`); };
  return <><Link className="tiny" to="/formation" style={{ display: "inline-block", padding: "14px 0 6px" }}>← {tr(lang, "nav.training")}</Link><PageTitle eyebrow={`${data.field} · ${data.level}`} title={<Bi_ v={data.title} />}><p className="lede" style={{ margin: 0 }}><Bi_ v={data.intro} /></p></PageTitle><div className="row wrap" style={{ gap: 6, marginBottom: 13 }}><span className="badge">⏱ {data.minutes} min</span><TierBadge tier={data.tier} /><span className="badge">{done.length}/{lessons.length}</span></div><div className="stack">{lessons.map((l: Any, i: number) => <article key={i} className={`card ${done.includes(i) ? "" : ""}`}><button className="between" style={{ width: "100%", border: 0, background: "none", padding: 0, textAlign: "left" }} onClick={() => toggle(i)}><div style={{ minWidth: 0 }}><div className="eyebrow blood">{String(i + 1).padStart(2, "0")} · {done.includes(i) ? "✓" : ""}</div><h2 className="h2" style={{ fontSize: 15, marginTop: 4 }}><Bi_ v={l.title || l.label || { fr: `Leçon ${i + 1}`, en: `Lesson ${i + 1}` }} /></h2></div><span className={`chip ${done.includes(i) ? "on" : ""}`}>{done.includes(i) ? "✓" : "○"}</span></button><div style={{ marginTop: 8, color: "var(--bone-dim)", fontSize: 14.5 }}><Bi_ v={l.body || l.text || l.description} /></div></article>)}{!lessons.length && <MissingTraining />}</div>{data.cases?.length > 0 && <section className="block-sec"><h2 className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Dossiers pour aller plus loin" : "Dossiers to go further"}</h2><div className="stack">{data.cases.map((c: Any) => <CaseCard key={c.slug} c={c} />)}</div></section>}</>;
}

function MissingTraining() { const lang = useLang(); return <div className="empty">{lang === "fr" ? "Leçons non documentées pour cette formation." : "Lessons not documented for this course."}</div>; }
