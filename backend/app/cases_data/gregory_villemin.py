"""
DOSSIER 08 — AFFAIRE GRÉGORY VILLEMIN (France, Vosges, 1984 — non résolue)

Dossier traité avec une prudence particulière : une personne a été
publiquement accusée à tort, un suspect est mort tué, un juge s'est donné la
mort. Chaque affirmation porte son niveau de certitude et sa source.
Rien n'est tranché là où la justice ne l'a pas tranché.
Sources publiques vérifiées le 2026-09-24.
"""
from ..case_template import (block, counterfactual, default_sections, fact, item,
                             merge_sections, question, source, txt)

CASE_ID = "affaire-gregory"
V = "2026-09-24"

SOURCES = [
    source("wiki-gregory-fr", CASE_ID, "Affaire Grégory", "Grégory case",
           "Wikipédia (français)", "Contributeurs", "https://fr.wikipedia.org/wiki/Affaire_Gr%C3%A9gory",
           "2026-09-20", "public_archive", "PROBABLE", V,
           "Encyclopédie collaborative détaillée : chronologie, décisions de justice, expertises. Niveau PROBABLE par "
           "prudence ; les éléments décisifs sont recoupés avec la presse.",
           "Detailed collaborative encyclopaedia: chronology, court decisions, expert examinations. PROBABLE level as "
           "a precaution; decisive elements are cross-checked with the press."),
    source("en-wiki-gregory", CASE_ID, "Murder of Grégory Villemin", "Murder of Grégory Villemin",
           "Wikipedia (English)", "Contributors", "https://en.wikipedia.org/wiki/Murder_of_Gr%C3%A9gory_Villemin",
           "2026-08-28", "public_archive", "PROBABLE", V,
           "Synthèse en anglais : déroulé du 16 octobre 1984, suites judiciaires, décès de Jean-Michel Lambert en 2017.",
           "English synthesis: course of 16 October 1984, judicial aftermath, death of Jean-Michel Lambert in 2017."),
    source("ici-dates-cles", CASE_ID,
           "Affaire Grégory : les dates clés du plus emblématique des dossiers judiciaires français",
           "Grégory case: the key dates of the most emblematic of French judicial files",
           "ICI (Radio France)", "Redaction",
           "https://www.ici.fr/infos/faits-divers-justice/affaire-gregory-les-dates-cles-du-plus-emblematique-des-dossiers-judiciaires-francais-1608893973",
           "2025-10-24", "press", "CONFIRMED", V,
           "Chronologie officielle : assassinat, dépaysement à Dijon, analyses ADN, annulations.",
           "Official chronology: murder, transfer to Dijon, DNA analyses, annulments."),
    source("obs-chronologie", CASE_ID, "[CHRONOLOGIE] L'affaire Villemin", "[CHRONOLOGY] The Villemin case",
           "L'Obs", "Redaction", "https://www.nouvelobs.com/societe/20080709.OBS2203/chronologie-l-affaire-villemin.html",
           "2010-05-05", "press", "CONFIRMED", V,
           "Chronologie de presse : découverte du corps, réouvertures d'instruction, demande de réhabilitation.",
           "Press chronology: discovery of the body, reopening of investigations, request for rehabilitation."),
    source("lesjours-gregory", CASE_ID, "Grégory — enquête en épisodes", "Grégory — an episodic investigation",
           "Les Jours", "Redaction", "https://lesjours.fr/obsessions/gregory/",
           "2021-11-21", "press", "CONFIRMED", V,
           "Traitement du chaos judiciaire, du traitement médiatique et du non-lieu de Christine Villemin en 1993.",
           "Coverage of the judicial chaos, the media treatment and Christine Villemin's 1993 dismissal."),
]

VICTIMS = [
    {
        "order": 0, "first_name": "Grégory", "last_name": "Villemin", "age": "4",
        "source": "ici-dates-cles", "reliability": "CONFIRMED", "anonymised": False,
        "life": {
            "fr": {"headline": "Qui était Grégory avant le 16 octobre 1984 ?", "items": [
                {"label": "Prénom", "text": "Grégory."},
                {"label": "Dates", "text": "Né le 24 août 1980, mort le 16 octobre 1984, à 4 ans."},
                {"label": "Lieu de vie", "text": "Lépanges-sur-Vologne, dans les Vosges, avec ses parents Christine et Jean-Marie Villemin."},
                {"label": "Ce jour-là", "text": "Il jouait devant le domicile familial en fin d'après-midi."}],
             "note": "Les éléments de vie personnelle (école, amis, caractère) ne figurent pas dans les sources "
                     "consultées. Cette fiche reste volontairement incomplète plutôt que reconstituée."},
            "en": {"headline": "Who was Grégory before 16 October 1984?", "items": [
                {"label": "First name", "text": "Grégory."},
                {"label": "Dates", "text": "Born 24 August 1980, died 16 October 1984, aged 4."},
                {"label": "Place of life", "text": "Lépanges-sur-Vologne, in the Vosges, with his parents Christine and Jean-Marie Villemin."},
                {"label": "That day", "text": "He was playing in front of the family home in the late afternoon."}],
             "note": "Personal details (school, friends, character) do not appear in the sources consulted. This file "
                     "remains deliberately incomplete rather than reconstructed."},
        },
        "disappearance": {
            "fr": {"items": [
                {"label": "Signalement", "text": "Peu après 17 h le 16 octobre 1984, sa mère signale qu'il ne joue plus devant la maison."},
                {"label": "Appel", "text": "À 17 h 30, son oncle Michel Villemin est informé par un appel anonyme que l'enfant a été emmené et jeté dans la Vologne."},
                {"label": "Découverte", "text": "À 21 h 15, le corps est retrouvé dans la Vologne à Docelles, à environ sept kilomètres en aval de Lépanges."},
                {"label": "Constatations", "text": "Les pieds, les mains et la tête étaient liés par des cordelettes ; le bonnet était rabattu sur le visage."}]},
            "en": {"items": [
                {"label": "Report", "text": "Shortly after 5 p.m. on 16 October 1984, his mother reports that he is no longer playing in front of the house."},
                {"label": "Call", "text": "At 5.30 p.m., his uncle Michel Villemin is told by an anonymous caller that the child has been taken and thrown into the Vologne river."},
                {"label": "Discovery", "text": "At 9.15 p.m., the body is found in the Vologne at Docelles, about seven kilometres downstream from Lépanges."},
                {"label": "Observations", "text": "The feet, hands and head were bound with cords; the cap was pulled over the face."}]},
        },
    }
]

OTHER_PROCEEDINGS = {
    "title": txt("Les autres personnes mises en cause", "The other persons indicted"),
    "body": txt(
        "Plusieurs personnes ont été mises en cause au fil de quarante ans de procédure. Bernard Laroche, inculpé puis "
        "bénéficiaire d'un non-lieu, a été tué en 1985 par Jean-Marie Villemin, le père de l'enfant, qui a été "
        "condamné pour ce meurtre et a ensuite demandé sa réhabilitation. Christine Villemin, la mère, a été "
        "inculpée puis a bénéficié d'un non-lieu en 1993. Murielle Bolle, mineure au moment des faits, a été "
        "entendue ; la solidité de son implication a été discutée par la justice elle-même. En 2017, un grand-oncle "
        "et une grand-tante ont été mis en examen ; ces mises en examen ont été annulées en 2018. Le juge "
        "d'instruction Jean-Michel Lambert s'est donné la mort en 2017. Aucune de ces personnes n'est présentée ici "
        "comme coupable : le meurtre n'est pas élucidé.",
        "Several people were indicted over forty years of proceedings. Bernard Laroche, indicted then granted a "
        "dismissal, was killed in 1985 by Jean-Marie Villemin, the child's father, who was convicted for that murder "
        "and later sought rehabilitation. Christine Villemin, the mother, was indicted then granted a dismissal in "
        "1993. Murielle Bolle, a minor at the time, was heard; the strength of her involvement was questioned by the "
        "justice system itself. In 2017, a great-uncle and a great-aunt were indicted; those indictments were annulled "
        "in 2018. Investigating judge Jean-Michel Lambert took his own life in 2017. None of these persons is "
        "presented here as guilty: the murder is not solved.",
    ),
    "reliability": "CONFIRMED", "source": "en-wiki-gregory",
}

MEMORIAL = {
    "title": txt("Grégory Villemin (1980-1984)", "Grégory Villemin (1980-1984)"),
    "biography": txt(
        "Grégory Villemin avait 4 ans. Il vivait à Lépanges-sur-Vologne, dans les Vosges. Le 16 octobre 1984, il "
        "jouait devant la maison familiale. Son corps a été retrouvé le soir même dans la Vologne, à Docelles. "
        "Quarante ans de procédure n'ont pas établi qui l'a tué.",
        "Grégory Villemin was 4 years old. He lived in Lépanges-sur-Vologne, in the Vosges. On 16 October 1984, he "
        "was playing in front of the family house. His body was found that evening in the Vologne river, at Docelles. "
        "Forty years of proceedings did not establish who killed him.",
    ),
    "testimony": txt(
        "Sa mère, Christine Villemin, a été inculpée, désignée publiquement comme l'auteure possible du meurtre de "
        "son fils, puis a obtenu un non-lieu en 1993. La presse de l'époque l'a décrite comme « la femme la plus haïe "
        "de France ». Ce traitement est documenté et constitue l'un des objets d'analyse de ce dossier.",
        "His mother, Christine Villemin, was indicted, publicly named as a possible author of her son's murder, then "
        "obtained a dismissal in 1993. The press of the time described her as 'the most hated woman in France'. That "
        "treatment is documented and constitutes one of the objects of analysis in this file.",
    ),
    "memory": txt(
        "Cette affaire est devenue en France la référence publique de ce qu'un emballement médiatique et judiciaire "
        "peut produire autour d'un enfant mort. Rendre hommage à Grégory Villemin, c'est aussi nommer ce qui a été "
        "fait à sa famille pendant ces années.",
        "This case became in France the public reference for what media and judicial frenzy can produce around a dead "
        "child. Paying homage to Grégory Villemin also means naming what was done to his family during those years.",
    ),
}

