import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api, endpoints, type Any } from "../lib/api";
import { useApp } from "../state/app";
import { pick, tr } from "../lib/i18n";
import { Bi_, ErrorState, Loading, PageTitle, TierBadge, useLang } from "../components/ui";

const CALIBRATION: Record<string, string> = {
  fr: "Les archives ne remplacent pas une enquête. Elles laissent visibles les faits, les doutes et les voix des victimes.",
  en: "Archives do not replace an investigation. They keep facts, doubts and victims' voices visible.",
};

export default function Account() {
  const lang = useLang();
  const user = useApp((s) => s.user);
  const tier = useApp((s) => s.tier);
  const authChecked = useApp((s) => s.authChecked);
  const login = useApp((s) => s.login);
  const register = useApp((s) => s.register);
  const logout = useApp((s) => s.logout);
  const switchTier = useApp((s) => s.switchTier);
  const authError = useApp((s) => s.authError);
  const a11y = useApp((s) => s.a11y);
  const setA11y = useApp((s) => s.setA11y);
  const [registerMode, setRegisterMode] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [display, setDisplay] = useState("");
  const [busy, setBusy] = useState(false);
  const [demoBusy, setDemoBusy] = useState("");
  const [voices, setVoices] = useState<Any[]>([]);
  const [voiceOpen, setVoiceOpen] = useState(false);

  useEffect(() => {
    if (!user) return;
    api.get<Any>(endpoints.voices()).then((r) => setVoices(r.voices || [])).catch(() => setVoices([]));
  }, [user]);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setBusy(true);
    if (registerMode) await register(email, password, display);
    else await login(email, password);
    setBusy(false);
  };

  const demo = async (which: "FREE" | "PREMIUM") => {
    setDemoBusy(which);
    const ok = await login(which === "FREE" ? "lecteur@yanisx.app" : "abonne@yanisx.app", which === "FREE" ? "lecteur-demo" : "abonne-demo");
    if (!ok) setDemoBusy("");
    else setDemoBusy("");
  };

  if (!authChecked) return <Loading />;
  if (!user) return <AuthForm lang={lang} registerMode={registerMode} setRegisterMode={setRegisterMode} email={email} setEmail={setEmail} password={password} setPassword={setPassword} display={display} setDisplay={setDisplay} submit={submit} busy={busy} error={authError} demo={demo} demoBusy={demoBusy} />;

  return <>
    <PageTitle eyebrow="👤" title={tr(lang, "nav.account")}><p className="small" style={{ margin: 0 }}>{user.display_name} · {user.email}</p></PageTitle>
    <div className="card" style={{ marginBottom: 12 }}><div className="between"><div><div className="eyebrow blood">{user.role}</div><div className="h2" style={{ fontSize: 17, marginTop: 5 }}>{user.display_name}</div><div className="tiny" style={{ marginTop: 3 }}>{user.email}</div></div><TierBadge tier={tier} /></div><div className="row wrap" style={{ gap: 8, marginTop: 13 }}><button className={`btn sm ${tier === "FREE" ? "primary" : "ghost"}`} onClick={() => switchTier("FREE")}>{tr(lang, "common.free")}</button><button className={`btn sm ${tier === "PREMIUM" ? "primary" : "ghost"}`} onClick={() => switchTier("PREMIUM")}>{tr(lang, "common.premium")}</button><button className="btn sm ghost" onClick={logout}>{tr(lang, "account.logout")}</button></div><div className="tiny" style={{ marginTop: 9 }}>{lang === "fr" ? "Démo locale : le sélecteur d'abonnement simule les droits ; un paiement réel sera branché côté serveur." : "Local demo: the tier switch simulates entitlements; real payment will be connected server-side."}</div></div>

    <section className="card" style={{ marginBottom: 12 }}><div className="between"><div><div className="eyebrow blood">⚙ {tr(lang, "account.a11y")}</div><div className="h2" style={{ fontSize: 15, marginTop: 5 }}>{lang === "fr" ? "Une écoute accessible" : "Accessible listening"}</div></div><span className="badge">WCAG</span></div><div className="stack" style={{ gap: 12, marginTop: 13 }}><label className="lbl">{lang === "fr" ? "Taille du texte" : "Text size"}<select className="field" style={{ width: "100%", borderRadius: 9 }} value={String(a11y.fontScale || 1)} onChange={(e) => setA11y({ fontScale: Number(e.target.value) })}><option value="0.9">90%</option><option value="1">100%</option><option value="1.15">115%</option><option value="1.3">130%</option><option value="1.5">150%</option></select></label><label className="row" style={{ justifyContent: "space-between" }}>{lang === "fr" ? "Contraste renforcé" : "High contrast"}<input type="checkbox" checked={a11y.contrast === "high"} onChange={(e) => setA11y({ contrast: e.target.checked ? "high" : "standard" })} /></label><label className="row" style={{ justifyContent: "space-between" }}>{lang === "fr" ? "Réduire les animations" : "Reduce motion"}<input type="checkbox" checked={Boolean(a11y.reduceMotion)} onChange={(e) => setA11y({ reduceMotion: e.target.checked })} /></label><label className="row" style={{ justifyContent: "space-between" }}>{lang === "fr" ? "Sous-titres / transcription par défaut" : "Captions / transcript by default"}<input type="checkbox" checked={a11y.captions !== false} onChange={(e) => setA11y({ captions: e.target.checked })} /></label></div></section>

    <VoiceStudio open={voiceOpen} setOpen={setVoiceOpen} voices={voices} setVoices={setVoices} lang={lang} />

    <section className="card" style={{ marginBottom: 12 }}><div className="eyebrow blood">🏅 {tr(lang, "account.badges")}</div><p className="small">{lang === "fr" ? "Les badges récompensent la compréhension, l'analyse, les chronologies et la mémoire. Jamais la violence." : "Badges reward understanding, analysis, timelines and memory. Never violence."}</p><Link className="btn sm ghost" to="/memoire">🕯 {tr(lang, "nav.memory")}</Link></section>

    <Link className="card" style={{ display: "block", marginBottom: 14 }} to="/ethique"><div className="eyebrow blood">⚖ {tr(lang, "nav.ethics")}</div><div className="h2" style={{ fontSize: 14, marginTop: 5 }}>{lang === "fr" ? "Lire la charte éditoriale" : "Read the editorial charter"} →</div></Link>
    {user.role === "admin" && <Link className="card" style={{ display: "block", marginBottom: 14 }} to="/admin"><div className="eyebrow blood">⚙ {lang === "fr" ? "Administration" : "Administration"}</div><div className="h2" style={{ fontSize: 14, marginTop: 5 }}>{lang === "fr" ? "Santé du catalogue et journal" : "Catalogue health and revision log"} →</div></Link>}
  </>;
}

