import React from "react";
import { Link } from "react-router-dom";
import { pick, tr, type Lang } from "../lib/i18n";
import type { Any, Bi } from "../lib/api";
import { useApp } from "../state/app";

/* ------------------------------------------------------------------ texte */
export function T({ k }: { k: string }) {
  const lang = useApp((s) => s.lang);
  return <>{tr(lang, k)}</>;
}

/** Rend une valeur bilingue dans la langue courante. */
export function Bi_({ v, fallback = "" }: { v: Bi | Any; fallback?: string }) {
  const lang = useApp((s) => s.lang);
  if (v === null || v === undefined || v === "") return <>{fallback}</>;
  if (typeof v === "string") return <>{v}</>;
  if (typeof v === "object" && !("fr" in v) && !("en" in v)) return <>{fallback}</>;
  const text = pick(v as Bi, lang);
  return <>{text || fallback}</>;
}

export function useLang(): Lang {
  return useApp((s) => s.lang);
}

/* ----------------------------------------------------------------- badges */
export const REL_CLASS: Record<string, string> = {
  CONFIRMED: "confirmed",
  PROBABLE: "probable",
  DISPUTED: "disputed",
  UNKNOWN: "unknown",
};

export function Reliability({ level, label }: { level?: string; label?: Bi }) {
  const meta = useApp((s) => s.meta);
  const lang = useApp((s) => s.lang);
  if (!level) return null;
  const found = (meta?.reliability || []).find((r: Any) => r.key === level);
  const text = label ? pick(label, lang) : found ? pick(found.label, lang) : level;
  return (
    <span className={`badge ${REL_CLASS[level] || ""}`} title={found ? pick(found.definition, lang) : level}>
      <span className="dot" /> {text}
    </span>
  );
}

export function StatusBadge({ status }: { status: string }) {
  const meta = useApp((s) => s.meta);
  const lang = useApp((s) => s.lang);
  const found = (meta?.statuses || []).find((s: Any) => s.key === status);
  return <span className="badge blood">{found ? pick(found.label, lang) : status}</span>;
}

export function TierBadge({ tier }: { tier?: string }) {
  const lang = useLang();
  if (!tier) return null;
  return <span className={`badge ${tier === "FREE" ? "free" : "premium"}`}>{tier === "FREE" ? (lang === "fr" ? "Libre" : "Free") : "Premium"}</span>;
}

/* ------------------------------------------------------------------ états */
export function Loading({ label }: { label?: string }) {
  const lang = useLang();
  return (
    <div className="stack" style={{ padding: "18px 0" }} aria-busy="true">
      <div className="eyebrow">{label || tr(lang, "common.loading")}</div>
      <div className="skeleton" style={{ width: "82%" }} />
      <div className="skeleton" style={{ width: "64%" }} />
      <div className="skeleton" style={{ width: "73%" }} />
    </div>
  );
}

export function ErrorState({ message, onRetry }: { message?: string; onRetry?: () => void }) {
  const lang = useLang();
  return (
    <div className="empty">
      <div className="h2" style={{ marginBottom: 6 }}>
        {tr(lang, "common.error")}
      </div>
      <div className="small" style={{ marginBottom: 12 }}>
        {message || tr(lang, "common.network")}
      </div>
      {onRetry && (
        <button className="btn sm" onClick={onRetry}>
          {tr(lang, "common.retry")}
        </button>
      )}
    </div>
  );
}

export function Empty({ children }: { children?: React.ReactNode }) {
  const lang = useLang();
  return <div className="empty">{children || tr(lang, "common.empty")}</div>;
}

export function Missing() {
  const lang = useLang();
  return (
    <div className="note neutral">
      <span className="badge unknown" style={{ marginRight: 8 }}>
        <span className="dot" /> {lang === "fr" ? "Inconnu" : "Unknown"}
      </span>
      {tr(lang, "common.missing")}
    </div>
  );
}