TIMELINE = [
    fact("Grégory Villemin, 4 ans, joue devant le domicile familial de Lépanges-sur-Vologne. Peu après 17 h, sa mère "
         "constate son absence. À 17 h 30, un oncle reçoit un appel anonyme annonçant que l'enfant a été jeté dans la "
         "Vologne. À 21 h 15, le corps est retrouvé à Docelles, pieds, mains et tête liés par des cordelettes.",
         "Grégory Villemin, 4, plays in front of the family home in Lépanges-sur-Vologne. Shortly after 5 p.m., his "
         "mother notices his absence. At 5.30 p.m., an uncle receives an anonymous call announcing the child has been "
         "thrown into the Vologne. At 9.15 p.m., the body is found at Docelles, feet, hands and head bound with cords.",
         "CONFIRMED", "en-wiki-gregory", "Le 16 octobre 1984", "16 October 1984", "1984-10-16"),
    fact("Un « corbeau » adresse des courriers à la famille et à la presse. Les expertises en écriture ultérieures "
         "ont mis hors de cause avec certitude Christine Villemin sur ce point ; les experts ayant étudié les "
         "cassettes s'accordent à dire qu'il ne s'agit pas de sa voix, la majorité estimant avoir affaire à une voix "
         "de femme.",
         "A 'corbeau' (anonymous letter writer) sends letters to the family and the press. Later handwriting "
         "examinations ruled out Christine Villemin with certainty on that point; the experts who studied the tapes "
         "agree it is not her voice, the majority considering it a woman's voice.",
         "CONFIRMED", "wiki-gregory-fr", "Le corbeau", "The anonymous writer", "1984-10"),
    fact("Bernard Laroche est inculpé sur la base notamment des déclarations de Murielle Bolle, alors mineure. La "
         "solidité de cette base est discutée par un magistrat lui-même, qui note l'âge et les facultés intellectuelles "
         "de la jeune fille.",
         "Bernard Laroche is indicted on the basis notably of statements by Murielle Bolle, then a minor. The strength "
         "of that basis is questioned by a magistrate himself, who notes the girl's age and intellectual faculties.",
         "PROBABLE", "wiki-gregory-fr", "Première inculpation", "First indictment", "1984-11"),
    fact("Bernard Laroche est tué par Jean-Marie Villemin, le père de l'enfant. Ce dernier sera condamné pour ce "
         "meurtre et demandera ensuite sa réhabilitation.",
         "Bernard Laroche is killed by Jean-Marie Villemin, the child's father. The latter will be convicted for that "
         "murder and later seek rehabilitation.",
         "CONFIRMED", "en-wiki-gregory", "Un meurtre dans l'affaire", "A murder within the case", "1985-03-29"),
    fact("Christine Villemin est inculpée. Elle bénéficiera d'un non-lieu en 1993.",
         "Christine Villemin is indicted. She will obtain a dismissal in 1993.",
         "CONFIRMED", "lesjours-gregory", "La mère inculpée", "The mother indicted", "1985"),
    fact("Le dossier est dépaysé à Dijon. L'instruction est confiée au juge Maurice Simon, qui décide de ne pas "
         "communiquer avec la presse. Un supplément d'information est ordonné.",
         "The file is transferred to Dijon. The investigation is entrusted to judge Maurice Simon, who decides not to "
         "communicate with the press. A supplementary investigation is ordered.",
         "CONFIRMED", "ici-dates-cles", "Dépaysement", "Transfer", "1987"),
    fact("Le juge Maurice Simon est victime d'un infarctus le 28 janvier 1990, tombe dans le coma et souffre "
         "d'amnésie à son réveil. Il doit abandonner l'affaire. Il meurt le 23 mai 1994. Ses cahiers, destinés à son "
         "fils, contiennent ses analyses.",
         "Judge Maurice Simon suffers a heart attack on 28 January 1990, falls into a coma and suffers amnesia on "
         "waking. He has to give up the case. He dies on 23 May 1994. His notebooks, intended for his son, contain "
         "his analyses.",
         "CONFIRMED", "wiki-gregory-fr", "Un juge empêché", "A judge prevented", "1990-01-28"),
    fact("Non-lieu au bénéfice de Christine Villemin.",
         "Dismissal in favour of Christine Villemin.",
         "CONFIRMED", "lesjours-gregory", "Non-lieu", "Dismissal", "1993"),
    fact("Des analyses ADN sont réalisées : comparaisons entre les ADN de plusieurs membres de la famille et ceux "
         "retrouvés sur les cordelettes, sur l'anorak de l'enfant, sur son menton, et sur certains courriers du "
         "corbeau dont celui du 16 octobre 1984. Une ordonnance de non-lieu est rendue en 2001.",
         "DNA analyses are carried out: comparisons between the DNA of several family members and that found on the "
         "cords, on the child's anorak, on his chin, and on certain letters from the anonymous writer including that "
         "of 16 October 1984. A dismissal order is issued in 2001.",
         "CONFIRMED", "ici-dates-cles", "L'ADN", "DNA", "2000-2001"),
    fact("Le procureur général de la cour d'appel de Dijon requiert la réouverture de l'instruction.",
         "The Prosecutor General of the Dijon court of appeal requests the reopening of the investigation.",
         "CONFIRMED", "obs-chronologie", "Réouverture", "Reopening", "2008-07-09"),
    fact("Un arrêt de la chambre de l'instruction retient qu'il subsiste dans le dossier des « charges très sérieuses "
         "» que Bernard Laroche ait enlevé Grégory Villemin le 16 octobre 1984, tout en précisant qu'il est "
         "impossible d'affirmer qu'il l'a assassiné.",
         "A ruling of the investigation chamber holds that 'very serious indications' remain in the file that Bernard "
         "Laroche abducted Grégory Villemin on 16 October 1984, while specifying that it is impossible to assert that "
         "he murdered him.",
         "CONFIRMED", "wiki-gregory-fr", "Charges sérieuses, sans certitude", "Serious indications, without certainty", "2018"),
    fact("En 2017, un grand-oncle et une grand-tante sont mis en examen. Le juge d'instruction Jean-Michel Lambert, "
         "premier magistrat instructeur du dossier et très critiqué pour sa conduite, se donne la mort.",
         "In 2017, a great-uncle and a great-aunt are indicted. Investigating judge Jean-Michel Lambert, the first "
         "investigating magistrate of the file and heavily criticised for his conduct, takes his own life.",
         "CONFIRMED", "en-wiki-gregory", "2017", "2017", "2017"),
    fact("Les mises en examen de 2017 sont annulées en 2018. L'arrêt n'annule pas le non-lieu de Christine Villemin.",
         "The 2017 indictments are annulled in 2018. The ruling does not annul Christine Villemin's dismissal.",
         "CONFIRMED", "wiki-gregory-fr", "Annulation", "Annulment", "2018"),
    fact("Monique Villemin, grand-mère paternelle, désignée par les enquêteurs comme l'auteure d'une lettre de "
         "menaces adressée en 1990 au juge Simon, meurt le 19 avril 2020.",
         "Monique Villemin, paternal grandmother, named by investigators as the author of a threatening letter sent "
         "in 1990 to judge Simon, dies on 19 April 2020.",
         "PROBABLE", "en-wiki-gregory", "Une désignation non jugée", "A designation never tried", "2020-04-19"),
]

LOCATIONS = [
    {"kind": "city", "names": txt("Lépanges-sur-Vologne (Vosges)", "Lépanges-sur-Vologne (Vosges)"),
     "city": "Lépanges-sur-Vologne", "region": "Grand Est / Vosges", "country": "FR",
     "lat": 48.19, "lon": 6.43, "precision": "city", "date": "1984-10-16",
     "note": txt("Domicile familial. Aucune adresse n'est publiée.", "Family home. No address is published."),
     "reliability": "CONFIRMED", "source": "ici-dates-cles"},
    {"kind": "city", "names": txt("Docelles — la Vologne", "Docelles — the Vologne river"),
     "city": "Docelles", "region": "Grand Est / Vosges", "country": "FR", "lat": 48.13, "lon": 6.55,
     "precision": "city", "date": "1984-10-16",
     "note": txt("Lieu de découverte du corps, à environ sept kilomètres en aval de Lépanges.",
                 "Place where the body was found, about seven kilometres downstream from Lépanges."),
     "reliability": "CONFIRMED", "source": "ici-dates-cles"},
    {"kind": "court", "names": txt("Dijon — instruction dépaycée", "Dijon — transferred investigation"),
     "city": "Dijon", "region": "Bourgogne", "country": "FR", "lat": 47.32, "lon": 5.04, "precision": "city",
     "date": "1987", "note": txt("Dépaysement du dossier et instruction du juge Maurice Simon.",
                                 "Transfer of the file and investigation by judge Maurice Simon."),
     "reliability": "CONFIRMED", "source": "ici-dates-cles"},
]

