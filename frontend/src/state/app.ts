import { create } from "zustand";
import { api, endpoints, setToken, getToken, type Any } from "../lib/api";
import type { Lang } from "../lib/i18n";

type A11y = { fontScale?: number; contrast?: string; reduceMotion?: boolean; captions?: boolean };

type AppState = {
  lang: Lang;
  setLang: (l: Lang) => void;
  meta: Any | null;
  metaError: string | null;
  loadMeta: () => Promise<void>;

  user: Any | null;
  tier: string;
  authChecked: boolean;
  authError: string | null;
  checkAuth: () => Promise<void>;
  login: (email: string, password: string) => Promise<boolean>;
  register: (email: string, password: string, display_name: string) => Promise<boolean>;
  logout: () => void;
  switchTier: (tier: "FREE" | "PREMIUM") => Promise<void>;

  a11y: A11y;
  setA11y: (patch: A11y) => Promise<void>;

  warned: Record<string, boolean>;
  acknowledgeWarning: (slug: string, remember: boolean) => void;
  isWarned: (slug: string) => boolean;

  progress: Any | null;
  loadProgress: () => Promise<void>;
  saveProgress: (kind: string, ref: string, value: Any) => Promise<void>;
  resume: Any | null;
  loadResume: () => Promise<void>;
  favourites: string[];
  toggleFavourite: (slug: string) => Promise<void>;
  award: (key: string, context?: string) => Promise<void>;
};

const storedLang = (localStorage.getItem("yanisx.lang") as Lang) || "fr";
const storedWarned = JSON.parse(localStorage.getItem("yanisx.warned") || "{}");
const storedA11y = JSON.parse(localStorage.getItem("yanisx.a11y") || "{}");

export function applyA11y(a: A11y) {
  const root = document.documentElement;
  root.style.setProperty("--fs", String(a.fontScale ?? 1));
  root.dataset.contrast = a.contrast === "high" ? "high" : "standard";
  root.dataset.motion = a.reduceMotion ? "reduce" : "full";
  root.lang = localStorage.getItem("yanisx.lang") || "fr";
}

export const useApp = create<AppState>((set, get) => ({
  lang: storedLang,
  setLang: (l) => {
    localStorage.setItem("yanisx.lang", l);
    document.documentElement.lang = l;
    set({ lang: l });
  },

  meta: null,
  metaError: null,
  loadMeta: async () => {
    try {
      const meta = await api.get<Any>(endpoints.meta());
      set({ meta, metaError: null });
    } catch (e: any) {
      set({ metaError: e.message || "meta" });
    }
  },

  user: null,
  tier: "FREE",
  authChecked: false,
  authError: null,
  checkAuth: async () => {
    if (!getToken()) {
      set({ authChecked: true, user: null, tier: "FREE" });
      applyA11y(storedA11y);
      return;
    }
    try {
      const r = await api.get<Any>(endpoints.me());
      set({ user: r.user, tier: r.tier || "FREE", authChecked: true, authError: null });
      if (r.user?.a11y) {
        const a = { ...storedA11y, ...r.user.a11y };
        localStorage.setItem("yanisx.a11y", JSON.stringify(a));
        set({ a11y: a });
        applyA11y(a);
      }
    } catch {
      setToken(null);
      set({ user: null, tier: "FREE", authChecked: true });
    }
  },
  login: async (email, password) => {
    try {
      const r = await api.post<Any>(endpoints.login(), { email, password });
      setToken(r.token);
      set({ user: r.user, tier: r.user.tier, authError: null });
      get().loadProgress();
      get().loadResume();
      return true;
    } catch (e: any) {
      set({ authError: e.message });
      return false;
    }
  },
  register: async (email, password, display_name) => {
    try {
      const r = await api.post<Any>(endpoints.register(), { email, password, display_name });
      setToken(r.token);
      set({ user: r.user, tier: r.user.tier, authError: null });
      return true;
    } catch (e: any) {
      set({ authError: e.message });
      return false;
    }
  },
  logout: () => {
    setToken(null);
    set({ user: null, tier: "FREE", progress: null, resume: null, favourites: [] });
  },
  switchTier: async (tier) => {
    try {
      const r = await api.patch<Any>(endpoints.patchMe(), { tier });
      setToken(r.token);
      set({ user: r.user, tier: r.user.tier });
    } catch (e: any) {
      set({ authError: e.message });
    }
  },

  a11y: storedA11y,
  setA11y: async (patch) => {
    const next = { ...get().a11y, ...patch };
    localStorage.setItem("yanisx.a11y", JSON.stringify(next));
    applyA11y(next);
    set({ a11y: next });
    if (get().user) {
      try {
        await api.put(endpoints.a11y(), patch);
      } catch {
        /* hors ligne : la préférence locale reste appliquée */
      }
    }
  },

  warned: storedWarned,
  acknowledgeWarning: (slug, remember) => {
    if (!remember) {
      set({ warned: { ...get().warned, [slug]: true } });
      return;
    }
    const next = { ...get().warned, [slug]: true };
    localStorage.setItem("yanisx.warned", JSON.stringify(next));
    set({ warned: next });
  },
  isWarned: (slug) => Boolean(get().warned[slug]),

  progress: null,
  loadProgress: async () => {
    if (!getToken()) return;
    try {
      const p = await api.get<Any>(endpoints.progress());
      const favs = (p.progress?.favourite || []).filter((f: Any) => f.value?.on).map((f: Any) => f.ref);
      set({ progress: p, favourites: favs });
    } catch {
      /* silencieux : la navigation anonyme reste possible */
    }
  },
  saveProgress: async (kind, ref, value) => {
    const local = JSON.parse(localStorage.getItem("yanisx.local-progress") || "{}");
    local[`${kind}:${ref}`] = value;
    localStorage.setItem("yanisx.local-progress", JSON.stringify(local));
    if (!getToken()) return;
    try {
      await api.put(endpoints.progressPut(kind, ref), value);
    } catch {
      /* la copie locale suffit pour la reprise */
    }
  },
  resume: null,
  loadResume: async () => {
    if (!getToken()) {
      const local = JSON.parse(localStorage.getItem("yanisx.local-progress") || "{}");
      const audio = Object.entries(local)
        .filter(([k]) => k.startsWith("audio:"))
        .map(([k, v]: [string, any]) => ({ ref: k.slice(6), at_sec: v.at_sec, mode: v.mode }));
      set({ resume: { audio } });
      return;
    }
    try {
      set({ resume: await api.get<Any>(endpoints.resume()) });
    } catch {
      /* ignore */
    }
  },
  favourites: [],
  toggleFavourite: async (slug) => {
    const has = get().favourites.includes(slug);
    set({ favourites: has ? get().favourites.filter((s) => s !== slug) : [...get().favourites, slug] });
    if (getToken()) {
      try {
        await api.post(endpoints.favourite(slug));
      } catch {
        /* bascule locale conservée */
      }
    } else {
      get().saveProgress("favourite", slug, { on: !has });
    }
  },
  award: async (key, context = "") => {
    if (getToken()) {
      try {
        await api.post(endpoints.badge(key), { context });
        get().loadProgress();
        return;
      } catch {
        /* ignore */
      }
    }
    const badges = JSON.parse(localStorage.getItem("yanisx.badges") || "{}");
    if (!badges[key]) {
      badges[key] = { context, at: new Date().toISOString() };
      localStorage.setItem("yanisx.badges", JSON.stringify(badges));
    }
  },
}));

applyA11y(storedA11y);
