/* YANIS//X — service worker.
 *
 * Trois objectifs, dans cet ordre de priorité :
 *
 * 1. **Ne jamais servir de donnée périmée à l'utilisateur.** Les réponses `/api`
 *    vont toujours au réseau. Ce catalogue documente des faits réels, datés et
 *    sourcés : afficher un cas tel qu'il était hier serait une faute
 *    éditoriale, pas seulement un bug. Aucun cache sur `/api`.
 *
 * 2. **L'application doit démarrer hors ligne** (tunnel, parking, zone blanche).
 *    Le squelette HTML et les assets sont mis en cache ; une
 *    navigation sans réseau retombe sur `index.html` et le routeur reprend la
 *    main.
 *
 * 3. **Les narrations doivent survivre au réseau** — c'est le cas d'usage
 *    voiture. Les fichiers audio sont servis cache-first puis rafraîchis en
 *    tâche de fond, pour qu'un épisode soit rejouable sans data.
 *
 * Le nom du cache porte la version : à chaque changement, l'ancien est purgé
 * au `activate`.
 */
const VERSION = "yanisx-pwa-1";
const SHELL_CACHE = `${VERSION}-shell`;
const ASSET_CACHE = `${VERSION}-assets`;
const AUDIO_CACHE = `${VERSION}-audio`;

const SHELL = [
  "/",
  "/index.html",
  "/manifest.webmanifest",
  "/icons/icon-192.png",
  "/icons/icon-512.png",
  "/icons/icon-maskable-512.png",
  "/icons/apple-touch-icon.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches
      .open(SHELL_CACHE)
      /* `addAll` échoue en bloc si un seul fichier manque : on met les pièces
         une par une pour qu'un asset absent ne condamne pas l'installation. */
      .then((cache) => Promise.allSettled(SHELL.map((u) => cache.add(u))))
      .then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(keys.filter((k) => !k.startsWith(VERSION)).map((k) => caches.delete(k))),
      )
      .then(() => self.clients.claim()),
  );
});

const isAudio = (url) =>
  url.pathname.startsWith("/api/audio/") || /\.(mp3|m4a|wav|ogg)$/i.test(url.pathname);

/** Cache d'abord, puis rafraîchissement en tâche de fond. */
async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName);
  const hit = await cache.match(request);
  const network = fetch(request)
    .then((res) => {
      if (res && res.ok) cache.put(request, res.clone());
      return res;
    })
    .catch(() => null);
  return hit || (await network) || Response.error();
}

/** Réseau d'abord, repli sur le cache — pour la navigation. */
async function networkFirstNavigation(request) {
  try {
    const res = await fetch(request);
    if (res && res.ok) {
      const cache = await caches.open(SHELL_CACHE);
      cache.put("/index.html", res.clone());
    }
    return res;
  } catch {
    const cache = await caches.open(SHELL_CACHE);
    return (
      (await cache.match("/index.html")) ||
      (await cache.match("/")) ||
      new Response("Hors ligne — l'application n'a pas pu démarrer.", {
        status: 503,
        headers: { "Content-Type": "text/plain; charset=utf-8" },
      })
    );
  }
}

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  /* 1. Les données ne sont jamais mises en cache. */
  if (url.pathname.startsWith("/api/") && !isAudio(url)) return;

  /* 2. Navigation : réseau d'abord, squelette en repli. */
  if (req.mode === "navigate") {
    event.respondWith(networkFirstNavigation(req));
    return;
  }

  /* 3. Audio : disponible hors ligne, rafraîchi ensuite. */
  if (isAudio(url)) {
    event.respondWith(staleWhileRevalidate(req, AUDIO_CACHE));
    return;
  }

  /* 4. Assets statiques. */
  event.respondWith(staleWhileRevalidate(req, ASSET_CACHE));
});

/* Permet à la page de demander l'activation immédiate d'une version neuve. */
self.addEventListener("message", (event) => {
  if (event.data === "skip-waiting") self.skipWaiting();
});