EVIDENCE = [
    {"kind": "physical", "weight": "documented", "reliability": "CONFIRMED", "source": "en-wiki-gregory",
     "title": txt("Les cordelettes", "The cords"),
     "description": txt(
         "Le corps a été retrouvé les pieds, les mains et la tête liés par des cordelettes, le bonnet rabattu sur le "
         "visage. Ces cordelettes ont ensuite supporté des analyses ADN.",
         "The body was found with feet, hands and head bound with cords, the cap pulled over the face. Those cords "
         "later supported DNA analyses.")},
    {"kind": "dna", "weight": "disputed", "reliability": "CONFIRMED", "source": "ici-dates-cles",
     "title": txt("Analyses ADN des années 2000", "DNA analyses of the 2000s"),
     "description": txt(
         "Des comparaisons ont été effectuées entre les ADN de plusieurs membres de la famille et les profils "
         "retrouvés sur les cordelettes, l'anorak, le menton de l'enfant et certains courriers. Une ordonnance de "
         "non-lieu a été rendue en 2001 : ces analyses n'ont pas abouti à une identification.",
         "Comparisons were made between the DNA of several family members and the profiles found on the cords, the "
         "anorak, the child's chin and certain letters. A dismissal order was issued in 2001: these analyses did not "
         "lead to an identification.")},
    {"kind": "documentary", "weight": "disputed", "reliability": "CONFIRMED", "source": "wiki-gregory-fr",
     "title": txt("Les courriers et cassettes du « corbeau »", "The anonymous writer's letters and tapes"),
     "description": txt(
         "Sept experts en écriture auprès de la Cour de cassation ont mis Christine Villemin hors de cause avec "
         "certitude concernant les courriers. Les experts ayant étudié les cassettes s'accordent sur le fait qu'il ne "
         "s'agit pas de sa voix ; la majorité estime avoir affaire à une voix de femme.",
         "Seven handwriting experts at the Court of Cassation ruled out Christine Villemin with certainty concerning "
         "the letters. The experts who studied the tapes agree it is not her voice; the majority consider it a "
         "woman's voice.")},
    {"kind": "testimony", "weight": "disputed", "reliability": "DISPUTED", "source": "wiki-gregory-fr",
     "title": txt("Les déclarations de Murielle Bolle", "Murielle Bolle's statements"),
     "description": txt(
         "Ces déclarations, recueillies alors que l'intéressée était mineure, ont fondé l'inculpation de Bernard "
         "Laroche. Un magistrat a écrit que cette base d'inculpation n'était « pas d'une solidité à toute épreuve, "
         "compte tenu de l'âge de Murielle Bolle et de ses facultés intellectuelles à mon avis relativement "
         "limitées ». La valeur de ce témoignage a donc été contestée au sein même de l'institution.",
         "These statements, collected while the person was a minor, founded Bernard Laroche's indictment. A magistrate "
         "wrote that this basis for indictment was 'not of unshakeable solidity, given Murielle Bolle's age and her "
         "intellectual faculties in my view relatively limited'. The value of that testimony was therefore contested "
         "within the institution itself.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "wiki-gregory-fr",
     "title": txt("Les cahiers du juge Simon", "Judge Simon's notebooks"),
     "description": txt(
         "Le juge Maurice Simon, qui avait choisi de ne pas communiquer avec la presse, a tenu des cahiers destinés à "
         "son fils. Ses investigations ont contribué à innocenter Christine Villemin. Il a dû abandonner l'affaire en "
         "1990 après un infarctus ayant entraîné une amnésie.",
         "Judge Maurice Simon, who had chosen not to communicate with the press, kept notebooks intended for his son. "
         "His investigations helped clear Christine Villemin. He had to give up the case in 1990 after a heart attack "
         "causing amnesia.")},
]

INVESTIGATION = {
    "steps": [
        {"n": 1, "date": "1984-10-16", "title": txt("Quatre heures", "Four hours"),
         "body": txt("Entre 17 h et 21 h 15, le 16 octobre 1984 : une absence constatée, un appel anonyme, un corps "
                     "retrouvé dans la rivière. C'est l'intégralité du temps dont dispose l'enquête pour ce qui "
                     "deviendra l'un des dossiers les plus longs de l'histoire judiciaire française.",
                     "Between 5 p.m. and 9.15 p.m. on 16 October 1984: a noticed absence, an anonymous call, a body "
                     "found in the river. That is all the time the investigation has for what would become one of the "
                     "longest files in French judicial history."),
         "reliability": "CONFIRMED", "source": "en-wiki-gregory", "premium": False},
        {"n": 2, "date": "1984-10", "title": txt("Un corbeau", "An anonymous writer"),
         "body": txt("Des courriers et des cassettes parviennent à la famille et à la presse. Leur auteur n'a jamais "
                     "été identifié avec certitude. Les expertises ultérieures ont écarté Christine Villemin.",
                     "Letters and tapes reach the family and the press. Their author has never been identified with "
                     "certainty. Later examinations ruled out Christine Villemin.",),
         "reliability": "CONFIRMED", "source": "wiki-gregory-fr", "premium": False},
        {"n": 3, "date": "1984-11", "title": txt("Une première inculpation", "A first indictment"),
         "body": txt("Bernard Laroche est inculpé, sur la base notamment des déclarations d'une mineure. Cette base "
                     "sera discutée par un magistrat.",
                     "Bernard Laroche is indicted, on the basis notably of a minor's statements. That basis would be "
                     "questioned by a magistrate."),
         "reliability": "PROBABLE", "source": "wiki-gregory-fr", "premium": True},
        {"n": 4, "date": "1985", "title": txt("Deux événements qui déforment le dossier", "Two events that distort the file"),
         "body": txt("Bernard Laroche est tué par le père de l'enfant, qui sera condamné pour ce meurtre. Christine "
                     "Villemin est inculpée. À partir de là, le dossier cesse d'être seulement une enquête : il "
                     "devient une affaire publique.",
                     "Bernard Laroche is killed by the child's father, who will be convicted for that murder. "
                     "Christine Villemin is indicted. From then on, the file ceases to be only an investigation: it "
                     "becomes a public case."),
         "reliability": "CONFIRMED", "source": "en-wiki-gregory", "premium": False},
        {"n": 5, "date": "1987", "title": txt("Le dépaysement et le silence d'un juge", "The transfer and a judge's silence"),
         "body": txt("Le dossier est dépaysé à Dijon. Le juge Maurice Simon choisit de ne pas communiquer avec la "
                     "presse. Ses travaux contribueront à innocenter la mère de l'enfant.",
                     "The file is transferred to Dijon. Judge Maurice Simon chooses not to communicate with the press. "
                     "His work would help clear the child's mother."),
         "reliability": "CONFIRMED", "source": "ici-dates-cles", "premium": True},
        {"n": 6, "date": "1990", "title": txt("Un juge remplacé par un accident", "A judge replaced by an accident"),
         "body": txt("Le 28 janvier 1990, le juge Simon est victime d'un infarctus, tombe dans le coma et souffre "
                     "d'amnésie au réveil. Il abandonne l'affaire. La continuité de l'instruction est rompue.",
                     "On 28 January 1990, judge Simon suffers a heart attack, falls into a coma and suffers amnesia on "
                     "waking. He gives up the case. The continuity of the investigation is broken."),
         "reliability": "CONFIRMED", "source": "wiki-gregory-fr", "premium": False},
        {"n": 7, "date": "1993", "title": txt("Un non-lieu", "A dismissal"),
         "body": txt("Christine Villemin bénéficie d'un non-lieu, huit ans après son inculpation.",
                     "Christine Villemin obtains a dismissal, eight years after her indictment."),
         "reliability": "CONFIRMED", "source": "lesjours-gregory", "premium": False},
        {"n": 8, "date": "2000-2001", "title": txt("L'ADN arrive, et ne tranche pas", "DNA arrives, and does not settle it"),
         "body": txt("Des comparaisons ADN sont effectuées sur les cordelettes, l'anorak, le menton de l'enfant et "
                     "certains courriers. Une ordonnance de non-lieu est rendue en 2001. La technique nouvelle ne "
                     "produit pas d'identification.",
                     "DNA comparisons are made on the cords, the anorak, the child's chin and certain letters. A "
                     "dismissal order is issued in 2001. The new technique produces no identification."),
         "reliability": "CONFIRMED", "source": "ici-dates-cles", "premium": True},
        {"n": 9, "date": "2008", "title": txt("Une réouverture", "A reopening"),
         "body": txt("Le procureur général de la cour d'appel de Dijon requiert la réouverture de l'instruction.",
                     "The Prosecutor General of the Dijon court of appeal requests the reopening of the investigation."),
         "reliability": "CONFIRMED", "source": "obs-chronologie", "premium": False},
        {"n": 10, "date": "2017-2018", "title": txt("Des mises en examen, puis leur annulation", "Indictments, then their annulment"),
         "body": txt("En 2017, un grand-oncle et une grand-tante sont mis en examen ; le premier juge d'instruction "
                     "du dossier se donne la mort. En 2018, un arrêt annule ces mises en examen, sans annuler le "
                     "non-lieu de Christine Villemin. Le même arrêt retient des « charges très sérieuses » d'enlèvement "
                     "contre Bernard Laroche, tout en disant impossible d'affirmer qu'il a assassiné l'enfant.",
                     "In 2017, a great-uncle and a great-aunt are indicted; the first investigating judge of the file "
                     "takes his own life. In 2018, a ruling annuls those indictments, without annulling Christine "
                     "Villemin's dismissal. The same ruling retains 'very serious indications' of abduction against "
                     "Bernard Laroche, while stating it is impossible to assert that he murdered the child."),
         "reliability": "CONFIRMED", "source": "wiki-gregory-fr", "premium": True},
    ],
    "reality": txt(
        "Voici comment l'enquête s'est réellement déroulée : quarante ans de procédure, plusieurs réouvertures, des "
        "techniques nouvelles appliquées à des scellés anciens sans aboutir, des mises en examen annulées, un non-lieu "
        "au bénéfice de la mère, et aucune identification de l'auteur. Le meurtre de Grégory Villemin n'est pas "
        "élucidé.",
        "This is how the investigation actually unfolded: forty years of proceedings, several reopenings, new "
        "techniques applied to old exhibits without success, annulled indictments, a dismissal in favour of the "
        "mother, and no identification of the author. The murder of Grégory Villemin is not solved."),
    "errors": [
        item("Une inculpation fondée sur les déclarations d'une mineure, dont la solidité a été contestée par un "
             "magistrat lui-même.",
             "An indictment founded on a minor's statements, whose solidity was contested by a magistrate himself.",
             "PROBABLE", "wiki-gregory-fr", "Témoignage fragile", "Fragile testimony"),
        item("Une mise en cause publique de la mère de l'enfant, close par un non-lieu en 1993 après huit ans.",
             "A public accusation against the child's mother, closed by a dismissal in 1993 after eight years.",
             "CONFIRMED", "lesjours-gregory", "Emballement", "Frenzy"),
        item("Une communication avec la presse qui a pesé sur la procédure : le juge Simon avait choisi la voie "
             "inverse.",
             "Communication with the press that weighed on the proceedings: judge Simon had chosen the opposite path.",
             "CONFIRMED", "ici-dates-cles", "Médias et justice", "Media and justice"),
        item("Des actes annulés pour irrégularité, privant le dossier d'éléments recueillis — y compris des actes du "
             "juge Simon selon les contestations de 2018.",
             "Acts annulled for irregularity, depriving the file of collected elements — including acts of judge "
             "Simon according to the 2018 challenges.",
             "PROBABLE", "wiki-gregory-fr", "Nullités", "Annulments"),
        item("La rupture de continuité de 1990 : un juge empêché par un accident, des cahiers personnels comme seule "
             "trace de son raisonnement.",
             "The break in continuity in 1990: a judge prevented by an accident, personal notebooks as the only trace "
             "of his reasoning.",
             "CONFIRMED", "wiki-gregory-fr", "Continuité", "Continuity"),
    ],
    "cold_case": {
        "what_we_know": [
            item("Grégory Villemin, 4 ans, est mort le 16 octobre 1984 ; son corps a été retrouvé dans la Vologne à "
                 "Docelles, ligoté.",
                 "Grégory Villemin, 4, died on 16 October 1984; his body was found in the Vologne at Docelles, bound.",
                 "CONFIRMED", "en-wiki-gregory"),
            item("Un appel anonyme a précédé la découverte du corps.",
                 "An anonymous call preceded the discovery of the body.", "CONFIRMED", "en-wiki-gregory"),
            item("Christine Villemin a bénéficié d'un non-lieu en 1993, non annulé par l'arrêt de 2018.",
                 "Christine Villemin obtained a dismissal in 1993, not annulled by the 2018 ruling.",
                 "CONFIRMED", "wiki-gregory-fr"),
            item("Les expertises en écriture ont mis Christine Villemin hors de cause avec certitude pour les "
                 "courriers du corbeau.",
                 "Handwriting examinations ruled out Christine Villemin with certainty for the anonymous letters.",
                 "CONFIRMED", "wiki-gregory-fr"),
        ],
        "what_is_probable": [
            item("La chambre de l'instruction a retenu en 2018 l'existence de « charges très sérieuses » que Bernard "
                 "Laroche ait enlevé l'enfant — sans qu'il soit possible d'affirmer qu'il l'a assassiné.",
                 "The investigation chamber held in 2018 that 'very serious indications' exist that Bernard Laroche "
                 "abducted the child — without it being possible to assert that he murdered him.",
                 "PROBABLE", "wiki-gregory-fr"),
        ],
        "what_is_disputed": [
            item("La valeur des déclarations de Murielle Bolle, recueillies lorsqu'elle était mineure.",
                 "The value of Murielle Bolle's statements, collected when she was a minor.",
                 "DISPUTED", "wiki-gregory-fr"),
            item("L'auteur des courriers et cassettes : les experts s'accordent pour exclure Christine Villemin, la "
                 "majorité estimant qu'il s'agit d'une voix de femme, sans identification.",
                 "The author of the letters and tapes: experts agree on excluding Christine Villemin, the majority "
                 "considering it a woman's voice, without identification.", "DISPUTED", "wiki-gregory-fr"),
            item("La désignation par les enquêteurs de Monique Villemin comme auteure d'une lettre de menaces de "
                 "1990 : elle est morte en 2020 sans avoir été jugée sur ce point.",
                 "Investigators' designation of Monique Villemin as author of a 1990 threatening letter: she died in "
                 "2020 without being tried on that point.", "DISPUTED", "en-wiki-gregory"),
        ],
        "what_is_unknown": [
            item("Qui a tué Grégory Villemin.", "Who killed Grégory Villemin.", "UNKNOWN", "en-wiki-gregory"),
            item("Le mobile : une revanche contre le père est évoquée dans les synthèses, sans motif établi.",
                 "The motive: revenge against the father is mentioned in syntheses, without an established motive.",
                 "UNKNOWN", "en-wiki-gregory"),
            item("L'auteur de l'appel anonyme du 16 octobre 1984 à 17 h 30.",
                 "The author of the anonymous call of 16 October 1984 at 5.30 p.m.", "UNKNOWN", "en-wiki-gregory"),
        ],
        "latest_progress": [
            item("2018 : annulation des mises en examen de 2017 ; le non-lieu de Christine Villemin n'est pas annulé.",
                 "2018: annulment of the 2017 indictments; Christine Villemin's dismissal is not annulled.",
                 "CONFIRMED", "wiki-gregory-fr"),
        ],
        "leads": [
            item("Les scellés conservés, dont les cordelettes et l'anorak, ont déjà supporté plusieurs campagnes "
                 "d'analyses.",
                 "The preserved exhibits, including the cords and the anorak, have already supported several analysis "
                 "campaigns.", "CONFIRMED", "ici-dates-cles"),
        ],
        "limits": [
            item("Plusieurs personnes susceptibles d'apporter des éléments sont décédées : Bernard Laroche (1985), le "
                 "juge Maurice Simon (1994), le juge Jean-Michel Lambert (2017), Monique Villemin (2020).",
                 "Several people capable of providing elements have died: Bernard Laroche (1985), judge Maurice Simon "
                 "(1994), judge Jean-Michel Lambert (2017), Monique Villemin (2020).",
                 "CONFIRMED", "en-wiki-gregory"),
        ],
    },
}

PSYCHOLOGY = {
    "disclaimer": txt("Ce dossier ne comporte pas d'auteur identifié : aucun module « Dans la tête » n'est applicable. "
                      "L'analyse porte ici sur les comportements collectifs — familiaux, médiatiques, judiciaires — "
                      "qui sont, eux, documentés.",
                      "This file has no identified author: no 'In the mind' module is applicable. The analysis here "
                      "concerns collective behaviours — family, media, judicial — which are themselves documented."),
    "blocks": [
        block("behaviour", "Un comportement collectif d'accusation", "A collective behaviour of accusation",
              "Une mère a été publiquement désignée, décrite par la presse comme « la femme la plus haïe de France », "
              "avant d'obtenir un non-lieu en 1993. Ce mécanisme est documenté : il combine pression médiatique, "
              "biais de confirmation et recherche d'une explication rapide.",
              "A mother was publicly named, described by the press as 'the most hated woman in France', before "
              "obtaining a dismissal in 1993. That mechanism is documented: it combines media pressure, confirmation "
              "bias and the search for a quick explanation.",
              "CONFIRMED", "lesjours-gregory"),
        block("behaviour", "Le passage à l'acte d'un père", "A father's act",
              "Jean-Marie Villemin a tué Bernard Laroche, puis a été condamné pour ce meurtre. C'est un fait jugé. "
              "L'application ne l'analyse pas psychologiquement : elle le situe dans une chronologie.",
              "Jean-Marie Villemin killed Bernard Laroche, then was convicted for that murder. This is a tried fact. "
              "The application does not analyse it psychologically: it places it in a chronology.",
              "CONFIRMED", "en-wiki-gregory"),
        block("behaviour", "Deux juges, deux rapports à la parole publique", "Two judges, two relationships to public speech",
              "Le juge Maurice Simon avait choisi de ne pas communiquer avec la presse. Le premier juge "
              "d'instruction, Jean-Michel Lambert, a été très critiqué pour sa conduite du dossier et s'est donné la "
              "mort en 2017. Ces deux trajectoires documentent le coût humain d'une exposition publique.",
              "Judge Maurice Simon had chosen not to communicate with the press. The first investigating judge, "
              "Jean-Michel Lambert, was heavily criticised for his handling of the file and took his own life in "
              "2017. These two trajectories document the human cost of public exposure.",
              "CONFIRMED", "en-wiki-gregory"),
        block("unknown", "Ce qui restera inconnu", "What will remain unknown",
              "Le mobile, l'identité de l'auteur et celle de l'appelant anonyme ne sont pas établis.",
              "The motive, the author's identity and that of the anonymous caller are not established.",
              "UNKNOWN", None),
    ],
}

VICTIMOLOGY = {
    "ethics_note": txt("La victime est un enfant de 4 ans. Aucune analyse de « choix de cible » n'est pertinente ni "
                      "acceptable ici : les éléments ci-dessous portent sur le contexte, pas sur la personne.",
                      "The victim is a 4-year-old child. No analysis of 'target selection' is relevant or acceptable "
                      "here: the elements below concern the context, not the person."),
    "blocks": [
        block("context", "Un enfant, un domicile, une rivière", "A child, a home, a river",
              "Grégory Villemin jouait devant le domicile familial en fin d'après-midi, dans un village des Vosges. La "
              "Vologne passe à proximité. Ce contexte géographique est le seul élément situationnel documenté.",
              "Grégory Villemin was playing in front of the family home in the late afternoon, in a Vosges village. "
              "The Vologne river runs nearby. This geographic context is the only documented situational element.",
              "CONFIRMED", "ici-dates-cles"),
        block("analysis", "Ce que ce dossier apprend de la victimologie", "What this file teaches about victimology",
              "Ici, la victimologie ne sert pas à comprendre un choix d'auteur : elle sert à mesurer ce qu'un "
              "traitement public peut faire à une famille déjà frappée. La mère a été inculpée, le père a été "
              "condamné pour un meurtre commis dans l'affaire, un oncle a reçu l'appel anonyme, une grand-mère a été "
              "désignée par les enquêteurs sans être jugée.",
              "Here, victimology does not serve to understand an author's choice: it serves to measure what public "
              "treatment can do to an already stricken family. The mother was indicted, the father was convicted of a "
              "murder committed within the case, an uncle received the anonymous call, a grandmother was named by "
              "investigators without being tried.",
              "CONFIRMED", "en-wiki-gregory"),
    ],
}

COURT = {
    "jurisdiction": txt("France — instruction à Épinal puis dépaysement à Dijon ; chambre de l'instruction de la cour "
                        "d'appel de Dijon",
                        "France — investigation in Épinal then transfer to Dijon; investigation chamber of the Dijon "
                        "court of appeal"),
    "verdict": txt("Aucun verdict sur le meurtre : l'auteur n'a jamais été identifié. Les décisions rendues portent "
                   "sur des non-lieux, des annulations d'actes, et la condamnation de Jean-Marie Villemin pour le "
                   "meurtre de Bernard Laroche.",
                   "No verdict on the murder: the author was never identified. The decisions rendered concern "
                   "dismissals, annulments of acts, and the conviction of Jean-Marie Villemin for the murder of "
                   "Bernard Laroche."),
    "sentence": {
        "label": txt("Aucune peine pour le meurtre de Grégory Villemin", "No sentence for the murder of Grégory Villemin"),
        "pronounced": "",
        "requested": txt("—", "—"),
        "cumul": txt("Jean-Marie Villemin a été condamné pour le meurtre de Bernard Laroche ; le parquet général a "
                     "indiqué en 2008 ne pas s'opposer à sa demande de réhabilitation.",
                     "Jean-Marie Villemin was convicted for the murder of Bernard Laroche; the Prosecutor General "
                     "indicated in 2008 that he would not oppose his request for rehabilitation."),
        "reasoning": txt("L'arrêt de 2018 retient des « charges très sérieuses » d'enlèvement contre Bernard Laroche, "
                         "tout en précisant qu'il est impossible d'affirmer qu'il a assassiné l'enfant.",
                         "The 2018 ruling retains 'very serious indications' of abduction against Bernard Laroche, "
                         "while specifying that it is impossible to assert that he murdered the child."),
        "appeal": txt("Les mises en examen de 2017 ont été annulées en 2018. Le non-lieu de Christine Villemin n'a "
                      "pas été annulé.",
                      "The 2017 indictments were annulled in 2018. Christine Villemin's dismissal was not annulled."),
        "reliability": "CONFIRMED", "source": "wiki-gregory-fr",
    },
    "consequences": [
        item("L'affaire est devenue la référence française en matière d'emballement médiatique et judiciaire.",
             "The case became the French reference for media and judicial frenzy.",
             "CONFIRMED", "lesjours-gregory"),
        item("Elle a alimenté la réflexion sur le secret de l'instruction, la communication des magistrats et la "
             "protection des personnes mises en cause.",
             "It fed reflection on the secrecy of investigations, magistrates' communication and the protection of "
             "indicted persons.",
             "PROBABLE", "ici-dates-cles"),
        item("Elle illustre les limites de l'ADN : appliquée à des scellés anciens, la technique n'a pas produit "
             "d'identification.",
             "It illustrates the limits of DNA: applied to old exhibits, the technique produced no identification.",
             "CONFIRMED", "ici-dates-cles"),
    ],
}

EXPERTS = [
    {"label": txt("Sept experts en écriture", "Seven handwriting experts"), "field": "forensic_science",
     "position": txt("Experts en écriture auprès de la Cour de cassation : ils ont mis Christine Villemin hors de "
                     "cause avec certitude concernant les courriers du corbeau.",
                     "Handwriting experts at the Court of Cassation: they ruled out Christine Villemin with certainty "
                     "concerning the anonymous letters."),
     "reliability": "CONFIRMED", "source": "wiki-gregory-fr"},
    {"label": txt("Experts en analyse vocale", "Voice analysis experts"), "field": "forensic_science",
     "position": txt("Tous s'accordent pour dire que la voix des cassettes n'est pas celle de Christine Villemin ; "
                     "la majorité estime avoir affaire à une voix de femme.",
                     "All agree that the voice on the tapes is not Christine Villemin's; the majority consider it a "
                     "woman's voice."),
     "reliability": "CONFIRMED", "source": "wiki-gregory-fr"},
    {"label": txt("Un magistrat sur la fragilité d'un témoignage", "A magistrate on the fragility of a testimony"),
     "field": "judicial",
     "position": txt("Un magistrat a écrit que la base d'inculpation de Bernard Laroche n'était « pas d'une solidité "
                     "à toute épreuve, compte tenu de l'âge de Murielle Bolle et de ses facultés intellectuelles à "
                     "mon avis relativement limitées ».",
                     "A magistrate wrote that the basis for Bernard Laroche's indictment was 'not of unshakeable "
                     "solidity, given Murielle Bolle's age and her intellectual faculties in my view relatively "
                     "limited'."),
     "reliability": "CONFIRMED", "source": "wiki-gregory-fr"},
    {"label": txt("La chambre de l'instruction (2018)", "The investigation chamber (2018)"), "field": "judicial",
     "position": txt("Des « charges très sérieuses » d'enlèvement subsistent contre Bernard Laroche ; il est "
                     "impossible d'affirmer qu'il a assassiné l'enfant.",
                     "'Very serious indications' of abduction remain against Bernard Laroche; it is impossible to "
                     "assert that he murdered the child."),
     "reliability": "CONFIRMED", "source": "wiki-gregory-fr"},
]
EXPERTS_AGREEMENT = txt("Tous les experts consultés s'accordent pour exclure Christine Villemin comme auteure des "
                        "courriers et des cassettes.",
                        "All consulted experts agree on excluding Christine Villemin as author of the letters and tapes.")
EXPERTS_DISAGREEMENT = txt("Ils divergent sur l'interprétation à donner aux charges subsistant contre Bernard "
                           "Laroche : enlèvement probable, assassinat impossible à affirmer.",
                           "They differ on the interpretation to give to the indications remaining against Bernard "
                           "Laroche: probable abduction, impossible to assert murder.")
EXPERTS_UNCERTAIN = txt("Ce qui reste incertain : l'identité de l'auteur du meurtre, celle du corbeau, celle de "
                        "l'appelant anonyme, et le mobile.",
                        "What remains uncertain: the identity of the murder's author, of the anonymous writer, of the "
                        "anonymous caller, and the motive.")

COUNTERFACTUALS = [
    counterfactual(
        "technology",
        "Et si l'ADN de 2000 avait été disponible en 1985 ?",
        "What if the DNA of 2000 had been available in 1985?",
        "Les cordelettes, l'anorak et le menton de l'enfant ont supporté des analyses ADN dans les années 2000, "
        "conclues par une ordonnance de non-lieu en 2001. La première inculpation date de 1984.",
        "The cords, the anorak and the child's chin supported DNA analyses in the 2000s, concluded by a dismissal "
        "order in 2001. The first indictment dates from 1984.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Première inculpation", "First indictment"), "date": "1984-11-05"},
            "hypothesis": {"label": txt("Technique ADN non disponible", "DNA technique unavailable"), "date": "1984-11-05"},
            "scenario_event": {"label": txt("Analyses ADN et non-lieu", "DNA analyses and dismissal"), "date": "2001-01-01"},
            "documented_offences_after": [],
            "jurisdiction_note": txt(
                "Point décisif : les analyses ADN réalisées dans les années 2000 n'ont pas produit d'identification et "
                "se sont conclues par un non-lieu. Un scénario dans lequel cette technique aurait été disponible en "
                "1985 ne permet donc pas d'affirmer qu'une identification aurait eu lieu : la technique a été "
                "appliquée, et elle n'a pas tranché. L'application affiche l'écart de temps et ce résultat, rien de "
                "plus.",
                "Decisive point: the DNA analyses carried out in the 2000s produced no identification and ended in a "
                "dismissal. A scenario in which that technique had been available in 1985 therefore does not allow "
                "asserting that an identification would have occurred: the technique was applied, and it did not "
                "settle anything. The application displays the time gap and that result, nothing more."),
        },
        [
            {"date": "1984-10-16", "kind": "reference", "label": txt("Scellés constitués", "Exhibits created")},
            {"date": "1984-11-05", "kind": "fact", "label": txt("Première inculpation", "First indictment")},
            {"date": "1993-01-01", "kind": "fact", "label": txt("Non-lieu de Christine Villemin", "Christine Villemin's dismissal")},
            {"date": "2001-01-01", "kind": "scenario", "label": txt("Analyses ADN, non-lieu", "DNA analyses, dismissal")},
        ],
        True, "ici-dates-cles"),
    counterfactual(
        "investigation_orientation",
        "Et si l'enquête avait été orientée différemment en 1984 ?",
        "What if the investigation had been steered differently in 1984?",
        "Une première inculpation est intervenue en 1984 sur la base de déclarations d'une mineure. Un non-lieu a "
        "suivi. Entre 1984 et 1993, la mère de l'enfant a été inculpée puis mise hors de cause.",
        "A first indictment occurred in 1984 on the basis of a minor's statements. A dismissal followed. Between 1984 "
        "and 1993, the child's mother was indicted then cleared.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Ouverture de l'information", "Opening of the investigation"), "date": "1984-10-17"},
            "hypothesis": {"label": txt("Première orientation de l'enquête", "First orientation of the investigation"), "date": "1984-11-05"},
            "scenario_event": {"label": txt("Non-lieu au bénéfice de la mère", "Dismissal in favour of the mother"), "date": "1993-02-03"},
            "documented_offences_after": [],
            "jurisdiction_note": txt(
                "Ce scénario ne porte pas sur des victimes ultérieures : aucun autre fait n'est documenté dans ce "
                "dossier après le 16 octobre 1984. Il porte sur les conséquences d'une orientation d'enquête pour les "
                "personnes mises en cause — dont l'une a été tuée en 1985, et dont une autre a passé huit ans sous "
                "inculpation avant un non-lieu.",
                "This scenario does not concern later victims: no other offence is documented in this file after "
                "16 October 1984. It concerns the consequences of an investigative orientation for the persons "
                "indicted — one of whom was killed in 1985, and another of whom spent eight years under indictment "
                "before a dismissal."),
        },
        [
            {"date": "1984-10-16", "kind": "reference", "label": txt("Meurtre", "Murder")},
            {"date": "1984-11-05", "kind": "hypothesis", "label": txt("Première inculpation", "First indictment")},
            {"date": "1985-03-29", "kind": "offence", "label": txt("Bernard Laroche tué", "Bernard Laroche killed")},
            {"date": "1993-02-03", "kind": "scenario", "label": txt("Non-lieu de Christine Villemin", "Christine Villemin's dismissal")},
            {"date": "2018-05-16", "kind": "outcome", "label": txt("Annulation des mises en examen de 2017", "Annulment of the 2017 indictments")},
        ],
        True, "lesjours-gregory"),
]

