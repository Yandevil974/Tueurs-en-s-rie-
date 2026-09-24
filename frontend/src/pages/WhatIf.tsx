import { useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import { Bi_, Empty, ErrorState, Loading, PageTitle, Reliability, SourceLine, useLang } from "../components/ui";

export default function WhatIf() {
  const lang = useLang();
  const [kind, setKind] = useState("");
  const { data, loading, error, reload } = useApi<Any>(endpoints.counterfactuals(kind ? `?kind=${encodeURIComponent(kind)}` : ""), [kind]);
  return (
    <>
      <PageTitle eyebrow="🔎" title={tr(lang, "nav.whatif")}>
        <p className="lede" style={{ margin: 0 }}>{lang === "fr" ? "Une question. Pas un jugement. Une reconstruction hypothétique, limitée par les faits documentés et le droit applicable." : "A question. Not a judgment. A hypothetical reconstruction, limited by documented facts and applicable law."}</p>
      </PageTitle>
      <div className="disclaimer" style={{ marginBottom: 13 }}>{pick(data?.disclaimer, lang) || tr(lang, "whatif.disclaimer")}</div>
      {data?.signature_line && <div className="note" style={{ marginBottom: 13 }}><em><Bi_ v={data.signature_line} /></em></div>}
      <div className="tabs"><button className={`chip ${!kind ? "on" : ""}`} onClick={() => setKind("")}>{tr(lang, "common.all")}</button>{(data?.kinds || []).map((x: Any) => <button key={x.key} className={`chip ${kind === x.key ? "on" : ""}`} onClick={() => setKind(x.key)}><Bi_ v={x.label} /></button>)}</div>
      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}
      {data && <><div className="tiny" style={{ margin: "10px 0" }}>{data.count} {lang === "fr" ? "reconstruction(s)" : "reconstruction(s)"}</div><div className="stack">{(data.items || []).map((x: Any) => <Link key={x.id} className="card" to={`/et-si/${x.id}`}><div className="between"><div className="eyebrow blood"><Bi_ v={x.kind_label} /></div><Reliability level={x.computable ? "PROBABLE" : "UNKNOWN"} /></div><h2 className="h2" style={{ fontSize: 15, margin: "6px 0" }}><Bi_ v={x.title} /></h2><p className="small" style={{ margin: 0 }}><Bi_ v={x.question} /></p><div className="tiny" style={{ marginTop: 8 }}>{x.case_id} · {x.computable ? (lang === "fr" ? "paramètres documentés" : "documented parameters") : tr(lang, "whatif.impossible")}</div></Link>)}{!data.items?.length && <Empty />}</div></>}
    </>
  );
}

