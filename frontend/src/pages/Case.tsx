import { useEffect, useMemo, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi, fmtDate } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import CaseCard from "../components/CaseCard";
import {
  BackLink,
  Bi_,
  Blocks,
  Cover,
  Empty,
  ErrorState,
  Item,
  Items,
  Loading,
  Missing,
  PageTitle,
  Reliability,
  SourceLine,
  StatusBadge,
  TierBadge,
  useLang,
} from "../components/ui";

const actionItems = [
  ["/podcasts", "case.listen", "🎧"],
  ["dossier", "case.dossier", "📁"],
  ["victimes", "case.victims", "🕯"],
  ["psychologie", "case.psychology", "🧠"],
  ["enquete", "case.investigation", "🔎"],
  ["chronologie", "case.timeline", "🗓"],
  ["carte", "case.map", "🗺"],
  ["justice", "case.justice", "⚖"],
  ["sources", "case.sources", "📎"],
  ["memoire", "case.memory", "🕯"],
];

function slugPath(slug: string, key: string) {
  return key.startsWith("/") ? key : `/dossiers/${slug}/${key}`;
}

function useCase(slug: string) {
  return useApi<Any>(endpoints.case(slug), [slug]);
}

function useSensitiveGate(c: Any | undefined, slug: string) {
  const warned = useApp((s) => s.isWarned(slug));
  const acknowledge = useApp((s) => s.acknowledgeWarning);
  const [show, setShow] = useState(false);
  useEffect(() => {
    if (c?.sensitive && !warned) setShow(true);
  }, [c?.sensitive, warned]);
  const close = (remember: boolean) => {
    acknowledge(slug, remember);
    setShow(false);
  };
  return { show: show && Boolean(c?.sensitive), close };
}

function SensitiveSheet({ onContinue, onBack }: { onContinue: (remember: boolean) => void; onBack: () => void }) {
  const lang = useLang();
  const [remember, setRemember] = useState(false);
  return (
    <div className="scrim center" role="alertdialog" aria-modal="true" aria-labelledby="sensitive-title">
      <div className="sheet">
        <div className="eyebrow blood">⚠ {tr(lang, "case.sensitive.title")}</div>
        <h2 id="sensitive-title" className="h2" style={{ margin: "8px 0 7px" }}>
          {lang === "fr" ? "Avant d'ouvrir ce dossier" : "Before opening this dossier"}
        </h2>
        <p className="lede" style={{ fontSize: 14 }}>
          {tr(lang, "case.sensitive.body")}
        </p>
        <div className="disclaimer" style={{ margin: "14px 0" }}>
          {lang === "fr"
            ? "Les victimes restent au centre. Le criminel est étudié ; il n'est ni glorifié ni admiré."
            : "Victims remain at the centre. The offender is studied; never glorified or admired."}
        </div>
        <label className="row" style={{ alignItems: "center", gap: 8, fontFamily: "var(--sans)", fontSize: 12, color: "var(--grey-2)" }}>
          <input type="checkbox" checked={remember} onChange={(e) => setRemember(e.target.checked)} />
          {tr(lang, "case.sensitive.remember")}
        </label>
        <div className="row" style={{ marginTop: 16, justifyContent: "flex-end" }}>
          <button className="btn ghost" onClick={onBack}>{tr(lang, "case.sensitive.stay")}</button>
          <button className="btn primary" onClick={() => onContinue(remember)}>{tr(lang, "case.sensitive.go")}</button>
        </div>
      </div>
    </div>
  );
}

