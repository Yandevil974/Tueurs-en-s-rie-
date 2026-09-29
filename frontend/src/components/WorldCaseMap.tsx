import { useEffect, useMemo, useRef, useState } from "react";
import { Link } from "react-router-dom";
import type { Any } from "../lib/api";
import { pick, tr } from "../lib/i18n";
import CaseCard from "./CaseCard";
import { Bi_, Empty, useLang } from "./ui";
import worldCountries from "../data/world-countries.json";

/**
 * Frontières Natural Earth (110m, domaine public), rendues en SVG sans tuiles
 * réseau. Les zones sélectionnables sont des continents, pas des lieux précis.
 */
const MAP_W = 1000;
const MAP_H = 470;
const MAP_PAD_Y = 20;
const LAT_LIMIT = 84;

type Point = [number, number];
type GeoFeature = {
  type: "Feature";
  properties: { name: string; iso: string; continent: string };
  geometry: { type: "Polygon" | "MultiPolygon"; coordinates: any };
};

type ContinentOption = {
  apiName: string;
  fr: string;
  en: string;
  geoName: string;
  anchor: Point;
};

const CONTINENTS: ContinentOption[] = [
  { apiName: "Amérique du Nord", fr: "Amérique du Nord", en: "North America", geoName: "North America", anchor: [215, 145] },
  { apiName: "Amérique du Sud", fr: "Amérique du Sud", en: "South America", geoName: "South America", anchor: [335, 305] },
  { apiName: "Europe", fr: "Europe", en: "Europe", geoName: "Europe", anchor: [520, 112] },
  { apiName: "Afrique", fr: "Afrique", en: "Africa", geoName: "Africa", anchor: [530, 240] },
  { apiName: "Asie", fr: "Asie", en: "Asia", geoName: "Asia", anchor: [735, 145] },
  { apiName: "Océanie", fr: "Océanie", en: "Oceania", geoName: "Oceania", anchor: [865, 325] },
];

const GEO_TO_API = Object.fromEntries(CONTINENTS.map((item) => [item.geoName, item.apiName]));
const FEATURES = (worldCountries.features || []) as GeoFeature[];

function project([longitude, latitude]: Point): Point {
  const lon = Math.max(-180, Math.min(180, longitude));
  const lat = Math.max(-LAT_LIMIT, Math.min(LAT_LIMIT, latitude));
  return [
    ((lon + 180) / 360) * MAP_W,
    MAP_PAD_Y + ((LAT_LIMIT - lat) / (LAT_LIMIT * 2)) * (MAP_H - MAP_PAD_Y * 2),
  ];
}

function ringPath(ring: Point[]): string {
  const fragments: Point[][] = [];
  let current: Point[] = [];
  let previousLongitude: number | null = null;

  for (const coordinate of ring) {
    const [longitude, latitude] = coordinate;
    if (previousLongitude !== null && Math.abs(longitude - previousLongitude) > 180) {
      if (current.length >= 3) fragments.push(current);
      current = [];
    }
    current.push(project([longitude, latitude]));
    previousLongitude = longitude;
  }
  if (current.length >= 3) fragments.push(current);

  return fragments
    .map((fragment) => {
      const [first, ...rest] = fragment;
      return `M${first[0].toFixed(1)},${first[1].toFixed(1)}${rest.map(([x, y]) => `L${x.toFixed(1)},${y.toFixed(1)}`).join("")}Z`;
    })
    .join("");
}

function featurePath(feature: GeoFeature): string {
  const polygons = feature.geometry.type === "Polygon" ? [feature.geometry.coordinates] : feature.geometry.coordinates;
  return polygons.map((polygon: Point[][]) => polygon.map(ringPath).join("")).join("");
}

function normalise(value: string) {
  return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[^a-z]/g, "");
}

function continentRecord(records: Any[], apiName: string) {
  const key = normalise(apiName);
  return records.find((record) => normalise(record.name || "") === key);
}

function label(option: ContinentOption, lang: string) {
  return option[lang === "en" ? "en" : "fr"];
}

