import metaData from "../data_embedded/meta.json";
import casesData from "../data_embedded/cases.json";
import exploreData from "../data_embedded/explore.json";
import archivesData from "../data_embedded/archives.json";
import memoryData from "../data_embedded/memory.json";
import glossaryData from "../data_embedded/glossary.json";
import countriesData from "../data_embedded/countries.json";
import coursesData from "../data_embedded/courses.json";
import episodesData from "../data_embedded/episodes.json";
import counterfactualsData from "../data_embedded/counterfactuals.json";

// Import tous les sous-fichiers de cas dynamiquement via Vite glob
const caseModules = import.meta.glob("../data_embedded/cases/**/*.json", { eager: true });
const episodeModules = import.meta.glob("../data_embedded/episodes/*.json", { eager: true });

export const embeddedData: Record<string, any> = {
  "/meta": metaData,
  "/cases": casesData,
  "/explore": exploreData,
  "/archives": archivesData,
  "/memory": memoryData,
  "/glossary": glossaryData,
  "/countries": countriesData,
  "/courses": coursesData,
  "/episodes": episodesData,
  "/counterfactuals": counterfactualsData,
};

export function getEmbeddedPayload(cleanPath: string): any {
  if (embeddedData[cleanPath]) {
    return embeddedData[cleanPath];
  }

  // /cases/{slug}
  const caseMatch = cleanPath.match(/^\/cases\/([^\/]+)$/);
  if (caseMatch) {
    const slug = caseMatch[1];
    const key = `../data_embedded/cases/${slug}.json`;
    if (caseModules[key]) return (caseModules[key] as any).default || caseModules[key];
  }

  // /cases/{slug}/{sub}
  const caseSubMatch = cleanPath.match(/^\/cases\/([^\/]+)\/([^\/]+)$/);
  if (caseSubMatch) {
    const slug = caseSubMatch[1];
    const sub = caseSubMatch[2];
    const key = `../data_embedded/cases/${slug}/${sub}.json`;
    if (caseModules[key]) return (caseModules[key] as any).default || caseModules[key];
  }

  // /episodes/{id}
  const epMatch = cleanPath.match(/^\/episodes\/(\d+)$/);
  if (epMatch) {
    const epid = epMatch[1];
    const key = `../data_embedded/episodes/${epid}.json`;
    if (episodeModules[key]) return (episodeModules[key] as any).default || episodeModules[key];
  }

  return null;
}