LESSONS = [
    item("Un témoignage recueilli auprès d'une mineure doit être examiné avec une prudence particulière : un "
         "magistrat l'a écrit dans ce dossier.",
         "Testimony collected from a minor must be examined with particular caution: a magistrate wrote so in this file.",
         "CONFIRMED", "wiki-gregory-fr", "Fragilité du témoignage", "Fragility of testimony"),
    item("Une mise en cause publique produit des effets irréversibles, indépendamment de l'issue judiciaire.",
         "A public accusation produces irreversible effects, regardless of the judicial outcome.",
         "CONFIRMED", "lesjours-gregory", "Médias", "Media"),
    item("Une technique scientifique nouvelle ne résout pas automatiquement un dossier ancien : ici, l'ADN a été "
         "appliqué et n'a pas permis d'identification.",
         "A new scientific technique does not automatically solve an old file: here, DNA was applied and allowed no "
         "identification.",
         "CONFIRMED", "ici-dates-cles", "Limites de la science", "Limits of science"),
    item("Des actes de procédure peuvent être annulés pour irrégularité, ce qui retire au dossier des éléments "
         "pourtant recueillis : la forme est une garantie, et elle a un coût.",
         "Procedural acts can be annulled for irregularity, removing from the file elements nonetheless collected: "
         "form is a guarantee, and it has a cost.",
         "CONFIRMED", "wiki-gregory-fr", "Procédure", "Procedure"),
    item("La continuité d'une instruction dépend d'un magistrat : un empêchement accidentel en 1990 a interrompu un "
         "travail dont les cahiers personnels étaient la seule trace.",
         "The continuity of an investigation depends on a magistrate: an accidental impediment in 1990 interrupted "
         "work of which personal notebooks were the only trace.",
         "CONFIRMED", "wiki-gregory-fr", "Continuité", "Continuity"),
    item("« Charges très sérieuses » et « impossible d'affirmer » peuvent coexister dans la même décision : c'est la "
         "formulation exacte de la chambre de l'instruction en 2018.",
         "'Very serious indications' and 'impossible to assert' can coexist in the same decision: that is the exact "
         "wording of the investigation chamber in 2018.",
         "CONFIRMED", "wiki-gregory-fr", "Niveaux de certitude", "Levels of certainty"),
    item("Une affaire non résolue reste une affaire : elle ne devient pas fictive parce qu'elle est sans coupable.",
         "An unsolved case remains a case: it does not become fiction because it has no culprit.",
         "CONFIRMED", "en-wiki-gregory", "Statut éditorial", "Editorial status"),
]

