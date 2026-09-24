import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi, fmtDate } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import { usePlayer, fmtTime } from "../state/player";
import CaseCard from "../components/CaseCard";
import { Bi_, Cover, Loading, ErrorState, PageTitle, useLang } from "../components/ui";

export default function Home() {
  const lang = useLang();
  const meta = useApp((s) => s.meta);
  const resume = useApp((s) => s.resume);
  const loadResume = useApp((s) => s.loadResume);
  const load = usePlayer((s) => s.load);
  const play = usePlayer((s) => s.play);
  const { data, loading, error, reload } = useApi<Any>(endpoints.cases());

  const cases: Any[] = data?.cases || [];
  const free = cases.filter((c) => c.tier === "FREE");
  const unsolved = cases.filter((c) => ["UNSOLVED", "ONGOING", "PARTIALLY_RESOLVED"].includes(c.status));
  const recent = [...cases].sort((a, b) => (b.published_at || "").localeCompare(a.published_at || ""));
  const hero = cases[0];

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
    <>
      <PageTitle eyebrow={tr(lang, "app.identity")} title={<>YANIS<em style={{ color: "var(--blood-bright)", fontStyle: "normal" }}>//</em>X</>}>
        <p className="lede" style={{ marginTop: 2 }}>
          {meta?.app ? pick(meta.app.tagline, lang) : tr(lang, "app.tagline")}
        </p>
      </PageTitle>

      {meta?.signature_line && (
        <div className="note" style={{ marginBottom: 16 }}>
          <em>
            <Bi_ v={meta.signature_line} />
          </em>
        </div>
      )}

      {hero && (
        <Link to={`/dossiers/${hero.slug}`} className="hero" style={{ display: "block", marginBottom: 18 }}>
          <Cover slug={hero.slug} title={hero.title} country={hero.country} period={hero.period_label} tall />
          <div className="overlay">
            <div className="eyebrow blood">{tr(lang, "home.latest")}</div>
            <div className="h1" style={{ fontSize: 21, margin: "6px 0 4px" }}>
              <Bi_ v={hero.title} />
            </div>
            <div className="small">
              {hero.country_name?.[lang] || hero.country} · <Bi_ v={hero.period_label} /> ·{" "}
              {pick(meta?.statuses?.find((s: Any) => s.key === hero.status)?.label, lang)}
            </div>
          </div>
        </Link>
      )}

      {resumeRows.length > 0 && (
        <section className="block-sec">
          <div className="between" style={{ marginBottom: 8 }}>
            <h2 className="h3">{tr(lang, "home.continue")}</h2>
            <Link className="tiny" to="/bibliotheque">
              {tr(lang, "nav.library")} →
            </Link>
          </div>
          <div className="stack">
            {resumeRows.map((r, i) => (
              <button key={i} className="card tight" style={{ textAlign: "left" }} onClick={() => openResume(r)}>
                <div className="between">
                  <div style={{ minWidth: 0 }}>
                    <div className="h2" style={{ fontSize: 13.5 }}>
                      {r.episode_title ? <Bi_ v={r.episode_title} /> : r.ref || r.case_id}
                    </div>
                    <div className="tiny mono">
                      {r.case_id || r.ref} · {fmtTime(r.at_sec || 0)}
                      {r.duration_sec ? ` / ${fmtTime(r.duration_sec)}` : ""}
                    </div>
                  </div>
                  <span className="playbtn" style={{ width: 38, height: 38, flex: "0 0 38px" }}>
                    ▶
                  </span>
                </div>
                {r.duration_sec ? (
                  <div className="progressline" style={{ marginTop: 9 }}>
                    <i style={{ width: `${Math.min(100, ((r.at_sec || 0) / r.duration_sec) * 100)}%` }} />
                  </div>
                ) : null}
              </button>
            ))}
          </div>
        </section>
      )}

      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}

      {data && (
        <>
          <section className="block-sec">
            <div className="between" style={{ marginBottom: 8 }}>
              <h2 className="h3">{tr(lang, "home.free")}</h2>
              <span className="tiny">{free.length}</span>
            </div>
            <div className="rail">
              {free.map((c) => (
                <CaseCard key={c.slug} c={c} compact />
              ))}
            </div>
          </section>

          <section className="block-sec">
            <div className="between" style={{ marginBottom: 8 }}>
              <h2 className="h3">{tr(lang, "home.unsolved")}</h2>
              <Link className="tiny" to="/cold-cases">
                {tr(lang, "nav.coldcases")} →
              </Link>
            </div>
            <div className="rail">
              {unsolved.map((c) => (
                <CaseCard key={c.slug} c={c} compact />
              ))}
            </div>
          </section>

          <section className="block-sec">
            <div className="between" style={{ marginBottom: 8 }}>
              <h2 className="h3">{tr(lang, "home.dossiers")}</h2>
              <Link className="tiny" to="/bibliotheque">
                {tr(lang, "common.all")} →
              </Link>
            </div>
            <div className="stack">
              {recent.map((c) => (
                <CaseCard key={c.slug} c={c} />
              ))}
            </div>
          </section>

          <Link to="/memoire" className="card" style={{ display: "block", marginBottom: 14 }}>
            <div className="between">
              <div>
                <div className="eyebrow blood">🕯 {tr(lang, "nav.memory")}</div>
                <div className="h2" style={{ fontSize: 15, marginTop: 5 }}>
                  {tr(lang, "home.memory")}
                </div>
                <div className="tiny" style={{ marginTop: 4 }}>
                  {meta?.counts?.victims} {lang === "fr" ? "fiches victimes" : "victim files"} ·{" "}
                  {lang === "fr" ? "toujours en accès libre" : "always free"}
                </div>
              </div>
              <span className="candle">🕯</span>
            </div>
          </Link>

          <section className="block-sec">
            <h2 className="h3" style={{ marginBottom: 9 }}>
              {tr(lang, "home.journey")}
            </h2>
            <div className="tiny" style={{ letterSpacing: "0.08em", lineHeight: 2 }}>
              {lang === "fr"
                ? "ÉCOUTER → DÉCOUVRIR → RÉFLÉCHIR → QUESTIONNER → ANALYSER → COMPRENDRE → ENQUÊTER → APPRENDRE → RENDRE HOMMAGE"
                : "LISTEN → DISCOVER → REFLECT → QUESTION → ANALYSE → UNDERSTAND → INVESTIGATE → LEARN → PAY HOMAGE"}
            </div>
          </section>
        </>
      )}
    </>
  );
}
