import { create } from "zustand";
import { api, endpoints, type Any } from "../lib/api";
import type { Lang } from "../lib/i18n";

type A11y = { fontScale?: number; contrast?: string; reduceMotion?: boolean; captions?: boolean };
type LocalProgress = Record<string, Any>;

const LOCAL_PROGRESS_KEY = "yanisx.local-progress";

function readStored<T>(key: string, fallback: T): T {
  try {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) as T : fallback;
  } catch {
    return fallback;
  }
}

function readLocalProgress(): LocalProgress {
  return readStored(LOCAL_PROGRESS_KEY, {});
}

function readFavourites(): string[] {
  return Object.entries(readLocalProgress())
    .filter(([key, value]) => key.startsWith("favourite:") && Boolean(value?.on))
    .map(([key]) => key.slice("favourite:".length));
}

const savedLang = localStorage.getItem("yanisx.lang");
const storedLang: Lang = savedLang === "en" ? "en" : "fr";
const storedWarned = readStored<Record<string, boolean>>("yanisx.warned", {});
const storedA11y = readStored<A11y>("yanisx.a11y", {});

export function applyA11y(a: A11y) {
  const root = document.documentElement;
  root.style.setProperty("--fs", String(a.fontScale ?? 1));
  root.dataset.contrast = a.contrast === "high" ? "high" : "standard";
  root.dataset.motion = a.reduceMotion ? "reduce" : "full";
  root.lang = localStorage.getItem("yanisx.lang") || "fr";
}

type AppState = {
  lang: Lang;
  setLang: (l: Lang) => void;
  meta: Any | null;
  metaError: string | null;
  loadMeta: () => Promise<void>;

  a11y: A11y;
  setA11y: (patch: A11y) => Promise<void>;

  warned: Record<string, boolean>;
  acknowledgeWarning: (slug: string, remember: boolean) => void;
  isWarned: (slug: string) => boolean;

  resume: Any | null;
  loadResume: () => Promise<void>;
  favourites: string[];
  toggleFavourite: (slug: string) => Promise<void>;
  saveProgress: (kind: string, ref: string, value: Any) => Promise<void>;
  award: (key: string, context?: string) => Promise<void>;
};

export const useApp = create<AppState>((set, get) => ({
  lang: storedLang,
  setLang: (lang) => {
    localStorage.setItem("yanisx.lang", lang);
    document.documentElement.lang = lang;
    set({ lang });
  },

  meta: null,
  metaError: null,
  loadMeta: async () => {
    try {
      const meta = await api.get<Any>(endpoints.meta());
      set({ meta, metaError: null });
    } catch (error: any) {
      set({ metaError: error.message || "meta" });
    }
  },

  a11y: storedA11y,
  setA11y: async (patch) => {
    const next = { ...get().a11y, ...patch };
    localStorage.setItem("yanisx.a11y", JSON.stringify(next));
    applyA11y(next);
    set({ a11y: next });
  },

  warned: storedWarned,
  acknowledgeWarning: (slug, remember) => {
    const next = { ...get().warned, [slug]: true };
    if (remember) localStorage.setItem("yanisx.warned", JSON.stringify(next));
    set({ warned: next });
  },
  isWarned: (slug) => Boolean(get().warned[slug]),

  resume: null,
  loadResume: async () => {
    const audio = Object.entries(readLocalProgress())
      .filter(([key]) => key.startsWith("audio:"))
      .map(([key, value]) => {
        const ref = key.slice("audio:".length);
        const [caseId] = ref.split(":");
        return {
          ref,
          case_id: caseId,
          episode_id: value.episode_id,
          episode_title: value.episode_title,
          duration_sec: value.duration_sec,
          at_sec: Number(value.at_sec || 0),
          saved_at: value.saved_at || "",
        };
      })
      .sort((a, b) => b.saved_at.localeCompare(a.saved_at))
      .slice(0, 8);
    set({ resume: { audio } });
  },
  favourites: readFavourites(),
  saveProgress: async (kind, ref, value) => {
    const local = readLocalProgress();
    local[`${kind}:${ref}`] = { ...value, saved_at: new Date().toISOString() };
    localStorage.setItem(LOCAL_PROGRESS_KEY, JSON.stringify(local));
  },
  toggleFavourite: async (slug) => {
    const has = get().favourites.includes(slug);
    const favourites = has
      ? get().favourites.filter((item) => item !== slug)
      : [...get().favourites, slug];
    const local = readLocalProgress();
    local[`favourite:${slug}`] = { on: !has, saved_at: new Date().toISOString() };
    localStorage.setItem(LOCAL_PROGRESS_KEY, JSON.stringify(local));
    set({ favourites });
  },
  award: async (key, context = "") => {
    const badges = readStored<Record<string, Any>>("yanisx.badges", {});
    if (!badges[key]) {
      badges[key] = { context, at: new Date().toISOString() };
      localStorage.setItem("yanisx.badges", JSON.stringify(badges));
    }
  },
}));

applyA11y(storedA11y);
