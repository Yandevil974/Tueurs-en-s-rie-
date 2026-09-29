/**
 * 🎧 Le moteur du podcast interactif (§3, §8, §26).
 *
 * Deux sources de lecture, jamais une fausse promesse :
 *  - `audio_status === "produced"` + fichier présent  → élément <audio> réel.
 *  - sinon (ou en secours) → moteur de synthèse vocale TTS intégré.
 *
 * Dans les deux cas : pause aux points pédagogiques, question à choix
 * multiples, explication en cinq volets, puis reprise.
 */
import { create } from "zustand";
import { api, endpoints, audioUrl, type Any } from "../lib/api";
import { useApp } from "./app";
import { tts } from "../lib/tts";

export type Segment = { id: string; t: number; speaker?: string; text: string; text_en?: string };

type PlayerState = {
  episode: Any | null;
  loading: boolean;
  error: string | null;
  playing: boolean;
  position: number;
  duration: number;
  speed: number;
  usingAudio: boolean;
  audioMissing: boolean;

  pending: Any | null;
  answered: Record<number, string>;
  skipped: Record<number, boolean>;
  explanation: Any | null;
  answering: boolean;

  load: (id: number, startAt?: number) => Promise<void>;
  play: () => void;
  pause: () => void;
  toggle: () => void;
  seek: (sec: number) => void;
  nudge: (delta: number) => void;
  setSpeed: (s: number) => void;
  stop: () => void;

  submit: (choice: string) => Promise<void>;
  skipQuestion: () => void;
  closeExplanation: () => void;

  currentSegment: () => Segment | null;
  currentIndex: () => number;
  nextPauseAt: () => number | null;
};

let audioEl: HTMLAudioElement | null = null;
let timer: number | null = null;
let lastSave = 0;
let currentTtsSegmentId: string | null = null;

/* ---------------------------------------------------------------
 * Restitution Bluetooth (voiture).
 * --------------------------------------------------------------- */
let mediaSessionBound = false;
let wakeLock: { release: () => Promise<void> } | null = null;

const mediaSessionSupported = () =>
  typeof navigator !== "undefined" && "mediaSession" in navigator;

const acquireWakeLock = async () => {
  if (!("wakeLock" in navigator) || wakeLock) return;
  try {
    wakeLock = await (navigator as unknown as { wakeLock: { request: (t: string) => Promise<{ release: () => Promise<void> }> } }).wakeLock.request("screen");
  } catch {
    /* refusé */
  }
};
const releaseWakeLock = async () => {
  try {
    await wakeLock?.release();
  } catch {
    /* déjà relâché */
  }
  wakeLock = null;
};

const episodeLabel = (ep: Any | null) => {
  if (!ep) return "";
  const t = ep.title;
  return (t && typeof t === "object" ? t.fr || t.en : t) || "";
};

const publishMetadata = (ep: Any | null) => {
  if (!mediaSessionSupported() || !ep) return;
  try {
    navigator.mediaSession.metadata = new MediaMetadata({
      title: episodeLabel(ep),
      artist: "YANIS//X",
      album: "à travers mon regard",
      artwork: [
        { src: "/icons/icon-512.png", sizes: "512x512", type: "image/png" },
        { src: "/icons/icon-192.png", sizes: "192x192", type: "image/png" },
      ],
    });
  } catch {
    /* métadonnées indisponibles */
  }
};

const publishState = (playing: boolean) => {
  if (!mediaSessionSupported()) return;
  try {
    navigator.mediaSession.playbackState = playing ? "playing" : "paused";
  } catch {
    /* ignoré */
  }
};

const chapterJump = (get: () => PlayerState, dir: 1 | -1) => {
  const st = get();
  const chs: number[] = Array.isArray(st.episode?.chapters)
    ? st.episode.chapters.map((c: Any) => c.at).filter((n: unknown): n is number => typeof n === "number")
    : [];
  if (!chs.length) {
    st.seek(Math.max(0, Math.min(st.duration, st.position + dir * 30)));
    return;
  }
  const ordered = [...chs].sort((a, b) => a - b);
  const next =
    dir === 1
      ? ordered.find((t) => t > st.position + 1)
      : [...ordered].reverse().find((t) => t < st.position - 1);
  st.seek(next == null ? (dir === 1 ? ordered[ordered.length - 1] : 0) : next);
};

