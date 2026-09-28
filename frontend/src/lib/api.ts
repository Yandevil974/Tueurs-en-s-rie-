/**
 * Client API hybride YANIS//X.
 * 
 * En environnement embarqué / Android APK ou hors ligne :
 * - Si le backend local / distant ne répond pas, il bascule automatiquement
 *   et de manière transparente sur les données JSON statiques pré-embarquées (/data/...).
 * - Les fichiers audio sont également résolus localement (/audio/...).
 * - L'application fonctionne donc à 100% sans serveur actif.
 */

export class ApiError extends Error {
  status: number;
  detail: unknown;
  constructor(status: number, detail: unknown, message: string) {
    super(message);
    this.status = status;
    this.detail = detail;
  }
}

let token: string | null = null;
export const setToken = (t: string | null) => {
  token = t;
  if (t) localStorage.setItem("yanisx.token", t);
  else localStorage.removeItem("yanisx.token");
};
export const getToken = () => token ?? localStorage.getItem("yanisx.token");

/** Résolution du chemin statique de repli */
function getStaticFallbackUrl(path: string): string {
  // Retirer les query params pour chercher le fichier statique
  const cleanPath = path.split("?")[0];

  if (cleanPath === "/meta") return "/data/meta.json";
  if (cleanPath === "/cases") return "/data/cases.json";
  if (cleanPath === "/explore") return "/data/explore.json";
  if (cleanPath === "/archives") return "/data/archives.json";
  if (cleanPath === "/memory") return "/data/memory.json";
  if (cleanPath === "/glossary") return "/data/glossary.json";
  if (cleanPath === "/countries") return "/data/countries.json";
  if (cleanPath === "/courses") return "/data/courses.json";
  if (cleanPath === "/episodes") return "/data/episodes.json";
  if (cleanPath === "/counterfactuals") return "/data/counterfactuals.json";

  // /cases/{slug} ou /cases/{slug}/{sub}
  const caseMatch = cleanPath.match(/^\/cases\/([^\/]+)(?:\/([^\/]+))?$/);
  if (caseMatch) {
    const slug = caseMatch[1];
    const sub = caseMatch[2];
    if (sub) {
      return `/data/cases/${slug}/${sub}.json`;
    }
    return `/data/cases/${slug}.json`;
  }

  // /episodes/{id}
  const epMatch = cleanPath.match(/^\/episodes\/(\d+)$/);
  if (epMatch) {
    return `/data/episodes/${epMatch[1]}.json`;
  }

  return `/data${cleanPath}.json`;
}

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const headers: Record<string, string> = { Accept: "application/json", ...(init.headers as object) };
  if (init.body && !headers["Content-Type"]) headers["Content-Type"] = "application/json";
  const tk = getToken();
  if (tk) headers.Authorization = `Bearer ${tk}`;

  let res: Response | null = null;
  let useFallback = false;

  // 1. Essai sur l'API backend
  try {
    res = await fetch(`/api${path}`, { ...init, headers });
    if (!res.ok && res.status >= 500) {
      useFallback = true;
    }
  } catch {
    useFallback = true;
  }

  // 2. Repli transparent sur les données embarquées (APK / Hors-ligne)
  if (useFallback || !res) {
    const fallbackUrl = getStaticFallbackUrl(path);
    try {
      res = await fetch(fallbackUrl);
    } catch {
      // Ignoré, l'erreur finale sera levée plus bas
    }
  }

  if (!res || !res.ok) {
    const detail = res ? `${res.status} ${res.statusText}` : "Connexion impossible";
    throw new ApiError(res?.status || 0, null, `Erreur chargement: ${detail}`);
  }

  const text = await res.text();
  const data = text ? JSON.parse(text) : null;
  return data as T;
}

export const api = {
  get: <T,>(p: string) => request<T>(p),
  post: <T,>(p: string, body?: unknown) => request<T>(p, { method: "POST", body: body === undefined ? undefined : JSON.stringify(body) }),
  put: <T,>(p: string, body?: unknown) => request<T>(p, { method: "PUT", body: body === undefined ? undefined : JSON.stringify(body) }),
  patch: <T,>(p: string, body?: unknown) => request<T>(p, { method: "PATCH", body: body === undefined ? undefined : JSON.stringify(body) }),
};