/* ------------------------------------------------------------------ source */
export function SourceLine({ source, compact }: { source?: Any | null; compact?: boolean }) {
  const lang = useLang();
  if (!source) return null;
  return (
    <div className="row wrap" style={{ gap: 6, marginTop: 7 }}>
      <Reliability level={source.reliability} />
      {source.url ? (
        <a className="tiny" href={source.url} target="_blank" rel="noreferrer noopener" style={{ textDecoration: "underline", textUnderlineOffset: 3 }}>
          {source.publisher || tr(lang, "common.source")} ↗
        </a>
      ) : (
        <span className="tiny">{source.publisher}</span>
      )}
      {!compact && source.date && <span className="tiny">· {source.date}</span>}
      {!compact && source.verified_at && (
        <span className="tiny">
          · {tr(lang, "common.verified")} {source.verified_at}
        </span>
      )}
    </div>
  );
}

/* ------------------------------------------------------------------ couverture */
const hash = (s: string) => {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) {
    h ^= s.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  return Math.abs(h);
};

/**
 * Plaque d'archive générée : sobre, aucune image externe, aucun visuel gore.
 * Le motif est déterministe (dérivé de l'identifiant du dossier).
 */
export function Cover({ slug, title, country, period, tall }: { slug: string; title?: Bi; country?: string; period?: Bi; tall?: boolean }) {
  const lang = useLang();
  const h = hash(slug);
  const angle = (h % 60) - 30;
  const cx = 20 + (h % 60);
  const cy = 18 + ((h >> 3) % 44);
  const rings = 2 + (h % 3);
  const label = title ? pick(title, lang) : slug;
  return (
    <svg
      className="cover"
      viewBox="0 0 160 100"
      preserveAspectRatio="xMidYMid slice"
      role="img"
      aria-label={label}
      style={tall ? { aspectRatio: "16 / 10", width: "100%", display: "block" } : { width: "100%", height: "100%", display: "block" }}
    >
      <defs>
        <linearGradient id={`g${slug}`} x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#191c21" />
          <stop offset="60%" stopColor="#0e1013" />
          <stop offset="100%" stopColor="#08090b" />
        </linearGradient>
        <clipPath id={`c${slug}`}>
          <rect x="0" y="0" width="160" height="100" />
        </clipPath>
      </defs>
      <g clipPath={`url(#c${slug})`}>
        <rect width="160" height="100" fill={`url(#g${slug})`} />
        <g stroke="#23262b" strokeWidth="0.35" opacity="0.85">
          {Array.from({ length: 11 }).map((_, i) => (
            <line key={`v${i}`} x1={i * 16} y1="0" x2={i * 16} y2="100" />
          ))}
          {Array.from({ length: 7 }).map((_, i) => (
            <line key={`h${i}`} x1="0" y1={i * 16} x2="160" y2={i * 16} />
          ))}
        </g>
        <g transform={`rotate(${angle} ${cx} ${cy})`} opacity="0.5">
          {Array.from({ length: rings }).map((_, i) => (
            <circle key={i} cx={cx} cy={cy} r={9 + i * 11} fill="none" stroke="#8e2233" strokeWidth={i === 0 ? 0.9 : 0.4} />
          ))}
          <line x1={cx - 46} y1={cy} x2={cx + 46} y2={cy} stroke="#8e2233" strokeWidth="0.4" strokeDasharray="2 3" />
        </g>
        <rect x="0" y="0" width="160" height="100" fill="url(#none)" opacity="0" />
        <g opacity="0.16">
          {Array.from({ length: 26 }).map((_, i) => (
            <rect key={i} x={(h >> (i % 7)) % 158} y={(h >> ((i % 5) + 2)) % 98} width="1.4" height="1.4" fill="#e8e4dc" />
          ))}
        </g>
        <text x="9" y="90" fill="#e8e4dc" fontFamily="ui-sans-serif, system-ui, sans-serif" fontSize="7" letterSpacing="1.6" opacity="0.92">
          {(country || "—").toUpperCase()}
        </text>
        <text x="151" y="90" textAnchor="end" fill="#9aa0a8" fontFamily="ui-monospace, monospace" fontSize="6" letterSpacing="0.8">
          {period ? pick(period, lang).toUpperCase() : ""}
        </text>
        <line x1="9" y1="80" x2="151" y2="80" stroke="#2b2f35" strokeWidth="0.5" />
      </g>
    </svg>
  );
}

