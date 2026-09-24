import { Link, useParams, useSearchParams } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { usePlayer, fmtTime } from "../state/player";
import { FullPlayer } from "../components/Player";
import { Bi_, Cover, ErrorState, Loading, PageTitle, useLang } from "../components/ui";
import { useState } from "react";

export default function Podcasts() {
  const lang = useLang();
  const [params] = useSearchParams();
  const caseFilter = params.get("case") || "";
  const [mode, setMode] = useState<string>("all");
  const query = new URLSearchParams();
  if (caseFilter) query.set("case", caseFilter);
  if (mode !== "all") query.set("mode", mode);
  const suffix = query.toString() ? `?${query.toString()}` : "";
  const { data, loading, error, reload } = useApi<Any>(endpoints.episodes(suffix), [mode, caseFilter]);
  const load = usePlayer((s) => s.load);
  const play = usePlayer((s) => s.play);
  const current = usePlayer((s) => s.episode);

  const modes: Any[] = data?.modes || [];

  return (
    <>
      <PageTitle eyebrow="🎧" title={tr(lang, "nav.podcasts")}>
        <p className="small" style={{ marginTop: 0 }}>
          {lang === "fr"
            ? "Chaque épisode s'arrête à un moment stratégique : une question, une explication, puis la lecture reprend."
            : "Each episode stops at a strategic moment: a question, an explanation, then playback resumes."}
        </p>
      </PageTitle>

      <div className="tabs">
        <button className={`chip ${mode === "all" ? "on" : ""}`} aria-pressed={mode === "all"} onClick={() => setMode("all")}>
          {tr(lang, "common.all")}
        </button>
        {modes.map((m: Any) => (
          <button key={m.key} className={`chip ${mode === m.key ? "on" : ""}`} aria-pressed={mode === m.key} onClick={() => setMode(m.key)} title={pick(m.description, lang)}>
            {pick(m.label, lang)}
          </button>
        ))}
      </div>

      {mode !== "all" && modes.find((m) => m.key === mode) && (
        <div className="note neutral" style={{ marginBottom: 12 }}>
          <Bi_ v={modes.find((m: Any) => m.key === mode)?.description} />
        </div>
      )}

      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}

      {data && (
        <div className="stack">
          {data.episodes.length === 0 && (
            <div className="empty">{lang === "fr" ? "Aucun épisode pour ce mode." : "No episode for this mode."}</div>
          )}
          {data.episodes.map((ep: Any) => (
            <article key={ep.id} className="card flush">
              <div style={{ padding: 12 }}>
                <div className="between" style={{ marginBottom: 7 }}>
                  <Link className="eyebrow blood" to={`/dossiers/${ep.case_id}`}>
                    {ep.case_id}
                  </Link>
                  <span className="tiny mono">
                    {fmtTime(ep.duration_sec)} · ép. {ep.number}
                  </span>
                </div>
                <h2 className="h2" style={{ fontSize: 16, marginBottom: 5 }}>
                  <Bi_ v={ep.title} />
                </h2>
                <p className="small" style={{ margin: "0 0 10px" }}>
                  <Bi_ v={ep.description} />
                </p>
                <div className="row wrap" style={{ gap: 6, marginBottom: 11 }}>
                  {(ep.modes || []).map((m: string) => (
                    <span key={m} className="badge">
                      {pick(modes.find((x: Any) => x.key === m)?.label, lang) || m}
                    </span>
                  ))}
                  {ep.audio_status === "produced" ? (
                    <span className="badge confirmed"><span className="dot" />{tr(lang, "player.audio")}</span>
                  ) : (
                    <span className="badge"><span className="dot" />{tr(lang, "player.transcript")}</span>
                  )}
                </div>
                <div className="row" style={{ gap: 8 }}>
                  <button
                    className="btn sm primary"
                    onClick={async () => {
                      await load(ep.id);
                      play();
                    }}
                  >
                    ▶ {tr(lang, "case.listen")}
                  </button>
                  <Link className="btn sm ghost" to={`/podcasts/${ep.id}`}>
                    {tr(lang, "player.transcript")}
                  </Link>
                  {current?.id === ep.id && <span className="tiny">{lang === "fr" ? "en cours" : "playing"}</span>}
                </div>
              </div>
            </article>
          ))}
        </div>
      )}
    </>
  );
}

export function EpisodePage() {
  const { id = "" } = useParams();
  const lang = useLang();
  const num = Number(id);
  const { data, loading, error, reload } = useApi<Any>(Number.isFinite(num) ? endpoints.episode(num) : null, [id]);

  if (loading) return <Loading />;
  if (error) return <ErrorState message={error} onRetry={reload} />;
  if (!data) return null;

  return (
    <>
      <Link className="tiny" to="/podcasts" style={{ display: "inline-block", padding: "14px 0 6px" }}>
        ← {tr(lang, "nav.podcasts")}
      </Link>
      <div className="hero" style={{ marginBottom: 14 }}>
        <Cover slug={data.case_id} title={data.title} period={{ fr: `ép. ${data.number}`, en: `ep. ${data.number}` }} tall />
        <div className="overlay">
          <div className="eyebrow blood">
            <Link to={`/dossiers/${data.case_id}`}>{data.case_id}</Link>
          </div>
          <div className="h1" style={{ fontSize: 20, margin: "6px 0 0" }}>
            <Bi_ v={data.title} />
          </div>
        </div>
      </div>
      <FullPlayer episodeId={num} />
      <div className="card" style={{ marginTop: 10 }}>
        <div className="h3" style={{ marginBottom: 8 }}>{tr(lang, "common.sources")}</div>
        <Link className="btn sm wide" to={`/dossiers/${data.case_id}/sources`}>
          {tr(lang, "case.sources")} →
        </Link>
      </div>
    </>
  );
}