function AuthForm({ lang, registerMode, setRegisterMode, email, setEmail, password, setPassword, display, setDisplay, submit, busy, error, demo, demoBusy }: any) {
  return <><PageTitle eyebrow="👤" title={registerMode ? tr(lang, "account.register") : tr(lang, "account.login")}><p className="small" style={{ margin: 0 }}>{lang === "fr" ? "La progression se sauvegarde sur ton compte ; la découverte des victimes reste possible sans compte." : "Progress saves to your account; victim discovery remains possible without an account."}</p></PageTitle><form className="card" onSubmit={submit}><label className="lbl">{tr(lang, "account.email")}</label><input className="field" style={{ width: "100%", borderRadius: 9, marginBottom: 10 }} type="email" required value={email} onChange={(e) => setEmail(e.target.value)} /><label className="lbl">{tr(lang, "account.password")}</label><input className="field" style={{ width: "100%", borderRadius: 9, marginBottom: 10 }} type="password" required minLength={8} value={password} onChange={(e) => setPassword(e.target.value)} />{registerMode && <><label className="lbl">{lang === "fr" ? "Nom affiché" : "Display name"}</label><input className="field" style={{ width: "100%", borderRadius: 9, marginBottom: 10 }} value={display} onChange={(e) => setDisplay(e.target.value)} /></>}<button className="btn primary wide" disabled={busy}>{busy ? "…" : registerMode ? tr(lang, "account.register") : tr(lang, "account.login")}</button>{error && <div className="note warn" style={{ marginTop: 10 }}>{error}</div>}</form><button className="btn ghost wide" style={{ marginTop: 10 }} onClick={() => setRegisterMode(!registerMode)}>{registerMode ? tr(lang, "account.login") : tr(lang, "account.register")}</button><section className="block-sec"><div className="h3" style={{ marginBottom: 8 }}>{tr(lang, "account.demo")}</div><div className="grid2"><button className="card tight" onClick={() => demo("FREE")} disabled={Boolean(demoBusy)}><div className="eyebrow">Lecteur</div><div className="h2" style={{ fontSize: 13, marginTop: 4 }}>FREE {demoBusy === "FREE" ? "…" : "→"}</div></button><button className="card tight" onClick={() => demo("PREMIUM")} disabled={Boolean(demoBusy)}><div className="eyebrow blood">Abonné</div><div className="h2" style={{ fontSize: 13, marginTop: 4 }}>PREMIUM {demoBusy === "PREMIUM" ? "…" : "→"}</div></button></div></section></>;
}

