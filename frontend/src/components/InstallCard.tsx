import { useEffect, useState } from "react";
import { useInstall } from "../lib/pwa";
import { tr } from "../lib/i18n";
import { useLang } from "./ui";

/** Carte « Installer l'application ».
 *
 * Elle n'apparaît que lorsqu'il y a quelque chose à proposer : Chrome a émis
 * `beforeinstallprompt`, ou une version neuve du service worker attend. Sur
 * une application déjà installée, elle disparaît — sauf pour la mise à jour,
 * qu'il faut pouvoir signaler.
 */
export default function InstallCard() {
  const lang = useLang();
  const { installed, canInstall, needsManualSteps, updateReady, install, applyUpdate } = useInstall();
  const [hidden, setHidden] = useState(() => localStorage.getItem("yanisx.install.dismissed") === "1");

  /* Un abonnement déjà installé ne peut pas être mis à jour par l'utilisateur :
     on propose de recharger quand même, mais discrètement. */
  useEffect(() => {
    if (!updateReady) return;
    setHidden(false);
  }, [updateReady]);

  if (hidden) return null;
  if (installed && !updateReady && !needsManualSteps) return null;
  if (!installed && !canInstall && !updateReady) {
    /* Ni Chrome prêt, ni mise à jour : on ne montre que la notice iOS. */
    if (!needsManualSteps) return null;
  }

  const dismiss = () => {
    localStorage.setItem("yanisx.install.dismissed", "1");
    setHidden(true);
  };

  return (
    <div className="card" style={{ margin: "14px 14px 0", display: "flex", gap: 12, alignItems: "flex-start" }}>
      <img
        src="/icons/icon-192.png"
        alt=""
        width={44}
        height={44}
        style={{ borderRadius: 10, flex: "0 0 auto", border: "1px solid var(--line)" }}
      />
      <div style={{ flex: 1, minWidth: 0 }}>
        <div className="eyebrow blood">
          {updateReady ? tr(lang, "install.update") : tr(lang, "install.title")}
        </div>
        <p className="small" style={{ margin: "4px 0 10px" }}>
          {updateReady ? "" : tr(lang, "install.hint")}
          {needsManualSteps && <span> {tr(lang, "install.ios")}</span>}
        </p>
        <div className="row" style={{ gap: 8 }}>
          {updateReady ? (
            <button className="btn primary sm" onClick={applyUpdate}>
              {tr(lang, "install.apply")}
            </button>
          ) : canInstall ? (
            <button className="btn primary sm" onClick={install}>
              ⤓ {tr(lang, "install.cta")}
            </button>
          ) : null}
          <button className="btn sm ghost" onClick={dismiss}>
            ✕
          </button>
        </div>
      </div>
    </div>
  );
}