/* ---------------------------------------------------------------- dossier */
export default function CasePage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useCase(slug);
  const recommendations = useApi<Any>(endpoints.recommendations(slug), [slug]);
  const nav = useNavigate();
  const gate = useSensitiveGate(data?.case, slug);
  const toggleFavourite = useApp((s) => s.toggleFavourite);
  const favourites = useApp((s) => s.favourites);
  const c = data?.case;
  const recs: Any[] = recommendations.data?.recommendations || [];

  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!c) return <Empty />;

  return (
    <>
      <BackLink to="/bibliotheque" />
      <div className="hero">
        <Cover slug={c.slug} title={c.title} country={c.country} period={c.period_label} tall />
        <div className="overlay">
          <div className="row wrap" style={{ gap: 6 }}>
            <StatusBadge status={c.status} />
            <TierBadge tier={c.tier} />
          </div>
          <h1 className="h1" style={{ fontSize: 23, margin: "7px 0 3px" }}><Bi_ v={c.title} /></h1>
          <div className="small">{c.country_name?.[lang] || c.country} · {c.region} · <Bi_ v={c.period_label} /></div>
        </div>
      </div>

      <div className="row" style={{ margin: "10px 0 0", justifyContent: "space-between" }}>
        <button className="btn sm primary" onClick={() => nav(`/podcasts?case=${encodeURIComponent(c.slug)}`)}>▶ {tr(lang, "case.listen")}</button>
        <button className={`btn sm ${favourites.includes(c.slug) ? "primary" : "ghost"}`} onClick={() => toggleFavourite(c.slug)} aria-pressed={favourites.includes(c.slug)}>
          {favourites.includes(c.slug) ? "★" : "☆"} {lang === "fr" ? "Favori" : "Favourite"}
        </button>
      </div>

      <div className="actionbar" aria-label={lang === "fr" ? "Sections du dossier" : "Dossier sections"}>
        {actionItems.map(([to, key, ico]) => (
          <Link key={key} to={slugPath(c.slug, to)}>
            <span className="ico">{ico}</span>{tr(lang, key)}
          </Link>
        ))}
      </div>

      <section className="block-sec">
        <div className="row wrap" style={{ gap: 6, marginBottom: 9 }}>
          <StatusBadge status={c.status} />
          <span className="badge">{c.country_name?.[lang] || c.country}</span>
          <span className="badge">{c.region || c.city}</span>
        </div>
        <p className="lede" style={{ margin: 0 }}><Bi_ v={c.subtitle} /></p>
        {c.status_note && <div className="note neutral" style={{ marginTop: 12 }}><Bi_ v={c.status_note} /></div>}
      </section>

      <section className="card" style={{ marginBottom: 12 }}>
        <div className="h3" style={{ marginBottom: 7 }}>{lang === "fr" ? "Le dossier" : "The dossier"}</div>
        <p style={{ margin: 0, color: "var(--bone-dim)", fontSize: 15 }}><Bi_ v={c.summary} /></p>
        <div className="row wrap" style={{ gap: 6, marginTop: 12 }}>
          {(c.tags || []).map((t: string) => <span className="chip" key={t}>{t.replace(/_/g, " ")}</span>)}
        </div>
      </section>

      <div className="grid2" style={{ marginBottom: 12 }}>
        <Stat label={lang === "fr" ? "Victimes documentées" : "Documented victims"} value={c.victims_count} to={`/dossiers/${c.slug}/victimes`} />
        <Stat label={lang === "fr" ? "Épisodes" : "Episodes"} value={c.episodes_count} to="/podcasts" />
        <Stat label={lang === "fr" ? "Étapes enquête" : "Investigation steps"} value={data.investigation_steps_count} to={`/dossiers/${c.slug}/enquete`} />
        <Stat label={lang === "fr" ? "Sources" : "Sources"} value={c.stats?.sources || "—"} to={`/dossiers/${c.slug}/sources`} />
      </div>

      <section className="block-sec">
        <div className="between" style={{ marginBottom: 8 }}>
          <h2 className="h3">{lang === "fr" ? "Les chapitres" : "Chapters"}</h2>
          <Link className="tiny" to={`/dossiers/${c.slug}/dossier`}>{tr(lang, "common.all")} →</Link>
        </div>
        <div className="stack">
          {(data.sections || []).slice(0, 6).map((s: Any) => (
            <Link key={s.key} to={`/dossiers/${c.slug}/dossier#${s.key}`} className="card tight">
              <div className="between">
                <div><div className="eyebrow">{s.key.replace(/_/g, " ")}</div><div className="h2" style={{ fontSize: 14, marginTop: 3 }}><Bi_ v={s.title} /></div></div>
                {s.locked ? <span className="badge premium">🔒 Premium</span> : <span className="tiny">→</span>}
              </div>
            </Link>
          ))}
        </div>
      </section>

      <section className="card" style={{ marginBottom: 14 }}>
        <div className="between">
          <div>
            <div className="eyebrow blood">🕯 {tr(lang, "case.memory")}</div>
            <div className="h2" style={{ fontSize: 14, marginTop: 5 }}>{tr(lang, "victim.question")}</div>
          </div>
          <Link className="btn sm ghost" to={`/dossiers/${c.slug}/memoire`}>{tr(lang, "common.open")}</Link>
        </div>
      </section>

      {recs.length > 0 && (
        <section className="block-sec">
          <div className="between" style={{ marginBottom: 8 }}>
            <h2 className="h3">{tr(lang, "case.similar")}</h2>
            <span className="tiny">{lang === "fr" ? "contexte · période · géographie · enquête" : "context · period · geography · investigation"}</span>
          </div>
          <div className="rail">
            {recs.map((r: Any) => <CaseCard key={r.case.slug} c={r.case} compact />)}
          </div>
        </section>
      )}

      {gate.show && <SensitiveSheet onContinue={gate.close} onBack={() => nav(-1)} />}
    </>
  );
}