UNKNOWNS = [
    item("Qui a tué Grégory Villemin.", "Who killed Grégory Villemin.", "UNKNOWN", "en-wiki-gregory"),
    item("Le mobile.", "The motive.", "UNKNOWN", "en-wiki-gregory"),
    item("L'auteur des courriers et cassettes.", "The author of the letters and tapes.", "UNKNOWN", "wiki-gregory-fr"),
    item("L'auteur de l'appel anonyme du 16 octobre 1984.", "The author of the anonymous call of 16 October 1984.",
         "UNKNOWN", "en-wiki-gregory"),
    item("La portée exacte des actes annulés, dont certains remontent au juge Simon.",
         "The exact scope of the annulled acts, some of which date back to judge Simon.", "DISPUTED", "wiki-gregory-fr"),
]

SECTIONS = merge_sections(default_sections(), [
    {"key": "introduction", "blocks": [block(
        "paragraph", "Une affaire sans coupable", "A case without a culprit",
        "Le 16 octobre 1984, un enfant de 4 ans est retrouvé mort dans une rivière des Vosges. Quarante ans de "
        "procédure, plusieurs réouvertures, des analyses ADN, des mises en examen annulées, un non-lieu au bénéfice "
        "de la mère : le meurtre n'est pas élucidé. Ce dossier est présenté comme tel — une affaire non résolue, et "
        "non un récit à suspense.",
        "On 16 October 1984, a 4-year-old child is found dead in a Vosges river. Forty years of proceedings, several "
        "reopenings, DNA analyses, annulled indictments, a dismissal in favour of the mother: the murder is not "
        "solved. This file is presented as such — an unsolved case, and not a suspense narrative.",
        "CONFIRMED", "en-wiki-gregory")]},
    {"key": "context", "blocks": [block(
        "paragraph", "La Vologne, un village, une famille", "The Vologne, a village, a family",
        "Lépanges-sur-Vologne, dans les Vosges. La rivière passe à quelques kilomètres. Le dossier s'inscrit dans un "
        "contexte familial et social que la presse a largement exposé — exposition qui fait elle-même partie de "
        "l'objet d'étude.",
        "Lépanges-sur-Vologne, in the Vosges. The river runs a few kilometres away. The file is set in a family and "
        "social context that the press widely exposed — an exposure that is itself part of the object of study.",
        "CONFIRMED", "ici-dates-cles")]},
    {"key": "offender", "blocks": [block(
        "unknown", "Aucun auteur identifié", "No identified author",
        "Aucune personne n'a été condamnée pour le meurtre de Grégory Villemin. Cette application n'affiche aucune "
        "fiche « auteur » pour ce dossier, et ne présente aucune personne mise en cause comme coupable.",
        "No person has been convicted of the murder of Grégory Villemin. This application displays no 'author' file "
        "for this dossier, and presents no indicted person as guilty.",
        "UNKNOWN", "en-wiki-gregory")]},
    {"key": "behaviour", "blocks": [block(
        "behaviour", "Analyser les comportements collectifs", "Analysing collective behaviours",
        "Faute d'auteur identifié, l'analyse comportementale porte sur ce qui est documenté : les comportements "
        "familiaux, médiatiques et judiciaires qui ont entouré le dossier.",
        "For lack of an identified author, behavioural analysis concerns what is documented: the family, media and "
        "judicial behaviours that surrounded the file.",
        "CONFIRMED", "lesjours-gregory")]},
    {"key": "consequences", "blocks": [block(
        "paragraph", "Ce que l'affaire a changé", "What the case changed",
        "Elle est devenue la référence publique française sur l'emballement médiatico-judiciaire, sur le secret de "
        "l'instruction et sur le coût humain d'une mise en cause publique — y compris pour les magistrats.",
        "It became the French public reference on media-judicial frenzy, on the secrecy of investigations and on the "
        "human cost of public accusation — including for magistrates.",
        "CONFIRMED", "lesjours-gregory")]},
])

