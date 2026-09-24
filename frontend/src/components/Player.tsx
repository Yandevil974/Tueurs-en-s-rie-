import { useEffect } from "react";
import { Link } from "react-router-dom";
import { usePlayer, fmtTime, type Segment } from "../state/player";
import { useApp } from "../state/app";
import { pick, tr } from "../lib/i18n";
import { Bi_, Reliability, SourceLine, useLang } from "./ui";
import type { Any } from "../lib/api";

/* ------------------------------------------------- barre persistante */
export function PlayerBar() {
  const lang = useLang();
  const ep = usePlayer((s) => s.episode);
  const playing = usePlayer((s) => s.playing);
  const position = usePlayer((s) => s.position);
  const duration = usePlayer((s) => s.duration);
  const toggle = usePlayer((s) => s.toggle);
  const seek = usePlayer((s) => s.seek);
  const pending = usePlayer((s) => s.pending);

  useEffect(() => {
    document.documentElement.style.setProperty("--player-h", ep ? "74px" : "0px");
  }, [ep]);

  if (!ep) return null;
  const pct = duration ? Math.min(100, (position / duration) * 100) : 0;

  return (
    <div className="playerbar">
      <div
        className="track"
        role="slider"
        tabIndex={0}
        aria-label={tr(lang, "player.transcript")}
        aria-valuenow={Math.round(position)}
        aria-valuemin={0}
        aria-valuemax={Math.round(duration)}
        onClick={(e) => {
          const r = (e.currentTarget as HTMLElement).getBoundingClientRect();
          seek(((e.clientX - r.left) / r.width) * duration);
        }}
        onKeyDown={(e) => {
          if (e.key === "ArrowRight") seek(position + 15);
          if (e.key === "ArrowLeft") seek(position - 15);
        }}
      >
        <i style={{ width: `${pct}%` }} />
      </div>
      <div className="rowline">
        <button className="playbtn" onClick={toggle} aria-label={playing ? tr(lang, "player.pause") : tr(lang, "player.play")}>
          {playing ? "❚❚" : "▶"}
        </button>
        <div className="meta">
          <div className="t">
            <Bi_ v={ep.title} />
          </div>
          <div className="s">
            {fmtTime(position)} / {fmtTime(duration)} · {ep.case_id}
            {pending ? ` · ⏸ ${tr(lang, "player.pausepoint")}` : ""}
          </div>
        </div>
        <Link className="iconbtn" to={`/podcasts/${ep.id}`} aria-label={tr(lang, "common.open")}>
          ⤢
        </Link>
      </div>
    </div>
  );
}

/* ------------------------------------------------- question + explication */
export function QuestionSheet() {
  const lang = useLang();
  const pending = usePlayer((s) => s.pending);
  const explanation = usePlayer((s) => s.explanation);
  const answering = usePlayer((s) => s.answering);
  const submit = usePlayer((s) => s.submit);
  const skip = usePlayer((s) => s.skipQuestion);
  const close = usePlayer((s) => s.closeExplanation);
  const chosen = usePlayer((s) => (s.pending ? s.answered[s.pending.id] : undefined));

  if (!pending) return null;
  const q: Any = pending;

  return (
    <div className="scrim center" role="dialog" aria-modal="true" aria-label={tr(lang, "question.title")}>
      <div className="sheet">
        <div className="eyebrow blood">{tr(lang, "question.title")}</div>
        <h2 className="h2" style={{ margin: "8px 0 4px" }}>
          <Bi_ v={q.prompt} />
        </h2>
        <div className="row wrap" style={{ gap: 6, marginBottom: 14 }}>
          <span className="badge">
            <Bi_ v={q.kind_label} />
          </span>
          {q.at_sec != null && <span className="badge mono">{fmtTime(q.at_sec)}</span>}
        </div>

        {!explanation ? (
          <>
            <div className="stack">
              {(q.choices || []).map((c: Any) => (
                <button
                  key={c.id}
                  className={`choice ${chosen === c.id ? "picked" : ""}`}
                  disabled={answering}
                  onClick={() => submit(c.id)}
                >
                  <span className="key">{String(c.id).toUpperCase()}</span>
                  <span>
                    <Bi_ v={c.label} />
                  </span>
                </button>
              ))}
            </div>
            <div className="row" style={{ marginTop: 14, justifyContent: "space-between" }}>
              <button className="btn sm ghost" onClick={skip} disabled={answering}>
                {tr(lang, "question.skip")}
              </button>
              {answering && <span className="tiny">{tr(lang, "common.loading")}</span>}
            </div>
          </>
        ) : (
          <Explanation ex={explanation} source={explanation.source} onDone={close} />
        )}
      </div>
    </div>
  );
}