function Stat({ label, value, to }: { label: string; value: React.ReactNode; to: string }) {
  return <Link className="card tight" to={to}><div className="h1" style={{ fontSize: 22 }}>{value}</div><div className="tiny" style={{ marginTop: 4 }}>{label}</div></Link>;
}

/* --------------------------------------------------------------- dossier */
export function DossierPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useCase(slug);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  const c = data?.case;
  if (!c) return <Empty />;
  return (
    <>
      <BackLink to={`/dossiers/${slug}`} />
      <PageTitle eyebrow={pick(c.title, lang)} title={lang === "fr" ? "Le dossier complet" : "The complete dossier"}>
        <p className="small" style={{ margin: 0 }}>{lang === "fr" ? "Vingt chapitres, un fil documentaire, des niveaux de fiabilité visibles." : "Twenty chapters, one documentary thread, visible reliability levels."}</p>
      </PageTitle>
      <div className="stack">
        {(data.sections || []).map((s: Any, i: number) => (
          <article id={s.key} key={s.key || i} className="card">
            <div className="between" style={{ marginBottom: 10 }}>
              <div><div className="eyebrow blood">{String(i + 1).padStart(2, "0")} · {s.key.replace(/_/g, " ")}</div><h2 className="h2" style={{ marginTop: 4 }}><Bi_ v={s.title} /></h2></div>
              {s.tier === "PREMIUM" && <TierBadge tier="PREMIUM" />}
            </div>
            {s.locked ? <LockedChapter /> : <Blocks blocks={s.blocks || []} />}
          </article>
        ))}
      </div>
    </>
  );
}

function LockedChapter() {
  const lang = useLang();
  return <div className="locked"><div style={{ fontSize: 22 }}>🔒</div><div className="h2" style={{ fontSize: 14, margin: "7px 0 4px" }}>{lang === "fr" ? "Chapitre Premium" : "Premium chapter"}</div><div className="small">{lang === "fr" ? "Le dossier conserve son existence ; le contenu est clairement marqué comme verrouillé." : "The chapter remains visible; its content is clearly marked as locked."}</div><Link className="btn sm primary" style={{ marginTop: 10 }} to="/compte">{tr(lang, "common.unlock")}</Link></div>;
}

