import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./styles.css";
import { applyA11y, useApp } from "./state/app";
import { registerServiceWorker } from "./lib/pwa";

applyA11y(JSON.parse(localStorage.getItem("yanisx.a11y") || "{}"));
document.documentElement.lang = useApp.getState().lang;

/* Service worker : c'est lui qui rend l'application installable et capable de
   démarrer sans réseau. Ignoré en développement (voir lib/pwa.ts). */
registerServiceWorker();

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
);
