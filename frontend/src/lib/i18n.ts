/** Internationalisation FR / EN (§47). Architecture prête pour DE/ES/IT/PT. */
import type { Bi } from "./api";

export type Lang = "fr" | "en";

type Dict = Record<string, { fr: string; en: string }>;

export const UI: Dict = {
  "app.name": { fr: "YANIS//X", en: "YANIS//X" },
  "app.tagline": { fr: "à travers mon regard", en: "through my eyes" },
  "app.identity": { fr: "Archives criminelles premium", en: "Premium criminal archives" },

  "nav.home": { fr: "Accueil", en: "Home" },
  "nav.search": { fr: "Rechercher", en: "Search" },
  "nav.explore": { fr: "Explorer", en: "Explore" },
  "nav.podcasts": { fr: "Podcasts", en: "Podcasts" },
  "nav.library": { fr: "Bibliothèque", en: "Library" },
  "nav.memory": { fr: "Mémoire", en: "Memory" },
  "nav.more": { fr: "Plus", en: "More" },
  "nav.psychology": { fr: "Psychologie", en: "Psychology" },
  "nav.investigations": { fr: "Enquêtes", en: "Investigations" },
  "nav.coldcases": { fr: "Cold cases", en: "Cold cases" },
  "nav.archives": { fr: "Archives", en: "Archives" },
  "nav.training": { fr: "Formation", en: "Training" },
  "nav.whatif": { fr: "Et si ?", en: "What if?" },
  "nav.ethics": { fr: "Éthique", en: "Ethics" },
  "nav.account": { fr: "Compte", en: "Account" },

  "home.continue": { fr: "Reprendre", en: "Resume" },
  "home.dossiers": { fr: "Dossiers", en: "Dossiers" },
  "home.latest": { fr: "Derniers dossiers publiés", en: "Latest published dossiers" },
  "home.journey": { fr: "Le parcours", en: "The journey" },
  "home.free": { fr: "En accès libre", en: "Free access" },
  "home.unsolved": { fr: "Non élucidés", en: "Unsolved" },
  "home.memory": { fr: "Ne jamais oublier les victimes", en: "Never forget the victims" },
  "home.analyst": { fr: "L'Analyste", en: "The Analyst" },
  "home.analyst.hint": {
    fr: "Pose une question : la réponse ne vient que des données documentées.",
    en: "Ask a question: the answer comes only from documented data.",
  },

  "common.loading": { fr: "Chargement…", en: "Loading…" },
  "common.error": { fr: "Une erreur est survenue", en: "Something went wrong" },
  "common.retry": { fr: "Réessayer", en: "Retry" },
  "common.back": { fr: "Retour", en: "Back" },
  "common.close": { fr: "Fermer", en: "Close" },
  "common.open": { fr: "Ouvrir", en: "Open" },
  "common.see": { fr: "Voir", en: "See" },
  "common.all": { fr: "Tout", en: "All" },
  "common.source": { fr: "Source", en: "Source" },
  "common.sources": { fr: "Sources", en: "Sources" },
  "common.date": { fr: "Date", en: "Date" },
  "common.author": { fr: "Auteur", en: "Author" },
  "common.type": { fr: "Type", en: "Type" },
  "common.link": { fr: "Lien", en: "Link" },
  "common.reliability": { fr: "Fiabilité", en: "Reliability" },
  "common.verified": { fr: "Vérifié le", en: "Verified on" },
  "common.premium": { fr: "Premium", en: "Premium" },
  "common.free": { fr: "Gratuit", en: "Free" },
  "common.locked": { fr: "Verrouillé", en: "Locked" },
  "common.unlock": { fr: "Débloquer", en: "Unlock" },
  "common.empty": { fr: "Rien à afficher pour l'instant.", en: "Nothing to display yet." },
  "common.network": {
    fr: "Serveur injoignable. Vérifie la connexion puis réessaie.",
    en: "Server unreachable. Check the connection and retry.",
  },
  "common.missing": {
    fr: "Donnée manquante : l'absence est affichée, jamais comblée.",
    en: "Missing data: the absence is displayed, never filled in.",
  },
  "common.copy": { fr: "Copier", en: "Copy" },
  "common.copied": { fr: "Copié", en: "Copied" },

  "case.listen": { fr: "Écouter", en: "Listen" },
  "case.dossier": { fr: "Dossier", en: "Dossier" },
  "case.victims": { fr: "Victimes", en: "Victims" },
  "case.psychology": { fr: "Psychologie", en: "Psychology" },
  "case.investigation": { fr: "Enquête", en: "Investigation" },
  "case.timeline": { fr: "Chronologie", en: "Chronology" },
  "case.map": { fr: "Carte", en: "Map" },
  "case.justice": { fr: "Justice", en: "Justice" },
  "case.sources": { fr: "Sources", en: "Sources" },
  "case.memory": { fr: "Mémoire", en: "Memory" },
  "case.clues": { fr: "Indices", en: "Clues" },
  "case.experts": { fr: "Experts", en: "Experts" },
  "case.lessons": { fr: "Leçons", en: "Lessons" },
  "case.whatif": { fr: "Et si ?", en: "What if?" },
  "case.status": { fr: "Statut", en: "Status" },
  "victim.count": { fr: "Victimes documentées", en: "Documented victims" },
  "victim.named": { fr: "Victimes nommées", en: "Named victims" },
  "cold.unknowns": { fr: "Zones d'ombre", en: "Unknown zones" },
  "podcasts": { fr: "Épisodes", en: "Episodes" },
  "case.period": { fr: "Période", en: "Period" },
  "case.country": { fr: "Pays", en: "Country" },
  "case.region": { fr: "Région", en: "Region" },
  "case.similar": { fr: "Dossiers rapprochés", en: "Related dossiers" },
  "case.sensitive.title": { fr: "Contenu sensible", en: "Sensitive content" },
  "case.sensitive.body": {
    fr: "Ce dossier documente des violences réelles. Il est traité sans complaisance et sans détail gratuit, mais il peut heurter.",
    en: "This dossier documents real violence. It is handled without indulgence and without gratuitous detail, but it may be distressing.",
  },
  "case.sensitive.go": { fr: "J'ai compris, continuer", en: "I understand, continue" },
  "case.sensitive.stay": { fr: "Revenir en arrière", en: "Go back" },
  "case.sensitive.remember": { fr: "Ne plus demander pour ce dossier", en: "Don't ask again for this dossier" },

  "victim.question": {
    fr: "QUI ÉTAIT CETTE PERSONNE AVANT DE DEVENIR UNE VICTIME ?",
    en: "WHO WAS THIS PERSON BEFORE BECOMING A VICTIM?",
  },
  "victim.age": { fr: "Âge", en: "Age" },
  "victim.anonymised": {
    fr: "Identité non publiée : l'absence est affichée plutôt qu'inventée.",
    en: "Identity not published: the absence is displayed rather than invented.",
  },

  "player.play": { fr: "Lecture", en: "Play" },
  "player.pause": { fr: "Pause", en: "Pause" },
  "player.mode": { fr: "Mode", en: "Mode" },
  "player.speed": { fr: "Vitesse", en: "Speed" },
  "player.transcript": { fr: "Transcription", en: "Transcript" },
  "player.script": {
    fr: "Lecture synchronisée de la transcription — la voix enregistrée n'est pas encore produite pour cet épisode.",
    en: "Synchronised transcript reading — the recorded voice is not produced yet for this episode.",
  },
  "player.audio": { fr: "Audio produit", en: "Produced audio" },
  "player.pausepoint": { fr: "Pause pédagogique", en: "Pedagogical pause" },
  "player.resume": { fr: "Reprendre la lecture", en: "Resume playback" },
  "player.saved": { fr: "Progression enregistrée", en: "Progress saved" },

  "question.title": { fr: "Une question", en: "A question" },
  "question.answer": { fr: "Valider", en: "Submit" },
  "question.skip": { fr: "Passer, reprendre la lecture", en: "Skip, resume playback" },
  "question.explanation": { fr: "Ce que l'on sait", en: "What we know" },
  "question.investigators": { fr: "Ce que les enquêteurs savaient", en: "What investigators knew" },
  "question.experts": { fr: "Ce que les experts ont proposé", en: "What experts proposed" },
  "question.documented": { fr: "Ce qui est documenté", en: "What is documented" },
  "question.hypothetical": { fr: "Ce qui reste hypothétique", en: "What remains hypothetical" },
  "question.couldnotknow": { fr: "Ce que vous ne pouviez pas savoir", en: "What you could not know" },
  "question.reward": {
    fr: "Ce qui est valorisé ici : la compréhension et l'analyse. Jamais la violence.",
    en: "What is valued here: understanding and analysis. Never violence.",
  },

  "whatif.disclaimer": { fr: "Ceci est une reconstruction hypothétique", en: "This is a hypothetical reconstruction" },
  "whatif.reflect": { fr: "À vous de réfléchir", en: "Your turn to reflect" },
  "whatif.save": { fr: "Enregistrer ma réflexion", en: "Save my reflection" },
  "whatif.computing": { fr: "Calcul à partir de dates documentées", en: "Computed from documented dates" },
  "whatif.impossible": {
    fr: "Calcul impossible avec suffisamment de fiabilité.",
    en: "Calculation impossible with sufficient reliability.",
  },

  "explore.drill": { fr: "Monde → Continent → Pays → Région → Ville → Affaire", en: "World → Continent → Country → Region → City → Case" },
  "explore.compare": { fr: "Comparateur", en: "Comparator" },
  "explore.map": { fr: "Carte", en: "Map" },

  "account.login": { fr: "Connexion", en: "Sign in" },
  "account.register": { fr: "Créer un compte", en: "Create an account" },
  "account.logout": { fr: "Se déconnecter", en: "Sign out" },
  "account.email": { fr: "Adresse e-mail", en: "Email address" },
  "account.password": { fr: "Mot de passe", en: "Password" },
  "account.badges": { fr: "Badges", en: "Badges" },
  "account.a11y": { fr: "Accessibilité", en: "Accessibility" },
  "account.voice": { fr: "Ma voix", en: "My voice" },
  "account.demo": { fr: "Comptes de démonstration", en: "Demo accounts" },
};

export function tr(lang: Lang, key: string): string {
  const row = UI[key];
  if (!row) return key;
  return row[lang] ?? row.fr;
}

/** Choisit la bonne langue dans une valeur bilingue, sans jamais inventer. */
export function pick(value: Bi, lang: Lang): string {
  if (value === null || value === undefined) return "";
  if (typeof value === "string") return value;
  const v = value[lang] ?? value.fr ?? value.en ?? "";
  return typeof v === "string" ? v : JSON.stringify(v);
}

export const LANGS: { code: Lang; label: string }[] = [
  { code: "fr", label: "FR" },
  { code: "en", label: "EN" },
];