/* -------------------------------------------------------------- victimes */
export function VictimsPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.victims(slug), [slug]);
  const [open, setOpen] = useState<number | null>(null);
  const award = useApp((s) => s.award);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return (
    <>
      <BackLink to={`/dossiers/${slug}`} />
      <PageTitle eyebrow="🕯" title={tr(lang, "case.victims")}>
        <p className="lede" style={{ margin: 0 }}>{tr(lang, "victim.question")}</p>
      </PageTitle>
      {data.ethics_note && <div className="note" style={{ marginBottom: 13 }}><Bi_ v={data.ethics_note} /></div>}
      <div className="row wrap" style={{ gap: 6, marginBottom: 12 }}><span className="badge free">{tr(lang, "common.free")}</span><span className="badge">{data.count}</span></div>
      {!data.victims?.length && <Missing />}
      <div className="stack">
        {(data.victims || []).map((v: Any) => {
          const items = v.life?.[lang]?.items || v.life?.fr?.items || [];
          const disappearance = v.disappearance?.[lang]?.items || v.disappearance?.fr?.items || [];
          const isOpen = open === v.id;
          return <article key={v.id} className="card" style={{ padding: 0, overflow: "hidden" }}>
            <button className="card tight" style={{ width: "100%", border: 0, borderRadius: 0, textAlign: "left", background: isOpen ? "var(--anthracite-2)" : "var(--anthracite)" }} onClick={() => { setOpen(isOpen ? null : v.id); award("victim_remembered", `${slug}:${v.id}`); }} aria-expanded={isOpen}>
              <div className="between"><div><div className="h2" style={{ fontSize: 15 }}>🕯 {v.anonymised ? (lang === "fr" ? "Identité non publiée" : "Identity not published") : v.name}</div><div className="tiny">{v.age ? `${tr(lang, "victim.age")} : ${v.age}` : ""}</div></div><Reliability level={v.reliability} /></div>
            </button>
            {isOpen && <div style={{ padding: 14 }}>
              {v.anonymised && <div className="note warn" style={{ marginBottom: 11 }}>{tr(lang, "victim.anonymised")}</div>}
              {items.length ? <dl className="kv" style={{ marginBottom: 12 }}>{items.map((it: Any, i: number) => <div style={{ display: "contents" }} key={i}><dt><Bi_ v={it.label} /></dt><dd>{typeof it.text === "object" ? <Bi_ v={it.text} /> : String(it.text ?? "")}</dd></div>)}</dl> : <Missing />}
              {disappearance.length > 0 && <><div className="h3" style={{ margin: "12px 0 6px" }}>{lang === "fr" ? "Ce que l'on sait de la disparition" : "What is known about the disappearance"}</div><dl className="kv">{disappearance.map((it: Any, i: number) => <div style={{ display: "contents" }} key={i}><dt><Bi_ v={it.label} /></dt><dd>{typeof it.text === "object" ? <Bi_ v={it.text} /> : String(it.text ?? "")}</dd></div>)}</dl></>}
              {v.note && <div className="note neutral" style={{ marginTop: 12 }}><Bi_ v={v.note} /></div>}
              <SourceLine source={v.source} />
            </div>}
          </article>;
        })}
      </div>
      <div className="disclaimer" style={{ marginTop: 16 }}>{lang === "fr" ? "La victimologie décrit un contexte ; elle ne cherche jamais une cause dans les caractéristiques de la victime." : "Victimology describes context; it never looks for a cause in a victim's characteristics."}</div>
    </>
  );
}

/* ----------------------------------------------------------- chronologie */
export function TimelinePage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.timeline(slug), [slug]);
  const [phase, setPhase] = useState("");
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  const events = (data.events || []).filter((e: Any) => !phase || e.phase === phase);
  return <>
    <BackLink to={`/dossiers/${slug}`} />
    <PageTitle eyebrow="🗓" title={tr(lang, "case.timeline")}><p className="small" style={{ margin: 0 }}>{data.count} {lang === "fr" ? "événements documentés" : "documented events"}</p></PageTitle>
    <div className="tabs"><button className={`chip ${!phase ? "on" : ""}`} onClick={() => setPhase("")}>{tr(lang, "common.all")}</button>{Object.keys(data.phases || {}).map((p) => <button key={p} className={`chip ${phase === p ? "on" : ""}`} onClick={() => setPhase(p)}>{p} ({data.phases[p]})</button>)}</div>
    <div className="tl" style={{ marginTop: 14 }}>{events.map((e: Any) => <article key={e.id} className={`tl-item ${(e.reliability || "").toLowerCase()}`}><div className="tl-date">{e.date || "—"}</div><h2 className="h2" style={{ fontSize: 15, margin: "3px 0" }}><Bi_ v={e.title} /></h2><p style={{ margin: 0, color: "var(--bone-dim)", fontSize: 14.5 }}><Bi_ v={e.body} /></p><div className="row wrap" style={{ gap: 6, marginTop: 7 }}><Reliability level={e.reliability} /><SourceLine source={e.source} compact /></div></article>)}</div>
    {!events.length && <Empty />}
  </>;
}