function VoiceStudio({ open, setOpen, voices, setVoices, lang }: any) {
  const [kind, setKind] = useState<"REAL" | "SYNTHETIC">("REAL");
  const [name, setName] = useState("");
  const [consent, setConsent] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const create = async () => { if (!name.trim()) return; setBusy(true); setError(""); try { const r = await api.post<Any>(endpoints.voices(), { name, kind, language: lang, samples: [{ text: CALIBRATION[lang], status: "pending" }], consent: kind === "SYNTHETIC" ? { voiceOwnerConsent: consent, explicit: consent, signedAt: consent ? new Date().toISOString() : "" } : {} }); setVoices([...voices, r]); setName(""); setConsent(false); } catch (e: any) { setError(e.message); } finally { setBusy(false); } };
  return <section className="card" style={{ marginBottom: 12 }}><div className="between"><div><div className="eyebrow blood">🎙 {tr(lang, "account.voice")}</div><div className="h2" style={{ fontSize: 15, marginTop: 5 }}>{lang === "fr" ? "Le studio de la voix d'identité" : "Identity voice studio"}</div></div><button className="btn sm" onClick={() => setOpen(!open)}>{open ? tr(lang, "common.close") : tr(lang, "common.open")}</button></div><p className="small">{lang === "fr" ? "La narration privilégie ta propre voix. Une voix synthétique exige l'accord explicite du propriétaire, daté et signé." : "Narration prioritises your own voice. A synthetic voice requires the voice owner's explicit, dated and signed consent."}</p>{voices.length > 0 && <div className="stack" style={{ gap: 6, marginBottom: 11 }}>{voices.map((v: Any) => <div className="card tight" key={v.id}><div className="between"><span className="h2" style={{ fontSize: 13 }}>{v.name}</span><span className="badge">{v.kind} · {v.status}</span></div></div>)}</div>}{open && <div className="stack" style={{ gap: 10 }}><div className="row wrap" style={{ gap: 6 }}><button className={`chip ${kind === "REAL" ? "on" : ""}`} onClick={() => setKind("REAL")}>{lang === "fr" ? "Ma voix · réelle" : "My voice · real"}</button><button className={`chip ${kind === "SYNTHETIC" ? "on" : ""}`} onClick={() => setKind("SYNTHETIC")}>{lang === "fr" ? "Synthétique · consentement requis" : "Synthetic · consent required"}</button></div><label className="lbl">{lang === "fr" ? "Nom du profil" : "Profile name"}<input className="field" style={{ width: "100%", borderRadius: 9 }} value={name} onChange={(e) => setName(e.target.value)} placeholder={lang === "fr" ? "Ma voix principale" : "My main voice"} /></label><div className="note neutral"><div className="eyebrow">{lang === "fr" ? "Parcours en cinq étapes" : "Five-step workflow"}</div><ol style={{ margin: "7px 0 0", paddingLeft: 19, color: "var(--bone-dim)", fontSize: 13.5 }}><li>{lang === "fr" ? "Enregistrer ou importer un échantillon" : "Record or import a sample"}</li><li>{lang === "fr" ? "Lire le texte de calibration" : "Read the calibration text"}</li><li>{lang === "fr" ? "Valider la prise" : "Validate the take"}</li><li>{lang === "fr" ? "Consentement explicite si synthèse" : "Explicit consent if synthetic"}</li><li>{lang === "fr" ? "Activer la voix d'identité" : "Activate identity voice"}</li></ol><p className="small" style={{ marginBottom: 0 }}><em>{CALIBRATION[lang]}</em></p></div>{kind === "SYNTHETIC" && <label className="row" style={{ alignItems: "flex-start", gap: 8, fontSize: 12.5 }}><input type="checkbox" checked={consent} onChange={(e) => setConsent(e.target.checked)} />{lang === "fr" ? "Je confirme disposer du consentement explicite, daté et signé du propriétaire de cette voix." : "I confirm I have the voice owner's explicit, dated and signed consent."}</label>}<button className="btn primary" disabled={busy || !name.trim() || (kind === "SYNTHETIC" && !consent)} onClick={create}>{busy ? "…" : lang === "fr" ? "Créer le profil" : "Create profile"}</button>{error && <div className="note warn">{error}</div>}</div>}</section>;
}
