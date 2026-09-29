import { useState } from "react";
import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi, fmtDate } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import { usePlayer, fmtTime } from "../state/player";
import CaseCard from "../components/CaseCard";
import { Bi_, Cover, Loading, ErrorState, PageTitle, StatusBadge, useLang } from "../components/ui";

const W = 720;
const H = 360;
const proj = (lat: number, lon: number) => ({ x: ((lon + 180) / 360) * W, y: ((90 - lat) / 180) * H });

export default function Home() {
  const lang = useLang();
  const meta = useApp((s) => s.meta);
  const resume = useApp((s) => s.resume);
  const loadResume = useApp((s) => s.loadResume);
  const load = usePlayer((s) => s.load);
  const play = usePlayer((s) => s.play);
  const { data, loading, error, reload } = useApi<Any>(endpoints.cases());
  const mapApi = useApi<Any>(endpoints.map());

  const [filterTab, setFilterTab] = useState<"all" | "free" | "unsolved" | "resolved">("all");
  const [selectedPoint, setSelectedPoint] = useState<Any | null>(null);

  const cases: Any[] = data?.cases || [];
  const free = cases.filter((c) => c.tier === "FREE");
  const unsolved = cases.filter((c) => ["UNSOLVED", "ONGOING", "PARTIALLY_RESOLVED"].includes(c.status));
  const resolved = cases.filter((c) => c.status === "RESOLVED");

  let displayedCases = cases;
  if (filterTab === "free") displayedCases = free;
  else if (filterTab === "unsolved") displayedCases = unsolved;
  else if (filterTab === "resolved") displayedCases = resolved;

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

  const points: Any[] = (mapApi.data?.case_points || []).filter((p: Any) => p.lat != null && p.lon != null);

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

      {/* VRAIE CARTE MONDE INTERACTIVE SUR L'ACCUEIL */}
      <section className="block-sec" style={{ marginBottom: 18 }}>
        <div className="between" style={{ marginBottom: 8 }}>
          <h2 className="h3">🌍 {lang === "fr" ? "Carte des dossiers mondiaux" : "Global dossiers map"}</h2>
          <Link className="tiny" to="/explorer/carte">{lang === "fr" ? "Agrandir" : "Full map"} →</Link>
        </div>
        <div className="card flush" style={{ overflow: "hidden", background: "#0c0e12" }}>
          <svg className="map" viewBox={`0 0 ${W} ${H}`} style={{ width: "100%", height: "auto", display: "block" }}>
            <rect width={W} height={H} fill="#0c0e12" />
            <g stroke="#1c2027" strokeWidth="0.6">
              {Array.from({ length: 13 }).map((_, i) => (
                <line key={`m${i}`} x1={(i * W) / 12} y1="0" x2={(i * W) / 12} y2={H} />
              ))}
              {Array.from({ length: 7 }).map((_, i) => (
                <line key={`p${i}`} x1="0" y1={(i * H) / 6} x2={W} y2={(i * H) / 6} />
              ))}
            </g>
            <line x1="0" y1={H / 2} x2={W} y2={H / 2} stroke="#2b3138" strokeWidth="1" strokeDasharray="4 4" />
            
            {/* Amérique du Nord */}
            <path d="M 50 40 L 110 35 L 170 35 L 220 50 L 260 70 L 250 110 L 210 130 L 190 170 L 160 150 L 120 120 L 70 90 Z" fill="#181d24" stroke="#262e38" strokeWidth="1" />
            {/* Amérique du Sud */}
            <path d="M 180 180 L 230 190 L 260 230 L 240 310 L 200 330 L 180 270 L 170 210 Z" fill="#181d24" stroke="#262e38" strokeWidth="1" />
            {/* Europe */}
            <path d="M 340 50 L 400 45 L 430 70 L 410 110 L 360 115 L 340 85 Z" fill="#181d24" stroke="#262e38" strokeWidth="1" />
            {/* Afrique */}
            <path d="M 340 125 L 420 125 L 440 180 L 410 280 L 370 280 L 330 200 L 330 140 Z" fill="#181d24" stroke="#262e38" strokeWidth="1" />
            {/* Asie & Moyen-Orient */}
            <path d="M 430 45 L 610 40 L 640 110 L 580 180 L 510 170 L 470 140 L 425 105 Z" fill="#181d24" stroke="#262e38" strokeWidth="1" />
            {/* Océanie / Australie */}
            <path d="M 550 230 L 630 230 L 630 290 L 560 290 Z" fill="#181d24" stroke="#262e38" strokeWidth="1" />

            {points.map((p) => {
              const { x, y } = proj(p.lat, p.lon);
              const color = p.status === "RESOLVED" ? "#3f9e63" : p.status === "UNSOLVED" ? "#c2603a" : "#c9a227";
              const isSel = selectedPoint?.slug === p.slug;
              return (
                <g key={p.slug} style={{ cursor: "pointer" }} onClick={() => setSelectedPoint(p)}>
                  <circle cx={x} cy={y} r={isSel ? "14" : "10"} fill={color} opacity={isSel ? "0.4" : "0.2"} />
                  <circle cx={x} cy={y} r={isSel ? "6" : "4.5"} fill={color} stroke="#fff" strokeWidth={isSel ? "2" : "1"} />
                </g>
              );
            })}
          </svg>
        </div>
        {selectedPoint && (
          <div className="card tight" style={{ marginTop: 8 }}>
            <div className="between">
              <div>
                <div className="h2" style={{ fontSize: 14 }}><Bi_ v={selectedPoint.title} /></div>
                <div className="tiny">{selectedPoint.country} · {selectedPoint.city || selectedPoint.region}</div>
              </div>
              <Link className="btn sm primary" to={`/dossiers/${selectedPoint.slug}`}>
                {tr(lang, "common.open")} →
              </Link>
            </div>
          </div>
        )}
      </section>

      {/* REPRISE */}
      {resumeRows.length > 0 && (
        <section className="block-sec">
          <div className="between" style={{ marginBottom: 8 }}>
            <h2 className="h3">{tr(lang, "home.continue")}</h2>
            <Link className="tiny" to="/bibliotheque">{tr(lang, "nav.library")} →</Link>
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
                  <span className="badge">▶</span>
                </div>
              </button>
            ))}
          </div>
        </section>
      )}

      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}

      {data && (
        <>
          {/* ACCÈS LIBRE ADAPTÉ À L'ÉCRAN */}
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

          {/* ONGLET DOSSIERS PLUTÔT QUE TOUT EN BLOC */}
          <section className="block-sec">
            <div className="between" style={{ marginBottom: 8 }}>
              <h2 className="h3">{tr(lang, "home.dossiers")}</h2>
              <span className="tiny">{displayedCases.length}</span>
            </div>
            <div className="tabs" style={{ marginBottom: 12 }}>
              <button className={`chip ${filterTab === "all" ? "on" : ""}`} onClick={() => setFilterTab("all")}>
                {lang === "fr" ? "Tous" : "All"} ({cases.length})
              </button>
              <button className={`chip ${filterTab === "free" ? "on" : ""}`} onClick={() => setFilterTab("free")}>
                {lang === "fr" ? "Accès libre" : "Free"} ({free.length})
              </button>
              <button className={`chip ${filterTab === "unsolved" ? "on" : ""}`} onClick={() => setFilterTab("unsolved")}>
                {lang === "fr" ? "Non résolus" : "Unsolved"} ({unsolved.length})
              </button>
              <button className={`chip ${filterTab === "resolved" ? "on" : ""}`} onClick={() => setFilterTab("resolved")}>
                {lang === "fr" ? "Résolus" : "Resolved"} ({resolved.length})
              </button>
            </div>
            <div className="stack">
              {displayedCases.map((c) => (
                <CaseCard key={c.slug} c={c} />
              ))}
            </div>
          </section>
        </>
      )}
    </>
  );
}