/* ----------------------------------------------------------- enquête */
export function InvestigationPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.investigation(slug), [slug]);
  const [step, setStep] = useState(0);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  const steps: Any[] = data.steps || [];
  const current = steps[step];
  return <>
    <BackLink to={`/dossiers/${slug}`} />
    <PageTitle eyebrow="🔎" title={tr(lang, "case.investigation")}><p className="small" style={{ margin: 0 }}>{lang === "fr" ? "Mode Enquête : révélation dans l'ordre où l'information est devenue disponible." : "Investigation mode: reveal information in the order it became available."}</p></PageTitle>
    <div className="note neutral" style={{ marginBottom: 12 }}>{lang === "fr" ? "Aucune information ne revient dans le passé : on raisonne avec ce que l'on savait à chaque étape." : "No information is sent back in time: reason with what was known at each step."}</div>
    <div className="tabs">{steps.map((s, i) => <button key={i} className={`chip ${i === step ? "on" : ""}`} onClick={() => setStep(i)} aria-pressed={i === step}>{String(i + 1).padStart(2, "0")} · <Bi_ v={s.title || s.phase || { fr: `Étape ${i + 1}`, en: `Step ${i + 1}` }} /></button>)}</div>
    {current ? <article className="card" style={{ marginTop: 8 }}><div className="between"><div><div className="eyebrow blood">{current.date || current.phase || `Étape ${step + 1}`}</div><h2 className="h2" style={{ marginTop: 5 }}><Bi_ v={current.title} /></h2></div>{current.locked && <span className="badge premium">🔒 Premium</span>}</div>{current.locked ? <LockedChapter /> : <><p style={{ color: "var(--bone-dim)", fontSize: 15 }}><Bi_ v={current.body || current.description || current.text} /></p>{current.what_was_known && <div className="note neutral"><strong>{lang === "fr" ? "Ce qui était connu" : "What was known"}</strong><br /><Bi_ v={current.what_was_known} /></div>}{current.question && <div className="note warn" style={{ marginTop: 10 }}>❓ <Bi_ v={current.question} /></div>}<div className="row wrap" style={{ gap: 6, marginTop: 10 }}>{current.reliability && <Reliability level={current.reliability} />}{current.source && <span className="tiny">{current.source}</span>}</div></>}</article> : <Empty />}
    <div className="between" style={{ marginTop: 12 }}><button className="btn sm" disabled={step <= 0} onClick={() => setStep(step - 1)}>←</button><span className="tiny">{steps.length ? `${step + 1} / ${steps.length}` : ""}</span><button className="btn sm" disabled={step >= steps.length - 1} onClick={() => setStep(step + 1)}>→</button></div>
    {data.errors?.length > 0 && <section className="block-sec"><h2 className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Erreurs de l'enquête" : "Investigation errors"}</h2><Items list={data.errors} /></section>}
  </>;
}