EPISODES = [
    {
        "number": 1,
        "title": txt("Quatre heures", "Four hours"),
        "description": txt("Vosges, 16 octobre 1984. Ce que l'on sait d'une journée, et ce que quarante ans de "
                           "procédure n'ont pas établi.",
                           "Vosges, 16 October 1984. What is known of one day, and what forty years of proceedings did "
                           "not establish."),
        "modes": ["documentary", "investigation", "chronology", "express", "victims", "expert"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 60, "title": txt("16 octobre 1984", "16 October 1984")},
            {"at": 240, "title": txt("Le corbeau", "The anonymous writer")},
            {"at": 420, "title": txt("1985 : deux événements", "1985: two events")},
            {"at": 600, "title": txt("Et maintenant, une question", "And now, a question")},
            {"at": 640, "title": txt("Ce que la science n'a pas tranché", "What science did not settle")},
        ],
        "transcript": {"segments": [
            {"id": "gr1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X, à travers mon regard. Cet épisode est différent des autres. Il ne se "
                     "termine pas par une arrestation, ni par un verdict. Il se termine par une phrase : le meurtre "
                     "n'est pas élucidé.",
             "text_en": "You are on YANIS//X, through my eyes. This episode is different from the others. It does not "
                        "end with an arrest, or with a verdict. It ends with one sentence: the murder is not solved."},
            {"id": "gr2", "t": 60, "speaker": "yanis",
             "text": "16 octobre 1984, Lépanges-sur-Vologne, dans les Vosges. Grégory Villemin a quatre ans. Il joue "
                     "devant la maison. Peu après dix-sept heures, sa mère constate qu'il n'y est plus. À dix-sept "
                     "heures trente, son oncle Michel reçoit un appel anonyme : l'enfant a été emmené, et jeté dans la "
                     "Vologne. À vingt et une heures quinze, le corps est retrouvé à Docelles, à environ sept "
                     "kilomètres en aval. Les pieds, les mains et la tête sont liés par des cordelettes. Le bonnet est "
                     "rabattu sur le visage.",
             "text_en": "16 October 1984, Lépanges-sur-Vologne, in the Vosges. Grégory Villemin is four years old. He "
                        "is playing in front of the house. Shortly after five in the afternoon, his mother notices he "
                        "is no longer there. At half past five, his uncle Michel receives an anonymous call: the child "
                        "has been taken, and thrown into the Vologne. At a quarter past nine, the body is found at "
                        "Docelles, about seven kilometres downstream. The feet, hands and head are bound with cords. "
                        "The cap is pulled over the face."},
            {"id": "gr3", "t": 240, "speaker": "yanis",
             "text": "Puis vient le corbeau. Des courriers, des cassettes, adressés à la famille et à la presse. "
                     "Sept experts en écriture auprès de la Cour de cassation mettront Christine Villemin hors de "
                     "cause avec certitude pour les courriers. Les experts qui ont étudié les cassettes s'accordent "
                     "tous : ce n'est pas sa voix. La majorité estime avoir affaire à une voix de femme. Personne n'a "
                     "jamais identifié l'auteur.",
             "text_en": "Then comes the anonymous writer. Letters, tapes, addressed to the family and the press. Seven "
                        "handwriting experts at the Court of Cassation would rule out Christine Villemin with certainty "
                        "for the letters. The experts who studied the tapes all agree: it is not her voice. The "
                        "majority consider it a woman's voice. Nobody ever identified the author."},
            {"id": "gr4", "t": 420, "speaker": "yanis",
             "text": "En 1985, deux événements déforment définitivement le dossier. Le 29 mars, Bernard Laroche, "
                     "inculpé puis bénéficiaire d'un non-lieu, est tué par Jean-Marie Villemin, le père de l'enfant. "
                     "Celui-ci sera condamné pour ce meurtre, et demandera plus tard sa réhabilitation. La même "
                     "année, Christine Villemin, la mère, est inculpée. La presse la décrira comme « la femme la plus "
                     "haïe de France ». Elle obtiendra un non-lieu en 1993, huit ans plus tard.",
             "text_en": "In 1985, two events permanently distort the file. On 29 March, Bernard Laroche, indicted then "
                        "granted a dismissal, is killed by Jean-Marie Villemin, the child's father. He will be "
                        "convicted of that murder, and later seek rehabilitation. The same year, Christine Villemin, "
                        "the mother, is indicted. The press would describe her as 'the most hated woman in France'. "
                        "She will obtain a dismissal in 1993, eight years later."},
            {"id": "gr5", "t": 600, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "gr6", "t": 640, "speaker": "yanis",
             "text": "Le dossier est dépaysé à Dijon en 1987. Le juge Maurice Simon choisit de ne pas parler à la "
                     "presse. Le 28 janvier 1990, il est victime d'un infarctus, tombe dans le coma, et souffre "
                     "d'amnésie à son réveil. Il doit abandonner l'affaire. Son raisonnement était consigné dans des "
                     "cahiers, destinés à son fils. Il meurt en 1994.",
             "text_en": "The file is transferred to Dijon in 1987. Judge Maurice Simon chooses not to speak to the "
                        "press. On 28 January 1990, he suffers a heart attack, falls into a coma, and has amnesia on "
                        "waking. He has to give up the case. His reasoning was recorded in notebooks, intended for "
                        "his son. He dies in 1994."},
            {"id": "gr7", "t": 800, "speaker": "yanis",
             "text": "Dans les années 2000, la science arrive. Des analyses ADN sont menées sur les cordelettes, sur "
                     "l'anorak, sur le menton de l'enfant, sur certains courriers du corbeau dont celui du 16 octobre "
                     "1984. En 2001, une ordonnance de non-lieu est rendue. L'ADN n'a pas identifié d'auteur.",
             "text_en": "In the 2000s, science arrives. DNA analyses are carried out on the cords, on the anorak, on "
                        "the child's chin, on certain letters from the anonymous writer including that of 16 October "
                        "1984. In 2001, a dismissal order is issued. DNA did not identify an author."},
            {"id": "gr8", "t": 940, "speaker": "yanis",
             "text": "En 2017, un grand-oncle et une grand-tante sont mis en examen. Le premier juge d'instruction du "
                     "dossier, Jean-Michel Lambert, se donne la mort. En 2018, la chambre de l'instruction annule ces "
                     "mises en examen — sans annuler le non-lieu de Christine Villemin. Dans le même arrêt, elle "
                     "écrit deux choses qui doivent être lues ensemble : il subsiste des « charges très sérieuses » "
                     "que Bernard Laroche ait enlevé l'enfant, et il est impossible d'affirmer qu'il l'a assassiné.",
             "text_en": "In 2017, a great-uncle and a great-aunt are indicted. The file's first investigating judge, "
                        "Jean-Michel Lambert, takes his own life. In 2018, the investigation chamber annuls those "
                        "indictments — without annulling Christine Villemin's dismissal. In the same ruling, it writes "
                        "two things that must be read together: 'very serious indications' remain that Bernard "
                        "Laroche abducted the child, and it is impossible to assert that he murdered him."},
            {"id": "gr9", "t": 1120, "speaker": "yanis",
             "text": "Grégory Villemin avait quatre ans. Cette application ne proposera pas de coupable. Elle affiche "
                     "ce que la justice a établi, ce qu'elle a annulé, ce qu'elle a dit impossible à affirmer, et ce "
                     "qu'elle ignore encore. Écouter les histoires. Comprendre les affaires. Ne jamais oublier les "
                     "victimes.",
             "text_en": "Grégory Villemin was four years old. This application will not propose a culprit. It displays "
                        "what justice established, what it annulled, what it declared impossible to assert, and what "
                        "it still does not know. Listen to the stories. Understand the cases. Never forget the victims."},
        ]},
    },
]

