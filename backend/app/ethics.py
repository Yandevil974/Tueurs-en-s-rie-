"""
Editorial constants and ethics (§44, §45, §51-§57).

Everything the application must NEVER do is encoded here as a rule the UI can
display, not just as a developer comment.
"""
from __future__ import annotations

APP_NAME = "YANIS//X"
APP_TAGLINE = {"fr": "À travers mon regard", "en": "Through my eyes"}

# The recurring signature of the "ET SI ?" segment (§53).
SIGNATURE_LINE = {
    "fr": "Et maintenant, une question. Pas un jugement. Une réflexion.",
    "en": "And now, a question. Not a judgement. A reflection.",
}

DISCLAIMER_COUNTERFACTUAL = {
    "fr": "CECI EST UNE RECONSTRUCTION HYPOTHÉTIQUE. Elle ne juge ni la justice, ni les magistrats, ni les "
          "personnes concernées. Elle s'appuie uniquement sur des faits documentés et datés, et sur la législation "
          "applicable à l'époque et au lieu.",
    "en": "THIS IS A HYPOTHETICAL RECONSTRUCTION. It judges neither the justice system, nor the magistrates, nor the "
          "persons concerned. It rests only on documented, dated facts and on the law applicable at the time and "
          "place.",
}

DISCLAIMER_PSYCHOLOGY = {
    "fr": "Aucun diagnostic psychiatrique n'est posé par cette application. Les éléments sont classés en FAIT, "
          "HYPOTHÈSE, ANALYSE D'EXPERT ou INCONNU.",
    "en": "No psychiatric diagnosis is made by this application. Elements are classified as FACT, HYPOTHESIS, EXPERT "
          "ANALYSIS or UNKNOWN.",
}

DISCLAIMER_VICTIMOLOGY = {
    "fr": "Aucune caractéristique d'une victime ne justifie ni n'explique moralement un crime. La responsabilité "
          "appartient à l'auteur.",
    "en": "No characteristic of a victim justifies or morally explains a crime. Responsibility lies with the author.",
}

INSUFFICIENT_DATA = {
    "fr": "Cette information n'est pas suffisamment documentée.",
    "en": "This information is not sufficiently documented.",
}

CALCULATION_IMPOSSIBLE = {
    "fr": "Calcul impossible avec suffisamment de fiabilité.",
    "en": "Calculation impossible with sufficient reliability.",
}

RELIABILITY = {
    "CONFIRMED": {
        "fr": "Confirmé", "en": "Confirmed", "color": "#3f9e63", "dot": "🟢",
        "definition": {"fr": "Établi par au moins une source vérifiée et datée.",
                       "en": "Established by at least one verified, dated source."},
    },
    "PROBABLE": {
        "fr": "Probable", "en": "Probable", "color": "#c9a227", "dot": "🟡",
        "definition": {"fr": "Convergent mais non confirmé par une source décisive.",
                       "en": "Convergent but not confirmed by a decisive source."},
    },
    "DISPUTED": {
        "fr": "Contesté", "en": "Disputed", "color": "#c2603a", "dot": "🟠",
        "definition": {"fr": "Deux sources ou deux lectures s'opposent ; l'écart est affiché.",
                       "en": "Two sources or two readings conflict; the gap is displayed."},
    },
    "UNKNOWN": {
        "fr": "Inconnu", "en": "Unknown", "color": "#8b8f96", "dot": "⚪",
        "definition": {"fr": "Non documenté. L'absence est affichée, jamais comblée.",
                       "en": "Not documented. The absence is displayed, never filled in."},
    },
}

STATUS = {
    "RESOLVED": {"fr": "Résolue", "en": "Resolved"},
    "UNSOLVED": {"fr": "Non résolue", "en": "Unsolved"},
    "HISTORICAL": {"fr": "Historique", "en": "Historical"},
    "ONGOING": {"fr": "En cours", "en": "Ongoing"},
    "PARTIALLY_RESOLVED": {"fr": "Partiellement résolue", "en": "Partially resolved"},
}

CASE_TYPE = {
    "serial": {"fr": "Tueur en série", "en": "Serial killer"},
    "cold_case": {"fr": "Cold case", "en": "Cold case"},
    "disappearance": {"fr": "Disparition", "en": "Disappearance"},
    "historical": {"fr": "Affaire historique", "en": "Historical case"},
    "single_homicide": {"fr": "Homicide", "en": "Homicide"},
    "miscarriage": {"fr": "Erreur judiciaire", "en": "Miscarriage of justice"},
}

# §26: podcast modes. Each one is a different way of reading the SAME dossier.
EPISODE_MODES = {
    "documentary": {"fr": "Documentaire", "en": "Documentary",
                    "desc": {"fr": "Le récit complet, de la première heure au verdict ou à l'impasse.",
                             "en": "The full narrative, from the first hour to the verdict or the dead end."}},
    "investigation": {"fr": "Enquête", "en": "Investigation",
                      "desc": {"fr": "Les informations dans l'ordre où les enquêteurs les ont obtenues.",
                               "en": "The information in the order investigators obtained it."}},
    "chronology": {"fr": "Chronologie", "en": "Chronology",
                   "desc": {"fr": "Les dates seules, sans interprétation.", "en": "Dates alone, without interpretation."}},
    "victims": {"fr": "Victimes", "en": "Victims",
                "desc": {"fr": "Qui étaient ces personnes avant de devenir des victimes.",
                         "en": "Who these people were before becoming victims."}},
    "express": {"fr": "Express", "en": "Express",
                "desc": {"fr": "L'essentiel en quelques minutes.", "en": "The essentials in a few minutes."}},
    "psychology": {"fr": "Psychologie", "en": "Psychology",
                   "desc": {"fr": "Comportements documentés, sans diagnostic.", "en": "Documented behaviour, no diagnosis."}},
    "expert": {"fr": "Expert", "en": "Expert",
               "desc": {"fr": "Ce que les experts ont dit, y compris leurs désaccords.",
                        "en": "What experts said, including their disagreements."}},
}