/* --------------------------------------------------------------- indices */
export function EvidencePage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.evidence(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="🔍" title={tr(lang, "case.clues")}><p className="small" style={{ margin: 0 }}>{lang === "fr" ? "Un indice est présenté avec son poids documentaire, pas comme une certitude automatique." : "Each clue is presented with its documentary weight, not as an automatic certainty."}</p></PageTitle>{data.locked && <LockedChapter />}<div className="stack" style={{ marginTop: 12 }}>{(data.evidence || []).map((e: Any) => <article key={e.id} className="card"><div className="between"><h2 className="h2" style={{ fontSize: 15 }}><Bi_ v={e.title} /></h2><Reliability level={e.reliability} /></div><div className="tiny" style={{ margin: "5px 0" }}>{e.kind} {e.weight ? `· ${e.weight}` : ""}</div><p style={{ margin: 0, color: "var(--bone-dim)", fontSize: 14.5 }}><Bi_ v={e.description} /></p><SourceLine source={e.source} /></article>)}{!data.evidence?.length && <Missing />}</div></>;
}

/* ------------------------------------------------------------- psychologie */
export function PsychologyPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.psychology(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="🧠" title={tr(lang, "case.psychology")}><p className="small" style={{ margin: 0 }}>{lang === "fr" ? "Dans la tête : comportement documenté, jamais diagnostic psychiatrique automatique." : "Inside the mind: documented behaviour, never an automatic psychiatric diagnosis."}</p></PageTitle><div className="disclaimer" style={{ marginBottom: 13 }}><Bi_ v={data.disclaimer} /></div>{data.locked ? <LockedChapter /> : <Blocks blocks={data.blocks || []} />}<div className="note neutral" style={{ marginTop: 16 }}>{lang === "fr" ? "Chaque élément doit rester séparé : FAIT · HYPOTHÈSE · ANALYSE D'EXPERT · INCONNU." : "Each element must remain separate: FACT · HYPOTHESIS · EXPERT ANALYSIS · UNKNOWN."}</div></>;
}

/* --------------------------------------------------------------- victimology */
export function VictimologyPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.victimology(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return <><PageTitle eyebrow="🕯" title={lang === "fr" ? "Victimologie" : "Victimology"}><p className="small" style={{ margin: 0 }}>{lang === "fr" ? "Comprendre le contexte sans jamais faire porter la cause du crime à la victime." : "Understand context without ever placing the cause of the crime on the victim."}</p></PageTitle><div className="note warn" style={{ marginBottom: 13 }}><Bi_ v={data.ethics_note} /></div><Blocks blocks={data.blocks || []} /></>;
}

/* ------------------------------------------------------------------ carte */
export function CaseMapPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.geography(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  const pts = (data.locations || []).filter((x: Any) => x.lat != null && x.lon != null);
  const p = (lat: number, lon: number) => ({ x: ((lon + 180) / 360) * 720, y: ((90 - lat) / 180) * 360 });
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="🗺" title={tr(lang, "case.map")}><p className="small" style={{ margin: 0 }}>{pick(data.no_exact_address, lang)}</p></PageTitle><svg className="map" viewBox="0 0 720 360" role="img" aria-label={tr(lang, "case.map")}><rect width="720" height="360" fill="#0c0e12" />{Array.from({ length: 13 }).map((_, i) => <line key={`v${i}`} x1={(i * 720) / 12} y1="0" x2={(i * 720) / 12} y2="360" stroke="#1c2027" strokeWidth=".6" />)}{Array.from({ length: 7 }).map((_, i) => <line key={`h${i}`} x1="0" y1={(i * 360) / 6} x2="720" y2={(i * 360) / 6} stroke="#1c2027" strokeWidth=".6" />)}{pts.map((l: Any) => { const q = p(l.lat, l.lon); return <g key={l.id}><circle cx={q.x} cy={q.y} r="11" fill="#8e2233" opacity=".15" /><circle cx={q.x} cy={q.y} r="4" fill="#c2334a" /></g>; })}</svg><div className="stack" style={{ marginTop: 12 }}>{(data.locations || []).map((l: Any) => <article className="card tight" key={l.id}><div className="between"><div><div className="h2" style={{ fontSize: 14 }}><Bi_ v={l.names} /></div><div className="tiny">{l.city} · {l.region || l.country} · {l.date}</div></div><Reliability level={l.reliability} /></div>{l.note && <div className="small" style={{ marginTop: 5 }}><Bi_ v={l.note} /></div>}<SourceLine source={l.source} /></article>)}</div></>;
}