const bindMediaSession = (get: () => PlayerState) => {
  if (!mediaSessionSupported() || mediaSessionBound) return;
  mediaSessionBound = true;
  const handlers: [MediaSessionAction, (d: never) => void][] = [
    ["play", () => get().play()],
    ["pause", () => get().pause()],
    ["stop", () => get().stop()],
    ["seekbackward", (d: { seekOffset?: number } | null) => get().nudge(-(d?.seekOffset || 15))],
    ["seekforward", (d: { seekOffset?: number } | null) => get().nudge(d?.seekOffset || 30)],
    ["seekto", (d: { seekTime?: number } | null) => {
      if (typeof d?.seekTime === "number") get().seek(d.seekTime);
    }],
    ["previoustrack", () => chapterJump(get, -1)],
    ["nexttrack", () => chapterJump(get, 1)],
  ];
  for (const [action, fn] of handlers) {
    try {
      navigator.mediaSession.setActionHandler(action, fn as MediaSessionActionHandler);
    } catch {
      /* action non supportée */
    }
  }
};

const stopTimer = () => {
  if (timer !== null) {
    clearInterval(timer);
    timer = null;
  }
};

export const usePlayer = create<PlayerState>((set, get) => {
  const save = () => {
    const { episode, position, playing } = get();
    if (!episode) return;
    const now = Date.now();
    if (now - lastSave < 6000 && playing) return;
    lastSave = now;
    const ref = `${episode.case_id}:${episode.number}`;
    useApp.getState().saveProgress("audio", ref, {
      at_sec: Math.round(position),
      episode_id: episode.id,
      case_title: episode.case_id,
    });
  };

  const tick = () => {
    const st = get();
    if (!st.playing || st.pending) return;

    if (st.usingAudio && audioEl) {
      const p = audioEl.currentTime;
      if (Math.abs(p - st.position) > 1.2) set({ position: p });
      else set({ position: p });
    } else {
      set({ position: Math.min(st.duration, st.position + 0.25 * st.speed) });
      const cur = get().currentSegment();
      if (cur && cur.id !== currentTtsSegmentId && cur.text) {
        currentTtsSegmentId = cur.id;
        tts.speak(cur.text);
      }
    }

    const pos = get().position;
    const q = (get().episode?.pause_points || []).find(
      (x: Any) => typeof x.at_sec === "number" && x.at_sec <= pos && !get().answered[x.id] && !get().skipped[x.id],
    );
    if (q) {
      if (audioEl) audioEl.pause();
      tts.pause();
      set({ playing: false, pending: q, explanation: null });
      publishState(false);
      save();
      return;
    }
    if (pos >= st.duration && st.duration > 0) {
      set({ playing: false });
      if (audioEl) audioEl.pause();
      tts.stop();
      publishState(false);
      releaseWakeLock();
      save();
    } else {
      save();
    }
  };

  const startTimer = () => {
    stopTimer();
    timer = window.setInterval(tick, 250);
  };

  bindMediaSession(() => get());

  return {
    episode: null,
    loading: false,
    error: null,
    playing: false,
    position: 0,
    duration: 0,
    speed: 1,
    usingAudio: false,
    audioMissing: false,
    pending: null,
    answered: {},
    skipped: {},
    explanation: null,
    answering: false,

    load: async (id, startAt = 0) => {
      set({ loading: true, error: null });
      stopTimer();
      if (audioEl) {
        audioEl.pause();
        audioEl.src = "";
        audioEl = null;
      }
      try {
        const ep = await api.get<Any>(endpoints.episode(id));
        const segments: Segment[] = ep.transcript?.segments || [];
        const duration = ep.duration_sec || (segments.length ? segments[segments.length - 1].t + 90 : 0);

        let usingAudio = false;
        let audioMissing = false;
        if (ep.audio_status === "produced" && ep.audio) {
          usingAudio = true;
          const url = audioUrl(ep.audio);
          audioEl = new Audio();
          audioEl.src = url;
          audioEl.preload = "auto";
          audioEl.addEventListener("ended", () => {
            set({ playing: false });
            publishState(false);
            releaseWakeLock();
          });
          audioEl.addEventListener("error", (e) => {
            console.warn("Échec lecture fichier audio, bascule vocale TTS:", e);
            set({ usingAudio: false, audioMissing: true });
          });
        } else if (ep.audio_status === "produced" && !ep.audio) {
          audioMissing = true;
        }

        const start = startAt > 0 && startAt < duration ? startAt : 0;
        set({
          episode: ep,
          duration,
          position: start,
          playing: false,
          loading: false,
          usingAudio,
          audioMissing,
          pending: null,
          explanation: null,
        });
        if (usingAudio && audioEl) audioEl.currentTime = start;
        publishMetadata(ep);
        publishState(false);
        startTimer();
      } catch (e: any) {
        set({ loading: false, error: e.message || "episode" });
      }
    },

    play: () => {
      const { pending, duration, position } = get();
      if (pending) return;
      if (duration > 0 && position >= duration - 0.5) set({ position: 0 });
      if (audioEl && get().usingAudio) {
        audioEl.playbackRate = get().speed;
        audioEl.play().catch((err) => {
          console.warn("Échec audioEl.play():", err);
          set({ usingAudio: false, audioMissing: true });
          const cur = get().currentSegment();
          if (cur && cur.text) {
            tts.speak(cur.text);
          }
        });
      } else {
        const cur = get().currentSegment();
        if (cur && cur.text) {
          tts.speak(cur.text);
        } else {
          tts.resume();
        }
      }
      set({ playing: true });
      publishState(true);
      acquireWakeLock();
      startTimer();
    },
    pause: () => {
      if (audioEl) audioEl.pause();
      tts.pause();
      set({ playing: false });
      publishState(false);
      releaseWakeLock();
      save();
    },
    toggle: () => (get().playing ? get().pause() : get().play()),
    seek: (sec) => {
      const clamped = Math.max(0, Math.min(get().duration || sec, sec));
      if (audioEl && get().usingAudio) audioEl.currentTime = clamped;
      set({ position: clamped });
    },
    nudge: (delta) => get().seek(get().position + delta),
    setSpeed: (s) => {
      if (audioEl) audioEl.playbackRate = s;
      set({ speed: s });
    },
    stop: () => {
      save();
      stopTimer();
      if (audioEl) {
        audioEl.pause();
        audioEl = null;
      }
      tts.stop();
      currentTtsSegmentId = null;
      publishState(false);
      releaseWakeLock();
      set({ episode: null, playing: false, position: 0, pending: null, explanation: null, usingAudio: false });
    },

    submit: async (choice) => {
      const q = get().pending;
      if (!q) return;
      set({ answering: true });
      try {
        const r = await api.post<Any>(endpoints.answer(q.id), { choice });
        set({
          answering: false,
          explanation: r,
          answered: { ...get().answered, [q.id]: choice },
        });
        const ep = get().episode;
        useApp.getState().saveProgress("question", `${ep?.case_id}:${ep?.number}:${q.id}`, {
          choice,
          kind: q.kind,
        });
        useApp.getState().award("analyst", `question:${q.id}`);
      } catch (e: any) {
        set({ answering: false, explanation: { error: e.message } });
      }
    },
    skipQuestion: () => {
      const q = get().pending;
      if (!q) return;
      set({ skipped: { ...get().skipped, [q.id]: true }, pending: null, explanation: null });
      get().seek(q.at_sec + 2);
      get().play();
    },
    closeExplanation: () => {
      const q = get().pending;
      set({ pending: null, explanation: null });
      if (q) get().seek((q.at_sec ?? get().position) + 2);
      get().play();
    },

    currentSegment: () => {
      const segs: Segment[] = get().episode?.transcript?.segments || [];
      if (!segs.length) return null;
      let cur = segs[0];
      for (const s of segs) if (s.t <= get().position) cur = s;
      return cur;
    },
    currentIndex: () => {
      const segs: Segment[] = get().episode?.transcript?.segments || [];
      const cur = get().currentSegment();
      return cur ? segs.indexOf(cur) : -1;
    },
    nextPauseAt: () => {
      const pts = (get().episode?.pause_points || [])
        .map((q: Any) => q.at_sec)
        .filter((n: number) => typeof n === "number" && n > get().position)
        .sort((a: number, b: number) => a - b);
      return pts.length ? pts[0] : null;
    },
  };
});

export const fmtTime = (sec: number) => {
  const s = Math.max(0, Math.floor(sec || 0));
  const m = Math.floor(s / 60);
  return `${m}:${String(s % 60).padStart(2, "0")}`;
};
