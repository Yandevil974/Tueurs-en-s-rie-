import { useEffect, useState } from "react";
import { Link, NavLink, useLocation } from "react-router-dom";
import { api, endpoints, type Any } from "../lib/api";
import { LANGS, pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import { PlayerBar, QuestionSheet } from "./Player";
import { Bi_, Reliability, SourceLine, useLang } from "./ui";

const PRIMARY = [
  { to: "/", k: "nav.home", ico: "🏠" },
  { to: "/explorer", k: "nav.explore", ico: "🌍" },
  { to: "/podcasts", k: "nav.podcasts", ico: "🎧" },
  { to: "/memoire", k: "nav.memory", ico: "🕯" },
  { to: "/plus", k: "nav.more", ico: "⋯" },
];

const SECONDARY = [
  { to: "/rechercher", k: "nav.search", ico: "🔎" },
  { to: "/bibliotheque", k: "nav.library", ico: "📚" },
  { to: "/psychologie", k: "nav.psychology", ico: "🧠" },
  { to: "/enquetes", k: "nav.investigations", ico: "🔎" },
  { to: "/cold-cases", k: "nav.coldcases", ico: "❄️" },
  { to: "/archives", k: "nav.archives", ico: "🗂" },
  { to: "/formation", k: "nav.training", ico: "🎓" },
  { to: "/et-si", k: "nav.whatif", ico: "🔎" },
  { to: "/ethique", k: "nav.ethics", ico: "⚖️" },
  { to: "/compte", k: "nav.account", ico: "👤" },
];

export default function Layout({ children }: { children: React.ReactNode }) {
  const lang = useLang();
  const setLang = useApp((s) => s.setLang);
  const loadMeta = useApp((s) => s.loadMeta);
  const checkAuth = useApp((s) => s.checkAuth);
  const meta = useApp((s) => s.meta);
  const metaError = useApp((s) => s.metaError);
  const user = useApp((s) => s.user);
  const [more, setMore] = useState(false);
  const [analyst, setAnalyst] = useState(false);
  const loc = useLocation();

  useEffect(() => {
    loadMeta();
    checkAuth();
    useApp.getState().loadResume();
  }, [loadMeta, checkAuth]);

  useEffect(() => {
    setMore(false);
    window.scrollTo({ top: 0 });
  }, [loc.pathname]);

  return (
    <div className="shell">
      <a className="skip" href="#main">
        {lang === "fr" ? "Aller au contenu" : "Skip to content"}
      </a>

      <header className="head">
        <Link to="/" style={{ display: "flex", alignItems: "baseline", gap: 6, minWidth: 0 }}>
          <span className="brand">
            YANIS<em>//</em>X
          </span>
          <span className="sub">{tr(lang, "app.tagline")}</span>
        </Link>
        <div className="head-actions">
          <div className="row" style={{ gap: 2 }}>
            {LANGS.map((l) => (
              <button
                key={l.code}
                className="chip"
                style={{ padding: "5px 9px", fontSize: 10 }}
                aria-pressed={lang === l.code}
                onClick={() => setLang(l.code)}
              >
                {l.label}
              </button>
            ))}
          </div>
          <Link className="iconbtn" to="/rechercher" aria-label={tr(lang, "nav.search")}>
            🔎
          </Link>
          <Link className="iconbtn" to="/compte" aria-label={tr(lang, "nav.account")}>
            {user ? "★" : "👤"}
          </Link>
        </div>
      </header>

      {metaError && (
        <div className="note warn" style={{ margin: 14 }}>
          {metaError} — <button className="btn sm ghost" onClick={loadMeta}>{tr(lang, "common.retry")}</button>
        </div>
      )}

      <main id="main">{children}</main>

      {meta && (
        <button className="fab" onClick={() => setAnalyst(true)} aria-label={tr(lang, "home.analyst")}>
          🧠
        </button>
      )}

      <nav className="nav" aria-label={lang === "fr" ? "Navigation principale" : "Main navigation"}>
        {PRIMARY.map((p) =>
          p.to === "/plus" ? (
            <button key={p.to} className={more ? "on" : ""} onClick={() => setMore(true)} aria-haspopup="dialog">
              <span className="ico">{p.ico}</span>
              {tr(lang, p.k)}
            </button>
          ) : (
            <NavLink key={p.to} to={p.to} end={p.to === "/"}>
              {({ isActive }) => (
                <button className={isActive ? "on" : ""} aria-current={isActive ? "page" : undefined} style={{ width: "100%" }}>
                  <span className="ico">{p.ico}</span>
                  {tr(lang, p.k)}
                </button>
              )}
            </NavLink>
          ),
        )}
      </nav>

      <PlayerBar />
      <QuestionSheet />

      {more && (
        <div className="scrim" role="dialog" aria-modal="true" aria-label={tr(lang, "nav.more")} onClick={() => setMore(false)}>
          <div className="sheet" onClick={(e) => e.stopPropagation()}>
            <div className="grab" />
            <div className="eyebrow blood" style={{ marginBottom: 12 }}>
              {tr(lang, "app.identity")}
            </div>
            <div className="grid2">
              {SECONDARY.map((s) => (
                <Link key={s.to} to={s.to} className="card tight" onClick={() => setMore(false)}>
                  <div style={{ fontSize: 18 }}>{s.ico}</div>
                  <div className="h2" style={{ fontSize: 13, marginTop: 5 }}>
                    {tr(lang, s.k)}
                  </div>
                </Link>
              ))}
            </div>
            <div className="tiny" style={{ marginTop: 14 }}>
              {meta?.counts
                ? `${meta.counts.cases} ${lang === "fr" ? "dossiers" : "dossiers"} · ${meta.counts.victims} ${
                    lang === "fr" ? "victimes" : "victims"
                  } · ${meta.counts.sources} ${lang === "fr" ? "sources" : "sources"}`
                : ""}
            </div>
          </div>
        </div>
      )}

      {analyst && <AnalystPanel onClose={() => setAnalyst(false)} />}
    </div>
  );
}

/* ---------------------------------------------------------- 🧠 L'ANALYSTE */
function AnalystPanel({ onClose }: { onClose: () => void }) {
  const lang = useLang();
  const [q, setQ] = useState("");
  const [busy, setBusy] = useState(false);
  const [res, setRes] = useState<Any | null>(null);
  const [err, setErr] = useState<string | null>(null);

  const ask = async (e?: React.FormEvent) => {
    e?.preventDefault();
    if (!q.trim()) return;
    setBusy(true);
    setErr(null);
    try {
      setRes(await api.post<Any>(endpoints.analyst(), { question: q.trim() }));
    } catch (ex: any) {
      setErr(ex.message);
    } finally {
      setBusy(false);
    }
  };

  const suggestions =
    lang === "fr"
      ? ["Qui était Estelle Mouzin ?", "Quelles preuves dans l'affaire Grégory ?", "Que dit la justice dans l'affaire BTK ?"]
      : ["Who was Estelle Mouzin?", "What evidence in the Grégory case?", "What did the court decide in the BTK case?"];

  return (
    <div className="scrim" role="dialog" aria-modal="true" aria-label={tr(lang, "home.analyst")} onClick={onClose}>
      <div className="sheet" onClick={(e) => e.stopPropagation()} style={{ minHeight: "62dvh" }}>
        <div className="grab" />
        <div className="between" style={{ marginBottom: 4 }}>
          <div className="eyebrow blood">🧠 {tr(lang, "home.analyst")}</div>
          <button className="iconbtn" onClick={onClose} aria-label={tr(lang, "common.close")}>
            ✕
          </button>
        </div>
        <p className="small" style={{ marginTop: 0 }}>
          {tr(lang, "home.analyst.hint")}
        </p>

        <form onSubmit={ask} className="field" style={{ marginBottom: 10 }}>
          <span>🔎</span>
          <input
            value={q}
            onChange={(e) => setQ(e.target.value)}
            placeholder={lang === "fr" ? "Pose ta question…" : "Ask your question…"}
            aria-label={tr(lang, "home.analyst")}
          />
          <button className="btn sm primary" type="submit" disabled={busy || !q.trim()}>
            {busy ? "…" : "OK"}
          </button>
        </form>

        <div className="row wrap" style={{ gap: 6, marginBottom: 14 }}>
          {suggestions.map((s) => (
            <button key={s} className="chip" onClick={() => setQ(s)}>
              {s}
            </button>
          ))}
        </div>

        {err && <div className="note warn">{err}</div>}

        {res && !res.documented && (
          <div className="note">
            <strong>{pick(res.answer, lang)}</strong>
            <div className="tiny" style={{ marginTop: 8 }}>
              {pick(res.policy, lang)}
            </div>
          </div>
        )}

        {res?.documented && (
          <div className="stack">
            <div className="tiny">{pick(res.answer, lang)}</div>
            {res.extracts.map((x: Any, i: number) => (
              <article className="card tight" key={i}>
                <div className="row wrap" style={{ gap: 6, marginBottom: 6 }}>
                  <span className="badge">{x.type}</span>
                  {x.case && <Link className="tiny" to={`/dossiers/${x.case}`}>{x.case}</Link>}
                  <Reliability level={x.reliability} />
                </div>
                <div style={{ fontSize: "14.5px" }}>
                  {x.label && typeof x.label === "object" && (x.label.fr || x.label.en) ? <strong><Bi_ v={x.label} /> — </strong> : null}
                  {typeof x.body === "object" && x.body !== null ? <Bi_ v={x.body} /> : String(x.body ?? "")}
                </div>
                <SourceLine source={x.source} compact />
                {x.href && (
                  <Link className="btn sm ghost" style={{ marginTop: 9 }} to={x.href}>
                    {tr(lang, "common.see")} →
                  </Link>
                )}
              </article>
            ))}
            <div className="tiny">{pick(res.no_speculation, lang)}</div>
          </div>
        )}

        {!res && !busy && (
          <div className="empty">
            {lang === "fr"
              ? "L'Analyste ne répond qu'à partir de données documentées et sourcées. Il n'invente jamais et ne complète jamais un trou du dossier."
              : "The Analyst answers only from documented, sourced data. It never invents and never fills a gap in the file."}
          </div>
        )}
      </div>
    </div>
  );
}