export function WhatIfDetail() {
  const { id = "" } = useParams();
  const lang = useLang();
  const user = useApp((s) => s.user);
  const { data, loading, error, reload } = useApi<Any>(endpoints.counterfactual(Number(id)), [id]);
  const [reflection, setReflection] = useState("");
  const [saved, setSaved] = useState<Any | null>(null);
  const [saveError, setSaveError] = useState("");
  const [saving, setSaving] = useState(false);
  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return <Empty />;
  const comp = data.computation || {};
  const result = comp.result || comp.value || comp;
  const events: Any[] = data.documented_events || [];
  const offences: Any[] = data.documented_offences_after || [];

  const save = async () => {
    if (!reflection.trim()) return;
    setSaving(true); setSaveError("");
    try { setSaved(await api.post<Any>(endpoints.reflect(Number(id)), { text: reflection })); } catch (e: any) { setSaveError(e.message); } finally { setSaving(false); }
  };

  return <><Link className="tiny" to="/et-si" style={{ display: "inline-block", padding: "14px 0 6px" }}>← {tr(lang, "nav.whatif")}</Link><PageTitle eyebrow="🔎" title={<Bi_ v={data.title} />}><p className="lede" style={{ margin: 0 }}><Bi_ v={data.question} /></p></PageTitle><div className="disclaimer" style={{ marginBottom: 13 }}><Bi_ v={data.disclaimer} /></div><div className="note" style={{ marginBottom: 13 }}><em><Bi_ v={data.signature_line} /></em></div><section className="card"><div className="h3" style={{ marginBottom: 8 }}>{tr(lang, "whatif.computing")}</div>{data.jurisdiction_note && <p className="small"><Bi_ v={data.jurisdiction_note} /></p>}<div className="stack" style={{ gap: 9 }}>{events.map((e: Any, i: number) => <div key={i} className="card tight"><div className="row wrap" style={{ gap: 6 }}><span className="badge">{e.date || "—"}</span>{e.reliability && <Reliability level={e.reliability} />}</div><div style={{ marginTop: 5, color: "var(--bone-dim)", fontSize: 14 }}><Bi_ v={e.label || e.description || e.event || e.text} /></div></div>)}</div>{data.computable && comp.status !== "impossible" ? <div className="note neutral" style={{ marginTop: 12 }}><strong>{lang === "fr" ? "Résultat calculé" : "Computed result"}</strong><ComputationView data={data} comp={comp} /></div> : <div className="note warn" style={{ marginTop: 12 }}>{tr(lang, "whatif.impossible")}</div>}</section>{offences.length > 0 && <section className="block-sec"><h2 className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "Faits documentés postérieurs" : "Documented subsequent facts"}</h2><div className="stack">{offences.map((x: Any, i: number) => <Item key={i} x={x} />)}</div></section>}<section className="card" style={{ marginTop: 14 }}><div className="eyebrow blood">{tr(lang, "whatif.reflect")}</div><p className="small">{lang === "fr" ? "Il n'y a pas de bonne réponse et aucun score. La réflexion est privée." : "There is no right answer and no score. The reflection is private."}</p><textarea className="ta" value={reflection} onChange={(e) => setReflection(e.target.value)} placeholder={lang === "fr" ? "Ce que cette hypothèse vous fait questionner…" : "What this hypothesis makes you question…"} maxLength={4000} />{!user ? <div className="note neutral" style={{ marginTop: 10 }}>{lang === "fr" ? "Connecte-toi pour enregistrer ta réflexion — elle ne sera jamais publiée." : "Sign in to save your reflection — it will never be published."}<br /><Link className="btn sm" style={{ marginTop: 8 }} to="/compte">{tr(lang, "account.login")}</Link></div> : <button className="btn primary wide" style={{ marginTop: 10 }} disabled={saving || !reflection.trim()} onClick={save}>{saving ? "…" : tr(lang, "whatif.save")}</button>}{saveError && <div className="note warn" style={{ marginTop: 9 }}>{saveError}</div>}{saved && <div className="note" style={{ marginTop: 9 }}>{pick(saved.private, lang)}</div>}</section><SourceLine source={data.source} /></>;
}

function ComputationView({ data, comp }: { data: Any; comp: Any }) {
  const lang = useLang();
  const labels: [string, string][] = [
    ["reference_event", lang === "fr" ? "Événement de référence" : "Reference event"],
    ["hypothesis", lang === "fr" ? "Hypothèse" : "Hypothesis"],
    ["scenario_event", lang === "fr" ? "Événement du scénario" : "Scenario event"],
    ["outcome_event", lang === "fr" ? "Événement observé" : "Observed event"],
  ];
  const spared = data.spared;
  return <div style={{ marginTop: 8 }}>
    <div className="stack" style={{ gap: 6 }}>
      {labels.map(([key, label]) => comp[key] && <div key={key} className="row wrap" style={{ justifyContent: "space-between", gap: 8 }}><span className="tiny">{label}</span><span className="small"><Bi_ v={comp[key].label} /> · <span className="mono">{comp[key].date || "—"}</span></span></div>)}
    </div>
    {spared && <div className="note" style={{ marginTop: 10 }}><strong>{lang === "fr" ? "Victimes potentiellement évitées" : "Potentially spared victims"}</strong><div style={{ marginTop: 4 }}>{spared.documented && spared.count != null ? spared.count : pick(spared.note, lang) || tr(lang, "whatif.impossible")}</div></div>}
    {comp.gaps && <div className="tiny" style={{ marginTop: 9 }}>{lang === "fr" ? "Écarts temporels calculés à partir des dates disponibles :" : "Time gaps computed from available dates:"} {Object.entries(comp.gaps).map(([k, v]) => `${k.replace(/_/g, " ")}=${v ?? "—"}`).join(" · ")}</div>}
  </div>;
}

function Item({ x }: { x: Any }) { const lang = useLang(); return <div className="card tight"><div className="row wrap" style={{ gap: 6 }}>{x.date && <span className="badge mono">{x.date}</span>}{x.reliability && <Reliability level={x.reliability} />}</div><div className="small" style={{ marginTop: 5 }}><Bi_ v={x.label || x.description || x.event || x.text} /></div><div className="tiny" style={{ marginTop: 5 }}>{x.note ? <Bi_ v={x.note} /> : ""}</div></div>; }
