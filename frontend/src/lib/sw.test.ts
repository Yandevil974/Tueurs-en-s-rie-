// @vitest-environment node
/**
 * Test de la politique de cache du service worker.
 *
 * Ce n'est pas un test décoratif. La règle numéro un du projet est qu'une
 * donnée périmée ne doit jamais être servie à l'utilisateur : le catalogue
 * documente des faits réels, datés et sourcés. Une régression ici afficherait
 * un dossier dans l'état où il était hier, sans le moindre signe pour
 * l'utilisateur. Le bug serait silencieux — d'où un test explicite.
 *
 * `sw.js` est écrit pour la portée globale d'un service worker. On le charge
 * dans un `vm` avec un `self`, un `caches` et un `fetch` simulés, puis on
 * déclenche des évènements et on observe ce qui sort.
 */
import { describe, expect, it, beforeEach } from "vitest";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import vm from "node:vm";

type Handler = (event: unknown) => void;

const SW_SRC = readFileSync(resolve(__dirname, "../../public/sw.js"), "utf8");

/** Cache mémoire fidèle à l'API Cache. */
function makeCacheStore() {
  const store = new Map<string, Map<string, { body: string; ok: boolean }>>();
  const name = (n: string) => {
    if (!store.has(n)) store.set(n, new Map());
    return store.get(n)!;
  };
  return {
    store,
    api: {
      async open(n: string) {
        const m = name(n);
        return {
          /* L'API Cache accepte une chaîne comme une Request. */
          async match(req: string | { url: string }) {
            const key = typeof req === "string" ? req : req.url;
            const hit = m.get(key);
            return hit ? { url: key, body: hit.body, ok: hit.ok } : undefined;
          },
          async put(req: { url: string }, res: { body: string; ok: boolean }) {
            m.set(req.url, { body: res.body, ok: res.ok });
          },
          async add(url: string) {
            m.set(url, { body: `précaché:${url}`, ok: true });
          },
        };
      },
      async keys() {
        return [...store.keys()];
      },
      async delete(n: string) {
        store.delete(n);
      },
    },
  };
}

function loadSW(opts: { offline?: boolean } = {}) {
  const cacheStore = makeCacheStore();
  const netCalls: string[] = [];
  const listeners: Record<string, Handler[]> = {};

  const self = {
    location: { origin: "https://app.test", href: "https://app.test/sw.js" },
    addEventListener: (t: string, h: Handler) => {
      (listeners[t] ||= []).push(h);
    },
    skipWaiting: async () => {},
    clients: { claim: async () => {} },
  };

  const ctx = {
    self,
    caches: cacheStore.api,
    fetch: async (req: { url: string } | string) => {
      const url = typeof req === "string" ? req : req.url;
      netCalls.push(url);
      if (opts.offline) throw new Error("offline");
      return { ok: true, body: `reseau:${url}`, clone: () => ({ ok: true, body: `reseau:${url}` }) };
    },
    Response: class {
      status: number;
      body: string;
      constructor(body: string, init?: { status?: number }) {
        this.body = body;
        this.status = init?.status ?? 200;
      }
      static error() {
        return { body: "ERREUR", ok: false };
      }
    },
    URL,
    console,
    Promise,
  };
  /* `caches` et `fetch` sont fournis comme globales du contexte : c'est ainsi
     que le service worker les voit. */
  vm.createContext(ctx);
  vm.runInContext(SW_SRC, ctx);

  return { self, listeners, cacheStore, netCalls };
}

/** Déclenche l'évènement install et attend le précache. */
async function fireInstall(listeners: Record<string, Handler[]>) {
  let pending: Promise<unknown> = Promise.resolve();
  const event = { waitUntil: (p: Promise<unknown>) => { pending = p; } };
  (listeners.install || []).forEach((h) => h(event));
  await pending;
}

/** Déclenche l'évènement fetch et renvoie la réponse du service worker. */
async function dispatch(listeners: Record<string, Handler[]>, req: { url: string; mode?: string; method?: string }) {
  let answered: unknown = "PAS DE respondWith";
  const event = {
    request: { method: "GET", mode: "no-cors", ...req },
    respondWith: (p: Promise<unknown>) => {
      answered = p;
    },
  };
  (listeners.fetch || []).forEach((h) => h(event));
  return typeof answered === "object" ? await (answered as Promise<any>) : answered;
}

describe("service worker — politique de cache", () => {
  let sw: ReturnType<typeof loadSW>;
  beforeEach(() => {
    sw = loadSW();
  });

  it("n'accède jamais au cache pour les données /api", async () => {
    /* Point de non-retour : si cette requête passe par le cache, l'utilisateur
       peut voir un dossier périmé. Elle doit atteindre le réseau, et le réseau
       seul. */
    /* Le service worker ne se substitue pas au navigateur : il declines de
       répondre, et la requête va donc au réseau, jamais au cache. C'est la
       propriété qui compte — le test vérifie l'absence de cache, pas
       l'identité de l'appelant réseau. */
    const res = await dispatch(sw.listeners, { url: "https://app.test/api/cases" });
    expect(res).toBe("PAS DE respondWith");
    expect(sw.netCalls).toHaveLength(0);
    const cacheNames = [...sw.cacheStore.store.keys()];
    const cached = cacheNames.flatMap((n) => [...sw.cacheStore.store.get(n)!.keys()]);
    expect(cached.some((u) => u.includes("/api/cases"))).toBe(false);
  });

  it("ignore les méthodes qui ne sont pas GET", async () => {
    const res = await dispatch(sw.listeners, {
      url: "https://app.test/api/auth/me/voices",
      method: "POST",
    });
    expect(res).toBe("PAS DE respondWith");
    expect(sw.netCalls).toHaveLength(0);
  });

  it("laisse passer les requêtes vers un autre domaine", async () => {
    const res = await dispatch(sw.listeners, { url: "https://exemple.test/ailleurs.mp3" });
    expect(res).toBe("PAS DE respondWith");
  });

  it("met les narrations en cache pour une écoute sans réseau", async () => {
    const url = "https://app.test/api/audio/yanisx-robert-pickton-ep1-nobodies.mp3";
    const first = await dispatch(sw.listeners, { url });
    expect(first?.body).toBe(`reseau:${url}`);

    /* Deuxième demande : servie depuis le cache, le réseau étant toujours sollicité
       en tâche de fond pour rafraîchir. */
    const second = await dispatch(sw.listeners, { url });
    expect(second?.body).toBe(`reseau:${url}`);
    expect(sw.netCalls.filter((u) => u === url).length).toBe(2);

    const cached = [...sw.cacheStore.store.values()].flatMap((m) => [...m.keys()]);
    expect(cached).toContain(url);
  });

  it("sert la page depuis le cache quand le réseau tombe", async () => {
    const off = loadSW({ offline: true });
    /* On amorce le squelette comme le ferait l'évènement install. */
    await fireInstall(off.listeners);

    const res = await dispatch(off.listeners, { url: "https://app.test/podcasts", mode: "navigate" });
    expect(res?.body).toContain("/index.html");
  });

  it("purge les caches des versions précédentes", async () => {
    await fireInstall(sw.listeners);
    const names = [...sw.cacheStore.store.keys()];
    expect(names.length).toBeGreaterThan(0);
    expect(names.every((n) => n.startsWith("yanisx-pwa-"))).toBe(true);
  });
});