function Explanation({ ex, source, onDone }: { ex: Any; source?: Any; onDone: () => void }) {
  const lang = useLang();
  if (ex.error) {
    return (
      <div>
        <div className="note warn">{ex.error}</div>
        <button className="btn wide" style={{ marginTop: 14 }} onClick={onDone}>
          {tr(lang, "player.resume")}
        </button>
      </div>
    );
  }
  const e = ex.explanation?.[lang] || ex.explanation?.fr || {};
  const rows: [string, string][] = [
    ["question.investigators", e.whatInvestigatorsKnew],
    ["question.experts", e.whatExpertsProposed],
    ["question.documented", e.documented],
    ["question.hypothetical", e.hypothetical],
    ["question.couldnotknow", e.whatYouCouldNotKnow],
  ];
  return (
    <div>
      <div className="eyebrow" style={{ marginBottom: 10 }}>
        {tr(lang, "question.explanation")}
      </div>
      <div className="stack" style={{ gap: 12 }}>
        {rows.map(([k, v]) =>
          v ? (
            <div key={k}>
              <div className="h3" style={{ marginBottom: 4 }}>
                {tr(lang, k)}
              </div>
              <p style={{ margin: 0, fontSize: "14.5px", color: "var(--bone-dim)" }}>{v}</p>
            </div>
          ) : null,
        )}
        {e.answer_note && (
          <div className="note">
            <strong>{lang === "fr" ? "Correction" : "Answer"} — </strong>
            {e.answer_note}
          </div>
        )}
      </div>
      <SourceLine source={source} />
      <div className="tiny" style={{ margin: "14px 0 10px" }}>
        {tr(lang, "question.reward")}
      </div>
      <button className="btn primary wide" onClick={onDone}>
        ▶ {tr(lang, "player.resume")}
      </button>
    </div>
  );
}

