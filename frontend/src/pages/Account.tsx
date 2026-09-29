import { Link } from "react-router-dom";
import { tr } from "../lib/i18n";
import { useApp } from "../state/app";
import { PageTitle, useLang } from "../components/ui";

export default function Account() {
  const lang = useLang();
  const a11y = useApp((s) => s.a11y);
  const setA11y = useApp((s) => s.setA11y);

  const resetLocalData = () => {
    const confirmed = window.confirm(lang === "fr"
      ? "Effacer les préférences, favoris, progressions et réflexions enregistrés sur cet appareil ?"
      : "Clear preferences, favourites, listening progress and reflections saved on this device?");
    if (!confirmed) return;
    for (const key of Object.keys(localStorage)) {
      if (key.startsWith("yanisx.")) localStorage.removeItem(key);
    }
    window.location.assign("/");
  };

  return (
    <>
      <PageTitle eyebrow="⚙" title={tr(lang, "nav.settings")}>
        <p className="small" style={{ margin: 0 }}>
          {lang === "fr"
            ? "YANIS//X est configurée pour un usage personnel : aucun compte, aucune adresse e-mail ni mot de passe."
            : "YANIS//X is set up for personal use: no account, email address or password."}
        </p>
      </PageTitle>

      <section className="card" style={{ marginBottom: 12 }}>
        <div className="between">
          <div>
            <div className="eyebrow blood">⚙ {tr(lang, "account.a11y")}</div>
            <h2 className="h2" style={{ fontSize: 15, marginTop: 5 }}>
              {lang === "fr" ? "Une lecture et une écoute adaptées" : "Reading and listening preferences"}
            </h2>
          </div>
          <span className="badge">{lang === "fr" ? "Sur cet appareil" : "This device"}</span>
        </div>
        <div className="stack" style={{ gap: 12, marginTop: 14 }}>
          <label className="lbl">
            {lang === "fr" ? "Taille du texte" : "Text size"}
            <select className="field" style={{ width: "100%", borderRadius: 9 }} value={String(a11y.fontScale || 1)} onChange={(e) => setA11y({ fontScale: Number(e.target.value) })}>
              <option value="0.9">90%</option>
              <option value="1">100%</option>
              <option value="1.15">115%</option>
              <option value="1.3">130%</option>
              <option value="1.5">150%</option>
            </select>
          </label>
          <label className="row" style={{ justifyContent: "space-between" }}>
            {lang === "fr" ? "Contraste renforcé" : "High contrast"}
            <input type="checkbox" checked={a11y.contrast === "high"} onChange={(e) => setA11y({ contrast: e.target.checked ? "high" : "standard" })} />
          </label>
          <label className="row" style={{ justifyContent: "space-between" }}>
            {lang === "fr" ? "Réduire les animations" : "Reduce motion"}
            <input type="checkbox" checked={Boolean(a11y.reduceMotion)} onChange={(e) => setA11y({ reduceMotion: e.target.checked })} />
          </label>
          <label className="row" style={{ justifyContent: "space-between" }}>
            {lang === "fr" ? "Afficher les transcriptions par défaut" : "Show transcripts by default"}
            <input type="checkbox" checked={a11y.captions !== false} onChange={(e) => setA11y({ captions: e.target.checked })} />
          </label>
        </div>
      </section>

      <section className="card" style={{ marginBottom: 12 }}>
        <div className="eyebrow blood">{lang === "fr" ? "Données locales" : "Local data"}</div>
        <h2 className="h2" style={{ fontSize: 15, marginTop: 5 }}>
          {lang === "fr" ? "Vos repères restent sur cet appareil" : "Your personal notes stay on this device"}
        </h2>
        <p className="small" style={{ marginBottom: 0 }}>
          {lang === "fr"
            ? "La langue, les favoris, la reprise audio, les réflexions et les préférences d’affichage sont enregistrés dans le stockage local du navigateur. Ils ne sont pas synchronisés avec un compte."
            : "Language, favourites, listening progress, reflections and display preferences are saved in this browser’s local storage. They are not synced to an account."}
        </p>
        <button className="btn sm ghost" style={{ marginTop: 13 }} onClick={resetLocalData}>
          {lang === "fr" ? "Effacer mes données locales" : "Clear my local data"}
        </button>
      </section>

      <Link className="card" style={{ display: "block", marginBottom: 14 }} to="/ethique">
        <div className="eyebrow blood">⚖ {tr(lang, "nav.ethics")}</div>
        <div className="h2" style={{ fontSize: 14, marginTop: 5 }}>
          {lang === "fr" ? "Lire la charte éditoriale" : "Read the editorial charter"} →
        </div>
      </Link>
    </>
  );
}
