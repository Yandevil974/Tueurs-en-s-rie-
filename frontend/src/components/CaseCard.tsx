import { Link } from "react-router-dom";
import type { Any } from "../lib/api";
import { pick } from "../lib/i18n";
import { useApp } from "../state/app";
import { Bi_, Cover, StatusBadge, TierBadge, useLang } from "./ui";

export default function CaseCard({ c, compact }: { c: Any; compact?: boolean }) {
  const lang = useLang();
  const favourites = useApp((s) => s.favourites);
  const fav = favourites.includes(c.slug);
  return (
    <Link to={`/dossiers/${c.slug}`} className="casecard" aria-label={pick(c.title, lang)}>
      <div className="cover">
        <Cover slug={c.slug} title={c.title} country={c.country} period={c.period_label} />
      </div>
      <div className="body">
        <div className="row wrap" style={{ gap: 6 }}>
          <StatusBadge status={c.status} />
          <span className="badge">
            {c.country_name?.[lang] || c.country} · <Bi_ v={c.period_label} />
          </span>
        </div>
        <div className="ttl">
          <Bi_ v={c.title} />
        </div>
        {!compact && (
          <div className="small" style={{ overflow: "hidden", display: "-webkit-box", WebkitLineClamp: 2, WebkitBoxOrient: "vertical" }}>
            <Bi_ v={c.subtitle} />
          </div>
        )}
        <div className="row wrap" style={{ gap: 6, marginTop: "auto" }}>
          <span className="tiny">
            {c.victims_count} {lang === "fr" ? "victime(s) documentée(s)" : "documented victim(s)"}
          </span>
          {c.episodes_count > 0 && <span className="tiny">· {c.episodes_count} 🎧</span>}
          <TierBadge tier={c.tier} />
          {fav && <span className="tiny">★</span>}
        </div>
      </div>
    </Link>
  );
}
