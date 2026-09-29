/** Installation de l'application sur le téléphone.
 *
 * Android n'a pas d'équivalent de « sur l'écran d'accueil » d'iOS, mais
 * Chrome expose `beforeinstallprompt`. On le capture au démarrage, on le
 * rend disponible à l'interface, et l'utilisateur déclenche l'installation
 * d'un appui. Chrome décide ensuite s'il accepte (critères : HTTPS, service
 * worker enregistré, engagement utilisateur, et non-installé déjà).
 *
 * Safari iOS ne déclenche jamais cet évènement : il faut utiliser le bouton
 * de partage d'iOS. D'où le repli manuel décrit plus bas.
 */
import { useCallback, useEffect, useState } from "react";

type BIPEvent = Event & {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed" }>;
};

/** L'appli tourne-t-elle déjà en fenêtre installée (ni barre d'URL ni onglet) ? */
export const isStandalone = () => {
  if (typeof window === "undefined") return false;
  const iosStandalone = (window.navigator as unknown as { standalone?: boolean }).standalone;
  return (
    window.matchMedia?.("(display-mode: standalone)").matches === true ||
    window.matchMedia?.("(display-mode: minimal-ui)").matches === true ||
    iosStandalone === true
  );
};

export const isIos = () =>
  typeof navigator !== "undefined" &&
  /iPad|iPhone|iPod/.test(navigator.userAgent) &&
  !("MSStream" in window);

let deferred: BIPEvent | null = null;
const listeners = new Set<() => void>();
const notify = () => listeners.forEach((fn) => fn());

if (typeof window !== "undefined") {
  window.addEventListener("beforeinstallprompt", (e) => {
    /* Sans preventDefault, Chrome affiche sa propre barre d'invite, qui
       terrasse la nôtre et n'est pas stylable. */
    e.preventDefault();
    deferred = e as BIPEvent;
    notify();
  });
  window.addEventListener("appinstalled", () => {
    deferred = null;
    notify();
  });
}

let updateReady = false;

/** Enregistre le service worker. En développement il est ignoré : un cache
 *  périmé en cours de rechargement serait plus difficile à diagnostiquer
 *  qu'un cache absent. */
export async function registerServiceWorker(onUpdate?: () => void) {
  if (!import.meta.env.PROD) return;
  if (!("serviceWorker" in navigator)) return;
  try {
    const reg = await navigator.serviceWorker.register("/sw.js", { scope: "/" });
    reg.addEventListener("updatefound", () => {
      const sw = reg.installing;
      if (!sw) return;
      sw.addEventListener("statechange", () => {
        if (sw.state === "installed" && navigator.serviceWorker.controller) {
          updateReady = true;
          onUpdate?.();
        }
      });
    });
  } catch {
    /* Pas de service worker : l'appli reste utilisable, simplement sans
       installation ni mode hors ligne. Ne pas casser le démarrage. */
  }
}

/** Force l'activation d'une version déjà téléchargée. */
export const activateUpdate = () => {
  navigator.serviceWorker?.getRegistration().then((r) => r?.waiting?.postMessage("skip-waiting"));
  window.location.reload();
};

export type InstallState = {
  /** L'appli est déjà installée et lancée en fenêtre autonome. */
  installed: boolean;
  /** L'invite est disponible et peut être déclenchée. */
  canInstall: boolean;
  /** iOS : il n'existe pas d'évènement, il faut passer par le menu Partager. */
  needsManualSteps: boolean;
  /** Une version neuve du service worker est prête. */
  updateReady: boolean;
  install: () => Promise<void>;
  applyUpdate: () => void;
};

export function useInstall(): InstallState {
  const [installed, setInstalled] = useState(isStandalone);
  const [canInstall, setCanInstall] = useState(deferred !== null);
  const [update, setUpdate] = useState(updateReady);

  useEffect(() => {
    const sync = () => setCanInstall(deferred !== null);
    listeners.add(sync);
    const mq = window.matchMedia("(display-mode: standalone)");
    const onMode = () => setInstalled(isStandalone());
    mq.addEventListener?.("change", onMode);
    return () => {
      listeners.delete(sync);
      mq.removeEventListener?.("change", onMode);
    };
  }, []);

  const install = useCallback(async () => {
    if (!deferred) return;
    await deferred.prompt();
    await deferred.userChoice;
    deferred = null;
    setCanInstall(false);
  }, []);

  return {
    installed,
    canInstall,
    needsManualSteps: !installed && !canInstall && isIos(),
    updateReady: update,
    install,
    applyUpdate: () => {
      activateUpdate();
    },
  };
}
