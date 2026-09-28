import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { HashRouter } from "react-router-dom";
import App from "./App";
import "./styles.css";
import { applyA11y, useApp } from "./state/app";
import { registerServiceWorker } from "./lib/pwa";

applyA11y(JSON.parse(localStorage.getItem("yanisx.a11y") || "{}"));
document.documentElement.lang = useApp.getState().lang;

/* Service worker : utile pour le mode web PWA hors-ligne */
registerServiceWorker();

const rootElement = document.getElementById("root");
if (rootElement) {
  // Remplacer le contenu initial de démarrage
  rootElement.innerHTML = "";
  createRoot(rootElement).render(
    <StrictMode>
      <HashRouter>
        <App />
      </HashRouter>
    </StrictMode>,
  );
}
