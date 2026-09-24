import { useState } from "react";
import { Link } from "react-router-dom";
import { endpoints, type Any } from "../lib/api";
import { useApi } from "../lib/hooks";
import { pick, tr } from "../lib/i18n";
import { useApp } from "../state/app";
import { Bi_, ErrorState, Loading, PageTitle, Reliability, useLang } from "../components/ui";

export default function Memory() {
  const lang = useLang();
  const award = useApp((s) => s.award);
  const [country, setCountry] = useState("");
  const [open, setOpen] = useState<string | null>(null);
  const path = country ? `/memory?country=${country}` : "/memory";
  const { data, loading, error, reload } = useApi<Any>(path, [country]);
  const countries = useApi<Any>("/memory/countries");

  const groups: Any[] = data?.groups || [];

  const toggle = (key: string) => {
    const next = open === key ? null : key;
    setOpen(next);
    if (next) award("victim_remembered", `victim:${next}`);
  };

  return (
    <>
      <PageTitle eyebrow="🕯" title={tr(lang, "nav.memory")}>
        <div className="note" style={{ marginTop: 4 }}>
          <strong>{pick(data?.question, lang) || tr(lang, "victim.question")}</strong>
        </div>
      </PageTitle>

      {data && (
        <div className="row wrap" style={{ gap: 6, marginBottom: 14 }}>
          <span className="badge free">{lang === "fr" ? "Accès libre permanent" : "Permanent free access"}</span>
          <span className="badge">
            {data.counts.victims} {lang === "fr" ? "victimes" : "victims"}
          </span>
          <span className="badge confirmed">
            <span className="dot" /> {data.counts.named} {lang === "fr" ? "nommées" : "named"}
          </span>
          {data.counts.not_documented > 0 && (
            <span className="badge unknown">
              <span className="dot" /> {data.counts.not_documented} {lang === "fr" ? "non documentées" : "not documented"}
            </span>
          )}
        </div>
      )}

      {data?.note_on_missing && (
        <div className="note neutral" style={{ marginBottom: 14 }}>
          {pick(data.note_on_missing, lang)}
        </div>
      )}

      {(countries.data?.countries || []).length > 0 && (
        <div className="tabs">
          <button className={`chip ${country === "" ? "on" : ""}`} aria-pressed={country === ""} onClick={() => setCountry("")}>
            {tr(lang, "common.all")}
          </button>
          {(countries.data?.countries || []).map((c: Any) => (
            <button key={c.code} className={`chip ${country === c.code ? "on" : ""}`} aria-pressed={country === c.code} onClick={() => setCountry(c.code)}>
              {c.flag} {c.names[lang] || c.names.fr} ({c.victims})
            </button>
          ))}
        </div>
      )}

      {loading && <Loading />}
      {error && <ErrorState message={error} onRetry={reload} />}

      {data && groups.length === 0 && !loading && (
        <div className="empty">{lang === "fr" ? "Aucune victime documentée pour ce pays." : "No documented victim for this country."}</div>
      )}

      <div className="stack" style={{ marginTop: 6 }}>
        {groups.map((g) => (
          <section key={g.case.slug} className="card">
            <div className="between" style={{ marginBottom: 10 }}>
              <div style={{ minWidth: 0 }}>
                <Link to={`/dossiers/${g.case.slug}`} className="eyebrow blood">
                  {g.case.slug}
                </Link>
                <h2 className="h2" style={{ fontSize: 15.5, marginTop: 4 }}>
                  <Bi_ v={g.case.title} />
                </h2>
                <div className="tiny">
                  {g.case.country_name?.[lang] || g.case.country} · <Bi_ v={g.case.period_label} />
                </div>
              </div>
              <Link className="btn sm ghost" to={`/dossiers/${g.case.slug}/memoire`}>
                {tr(lang, "case.memory")}
              </Link>
            </div>

            {g.memorial.map((m: Any) => (
              <div key={m.id} className="note" style={{ marginBottom: 10 }}>
                {m.title && (m.title.fr || m.title.en) && (
                  <div className="h3" style={{ marginBottom: 5 }}>
                    <Bi_ v={m.title} />
                  </div>
                )}
                {m.biography && (m.biography.fr || m.biography.en) && (
                  <p style={{ margin: "0 0 7px", fontSize: "14px", color: "var(--bone-dim)" }}>
                    <Bi_ v={m.biography} />
                  </p>
                )}
                {m.testimony && (m.testimony.fr || m.testimony.en) && (
                  <p style={{ margin: 0, fontSize: "14px", fontStyle: "italic", color: "var(--bone-dim)" }}>
                    <Bi_ v={m.testimony} />
                  </p>
                )}
              </div>
            ))}

            <div className="stack" style={{ gap: 8 }}>
              {g.victims.map((v: Any) => {
                const key = `${g.case.slug}:${v.id}`;
                const isOpen = open === key;
                const items = (lang === "en" ? v.life?.en?.items : v.life?.fr?.items) || v.life?.fr?.items || [];
                const dis = (lang === "en" ? v.disappearance?.en?.items : v.disappearance?.fr?.items) || v.disappearance?.fr?.items || [];
                const headline = (lang === "en" ? v.life?.en?.headline : v.life?.fr?.headline) || v.life?.fr?.headline;
                return (
                  <article key={v.id} style={{ border: "1px solid var(--line)", borderRadius: 12, overflow: "hidden" }}>
                    <button
                      className="card tight"
                      style={{ width: "100%", textAlign: "left", border: 0, borderRadius: 0, background: isOpen ? "var(--anthracite-2)" : "var(--ink-2)" }}
                      onClick={() => toggle(key)}
                      aria-expanded={isOpen}
                    >
                      <div className="between">
                        <div style={{ minWidth: 0 }}>
                          <div className="h2" style={{ fontSize: 14.5 }}>
                            🕯 {v.anonymised ? (lang === "fr" ? "Identité non publiée" : "Identity not published") : v.name || `${v.first_name} ${v.last_name}`}
                          </div>
                          <div className="tiny">
                            {v.age ? `${tr(lang, "victim.age")} : ${v.age}` : ""} {headline ? `· ${headline}` : ""}
                          </div>
                        </div>
                        <Reliability level={v.reliability} />
                      </div>
                    </button>

                    {isOpen && (
                      <div style={{ padding: 13, background: "var(--anthracite)" }}>
                        {v.anonymised && <div className="note warn" style={{ marginBottom: 10 }}>{tr(lang, "victim.anonymised")}</div>}

                        {items.length > 0 ? (
                          <dl className="kv" style={{ marginBottom: 12 }}>
                            {items.map((it: Any, i: number) => (
                              <div key={i} style={{ display: "contents" }}>
                                <dt>
                                  <Bi_ v={it.label} />
                                </dt>
                                <dd>{typeof it.text === "object" ? <Bi_ v={it.text} /> : String(it.text ?? "")}</dd>
                              </div>
                            ))}
                          </dl>
                        ) : (
                          <div className="note neutral" style={{ marginBottom: 12 }}>{tr(lang, "common.missing")}</div>
                        )}

                        {dis.length > 0 && (
                          <>
                            <div className="h3" style={{ marginBottom: 6 }}>
                              {lang === "fr" ? "Circonstances" : "Circumstances"}
                            </div>
                            <dl className="kv" style={{ marginBottom: 12 }}>
                              {dis.map((it: Any, i: number) => (
                                <div key={i} style={{ display: "contents" }}>
                                  <dt>
                                    <Bi_ v={it.label} />
                                  </dt>
                                  <dd>{typeof it.text === "object" ? <Bi_ v={it.text} /> : String(it.text ?? "")}</dd>
                                </div>
                              ))}
                            </dl>
                          </>
                        )}

                        {(v.note?.fr || v.note?.en) && (
                          <div className="note neutral" style={{ marginBottom: 12 }}>
                            <Bi_ v={v.note} />
                          </div>
                        )}

                        {v.memorials?.length > 0 && (
                          <div className="stack" style={{ gap: 8, marginBottom: 12 }}>
                            {v.memorials.map((m: Any) => (
                              <div key={m.id} className="note">
                                {m.memory && (m.memory.fr || m.memory.en) && <Bi_ v={m.memory} />}
                              </div>
                            ))}
                          </div>
                        )}

                        {v.source && (
                          <div className="tiny">
                            {tr(lang, "common.source")} : {v.source.publisher} · {v.source.date} ·{" "}
                            {v.source.url && (
                              <a href={v.source.url} target="_blank" rel="noreferrer noopener" style={{ textDecoration: "underline" }}>
                                {tr(lang, "common.link")} ↗
                              </a>
                            )}
                          </div>
                        )}

                        <div className="row" style={{ gap: 8, marginTop: 12 }}>
                          <Link className="btn sm ghost" to={`/dossiers/${g.case.slug}`}>
                            {tr(lang, "case.dossier")} →
                          </Link>
                          <Link className="btn sm ghost" to={`/dossiers/${g.case.slug}/memoire`}>
                            🕯 {tr(lang, "case.memory")}
                          </Link>
                        </div>
                      </div>
                    )}
                  </article>
                );
              })}
            </div>
          </section>
        ))}
      </div>

      {data?.ethics_note && (
        <div className="disclaimer" style={{ margin: "18px 0" }}>
          {pick(data.ethics_note, lang)}
        </div>
      )}
    </>
  );
}