QUESTIONS = [
    question("1", 600, "evidence",
             "Des analyses ADN sont menées dans les années 2000 sur les cordelettes, l'anorak et des courriers. Une ordonnance de non-lieu est rendue en 2001. Que faut-il en conclure ?",
             "DNA analyses are carried out in the 2000s on the cords, the anorak and letters. A dismissal order is issued in 2001. What should be concluded?",
             [("a", "Que l'ADN a identifié l'auteur mais que le résultat a été écarté", "That DNA identified the author but the result was discarded"),
              ("b", "Que la technique a été appliquée aux scellés disponibles et n'a pas produit d'identification", "That the technique was applied to the available exhibits and produced no identification"),
              ("c", "Que les scellés avaient été perdus", "That the exhibits had been lost"),
              ("d", "Que l'ADN ne peut jamais rien établir", "That DNA can never establish anything")],
             {"fr": {"whatInvestigatorsKnew": "Des comparaisons ont été effectuées entre les ADN de plusieurs membres de la famille et les profils retrouvés sur les cordelettes, l'anorak, le menton de l'enfant et certains courriers.",
                     "whatExpertsProposed": "L'ADN permet une comparaison, pas une histoire. Un profil issu de scellés anciens peut être inexploitable, mélangé, ou ne correspondre à personne de fiché. L'absence d'identification est un résultat, pas un échec de la méthode.",
                     "documented": "Les analyses et le non-lieu de 2001 sont documentés par la chronologie d'ICI.",
                     "hypothetical": "Ce qu'une campagne d'analyses plus récente produirait sur les mêmes scellés.",
                     "whatYouCouldNotKnow": "Vous ne pouvez pas connaître le détail technique des profils obtenus : il ne figure pas dans les sources consultées.",
                     "answer_note": "La réponse attendue est B. A est contraire aux sources ; D est une généralisation abusive."},
              "en": {"whatInvestigatorsKnew": "Comparisons were made between the DNA of several family members and profiles found on the cords, the anorak, the child's chin and certain letters.",
                     "whatExpertsProposed": "DNA allows a comparison, not a story. A profile from old exhibits may be unusable, mixed, or match nobody on record. The absence of identification is a result, not a failure of the method.",
                     "documented": "The analyses and the 2001 dismissal are documented by ICI's chronology.",
                     "hypothetical": "What a more recent analysis campaign would produce on the same exhibits.",
                     "whatYouCouldNotKnow": "You cannot know the technical detail of the profiles obtained: it does not appear in the sources consulted.",
                     "answer_note": "The expected answer is B. A is contrary to the sources; D is an abusive generalisation."}},
             "ici-dates-cles"),
    question("1", 400, "bias",
             "Une mère est inculpée et décrite par la presse comme « la femme la plus haïe de France ». Elle obtient un non-lieu huit ans plus tard. Quel mécanisme ce dossier illustre-t-il ?",
             "A mother is indicted and described by the press as 'the most hated woman in France'. She obtains a dismissal eight years later. What mechanism does this file illustrate?",
             [("a", "Un biais de confirmation collectif, renforcé par l'exposition médiatique", "A collective confirmation bias, reinforced by media exposure"),
              ("b", "Une erreur exclusivement technique", "An exclusively technical error"),
              ("c", "Une manipulation volontaire des preuves", "A deliberate manipulation of evidence"),
              ("d", "Aucun mécanisme identifiable", "No identifiable mechanism")],
             {"fr": {"whatInvestigatorsKnew": "Christine Villemin a été inculpée en 1985, mise en cause publiquement, puis a bénéficié d'un non-lieu en 1993. Les expertises en écriture l'ont mise hors de cause avec certitude pour les courriers.",
                     "whatExpertsProposed": "Lorsqu'une hypothèse devient publique et dominante, les éléments qui la confortent sont survalorisés et ceux qui la contredisent minimisés. La pression médiatique accélère ce mécanisme.",
                     "documented": "Le non-lieu, les expertises en écriture et le traitement médiatique sont documentés.",
                     "hypothetical": "Ce qu'aurait produit une instruction conduite hors de toute exposition publique.",
                     "whatYouCouldNotKnow": "Vous ne pouvez pas connaître le détail des actes annulés ni l'intégralité du raisonnement du juge Simon, consigné dans des cahiers personnels.",
                     "answer_note": "La réponse attendue est A. B et C ne sont pas établis par les sources ; C serait une accusation sans fondement."},
              "en": {"whatInvestigatorsKnew": "Christine Villemin was indicted in 1985, publicly accused, then granted a dismissal in 1993. Handwriting examinations ruled her out with certainty for the letters.",
                     "whatExpertsProposed": "When a hypothesis becomes public and dominant, elements supporting it are overvalued and those contradicting it minimised. Media pressure accelerates that mechanism.",
                     "documented": "The dismissal, the handwriting examinations and the media treatment are documented.",
                     "hypothetical": "What an investigation conducted away from any public exposure would have produced.",
                     "whatYouCouldNotKnow": "You cannot know the detail of the annulled acts or the whole of judge Simon's reasoning, recorded in personal notebooks.",
                     "answer_note": "The expected answer is A. B and C are not established by the sources; C would be an unfounded accusation."}},
             "lesjours-gregory"),
    question("1", 1080, "investigation",
             "Un arrêt retient des « charges très sérieuses » d'enlèvement contre une personne décédée, et dit impossible d'affirmer qu'elle a assassiné l'enfant. Comment l'application doit-elle afficher cette information ?",
             "A ruling retains 'very serious indications' of abduction against a deceased person, and says it is impossible to assert that he murdered the child. How should the application display this information?",
             [("a", "Comme une culpabilité établie", "As established guilt"),
              ("b", "Comme une probabilité, avec la réserve exacte de la décision", "As a probability, with the exact reservation of the decision"),
              ("c", "Comme une rumeur judiciaire", "As a judicial rumour"),
              ("d", "Ne pas l'afficher", "Not display it")],
             {"fr": {"whatInvestigatorsKnew": "L'arrêt de la chambre de l'instruction contient les deux énoncés : charges très sérieuses d'enlèvement, impossibilité d'affirmer l'assassinat.",
                     "whatExpertsProposed": "Une décision de justice se cite avec son niveau exact de certitude. Reformuler « charges très sérieuses » en « coupable » est une transformation du document, pas une synthèse.",
                     "documented": "La formulation figure dans l'article de Wikipédia citant l'arrêt.",
                     "hypothetical": "Aucune : la question porte sur la méthode d'affichage.",
                     "whatYouCouldNotKnow": "Rien : l'énoncé est public.",
                     "answer_note": "La réponse attendue est B. C'est le principe même du système de fiabilité à quatre niveaux de cette application."},
              "en": {"whatInvestigatorsKnew": "The investigation chamber's ruling contains both statements: very serious indications of abduction, impossibility of asserting murder.",
                     "whatExpertsProposed": "A court decision is quoted with its exact level of certainty. Rewording 'very serious indications' as 'guilty' is a transformation of the document, not a summary.",
                     "documented": "The wording appears in the Wikipedia article citing the ruling.",
                     "hypothetical": "None: the question concerns display method.",
                     "whatYouCouldNotKnow": "Nothing: the statement is public.",
                     "answer_note": "The expected answer is B. It is the very principle of this application's four-level reliability system."}},
             "wiki-gregory-fr"),
]

