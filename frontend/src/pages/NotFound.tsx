import { Link } from "react-router-dom";
import { tr } from "../lib/i18n";
import { useLang } from "../components/ui";

export default function NotFound() {
  const lang = useLang();
  return <div className="empty" style={{ marginTop: 28 }}><div className="eyebrow blood">404</div><h1 className="h1" style={{ margin: "9px 0" }}>{lang === "fr" ? "Page absente" : "Page not found"}</h1><p className="small">{lang === "fr" ? "Aucun écran mort : cette adresse ne correspond à aucun contenu documenté." : "No dead screen: this address does not match documented content."}</p><Link className="btn primary" to="/">{tr(lang, "nav.home")}</Link></div>;
}