/* ---------------------------------------------------------------- justice */
export function CourtPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.court(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="⚖" title={tr(lang, "case.justice")}><p className="small" style={{ margin: 0 }}>{data.jurisdiction}</p></PageTitle><div className="card"><div className="h3" style={{ marginBottom: 6 }}>{lang === "fr" ? "Verdict" : "Verdict"}</div><p style={{ margin: 0, color: "var(--bone-dim)", fontSize: 15 }}><Bi_ v={data.verdict} /></p><hr className="rule" /><div className="h3" style={{ marginBottom: 6 }}>{lang === "fr" ? "Peine" : "Sentence"}</div><p style={{ margin: 0, color: "var(--bone-dim)", fontSize: 15 }}><Bi_ v={data.sentence} /></p></div>{data.appeals?.length > 0 && <section className="block-sec"><h2 className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Recours et suites" : "Appeals and consequences"}</h2><Items list={data.appeals.map((x: Any) => ({ text: x }))} /></section>}{data.consequences?.length > 0 && <section className="block-sec"><h2 className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Conséquences" : "Consequences"}</h2><Items list={data.consequences} /></section>}</>;
}

/* ---------------------------------------------------------------- sources */
export function SourcesPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.sources(slug), [slug]);
  const [level, setLevel] = useState("");
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  const rows = (data.sources || []).filter((s: Any) => !level || s.reliability === level);
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="📎" title={tr(lang, "case.sources")}><p className="small" style={{ margin: 0 }}>{data.count} · {pick(data.policy, lang)}</p></PageTitle><div className="tabs"><button className={`chip ${!level ? "on" : ""}`} onClick={() => setLevel("")}>{tr(lang, "common.all")}</button>{(data.levels || []).map((l: Any) => <button key={l.key} className={`chip ${level === l.key ? "on" : ""}`} onClick={() => setLevel(l.key)}><span className="dot" style={{ display: "inline-block", background: l.color }} />{pick(l.label, lang)}</button>)}</div><div className="stack" style={{ marginTop: 10 }}>{rows.map((s: Any) => <article className="card" key={s.id}><div className="between"><h2 className="h2" style={{ fontSize: 14.5 }}><Bi_ v={s.title} /></h2><Reliability level={s.reliability} /></div><div className="tiny" style={{ marginTop: 5 }}>{s.author} · {s.publisher} · {s.type}</div><div className="tiny mono" style={{ marginTop: 3 }}>{s.date} · {tr(lang, "common.verified")} {s.verified_at}</div>{s.note && <div className="small" style={{ marginTop: 7 }}><Bi_ v={s.note} /></div>}{s.url && <a className="btn sm ghost" href={s.url} target="_blank" rel="noreferrer noopener" style={{ marginTop: 10 }}>{tr(lang, "common.link")} ↗</a>}</article>)}{!rows.length && <Empty />}</div></>;
}

/* ---------------------------------------------------------------- mémoire */
export function MemorialPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.memorial(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="🕯" title={tr(lang, "case.memory")}><p className="lede" style={{ margin: 0 }}>{tr(lang, "victim.question")}</p></PageTitle><div className="note" style={{ marginBottom: 13 }}>{pick(data.never_paywalled, lang)}</div><div className="stack">{(data.memorials || []).map((m: Any) => <article className="card" key={m.id}>{m.title && <h2 className="h2" style={{ fontSize: 15, marginBottom: 7 }}><Bi_ v={m.title} /></h2>}{m.biography && <p style={{ color: "var(--bone-dim)", fontSize: 15 }}><Bi_ v={m.biography} /></p>}{m.testimony && <p style={{ color: "var(--bone-dim)", fontSize: 14.5, fontStyle: "italic" }}><Bi_ v={m.testimony} /></p>}{m.memory && <div className="note neutral"><Bi_ v={m.memory} /></div>}</article>)}{!data.memorials?.length && <Missing />}</div></>;
}

