import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./styles.css";
import { applyA11y, useApp } from "./state/app";

applyA11y(JSON.parse(localStorage.getItem("yanisx.a11y") || "{}"));
document.documentElement.lang = useApp.getState().lang;

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
);