QUESTION_KINDS = {
    "behaviour": {"fr": "Comportement", "en": "Behaviour"},
    "investigation": {"fr": "Enquête", "en": "Investigation"},
    "psychology": {"fr": "Psychologie", "en": "Psychology"},
    "chronology": {"fr": "Chronologie", "en": "Chronology"},
    "victimology": {"fr": "Victimologie", "en": "Victimology"},
    "evidence": {"fr": "Indices", "en": "Evidence"},
    "bias": {"fr": "Biais", "en": "Bias"},
}

COUNTERFACTUAL_KINDS = {
    "lead_not_pursued": {"fr": "Piste non exploitée", "en": "Lead not pursued"},
    "technology": {"fr": "Technologie", "en": "Technology"},
    "release": {"fr": "Libération", "en": "Release"},
    "evidence_linkage": {"fr": "Rapprochement de preuves", "en": "Evidence linkage"},
    "sentence_enforcement": {"fr": "Exécution de la peine", "en": "Sentence enforcement"},
    "report_not_followed": {"fr": "Signalement non suivi", "en": "Report not followed up"},
    "forensic_delay": {"fr": "Retard d'expertise", "en": "Forensic delay"},
    "communication": {"fr": "Communication", "en": "Communication"},
    "professional_position": {"fr": "Position professionnelle", "en": "Professional position"},
    "sentence": {"fr": "Peine prononcée", "en": "Sentence pronounced"},
    "denunciation": {"fr": "Dénonciation", "en": "Denunciation"},
    "hoax_believed": {"fr": "Canular pris au sérieux", "en": "Hoax taken seriously"},
    "investigation_orientation": {"fr": "Orientation de l'enquête", "en": "Investigation orientation"},
    "dna_available": {"fr": "ADN disponible", "en": "DNA available"},
    "arrest_timing": {"fr": "Moment de l'arrestation", "en": "Arrest timing"},
}

# §36: sober gamification. Never rewards violence.
BADGES = [
    {"key": "dossier_discovered", "fr": "Dossier découvert", "en": "Dossier discovered",
     "rule_fr": "Ouvrir un dossier complet.", "rule_en": "Open a complete dossier."},
    {"key": "chronology_completed", "fr": "Chronologie terminée", "en": "Chronology completed",
     "rule_fr": "Parcourir une chronologie jusqu'au bout.", "rule_en": "Go through a chronology to the end."},
    {"key": "investigation_completed", "fr": "Enquête terminée", "en": "Investigation completed",
     "rule_fr": "Suivre toutes les étapes d'une enquête.", "rule_en": "Follow every step of an investigation."},
    {"key": "victim_remembered", "fr": "Victime honorée", "en": "Victim honoured",
     "rule_fr": "Consulter une fiche victime et sa page mémoire.", "rule_en": "Consult a victim file and their memory page."},
    {"key": "source_read", "fr": "Source consultée", "en": "Source consulted",
     "rule_fr": "Ouvrir une source et son niveau de fiabilité.", "rule_en": "Open a source and its reliability level."},
    {"key": "reflection_written", "fr": "Réflexion écrite", "en": "Reflection written",
     "rule_fr": "Enregistrer une réflexion personnelle dans « Et si ? ».", "rule_en": "Save a personal reflection in 'What if?'."},
    {"key": "analyst", "fr": "Analyste", "en": "Analyst",
     "rule_fr": "Répondre correctement à 20 questions pédagogiques.", "rule_en": "Answer 20 pedagogical questions correctly."},
    {"key": "course_completed", "fr": "Formation suivie", "en": "Course completed",
     "rule_fr": "Terminer un module de formation.", "rule_en": "Finish a training module."},
]

NEVER = {
    "fr": [
        "Ne jamais glorifier, romantiser ou idolâtrer un auteur de crime.",
        "Ne jamais classer les auteurs par dangerosité, intelligence ou nombre de victimes.",
        "Ne jamais détailler gratuitement des violences ou des souffrances.",
        "Ne jamais publier une adresse privée exacte.",
        "Ne jamais inventer une source, une citation, une date ou une identité.",
        "Ne jamais présenter une fiction comme un fait.",
        "Ne jamais poser un diagnostic psychiatrique.",
        "Ne jamais rendre payante la mémoire essentielle des victimes.",
        "Ne jamais transformer un crime en jeu ou en compétition.",
    ],
    "en": [
        "Never glorify, romanticise or idolise the author of a crime.",
        "Never rank authors by dangerousness, intelligence or number of victims.",
        "Never give gratuitous detail of violence or suffering.",
        "Never publish an exact private address.",
        "Never invent a source, a quote, a date or an identity.",
        "Never present fiction as fact.",
        "Never make a psychiatric diagnosis.",
        "Never paywall the essential memory of victims.",
        "Never turn a crime into a game or a competition.",
    ],
}