export const audioUrl = (file: string) => {
  // Prise en charge locale directe dans l'APK et repli
  return `/audio/${encodeURIComponent(file)}`;
};

/** Types lâches : le contenu est bilingue et polymorphe par conception. */
export type Bi = { fr?: string; en?: string } | string | null | undefined;
export type Any = Record<string, any>;

export const endpoints = {
  health: () => "/health",
  meta: () => "/meta",
  ethics: () => "/ethics",
  cases: (q = "") => `/cases${q}`,
  case: (slug: string) => `/cases/${slug}`,
  section: (slug: string, key: string) => `/cases/${slug}/sections/${key}`,
  victims: (slug: string) => `/cases/${slug}/victims`,
  memorial: (slug: string) => `/cases/${slug}/memorial`,
  timeline: (slug: string) => `/cases/${slug}/timeline`,
  geography: (slug: string) => `/cases/${slug}/geography`,
  evidence: (slug: string) => `/cases/${slug}/evidence`,
  investigation: (slug: string) => `/cases/${slug}/investigation`,
  psychology: (slug: string) => `/cases/${slug}/psychology`,
  victimology: (slug: string) => `/cases/${slug}/victimology`,
  court: (slug: string) => `/cases/${slug}/court`,
  experts: (slug: string) => `/cases/${slug}/experts`,
  sources: (slug: string) => `/cases/${slug}/sources`,
  lessons: (slug: string) => `/cases/${slug}/lessons`,
  questions: (slug: string) => `/cases/${slug}/questions`,
  recommendations: (slug: string) => `/cases/${slug}/recommendations`,
  episodes: (q = "") => `/episodes${q}`,
  episode: (id: number) => `/episodes/${id}`,
  transcript: (id: number) => `/episodes/${id}/transcript`,
  answer: (id: number) => `/questions/${id}/answer`,
  counterfactuals: (q = "") => `/counterfactuals${q}`,
  counterfactual: (id: number) => `/counterfactuals/${id}`,
  reflect: (id: number) => `/counterfactuals/${id}/reflect`,
  world: () => "/explore",
  continent: (c: string) => `/explore/continent/${encodeURIComponent(c)}`,
  country: (c: string) => `/explore/country/${c}`,
  region: (c: string, r: string) => `/explore/country/${c}/region/${encodeURIComponent(r)}`,
  city: (c: string, v: string) => `/explore/country/${c}/city/${encodeURIComponent(v)}`,
  map: (q = "") => `/explore/map${q}`,
  compare: (ids: string[]) => `/explore/compare?ids=${ids.join(",")}`,
  search: (q: string) => `/search?q=${encodeURIComponent(q)}`,
  analyst: () => "/analyst",
  archives: (q = "") => `/archives${q}`,
  allSources: () => "/sources",
  glossary: (q = "") => `/glossary${q}`,
  glossaryEntry: (slug: string) => `/glossary/${slug}`,
  courses: () => "/courses",
  course: (slug: string) => `/courses/${slug}`,
  countries: () => "/countries",
  login: () => "/auth/login",
  register: () => "/auth/register",
  me: () => "/auth/me",
  patchMe: () => "/auth/me",
  a11y: () => "/auth/me/a11y",
  progress: () => "/progress",
  progressPut: (kind: string, ref: string) => `/progress/${kind}/${ref}`,
  resume: () => "/progress/resume",
  favourite: (slug: string) => `/progress/favourite/${slug}`,
  badge: (key: string) => `/progress/badge/${key}`,
  voices: () => "/auth/me/voices",
  adminStats: () => "/admin/stats",
  adminRevisions: () => "/admin/revisions",
  adminReseed: () => "/admin/reseed",
  adminPatchCase: (slug: string) => `/admin/cases/${slug}`,
  adminVerifySource: (id: number) => `/admin/sources/${id}/verify`,
  adminBroadcastNotification: () => "/admin/notifications",
  notifications: () => "/notifications",
  notificationRead: (id: number) => `/notifications/${id}/read`,
  notificationsReadAll: () => "/notifications/read-all",
};
