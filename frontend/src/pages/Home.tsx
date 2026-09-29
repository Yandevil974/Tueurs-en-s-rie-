import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import { usePlayer, fmtTime } from "../state/player";
import CaseCard from "../components/CaseCard";
import WorldCaseMap from "../components/WorldCaseMap";
import { Bi_, Cover, ErrorState, Loading, useLang } from "../components/ui";
import { useState } from "react";

type CaseFilter = "all" | "unresolved" | "resolved";

export default function Home() {
  const lang = useLang();
  const meta = useApp((s) => s.meta);
  const resume = useApp((s) => s.resume);
  const loadResume = useApp((s) => s.loadResume);
  const load = usePlayer((s) => s.load);
  const play = usePlayer((s) => s.play);
  const [filter, setFilter] = useState<CaseFilter>("all");
  const casesRequest = useApi<Any>(endpoints.cases());
  const worldRequest = useApi<Any>(endpoints.world());

  const cases: Any[] = casesRequest.data?.cases || [];
  const recent = [...cases].sort((a, b) => (b.published_at || "").localeCompare(a.published_at || ""));
  const featured = recent[0];
  const unresolved = cases.filter((c) => ["UNSOLVED", "ONGOING", "PARTIALLY_RESOLVED"].includes(c.status));
  const resolved = cases.filter((c) => c.status === "RESOLVED");
  const shownCases = filter === "unresolved" ? unresolved : filter === "resolved" ? resolved : recent;
  const resumeRows: Any[] = (resume?.audio || []).slice(0, 4);

  const openResume = async (row: Any) => {
    if (row.episode_id) {
      await load(row.episode_id, row.at_sec || 0);
      play();
    } else {
      loadResume();
    }
  };

  return (
    <div className="home-page">
      <section className="home-welcome">
        <div className="home-welcome-orbit" aria-hidden="true" />
        <div className="home-welcome-copy">
          <div className="eyebrow blood">{tr(lang, "app.identity")} · {tr(lang, "app.tagline")}</div>
          <div className="home-wordmark" aria-label="YANIS X">
            YANIS<span>//X</span>
          </div>
          <h1>{tr(lang, "home.hero.title")}</h1>
          <p>{tr(lang, "home.hero.description")}</p>
          <div className="home-hero-actions">
            <Link className="btn primary sm" to="/bibliotheque">{tr(lang, "home.hero.browse")} <span aria-hidden="true">→</span></Link>
            <Link className="btn ghost sm" to="/memoire">🕯 {tr(lang, "nav.memory")}</Link>
          </div>
        </div>
        <div className="home-stats" aria-label={lang === "fr" ? "Le catalogue" : "The catalogue"}>
          <div><strong>{meta?.counts?.cases ?? cases.length}</strong><span>{lang === "fr" ? "dossiers" : "dossiers"}</span></div>
          <div><strong>{meta?.counts?.victims ?? "—"}</strong><span>{lang === "fr" ? "victimes documentées" : "documented victims"}</span></div>
          <div><strong>{meta?.counts?.sources ?? "—"}</strong><span>{lang === "fr" ? "sources" : "sources"}</span></div>
        </div>
      </section>

      {meta?.signature_line && (
        <blockquote className="home-signature">
          <span className="eyebrow">{lang === "fr" ? "La ligne éditoriale" : "Editorial principle"}</span>
          <p><Bi_ v={meta.signature_line} /></p>
        </blockquote>
      )}

      <WorldCaseMap
        cases={cases}
        continents={worldRequest.data?.continents || []}
        loading={casesRequest.loading || worldRequest.loading}
      />

      {resumeRows.length > 0 && (
        <section className="block-sec home-resume">
          <div className="between home-section-heading">
            <div>
              <div className="eyebrow blood">{lang === "fr" ? "Votre écoute" : "Your listening"}</div>
              <h2 className="h2">{tr(lang, "home.continue")}</h2>
            </div>
            <Link className="tiny" to="/bibliotheque">{tr(lang, "nav.library")} →</Link>
          </div>
          <div className="stack">
            {resumeRows.map((row: Any, index: number) => (
              <button key={`${row.ref || row.case_id}-${index}`} className="resume-row" onClick={() => openResume(row)}>
                <span className="resume-play" aria-hidden="true">▶</span>
                <span className="resume-copy">
                  <strong>{row.episode_title ? <Bi_ v={row.episode_title} /> : row.ref || row.case_id}</strong>
                  <small>{row.case_id || row.ref} · {fmtTime(row.at_sec || 0)}{row.duration_sec ? ` / ${fmtTime(row.duration_sec)}` : ""}</small>
                  {row.duration_sec > 0 && <span className="progressline"><i style={{ width: `${Math.min(100, ((row.at_sec || 0) / row.duration_sec) * 100)}%` }} /></span>}
                </span>
              </button>
            ))}
          </div>
        </section>
      )}

      {casesRequest.loading && <Loading />}
      {casesRequest.error && <ErrorState message={casesRequest.error} onRetry={casesRequest.reload} />}

      {featured && (
        <section className="home-featured block-sec">
          <div className="between home-section-heading">
            <div>
              <div className="eyebrow blood">{tr(lang, "home.latest")}</div>
              <h2 className="h2">{lang === "fr" ? "À la une" : "Featured dossier"}</h2>
            </div>
            <Link className="tiny" to="/bibliotheque">{tr(lang, "common.all")} →</Link>
          </div>
          <Link to={`/dossiers/${featured.slug}`} className="home-feature-card">
            <div className="home-feature-cover">
              <Cover slug={featured.slug} title={featured.title} country={featured.country} period={featured.period_label} />
            </div>
            <div className="home-feature-copy">
              <div className="row wrap" style={{ gap: 6 }}>
                <span className="badge blood">{featured.country_name?.[lang] || featured.country}</span>
                <span className="tiny"><Bi_ v={featured.period_label} /></span>
              </div>
              <h3><Bi_ v={featured.title} /></h3>
              <p><Bi_ v={featured.subtitle || featured.summary} /></p>
              <span className="home-feature-link">{tr(lang, "common.open")} <span aria-hidden="true">→</span></span>
            </div>
          </Link>
        </section>
      )}

      {casesRequest.data && (
        <section className="block-sec home-catalogue">
          <div className="between home-section-heading">
            <div>
              <div className="eyebrow blood">{lang === "fr" ? "Le catalogue" : "The catalogue"}</div>
              <h2 className="h2">{tr(lang, "home.dossiers")}</h2>
            </div>
            <span className="badge">{shownCases.length} {lang === "fr" ? "dossier(s)" : "dossier(s)"}</span>
          </div>
          <div className="tabs home-case-filters" role="group" aria-label={lang === "fr" ? "Filtrer les dossiers" : "Filter dossiers"}>
            <button className={`chip ${filter === "all" ? "on" : ""}`} aria-pressed={filter === "all"} onClick={() => setFilter("all")}>
              {lang === "fr" ? "Tous" : "All"} <span>{cases.length}</span>
            </button>
            <button className={`chip ${filter === "unresolved" ? "on" : ""}`} aria-pressed={filter === "unresolved"} onClick={() => setFilter("unresolved")}>
              {lang === "fr" ? "Non résolues / en cours" : "Unresolved / ongoing"} <span>{unresolved.length}</span>
            </button>
            <button className={`chip ${filter === "resolved" ? "on" : ""}`} aria-pressed={filter === "resolved"} onClick={() => setFilter("resolved")}>
              {lang === "fr" ? "Résolues" : "Resolved"} <span>{resolved.length}</span>
            </button>
          </div>
          <div className="home-case-grid">
            {shownCases.map((caseFile) => <CaseCard key={caseFile.slug} c={caseFile} />)}
          </div>
          {!shownCases.length && <div className="empty">{lang === "fr" ? "Aucun dossier dans cette sélection." : "No dossier in this selection."}</div>}
        </section>
      )}

      <Link to="/memoire" className="home-memory-link">
        <span className="home-memory-icon" aria-hidden="true">🕯</span>
        <span><small>{lang === "fr" ? "Au centre de chaque dossier" : "At the heart of every dossier"}</small><strong>{tr(lang, "home.memory")}</strong></span>
        <span className="home-feature-link" aria-hidden="true">→</span>
      </Link>
    </div>
  );
}
