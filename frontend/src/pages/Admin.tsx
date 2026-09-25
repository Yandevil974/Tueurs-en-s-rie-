import { useState } from "react";
import { Link } from "react-router-dom";
import { api, endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import { Bi_, Empty, ErrorState, Loading, PageTitle, Reliability, useLang } from "../components/ui";

/**
 * Administration réelle, réservée au rôle admin. Les indicateurs viennent de
 * /admin/stats : aucune pastille de santé n'est calculée côté interface.
 */
export default function Admin() {
  const lang = useLang();
  const user = useApp((s) => s.user);
  const [reason, setReason] = useState("");
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState<Any | null>(null);
  const [notification, setNotification] = useState({ titleFr: "", titleEn: "", bodyFr: "", bodyEn: "", href: "", reason: "" });
  const [notificationBusy, setNotificationBusy] = useState(false);
  const [notificationResult, setNotificationResult] = useState<Any | null>(null);
  const isAdmin = user?.role === "admin";
  const stats = useApi<Any>(isAdmin ? endpoints.adminStats() : null, [isAdmin]);
  const revisions = useApi<Any>(isAdmin ? endpoints.adminRevisions() : null, [isAdmin]);

  if (!user) {
    return (
      <>
        <PageTitle eyebrow="⚙" title={lang === "fr" ? "Administration" : "Administration"} />
        <div className="locked">
          <div style={{ fontSize: 22 }}>🔒</div>
          <div className="h2" style={{ fontSize: 14, margin: "8px 0 5px" }}>{lang === "fr" ? "Connexion requise" : "Sign in required"}</div>
          <Link className="btn sm primary" to="/compte">{tr(lang, "account.login")}</Link>
        </div>
      </>
    );
  }

  if (!isAdmin) {
    return (
      <>
        <PageTitle eyebrow="⚙" title={lang === "fr" ? "Administration" : "Administration"} />
        <div className="locked">
          <div style={{ fontSize: 22 }}>⛔</div>
          <div className="h2" style={{ fontSize: 14, margin: "8px 0 5px" }}>{lang === "fr" ? "Accès réservé à l'équipe éditoriale" : "Reserved for the editorial team"}</div>
          <div className="small">{user.email}</div>
        </div>
      </>
    );
  }

  const reseed = async () => {
    if (!reason.trim() || !window.confirm(lang === "fr" ? "Reconstruire le catalogue depuis les dossiers Python ?" : "Rebuild the catalogue from the Python dossiers?")) return;
    setBusy(true);
    setMessage(null);
    try {
      const result = await api.post<Any>(endpoints.adminReseed(), { reason: reason.trim() });
      setMessage(result);
      setReason("");
      await Promise.all([stats.reload(), revisions.reload()]);
    } catch (e: any) {
      setMessage({ error: e.message });
    } finally {
      setBusy(false);
    }
  };

  const publishNotification = async () => {
    if (!notification.titleFr.trim() || !notification.bodyFr.trim()) return;
    setNotificationBusy(true);
    setNotificationResult(null);
    try {
      const result = await api.post<Any>(endpoints.adminBroadcastNotification(), {
        title: { fr: notification.titleFr.trim(), en: notification.titleEn.trim() || notification.titleFr.trim() },
        body: { fr: notification.bodyFr.trim(), en: notification.bodyEn.trim() || notification.bodyFr.trim() },
        href: notification.href.trim(),
        kind: "editorial",
        reason: notification.reason.trim() || "editorial notification",
      });
      setNotificationResult(result);
      setNotification({ titleFr: "", titleEn: "", bodyFr: "", bodyEn: "", href: "", reason: "" });
      await revisions.reload();
    } catch (e: any) {
      setNotificationResult({ error: e.message });
    } finally {
      setNotificationBusy(false);
    }
  };

  return (
    <>
      <PageTitle eyebrow="⚙" title={lang === "fr" ? "Administration éditoriale" : "Editorial administration"}>
        <p className="small" style={{ margin: 0 }}>{user.email} · {user.role}</p>
      </PageTitle>

      {stats.loading && <Loading />}
      {stats.error && <ErrorState message={stats.error} onRetry={stats.reload} />}
      {stats.data && <>
        <div className="grid2" style={{ marginBottom: 12 }}>
          <Metric value={stats.data.cases} label={lang === "fr" ? "Dossiers" : "Dossiers"} />
          <Metric value={stats.data.victims} label={lang === "fr" ? "Victimes" : "Victims"} />
          <Metric value={stats.data.sources} label={lang === "fr" ? "Sources" : "Sources"} />
          <Metric value={stats.data.episodes} label={lang === "fr" ? "Épisodes" : "Episodes"} />
        </div>

        <section className="card" style={{ marginBottom: 12 }}>
          <div className="between" style={{ marginBottom: 9 }}>
            <div className="eyebrow blood">{lang === "fr" ? "Santé du catalogue" : "Catalogue health"}</div>
            <span className={`badge ${stats.data.health?.memorial_tier_ok ? "confirmed" : "disputed"}`}>
              <span className="dot" /> {stats.data.health?.memorial_tier_ok ? (lang === "fr" ? "Conforme" : "OK") : (lang === "fr" ? "À corriger" : "Review")}
            </span>
          </div>
          <div className="stack" style={{ gap: 7 }}>
            <HealthRow ok={!stats.data.health?.unsourced_victims?.length} label={lang === "fr" ? "Victimes nommées sans source" : "Named victims without a source"} count={stats.data.health?.unsourced_victims?.length || 0} />
            <HealthRow ok={Boolean(stats.data.health?.memorial_tier_ok)} label={lang === "fr" ? "Mémoriaux payants" : "Paywalled memorials"} count={stats.data.health?.paywalled_memorials?.length || 0} />
            <HealthRow ok={!stats.data.health?.episodes_without_transcript?.length} label={lang === "fr" ? "Épisodes sans transcription" : "Episodes without transcript"} count={stats.data.health?.episodes_without_transcript?.length || 0} />
            <HealthRow ok={!stats.data.health?.cases_without_signature_line?.length} label={lang === "fr" ? "Épisodes sans phrase signature" : "Episodes without signature line"} count={stats.data.health?.cases_without_signature_line?.length || 0} />
          </div>
          <div className="tiny" style={{ marginTop: 10 }}>{lang === "fr" ? "Contrôlé le" : "Checked on"} {stats.data.checked_at}</div>
        </section>

        {stats.data.health?.unsourced_victims?.length > 0 && <section className="card" style={{ marginBottom: 12 }}><div className="h3" style={{ marginBottom: 8 }}>{lang === "fr" ? "À documenter" : "To document"}</div><div className="stack">{stats.data.health.unsourced_victims.map((x: Any, i: number) => <div className="row wrap" key={i}><Reliability level="UNKNOWN" /><span className="small">{x.case} · {x.victim || (lang === "fr" ? "Identité non publiée" : "Identity not published")}</span></div>)}</div></section>}
      </>}

      <section className="card" style={{ marginBottom: 12 }}>
        <div className="eyebrow blood">↻ {lang === "fr" ? "Reconstruire le catalogue" : "Rebuild catalogue"}</div>
        <p className="small">{lang === "fr" ? "Le contenu structurel vient des dossiers Python sourcés. Chaque reconstruction est journalisée." : "Structural content comes from sourced Python dossiers. Every rebuild is logged."}</p>
        <label className="lbl">{lang === "fr" ? "Motif obligatoire" : "Required reason"}</label>
        <textarea className="ta" style={{ minHeight: 70 }} value={reason} onChange={(e) => setReason(e.target.value)} placeholder={lang === "fr" ? "Ex. vérification après ajout d'une source…" : "E.g. verification after adding a source…"} />
        <button className="btn primary" style={{ marginTop: 9 }} disabled={busy || !reason.trim()} onClick={reseed}>{busy ? "…" : lang === "fr" ? "Reconstruire et journaliser" : "Rebuild and log"}</button>
        {message?.error && <div className="note warn" style={{ marginTop: 10 }}>{message.error}</div>}
        {message?.reseeded && <div className="note" style={{ marginTop: 10 }}>{lang === "fr" ? "Catalogue reconstruit." : "Catalogue rebuilt."} · {message.counts?.cases} {lang === "fr" ? "dossiers" : "dossiers"}</div>}
      </section>

      <section className="card" style={{ marginBottom: 12 }}>
        <div className="eyebrow blood">🔔 {lang === "fr" ? "Notification éditoriale" : "Editorial notification"}</div>
        <p className="small">{lang === "fr" ? "Message explicitement rédigé par l'équipe, envoyé aux comptes existants. Aucun texte automatique n'est inventé." : "A message explicitly authored by the team, sent to existing accounts. No automatic text is invented."}</p>
        <div className="grid2">
          <Field label="Titre FR" value={notification.titleFr} onChange={(v) => setNotification({ ...notification, titleFr: v })} />
          <Field label="Title EN" value={notification.titleEn} onChange={(v) => setNotification({ ...notification, titleEn: v })} />
        </div>
        <label className="lbl">{lang === "fr" ? "Message FR" : "Message FR"}<textarea className="ta" style={{ minHeight: 74 }} value={notification.bodyFr} onChange={(e) => setNotification({ ...notification, bodyFr: e.target.value })} /></label>
        <label className="lbl">Message EN<textarea className="ta" style={{ minHeight: 74 }} value={notification.bodyEn} onChange={(e) => setNotification({ ...notification, bodyEn: e.target.value })} /></label>
        <div className="grid2"><Field label="Lien interne" value={notification.href} onChange={(v) => setNotification({ ...notification, href: v })} placeholder="/dossiers/..." /><Field label={lang === "fr" ? "Motif journal" : "Log reason"} value={notification.reason} onChange={(v) => setNotification({ ...notification, reason: v })} /></div>
        <button className="btn primary" style={{ marginTop: 9 }} disabled={notificationBusy || !notification.titleFr.trim() || !notification.bodyFr.trim()} onClick={publishNotification}>{notificationBusy ? "…" : lang === "fr" ? "Publier la notification" : "Publish notification"}</button>
        {notificationResult?.error && <div className="note warn" style={{ marginTop: 10 }}>{notificationResult.error}</div>}
        {notificationResult?.published && <div className="note" style={{ marginTop: 10 }}>{notificationResult.recipients} {lang === "fr" ? "destinataire(s)" : "recipient(s)"}</div>}
      </section>

      <section className="block-sec">
        <div className="between" style={{ marginBottom: 8 }}><h2 className="h3">{lang === "fr" ? "Journal des révisions" : "Revision log"}</h2><button className="btn sm ghost" onClick={revisions.reload}>{tr(lang, "common.retry")}</button></div>
        {revisions.loading && <Loading />}
        {revisions.error && <ErrorState message={revisions.error} onRetry={revisions.reload} />}
        {revisions.data && <div className="stack">{(revisions.data.revisions || []).slice(0, 20).map((r: Any) => <article className="card tight" key={r.id}><div className="between"><div className="row wrap" style={{ gap: 6 }}><span className="badge">{r.action}</span><span className="badge">{r.entity}</span></div><span className="tiny mono">{r.created_at}</span></div><div className="small" style={{ marginTop: 6 }}>{r.reason || (lang === "fr" ? "Sans motif" : "No reason")}</div></article>)}{!revisions.data.revisions?.length && <Empty />}</div>}
      </section>
    </>
  );
}

function Field({ label, value, onChange, placeholder }: { label: string; value: string; onChange: (value: string) => void; placeholder?: string }) {
  return <label className="lbl">{label}<div className="field" style={{ width: "100%", borderRadius: 9 }}><input value={value} onChange={(e) => onChange(e.target.value)} placeholder={placeholder} /></div></label>;
}

function Metric({ value, label }: { value: React.ReactNode; label: string }) {
  return <div className="card tight"><div className="h1" style={{ fontSize: 22 }}>{value}</div><div className="tiny" style={{ marginTop: 3 }}>{label}</div></div>;
}

function HealthRow({ ok, label, count }: { ok: boolean; label: string; count: number }) {
  return <div className="between"><span className="small">{ok ? "✓" : "!"} {label}</span><span className={`badge ${ok ? "confirmed" : "disputed"}`}><span className="dot" />{count}</span></div>;
}