/* ---------------------------------------------------------------- experts */
export function ExpertsPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.experts(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="🧠" title={tr(lang, "case.experts")}><p className="small" style={{ margin: 0 }}>{lang === "fr" ? "Accords, désaccords et limites : les experts ne sont pas une voix unique." : "Agreements, disagreements and limits: experts are not one single voice."}</p></PageTitle><div className="grid2" style={{ marginBottom: 12 }}><div className="card tight"><div className="eyebrow">{lang === "fr" ? "Accord" : "Agreement"}</div><div style={{ marginTop: 5, fontSize: 14 }}><Bi_ v={data.agreement} /></div></div><div className="card tight"><div className="eyebrow">{lang === "fr" ? "Désaccord" : "Disagreement"}</div><div style={{ marginTop: 5, fontSize: 14 }}><Bi_ v={data.disagreement} /></div></div></div><div className="stack">{(data.experts || []).map((x: Any) => <article className="card" key={x.id}><div className="between"><h2 className="h2" style={{ fontSize: 15 }}><Bi_ v={x.label} /></h2><span className="badge">{x.field}</span></div><p style={{ margin: "8px 0 0", color: "var(--bone-dim)", fontSize: 14.5 }}><Bi_ v={x.position} /></p><SourceLine source={x.source} /></article>)}{!data.experts?.length && <Missing />}</div>{data.uncertain && <div className="note neutral" style={{ marginTop: 13 }}><Bi_ v={data.uncertain} /></div>}</>;
}

/* ---------------------------------------------------------------- leçons */
export function LessonsPage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.lessons(slug), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="🎓" title={tr(lang, "case.lessons")}><p className="small" style={{ margin: 0 }}>{lang === "fr" ? "Ce que l'affaire nous apprend : 5 à 10 leçons, sans morale facile." : "What the case teaches us: 5 to 10 lessons, without easy morals."}</p></PageTitle><div className="stack">{(data.lessons || []).map((x: Any, i: number) => <div key={i} className="card"><div className="eyebrow blood">{String(i + 1).padStart(2, "0")}</div><div style={{ marginTop: 5, color: "var(--bone-dim)", fontSize: 15 }}><Bi_ v={x.text} /></div><div className="row wrap" style={{ gap: 6, marginTop: 8 }}>{x.reliability && <Reliability level={x.reliability} />}</div></div>)}{!data.lessons?.length && <Missing />}</div>{data.errors?.length > 0 && <section className="block-sec"><h2 className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Erreurs de l'enquête" : "Investigation errors"}</h2><Items list={data.errors} /></section>}{data.unknowns?.length > 0 && <section className="block-sec"><h2 className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Zones d'ombre" : "Unknowns"}</h2><Items list={data.unknowns} /></section>}</>;
}

/* ------------------------------------------------------------- Et si? */
export function WhatIfCasePage() {
  const { slug = "" } = useParams();
  const lang = useLang();
  const { data, loading, error, reload } = useApi<Any>(endpoints.counterfactuals(`?case=${encodeURIComponent(slug)}`), [slug]);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  return <><BackLink to={`/dossiers/${slug}`} /><PageTitle eyebrow="🔎" title={tr(lang, "case.whatif")}><p className="small" style={{ margin: 0 }}>{lang === "fr" ? "Une reconstruction hypothétique, jamais un jugement." : "A hypothetical reconstruction, never a judgment."}</p></PageTitle><div className="disclaimer" style={{ marginBottom: 13 }}>{tr(lang, "whatif.disclaimer")}</div><div className="stack">{(data?.items || []).map((x: Any) => <Link key={x.id} to={`/et-si/${x.id}`} className="card"><div className="eyebrow blood"><Bi_ v={x.kind_label} /></div><h2 className="h2" style={{ fontSize: 15, margin: "6px 0" }}><Bi_ v={x.title} /></h2><div className="small"><Bi_ v={x.question} /></div></Link>)}{!data?.items?.length && <Missing />}</div></>;
}