export default function WorldCaseMap({
  cases,
  continents,
  loading = false,
}: {
  cases: Any[];
  continents: Any[];
  loading?: boolean;
}) {
  const lang = useLang();
  const [selected, setSelected] = useState<string | null>(null);
  const [hovered, setHovered] = useState<string | null>(null);
  const didAutoSelect = useRef(false);

  const options = useMemo(() => CONTINENTS.map((option) => {
    const record = continentRecord(continents, option.apiName);
    const countries: Any[] = record?.countries || [];
    const countryCodes = new Set(countries.map((country) => String(country.code || "").toUpperCase()));
    const relatedCases = cases.filter((item) => countryCodes.has(String(item.country || "").toUpperCase()));
    return { ...option, cases: relatedCases, countries, count: relatedCases.length };
  }), [cases, continents]);

  useEffect(() => {
    if (didAutoSelect.current || loading) return;
    const mostRepresented = [...options].sort((a, b) => b.count - a.count).find((option) => option.count > 0);
    if (mostRepresented) setSelected(mostRepresented.apiName);
    didAutoSelect.current = true;
  }, [loading, options]);

  const paths = useMemo(() => FEATURES.map((feature) => ({
    key: `${feature.properties.iso}-${feature.properties.name}`,
    name: feature.properties.name,
    apiContinent: GEO_TO_API[feature.properties.continent],
    d: featurePath(feature),
  })), []);

  const active = options.find((option) => option.apiName === selected) || null;
  const select = (apiName: string | null) => {
    didAutoSelect.current = true;
    setSelected(apiName);
  };
  const selectedName = active ? label(active, lang) : "";
  const longitudes = [-120, -60, 0, 60, 120];
  const latitudes = [-60, -30, 0, 30, 60];

  return (
    <section className="world-map-section" aria-labelledby="world-map-heading">
      <div className="world-map-heading between">
        <div>
          <div className="eyebrow blood">{lang === "fr" ? "Explorer par territoire" : "Explore by region"}</div>
          <h2 id="world-map-heading" className="h2">
            {lang === "fr" ? "Les affaires, sur la carte" : "Cases on the map"}
          </h2>
        </div>
        <Link className="tiny world-map-expand" to="/explorer/carte">
          {lang === "fr" ? "Plein écran" : "Full map"} ↗
        </Link>
      </div>
      <p className="small world-map-intro">
        {lang === "fr"
          ? "Touchez un continent pour afficher les dossiers qui s’y rapportent. Les contours montrent les pays ; aucune adresse précise n’est affichée."
          : "Tap a continent to see its related dossiers. Country outlines are shown; no exact address is displayed."}
      </p>

      <div className="world-map-frame">
        <svg
          className="world-map-svg"
          viewBox={`0 0 ${MAP_W} ${MAP_H}`}
          role="img"
          aria-label={lang === "fr" ? "Carte du monde interactive par continent" : "Interactive world map by continent"}
        >
          <defs>
            <linearGradient id="world-ocean" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stopColor="#111922" />
              <stop offset="100%" stopColor="#0b1016" />
            </linearGradient>
            <linearGradient id="world-land-active" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#672a38" />
              <stop offset="100%" stopColor="#3c2029" />
            </linearGradient>
            <filter id="world-glow" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="8" result="blur" />
              <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
            </filter>
          </defs>
          <rect className="world-map-ocean" width={MAP_W} height={MAP_H} rx="20" fill="url(#world-ocean)" />
          <g className="world-map-graticule" aria-hidden="true">
            {longitudes.map((longitude) => {
              const [x] = project([longitude, 0]);
              return <line key={`lon-${longitude}`} x1={x} y1="0" x2={x} y2={MAP_H} />;
            })}
            {latitudes.map((latitude) => {
              const [, y] = project([0, latitude]);
              return <line key={`lat-${latitude}`} x1="0" y1={y} x2={MAP_W} y2={y} />;
            })}
          </g>
          <g className="world-map-countries" aria-hidden="true">
            {paths.map((path) => {
              const isSelected = Boolean(active && path.apiContinent === active.apiName);
              const hasCases = options.some((option) => option.apiName === path.apiContinent && option.count > 0);
              return (
                <path
                  key={path.key}
                  d={path.d}
                  className={`world-map-country${hasCases ? " has-cases" : ""}${isSelected ? " is-selected" : ""}${hovered === path.apiContinent ? " is-hovered" : ""}`}
                  fill={isSelected ? "url(#world-land-active)" : hasCases ? "#29323a" : "#1c252c"}
                  stroke={isSelected ? "#d27a87" : "#35414a"}
                  onClick={() => path.apiContinent && select(path.apiContinent)}
                  onMouseEnter={() => setHovered(path.apiContinent || null)}
                  onMouseLeave={() => setHovered(null)}
                >
                  <title>{path.name}</title>
                </path>
              );
            })}
          </g>
          <g className="world-map-labels">
            {options.filter((option) => option.count > 0).map((option) => {
              const [x, y] = option.anchor;
              const isSelected = selected === option.apiName;
              return (
                <g
                  key={option.apiName}
                  className={`world-map-count${isSelected ? " is-selected" : ""}`}
                  transform={`translate(${x},${y})`}
                  onClick={() => select(option.apiName)}
                  aria-hidden="true"
                >
                  <circle className="world-map-count-glow" r="22" />
                  <circle className="world-map-count-core" r="14" />
                  <text y="4">{option.count}</text>
                </g>
              );
            })}
          </g>
        </svg>
        <div className="world-map-caption">
          <span className="world-map-caption-dot" />
          {lang === "fr" ? "Nombre de dossiers par continent" : "Dossiers by continent"}
        </div>
      </div>

      <div className="world-map-filters" role="group" aria-label={lang === "fr" ? "Choisir un continent" : "Choose a continent"}>
        {options.map((option) => (
          <button
            key={option.apiName}
            type="button"
            className={`continent-filter${selected === option.apiName ? " is-selected" : ""}`}
            aria-pressed={selected === option.apiName}
            onClick={() => select(option.apiName)}
          >
            <span>{label(option, lang)}</span>
            <span className="continent-filter-count">{option.count}</span>
          </button>
        ))}
        <button
          type="button"
          className={`continent-filter all${selected === null ? " is-selected" : ""}`}
          aria-pressed={selected === null}
          onClick={() => select(null)}
        >
          <span>{lang === "fr" ? "Tous" : "All"}</span>
          <span className="continent-filter-count">{cases.length}</span>
        </button>
      </div>

      <div className="world-map-results" aria-live="polite">
        <div className="between world-map-results-title">
          <div>
            <div className="eyebrow">{lang === "fr" ? "Sélection" : "Selection"}</div>
            <h3 className="h2">
              {active ? selectedName : lang === "fr" ? "Tous les dossiers" : "All dossiers"}
            </h3>
          </div>
          <span className="badge blood">
            {active ? active.count : cases.length} {lang === "fr" ? "dossier(s)" : "dossier(s)"}
          </span>
        </div>

        {active && active.countries.length > 0 && (
          <div className="world-map-countries-list">
            {active.countries.map((country: Any) => (
              <Link
                className="world-map-country-chip"
                key={country.code}
                to={`/explorer/pays/${country.code}`}
                title={lang === "fr" ? "Voir les dossiers du pays" : "See dossiers from this country"}
              >
                <span>{country.flag}</span>
                <span>{country.names?.[lang] || country.names?.fr || country.code}</span>
                <span className="tiny">{country.cases}</span>
              </Link>
            ))}
          </div>
        )}

        {loading ? (
          <div className="empty">{lang === "fr" ? "Chargement du catalogue…" : "Loading the catalogue…"}</div>
        ) : (active ? active.cases : cases).length > 0 ? (
          <div className="world-case-grid">
            {(active ? active.cases : cases).map((caseFile: Any) => (
              <CaseCard key={caseFile.slug} c={caseFile} compact />
            ))}
          </div>
        ) : (
          <Empty>
            {lang === "fr"
              ? `Aucun dossier du catalogue n’est encore rattaché à ${selectedName || "ce territoire"}.`
              : `No dossier in the catalogue is currently linked to ${selectedName || "this region"}.`}
          </Empty>
        )}
      </div>
    </section>
  );
}