/* ------------------------------------------------------------------ blocs */
/** Rend les blocs authored d'une section du dossier (paragraphes, listes). */
export function Blocks({ blocks }: { blocks: Any[] }) {
  const lang = useLang();
  if (!blocks || !blocks.length) return <Missing />;
  return (
    <div className="stack" style={{ gap: 14 }}>
      {blocks.map((b, i) => (
        <article key={i}>
          {b.title && (b.title.fr || b.title.en) && (
            <h3 className="h3" style={{ marginBottom: 6 }}>
              <Bi_ v={b.title} />
            </h3>
          )}
          {b.body && (b.body.fr || b.body.en) && (
            <p style={{ margin: "0 0 8px", fontSize: "15px", color: "var(--bone-dim)" }}>
              <Bi_ v={b.body} />
            </p>
          )}
          {Array.isArray(b.items) && b.items.length > 0 && (
            <ul style={{ margin: 0, paddingLeft: 18 }}>
              {b.items.map((it: Any, j: number) => (
                <li key={j} style={{ marginBottom: 6, color: "var(--bone-dim)", fontSize: "14.5px" }}>
                  {it.label && (it.label.fr || it.label.en) && (
                    <span className="eyebrow" style={{ marginRight: 6 }}>
                      <Bi_ v={it.label} /> —
                    </span>
                  )}
                  {it.text && typeof it.text === "object" ? <Bi_ v={it.text} /> : <>{String(it.text ?? "")}</>}
                  {it.reliability && (
                    <span style={{ marginLeft: 8 }}>
                      <Reliability level={it.reliability} />
                    </span>
                  )}
                </li>
              ))}
            </ul>
          )}
          <div className="row wrap" style={{ gap: 8, marginTop: 8 }}>
            {b.reliability && <Reliability level={b.reliability} />}
            {b.source && <span className="tiny">réf. {b.source}</span>}
          </div>
          {b.kind === "unknown" && <div className="tiny" style={{ marginTop: 6 }}>{tr(lang, "common.missing")}</div>}
        </article>
      ))}
    </div>
  );
}

/** Une puce d'élément (leçons, zones d'ombre, erreurs). */
export function Item({ it }: { it: Any }) {
  return (
    <div className="card tight">
      <div style={{ fontSize: "14.5px", color: "var(--bone-dim)" }}>
        {it.text && typeof it.text === "object" ? <Bi_ v={it.text} /> : <>{String(it.text ?? "")}</>}
      </div>
      <div className="row wrap" style={{ gap: 8, marginTop: 8 }}>
        {it.label && (it.label.fr || it.label.en) && (
          <span className="badge">
            <Bi_ v={it.label} />
          </span>
        )}
        {it.reliability && <Reliability level={it.reliability} />}
        {it.source && <span className="tiny">réf. {it.source}</span>}
      </div>
    </div>
  );
}

export function Items({ list }: { list: Any[] }) {
  if (!list || !list.length) return <Missing />;
  return (
    <div className="stack">
      {list.map((it, i) => (
        <Item key={i} it={it} />
      ))}
    </div>
  );
}

export function PageTitle({ eyebrow, title, children }: { eyebrow?: string; title: React.ReactNode; children?: React.ReactNode }) {
  return (
    <header style={{ padding: "20px 0 6px" }}>
      {eyebrow && <div className="eyebrow blood">{eyebrow}</div>}
      <h1 className="h1" style={{ margin: "6px 0 8px" }}>
        {title}
      </h1>
      {children}
    </header>
  );
}

export function BackLink({ to, label }: { to: string; label?: string }) {
  const lang = useLang();
  return (
    <Link to={to} className="tiny" style={{ display: "inline-flex", gap: 6, alignItems: "center", padding: "10px 0" }}>
      ← {label || tr(lang, "common.back")}
    </Link>
  );
}
