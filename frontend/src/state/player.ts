/**
 * 🎧 Le moteur du podcast interactif (§3, §8, §26).
 *
 * Deux sources de lecture, jamais une fausse promesse :
 *  - `audio_status === "produced"` + fichier présent  → élément <audio> réel,
 *    diffusé en HTTP Range par le backend (seek + reprise).
 *  - sinon → lecture synchronisée de la transcription (le texte défile au
 *    rythme des horodatages du script). L'interface le dit explicitement.
 *
 * Dans les deux cas : pause aux points pédagogiques, question à choix
 * multiples, explication en cinq volets, puis reprise.
 */
import { create } from "zustand";
import { api, endpoints, audioUrl, type Any } from "../lib/api";
import { useApp } from "./app";

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
    }

    const pos = get().position;
    const q = (get().episode?.pause_points || []).find(
      (x: Any) => typeof x.at_sec === "number" && x.at_sec <= pos && !get().answered[x.id] && !get().skipped[x.id],
    );
    if (q) {
      if (audioEl) audioEl.pause();
      set({ playing: false, pending: q, explanation: null });
      save();
      return;
    }
    if (pos >= st.duration && st.duration > 0) {
      set({ playing: false });
      if (audioEl) audioEl.pause();
      save();
    } else {
      save();
    }
  };

  const startTimer = () => {
    stopTimer();
    timer = window.setInterval(tick, 250);
  };

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
          const probe = await fetch(audioUrl(ep.audio), { method: "HEAD" }).catch(() => null);
          if (probe && probe.ok) {
            usingAudio = true;
            audioEl = new Audio(audioUrl(ep.audio));
            audioEl.preload = "auto";
            audioEl.addEventListener("ended", () => set({ playing: false }));
          } else {
            audioMissing = true;
          }
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
        audioEl.play().catch(() => set({ usingAudio: false }));
      }
      set({ playing: true });
      startTimer();
    },
    pause: () => {
      if (audioEl) audioEl.pause();
      set({ playing: false });
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
