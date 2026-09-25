/**
 * Client API. Toujours en URL relative : le serveur de dev relaie /api vers le
 * backend, donc le navigateur n'appelle jamais localhost (§contraintes aperçu).
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

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const headers: Record<string, string> = { Accept: "application/json", ...(init.headers as object) };
  if (init.body && !headers["Content-Type"]) headers["Content-Type"] = "application/json";
  const tk = getToken();
  if (tk) headers.Authorization = `Bearer ${tk}`;

  let res: Response;
  try {
    res = await fetch(`/api${path}`, { ...init, headers });
  } catch {
    throw new ApiError(0, null, "Connexion au serveur impossible / Cannot reach the server");
  }
  const text = await res.text();
  const data = text ? JSON.parse(text) : null;
  if (!res.ok) {
    const detail = (data && (data.detail || data.message)) || res.statusText;
    throw new ApiError(res.status, data, typeof detail === "string" ? detail : JSON.stringify(detail));
  }
  return data as T;
}

export const api = {
  get: <T,>(p: string) => request<T>(p),
  post: <T,>(p: string, body?: unknown) => request<T>(p, { method: "POST", body: body === undefined ? undefined : JSON.stringify(body) }),
  put: <T,>(p: string, body?: unknown) => request<T>(p, { method: "PUT", body: body === undefined ? undefined : JSON.stringify(body) }),
  patch: <T,>(p: string, body?: unknown) => request<T>(p, { method: "PATCH", body: body === undefined ? undefined : JSON.stringify(body) }),
};

export const audioUrl = (file: string) => `/api/audio/${encodeURIComponent(file)}`;

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