CASE = {
    "id": CASE_ID,
    "title": txt("Affaire Grégory Villemin", "The Grégory Villemin case"),
    "subtitle": txt("Vosges, 16 octobre 1984. Un enfant de 4 ans, quarante ans de procédure, et aucune identification.",
                    "Vosges, 16 October 1984. A 4-year-old child, forty years of proceedings, and no identification."),
    "country": "FR", "region": "Grand Est / Vosges", "city": "Lépanges-sur-Vologne",
    "year_start": 1984, "year_end": 2025, "period_label": txt("1984 – aujourd'hui", "1984 – today"),
    "status": "UNSOLVED",
    "status_note": txt("Aucune personne n'a été condamnée pour ce meurtre. Le dossier a connu plusieurs réouvertures "
                       "et des annulations d'actes.",
                       "No person has been convicted of this murder. The file has seen several reopenings and "
                       "annulments of acts."),
    "type": "cold_case",
    "tags": ["cold_case", "child_victim", "france", "judicial_errors", "media_frenzy", "dna", "unsolved", "annulled_acts"],
    "tier": "FREE", "editorial": "yanis", "published_at": "2026-09-24", "sensitive": True,
    "triggers": txt("Meurtre d'un enfant de 4 ans ; mise en cause publique de la mère ; suicides et meurtre au sein "
                    "de la procédure.",
                    "Murder of a 4-year-old child; public accusation against the mother; suicides and a murder within "
                    "the proceedings."),
    "lat": 48.19, "lon": 6.43, "cover": "cover-gregory",
    "stats": {"victims_documented": 1, "procedure_years": 41, "reopenings": 3},
    "summary": txt(
        "Le 16 octobre 1984, Grégory Villemin, 4 ans, disparaît du devant du domicile familial à Lépanges-sur-Vologne "
        "(Vosges). Un oncle reçoit à 17 h 30 un appel anonyme annonçant que l'enfant a été jeté dans la Vologne ; le "
        "corps est retrouvé à 21 h 15 à Docelles, les pieds, les mains et la tête liés par des cordelettes. Suivent "
        "quarante ans de procédure : des courriers et cassettes d'un « corbeau » jamais identifié, l'inculpation de "
        "Bernard Laroche puis son non-lieu, son meurtre en 1985 par le père de l'enfant — qui sera condamné pour ce "
        "fait —, l'inculpation de la mère Christine Villemin, son non-lieu en 1993, le dépaysement à Dijon en 1987, "
        "l'empêchement du juge Maurice Simon en 1990, des analyses ADN conclues par un non-lieu en 2001, une "
        "réouverture en 2008, des mises en examen en 2017 annulées en 2018, et le suicide la même année du premier "
        "juge d'instruction. En 2018, la chambre de l'instruction retient des « charges très sérieuses » que Bernard "
        "Laroche ait enlevé l'enfant, tout en disant impossible d'affirmer qu'il l'a assassiné. Le meurtre n'est pas "
        "élucidé.",
        "On 16 October 1984, Grégory Villemin, 4, disappears from in front of the family home in "
        "Lépanges-sur-Vologne (Vosges). An uncle receives at 5.30 p.m. an anonymous call announcing the child has "
        "been thrown into the Vologne; the body is found at 9.15 p.m. at Docelles, feet, hands and head bound with "
        "cords. Forty years of proceedings follow: letters and tapes from an anonymous writer never identified, the "
        "indictment of Bernard Laroche then his dismissal, his murder in 1985 by the child's father — who was "
        "convicted for that act —, the indictment of the mother Christine Villemin, her dismissal in 1993, the "
        "transfer to Dijon in 1987, judge Maurice Simon's impediment in 1990, DNA analyses concluded by a dismissal "
        "in 2001, a reopening in 2008, indictments in 2017 annulled in 2018, and the suicide the same year of the "
        "first investigating judge. In 2018, the investigation chamber retained 'very serious indications' that "
        "Bernard Laroche abducted the child, while stating it is impossible to assert that he murdered him. The "
        "murder is not solved."),
    "sources": SOURCES, "victims": VICTIMS, "other_proceedings": OTHER_PROCEEDINGS, "memorial": MEMORIAL,
    "timeline": TIMELINE, "locations": LOCATIONS, "evidence": EVIDENCE, "investigation": INVESTIGATION,
    "psychology": PSYCHOLOGY, "victimology": VICTIMOLOGY, "court": COURT, "experts": EXPERTS,
    "experts_agreement": EXPERTS_AGREEMENT, "experts_disagreement": EXPERTS_DISAGREEMENT,
    "experts_uncertain": EXPERTS_UNCERTAIN, "counterfactuals": COUNTERFACTUALS, "lessons": LESSONS,
    "unknowns": UNKNOWNS, "sections": SECTIONS, "episodes": EPISODES, "questions": QUESTIONS,
}