/* ------------------------------------------------- lecteur complet */
export function FullPlayer({ episodeId }: { episodeId: number }) {
  const lang = useLang();
  const st = usePlayer();
  const ep = st.episode;

  useEffect(() => {
    if (!ep || ep.id !== episodeId) st.load(episodeId);
    return () => {
      /* la lecture continue en arrière-plan : la barre persistante prend le relais */
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [episodeId]);

  if (st.loading) return <div className="stack"><div className="skeleton" style={{ height: 90 }} /><div className="skeleton" style={{ height: 20 }} /></div>;
  if (st.error) return <div className="note warn">{st.error}</div>;
  if (!ep) return null;

  const segments: Segment[] = ep.transcript?.segments || [];
  const idx = st.currentIndex();
  const pct = st.duration ? (st.position / st.duration) * 100 : 0;
  const nextPause = st.nextPauseAt();

  return (
    <div className="fullplayer">
      <div className="card">
        <div className="between" style={{ marginBottom: 10 }}>
          <div className="eyebrow blood">🎧 {ep.case_id}</div>
          <div className="row" style={{ gap: 6 }}>
            {(ep.modes || []).slice(0, 3).map((m: string) => (
              <span key={m} className="badge">
                {m}
              </span>
            ))}
          </div>
        </div>
        <h2 className="h2" style={{ marginBottom: 6 }}>
          <Bi_ v={ep.title} />
        </h2>
        <p className="small" style={{ margin: "0 0 12px" }}>
          <Bi_ v={ep.description} />
        </p>

        <div className="progressline" style={{ marginBottom: 6 }}>
          <i style={{ width: `${pct}%` }} />
        </div>
        <div className="between tiny" style={{ marginBottom: 12 }}>
          <span className="mono">
            {fmtTime(st.position)} / {fmtTime(st.duration)}
          </span>
          <span className="mono">
            {st.usingAudio ? tr(lang, "player.audio") : tr(lang, "player.transcript")}
            {nextPause != null ? ` · ⏸ ${fmtTime(nextPause)}` : ""}
          </span>
        </div>

        <div className="row wrap" style={{ gap: 8 }}>
          <button className="playbtn" onClick={st.toggle} aria-label={st.playing ? tr(lang, "player.pause") : tr(lang, "player.play")}>
            {st.playing ? "❚❚" : "▶"}
          </button>
          <button className="btn sm" onClick={() => st.nudge(-15)}>
            −15s
          </button>
          <button className="btn sm" onClick={() => st.nudge(30)}>
            +30s
          </button>
          {[0.75, 1, 1.25, 1.5].map((s) => (
            <button key={s} className={`chip ${st.speed === s ? "on" : ""}`} onClick={() => st.setSpeed(s)} aria-pressed={st.speed === s}>
              ×{s}
            </button>
          ))}
        </div>

        {(st.audioMissing || !st.usingAudio) && (
          <div className="note neutral" style={{ marginTop: 12 }}>
            {tr(lang, "player.script")}
          </div>
        )}

        {Array.isArray(ep.chapters) && ep.chapters.length > 0 && (
          <div className="tabs" style={{ marginTop: 12 }}>
            {ep.chapters.map((ch: Any, i: number) => (
              <button key={i} className="chip" onClick={() => st.seek(ch.at)} title={pick(ch.title, lang)}>
                {fmtTime(ch.at)} · <Bi_ v={ch.title} />
              </button>
            ))}
          </div>
        )}
      </div>

      <div className="card" style={{ marginTop: 10 }}>
        <div className="h3" style={{ marginBottom: 10 }}>
          {tr(lang, "player.transcript")}
        </div>
        <div>
          {segments.map((s, i) => {
            const isPause = (ep.pause_points || []).some((q: Any) => q.at_sec === s.t);
            return (
              <div
                key={s.id || i}
                className={`seg ${i === idx ? "now" : ""} ${isPause ? "q" : ""}`}
                onClick={() => st.seek(s.t)}
                role="button"
                tabIndex={0}
                onKeyDown={(e) => e.key === "Enter" && st.seek(s.t)}
              >
                <span className="tm">{fmtTime(s.t)}</span>
                {lang === "en" && s.text_en ? s.text_en : s.text}
                {isPause && <span className="badge probable" style={{ marginLeft: 8 }}><span className="dot" /> ⏸</span>}
              </div>
            );
          })}
        </div>
      </div>

      {Array.isArray(ep.pause_points) && ep.pause_points.length > 0 && (
        <div className="card" style={{ marginTop: 10 }}>
          <div className="h3" style={{ marginBottom: 8 }}>
            {tr(lang, "player.pausepoint")}
          </div>
          <div className="stack">
            {ep.pause_points.map((q: Any) => (
              <button key={q.id} className="choice" onClick={() => st.seek(Math.max(0, (q.at_sec ?? 0) - 1))}>
                <span className="key">{fmtTime(q.at_sec ?? 0)}</span>
                <span>
                  <Bi_ v={q.prompt} />
                  <span style={{ display: "block", marginTop: 5 }}>
                    <Reliability level="PROBABLE" label={q.kind_label} />
                  </span>
                </span>
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
