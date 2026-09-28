"""
DOSSIER 09 — ROBERT PICKTON (Canada, Colombie-Britannique, 1978-2024)

Angle éditorial : victimologie systémique. Ce dossier ne raconte pas « un tueur » :
il documente ce qu'un système a fait de femmes, et ce qu'une institution a mis
six ans à reconnaître.

Toutes les sources sont publiques, datées et vérifiées le 2026-09-28.
Niveau de fiabilité affiché sur chaque fait : CONFIRMED / PROBABLE / DISPUTED / UNKNOWN.
Aucune victimisation n'est expliquée par une caractéristique des victimes.
"""
from ..case_template import (block, counterfactual, default_sections, fact, item,
                             merge_sections, question, source, txt)

CASE_ID = "robert-pickton"
V = "2026-09-28"

SOURCES = [
    source("forsaken-es", CASE_ID,
           "Forsaken — Rapport de la Commission d'enquête sur les femmes disparues et assassinées, sommaire",
           "Forsaken — Report of the Missing Women Commission of Inquiry, executive summary",
           "Gouvernement de Colombie-Britannique", "Wally T. Oppal, commissaire",
           "https://www2.gov.bc.ca/assets/gov/law-crime-and-justice/about-bc-justice-system/inquiries/forsaken-es.pdf",
           "2012-11-19", "official", "CONFIRMED", V,
           "Document primaire. Conclusions : « une défaillance manifeste » (blatant failure) des enquêtes sur les "
           "disparues du Downtown Eastside, avec un biais systémique. 63 recommandations et deux mesures urgentes.",
           "Primary document. Findings: a 'blatant failure' of the missing women investigations, with systemic bias. "
           "63 recommendations and two urgent measures."),

    source("forsaken-vol1", CASE_ID,
           "Forsaken, volume I — Les femmes, leurs vies et le cadre de l'enquête",
           "Forsaken, volume I — The women, their lives and the framework of inquiry",
           "Gouvernement de Colombie-Britannique", "Wally T. Oppal, commissaire",
           "https://www2.gov.bc.ca/assets/gov/law-crime-and-justice/about-bc-justice-system/inquiries/forsaken-vol_1.pdf",
           "2012-11-19", "official", "CONFIRMED", V,
           "Conditions de vie, marginalisation et vulnérabilité dans le Downtown Eastside ; portraits documentés de "
           "nombreuses femmes disparues ; les quatre affiches successives de femmes disparues (2001, 2002, 2003, 2004).",
           "Living conditions, marginalisation and vulnerability in the Downtown Eastside; documented portraits of many "
           "missing women; the four successive missing women posters (2001, 2002, 2003, 2004)."),

    source("forsaken-vol2b", CASE_ID,
           "Forsaken, volume IIB — Nobodies : comment et pourquoi nous avons échoué, parties 3, 4 et 5",
           "Forsaken, volume IIB — Nobodies: how and why we failed, parts 3, 4 and 5",
           "Gouvernement de Colombie-Britannique", "Wally T. Oppal, commissaire",
           "https://www2.gov.bc.ca/assets/gov/law-crime-and-justice/about-bc-justice-system/inquiries/forsaken-vol_2b.pdf",
           "2012-11-19", "official", "CONFIRMED", V,
           "Biais systémique, absence d'urgence, retards de transmission des dossiers, absence de gestion de dossier "
           "majeur, coordination entre la police de Vancouver et la GRC.",
           "Systemic bias, lack of urgency, delays in transferring files, absence of major case management, "
           "coordination between the Vancouver Police Department and the RCMP."),

    source("forsaken-vol3", CASE_ID,
           "Forsaken, volume III — Gone, but not Forgotten",
           "Forsaken, volume III — Gone, but not Forgotten",
           "Gouvernement de Colombie-Britannique", "Wally T. Oppal, commissaire",
           "https://www2.gov.bc.ca/assets/gov/law-crime-and-justice/about-bc-justice-system/inquiries/forsaken-vol_3.pdf",
           "2012-11-15", "official", "CONFIRMED", V,
           "Recommandations de politique publique : compensation des enfants, prévention, transports, formation "
           "policière, lien avec l'Enquête nationale sur les femmes et filles autochtones disparues et assassinées.",
           "Policy recommendations: compensation for children, prevention, transport, police training, and links with "
           "the National Inquiry into missing and murdered Indigenous women and girls."),

    source("forsaken-vol4", CASE_ID,
           "Forsaken, volume IV — Le processus de la Commission",
           "Forsaken, volume IV — The Commission's process",
           "Gouvernement de Colombie-Britannique", "Wally T. Oppal, commissaire",
           "https://www2.gov.bc.ca/assets/gov/law-crime-and-justice/about-bc-justice-system/inquiries/forsaken-vol_4.pdf",
           "2012-11-19", "official", "CONFIRMED", V,
           "Portée du mandat : les enquêtes menées du 23 janvier 1997 au 5 février 2002, portant sur plus de "
           "65 femmes disparues et assassinées, ainsi que la décision de surseoir du 26-27 janvier 1998.",
           "Scope of the mandate: investigations from 23 January 1997 to 5 February 2002, covering more than 65 "
           "missing and murdered women, and the stay decision of 26-27 January 1998."),

    source("cbc-verdict", CASE_ID,
           "Pickton obtient la peine maximale pour six meurtres",
           "Pickton gets maximum sentence for murders",
           "CBC News", "Rédaction",
           "https://www.cbc.ca/news/canada/british-columbia/pickton-gets-maximum-sentence-for-murders-1.650944",
           "2007-12-12", "press", "CONFIRMED", V,
           "Condamnation du 11 décembre 2007 : réclusion à perpétuité sans possibilité de libération conditionnelle "
           "pendant 25 ans, après dix-huit déclarations d'impact des victimes lues par le juge.",
           "Sentencing on 11 December 2007: life imprisonment with no possibility of parole for 25 years, after "
           "eighteen victim impact statements read by the judge."),

    source("cbc-scc", CASE_ID,
           "Pickton n'obtiendra pas de nouveau procès : la Cour suprême",
           "Pickton won't get new trial: top court",
           "CBC News", "Rédaction",
           "https://www.cbc.ca/news/canada/robert-pickton-won-t-get-new-trial-top-court-1.865566",
           "2010-07-31", "press", "CONFIRMED", V,
           "30 juillet 2010 : la Cour suprême du Canada rejette l'appel à l'unanimité. Motifs : « preuve "
           "accablante », « aucune erreur de droit ni déni de justice ». Citation de la juge Louise Charron.",
           "30 July 2010: the Supreme Court of Canada unanimously dismisses the appeal. Grounds: 'overwhelming "
           "evidence', 'no legal error nor miscarriage of justice'. Quote from Justice Louise Charron."),

    source("cbc-timeline", CASE_ID,
           "Chronologie du procès Pickton",
           "Pickton trial timeline",
           "CBC News", "Rédaction",
           "https://www.cbc.ca/news/canada/pickton-trial-timeline-1.927418",
           "2016-11-01", "press", "CONFIRMED", V,
           "Condamnation, voies d'appel, dates clés. Document utilisé ici pour les dates de 2010.",
           "Conviction, appeal paths, key dates. Used here for the 2010 dates."),

    source("cbc-inquiry", CASE_ID,
           "L'enquête Pickton dénonce des « défaillances manifestes » de la police",
           "Pickton inquiry slams 'blatant failures' by police",
           "CBC News", "Rédaction",
           "https://cbc.ca/amp/1.1191108",
           "2012-12-17", "press", "CONFIRMED", V,
           "Restitution des conclusions du rapport Oppal : absence de stratégie de protection des femmes du Downtown "
           "Eastside avant quelques semaines avant l'arrestation, absence de gestion de dossier majeur, "
           "coordination défaillante entre deux services de police.",
           "Restatement of the Oppal report findings: no protection strategy for Downtown Eastside women until weeks "
           "before the arrest, no major case management, failed coordination between two police services."),

    source("tce", CASE_ID,
           "L'affaire Robert Pickton",
           "Robert Pickton Case",
           "L'Encyclopédie canadienne", "Rédaction",
           "https://thecanadianencyclopedia.ca/en/article/robert-pickton-case",
           "2020-10-08", "reference", "CONFIRMED", V,
           "Source de synthèse : au moins 65 femmes disparues du Downtown Eastside entre 1978 et 2001 ; 26 mises en "
           "accusation ; 6 condamnations ; la femme non identifiée dite « Jane Doe » dont l'accusation a été rejetée.",
           "Synthesis source: at least 65 women missing from the Downtown Eastside between 1978 and 2001; 26 charged; "
           "6 convicted; the unidentified woman known as 'Jane Doe' whose count was dismissed."),

    source("vsun-timeline", CASE_ID,
           "Chronologie des femmes disparues",
           "Missing women timeline",
           "Vancouver Sun", "Kate Bird et Jonathan Fowlie",
           "https://vancouversun.com/news/metro/missing-women-timeline",
           "2012-12-17", "press", "CONFIRMED", V,
           "Recueil de dates de l'enquête publique, du premier nom de la liste (1978) à la remise du rapport "
           "(23 novembre 2012). Utilisé ici pour la chronologie institutionnelle.",
           "A collection of public inquiry dates, from the first name on the list (1978) to the tabling of the "
           "report (23 November 2012). Used here for the institutional chronology."),

    source("vsun-evidence", CASE_ID,
           "La GRC veut détruire les preuves de la ferme de Robert Pickton. Devrait-elle le pouvoir ?",
           "RCMP want to destroy evidence from Robert Pickton's farm. Should they?",
           "Vancouver Sun", "Rédaction",
           "https://vancouversun.com/news/crime/exclusive-bc-serial-killer-robert-pickton-evidence",
           "2023-12-08", "press", "CONFIRMED", V,
           "Demande de la GRC de détruire environ 14 000 objets saisis ; opposition de 40 groupes et personnes ; une "
           "petite partie des objets sera restituée aux familles.",
           "The RCMP's application to dispose of about 14,000 seized items; opposition from 40 groups and "
           "individuals; a small portion of the items will be returned to families."),

    source("hashilthsa", CASE_ID,
           "La GRC demande la destruction des preuves récoltées dans l'affaire du meurtre de Pickton",
           "RCMP applies to destroy evidence gathered in Pickton murder case",
           "Huu-ay-aht / Tribal Councils Media", "Rédaction",
           "https://hashilthsa.com/news/2023-12-21/rcmp-applies-destroy-evidence-gathered-pickton-murder-case",
           "2023-12-21", "press", "CONFIRMED", V,
           "Chiffres de la recherche sur la ferme (383 000 verges cubes de terre Tamisées, plus de 600 000 objets "
           "saisis) et citation du First Nations Leadership Council sur la marginalisation des victimes.",
           "Figures from the farm search (383,000 cubic yards of sifted soil, more than 600,000 items seized) and a "
           "quote from the First Nations Leadership Council on the marginalisation of victims."),

    source("apntn-death", CASE_ID,
           "Robert Pickton est mort à l'hôpital après l'agression qui a eu lieu en prison le 19 mai",
           "Robert Pickton dead in hospital following prison attack on May 19",
           "APTN — Aboriginal Peoples Television Network", "Rédaction",
           "https://www.aptnnews.ca/national-news/serial-killer-robert-pickton-dead-quebec-prison/",
           "2024-05-31", "press", "CONFIRMED", V,
           "Source autochtone indépendante. Agression le 19 mai 2024 à l'établissement Port-Cartier, transfert à "
           "l'hôpital de Québec, décès le 31 mai 2024. Condamnation à perpétuité commencée le 11 décembre 2007.",
           "Independent Indigenous source. Assault on 19 May 2024 at Port-Cartier Institution, transfer to a Quebec "
           "City hospital, death on 31 May 2024. Life sentence commenced 11 December 2007."),

    source("reuters-death", CASE_ID,
           "Le tueur en série canadien Robert Pickton meurt après une attaque en prison",
           "Canadian serial killer Robert Pickton dies after prison attack",
           "Reuters", "Rédaction",
           "https://www.reuters.com/world/americas/canadian-serial-killer-robert-pickton-dies-after-prison-attack-2024-05-31/",
           "2024-05-31", "press", "CONFIRMED", V,
           "Confirmation internationale du décès, à 74 ans. Mentionne les restes ou l'ADN de 33 femmes retrouvés "
           "sur la propriété de Port Coquitlam.",
           "International confirmation of his death, aged 74. Mentions the remains or DNA of 33 women found on the "
           "Port Coquitlam property."),

    source("tgm-timeline", CASE_ID,
           "Qui était Robert Pickton ? Chronologie jusqu'à sa condamnation et sa mort",
           "Who was Robert Pickton? A timeline of events leading to the serial killer's conviction and death",
           "The Globe and Mail", "Rédaction",
           "https://www.theglobeandmail.com/canada/british-columbia/article-robert-pickton-timeline/",
           "2024-06-02", "press", "CONFIRMED", V,
           "Chronologie de référence : condamnation du 9 décembre 2007, peine du 11 décembre 2007, appel rejeté en "
           "2009, Cour suprême en 2010, abandon des 20 chefs le 4 août 2010, accord civil en mars 2014.",
           "Reference chronology: conviction on 9 December 2007, sentence on 11 December 2007, appeal dismissed in "
           "2009, Supreme Court in 2010, discontinuance of the 20 counts on 4 August 2010, civil settlement in "
           "March 2014."),

    source("tgm-families", CASE_ID,
           "Les familles des victimes de Pickton dénoncent une « enquête sans les preuves »",
           "Families of Pickton victims denounce 'missing-evidence inquiry'",
           "The Globe and Mail", "Rédaction",
           "https://www.theglobeandmail.com/news/british-columbia/families-of-pickton-victims-denounce-missing-evidence-inquiry/article4231153/",
           "2012-06-05", "press", "CONFIRMED", V,
           "Témoignage de Cameron Ward, avocat de 25 familles, devant la Commission. Source du point de vue des "
           "familles, indispensable pour équilibrer le dossier.",
           "Testimony from Cameron Ward, counsel to 25 families, before the Commission. The families' point of view "
           "is essential to balance the file."),

    source("star-fund", CASE_ID,
           "Les enfants des victimes de Pickton partagent une compensation de 4,9 millions de dollars",
           "Pickton victims' children get $4.9 million in compensation",
           "The Toronto Star", "Rédaction",
           "https://www.thestar.com/news/canada/robert-pickton-victims-children-get-4-9-million-in-compensation/article_853df868-8100-5021-b9c3-d97cfd55b09d.html",
           "2014-03-18", "press", "CONFIRMED", V,
           "Fonds de 4,9 M$ réparti entre 98 enfants : 40 % fédéral, 40 % provincial, 20 % ville de Vancouver. "
           "Déclaration du chef de la police de Vancouver Jim Chu.",
           "A $4.9M fund shared by 98 children: 40% federal, 40% provincial, 20% City of Vancouver. Statement from "
           "Vancouver Police Chief Jim Chu."),

    source("cbc-civil", CASE_ID,
           "La recherche de la vérité continuera quel que soit le sort de Robert Pickton, disent les défenseurs",
           "Search for truth will go on regardless of Robert Pickton's fate, victims' advocates say",
           "CBC News", "Rédaction",
           "https://www.cbc.ca/news/canada/british-columbia/robert-pickton-victims-civil-suit-rcmp-evidence-1.7213928",
           "2024-05-24", "press", "CONFIRMED", V,
           "État des procédures civiles en 2024 : opposition des familles à la destruction des preuves ; plusieurs "
           "actions reste ouvertes contre Robert et David Pickton ; rappel du règlement de 2014.",
           "State of civil proceedings in 2024: families opposing evidence disposal; several lawsuits still open against "
           "Robert and David Pickton; reminder of the 2014 settlement."),

    source("cbc-death-charge", CASE_ID,
           "Un détenu accusé de meurtre au premier degré dans la mort du tueur en série Robert Pickton",
           "Inmate charged with 1st-degree murder in death of serial killer Robert Pickton",
           "CBC News", "Rédaction",
           "https://www.cbc.ca/news/canada/montreal/robert-pickton-serial-killer-murder-1.7590365",
           "2025-07-21", "press", "CONFIRMED", V,
           "3 juillet 2025 : accusation de meurtre au premier degré contre un codétenu. Utilisé ici pour la seule "
           "section « après » du dossier, sans commenter l'accusé.",
           "3 July 2025: first-degree murder charge laid against a fellow inmate. Used here only for the closing "
           "'after' section, with no comment on the accused."),

    source("rcmp-gazette", CASE_ID,
           "Les enquêteurs de l'affaire Pickton ont étudié le travail réalisé à Ground Zero",
           "Pickton investigators studied work done at Ground Zero",
           "Gendarmerie royale du Canada — Gazette", "Rédaction",
           "https://rcmp.ca/en/gazette/pickton-investigators-studied-work-done-ground-zero",
           "2024-04-24", "official", "CONFIRMED", V,
           "Récit de la GRC sur la fouille de 2002 et l'influence des méthodes de récupération du site du World "
           "Trade Center. Point de vue de l'institution elle-même — affiché comme tel.",
           "The RCMP's own account of the 2002 search and the influence of World Trade Center recovery methods. The "
           "institution's own point of view — displayed as such."),

    source("afn-mmiwg", CASE_ID,
           "Femmes et filles autochtones assassinées et disparues",
           "Murdered and Missing Indigenous Women and Girls",
           "Assembly of First Nations", "Rédaction",
           "https://afn.ca/rights-justice/murdered-missing-indigenous-women-girls/",
           "2025-05-22", "official", "CONFIRMED", V,
           "Rappel du rapport final Reclaiming Power and Place (3 juin 2019) et de ses 231 appels à la justice, "
           "regroupés en 18 appels principaux.",
           "Reminder of the final report Reclaiming Power and Place (3 June 2019) and its 231 calls for justice, "
           "grouped into 18 main calls."),

    source("tgm-charged", CASE_ID,
           "Un agriculteur de la Colombie-Britannique inculpé dans la mort de deux femmes",
           "B.C. farmer charged in deaths of two women",
           "The Globe and Mail", "Rédaction",
           "https://www.theglobeandmail.com/news/national/bc-farmer-charged-in-deaths-of-two-women/article4131949/",
           "2002-02-23", "press", "CONFIRMED", V,
           "Compte rendu du 23 février 2002 : arrestation de Pickton la veille à Surrey, deux chefs de meurtre au "
           "premier degré, perquisitions successives sur la ferme à la suite d'un premier mandat, et plus de "
           "600 appels reçus sur une ligne ouverte deux semaines plus tôt.",
           "Report of 23 February 2002: Pickton's arrest the previous day in Surrey, two counts of first-degree "
           "murder, successive searches of the farm following a first warrant, and more than 600 calls to a tip "
           "line opened two weeks earlier."),

    source("guardian-trial", CASE_ID,
           "Un agriculteur « écorché une victime sur un croc de boucherie »",
           "Farmer 'skinned victim on meat hook'",
           "The Guardian", "Rédaction",
           "https://www.theguardian.com/world/2007/jan/26/1",
           "2007-01-26", "press", "CONFIRMED", V,
           "Déroulé du procès en janvier 2007. Mention explicite de « trois profils ADN non identifiés » "
           "retrouvés sur la ferme, et d'une liste de plus de soixante femmes disparues maintenue par la police.",
           "Trial coverage in January 2007. Explicit mention of 'three unidentified DNA profiles' found on the "
           "farm, and of a list of more than sixty missing women maintained by police."),

    source("cbc-lane", CASE_ID,
           "Vigil tenue sur la ferme de Robert Pickton alors que le tueur en série allait pouvoir demander la "
           "libération de jour",
           "Vigil held at site of Robert Pickton's farm as serial killer soon eligible to apply for day parole",
           "CBC News", "Rédaction",
           "https://cbc.ca/amp/1.7122038",
           "2024-01-24", "press", "CONFIRMED", V,
           "Stephanie Lane, 20 ans, signalée disparue en 1997 ; ses restes, trouvés en 2003, ne furent rendus à sa "
           "famille qu'en 2014 ; Pickton ne fut jamais inculpé. CBC la présente comme la plus jeune victime "
           "présumée.",
           "Stephanie Lane, 20, reported missing in 1997; her remains, found in 2003, were returned to her family "
           "only in 2014; Pickton was never charged. CBC presents her as the youngest presumed victim."),
]

VICTIMS = [
    # --- Les six femmes dont la mort a été jugée -----------------------
    {"order": 0, "first_name": "Sereena", "last_name": "Abotsway", "age": "29",
     "anonymised": False, "reliability": "CONFIRMED", "source": "cbc-verdict",
     "life": {"fr": {"headline": "La première victime nommée au procès",
                     "items": [
                         {"label": "Signalée disparue", "text": "Août 2001. Elle avait été signalée disparue par sa mère adoptive. C'est le premier nom que l'accusation a porté au procès de 2007."},
                         {"label": "Lien matériel retrouvé", "text": "Un inhalateur d'asthme prescrit à son nom a été retrouvé sur la ferme de Port Coquitlam. C'est l'objet qui a relié la propriété à une femme portée disparue."},
                         {"label": "Verdict", "text": "Condamnation à deux chefs de meurtre au second degré le 9 décembre 2007."}],
                     "note": "Elle est l'une des six femmes dont la mort a été jugée. Son corps n'a jamais été rendu à sa famille : seuls des fragments l'ont été, après l'identification."},
              "en": {"headline": "The first victim named at trial",
                     "items": [
                         {"label": "Reported missing", "text": "August 2001. She was reported missing by her foster mother. She is the first name the prosecution put to trial in 2007."},
                         {"label": "Physical link recovered", "text": "A prescription asthma inhaler bearing her name was recovered on the Port Coquitlam farm. It is the item that connected the property to a reported missing woman."},
                         {"label": "Verdict", "text": "Convicted on two counts of second-degree murder on 9 December 2007."}],
                     "note": "She is one of the six women whose deaths were tried. Her body was never returned to her family: only fragments were, after identification."}}},

    {"order": 1, "first_name": "Mona", "last_name": "Lee Wilson", "age": "—",
     "anonymised": False, "reliability": "CONFIRMED", "source": "cbc-verdict",
     "life": {"fr": {"headline": "Cinq ans quand la photo a été prise",
                     "items": [
                         {"label": "Disparue", "text": "Vancouver, Downtown Eastside, 2000. Elle avait quitté son environment familial très jeune."},
                         {"label": "Dans la mémoire de sa sœur", "text": "Sa sœur Ada Wilson a tenu une cérémonie commémorative à sa mémoire à l'église St John the Divine de Vancouver. Une photographie d'elle, enfant, a circulé pendant des décennies."},
                         {"label": "Verdict", "text": "Condamnation à deux chefs de meurtre au second degré le 9 décembre 2007."}],
                     "note": "La photographie d'enfance de Mona Wilson a été l'un des premiers visuels d'un avis de recherche au Canada. Elle a été reprise pendant plus de vingt ans."},
              "en": {"headline": "Five years old when the photograph was taken",
                     "items": [
                         {"label": "Disappeared", "text": "Vancouver, Downtown Eastside, 2000. She had left her family environment very young."},
                         {"label": "In her sister's memory", "text": "Her sister Ada Wilson held a memorial service for her at St John the Divine Church in Vancouver. A photograph of her as a child circulated for decades."},
                         {"label": "Verdict", "text": "Convicted on two counts of second-degree murder on 9 December 2007."}],
                     "note": "The childhood photograph of Mona Wilson was among the first images on a missing person notice in Canada. It was reused for more than twenty years."}}},

    {"order": 2, "first_name": "Andrea", "last_name": "Joesbury", "age": "22",
     "anonymised": False, "reliability": "CONFIRMED", "source": "cbc-verdict",
     "life": {"fr": {"headline": "Un hôtel du Downtown Eastside",
                     "items": [
                         {"label": "Disparue", "text": "Juin 2001. Elle vivait dans un petit hôtel du Downtown Eastside, le quartier où elle avait disparu."},
                         {"label": "Un crâne coupé en deux", "text": "Un crâne attribué à l'une des six femmes a été retrouvé dans un congélateur, coupé en deux, les mains et les pieds placés à l'intérieur. Il a été relié à son cas par l'ADN."},
                         {"label": "Verdict", "text": "Condamnation à deux chefs de meurtre au second degré le 9 décembre 2007."}],
                     "note": "Ce dossier ne reproduit aucun détail graphique des scènes. Seule la tracé factuelle de la découverte est mentionnée, parce qu'elle est le cœur de la preuve."},
              "en": {"headline": "A Downtown Eastside hotel",
                     "items": [
                         {"label": "Disappeared", "text": "June 2001. She lived in a small Downtown Eastside hotel, in the very neighbourhood where she disappeared."},
                         {"label": "A skull cut in two", "text": "A skull attributed to one of the six women was found in a freezer, cut in two, hands and feet placed inside. It was connected to her case by DNA."},
                         {"label": "Verdict", "text": "Convicted on two counts of second-degree murder on 9 December 2007."}],
                     "note": "This dossier reproduces no graphic detail of the scenes. Only the factual course of the discovery is mentioned, because it is the core of the evidence."}}},

    {"order": 3, "first_name": "Marnie", "last_name": "Frey", "age": "—",
     "anonymised": False, "reliability": "CONFIRMED", "source": "cbc-verdict",
     "life": {"fr": {"headline": "La déclaration d'un père",
                     "items": [
                         {"label": "Disparue", "text": "Downtown Eastside, début des années 2000."},
                         {"label": "Ce que son père a demandé à la cour", "text": "Lors de la sentencing de décembre 2007, son père a déclaré au juge que la peine maximale lui apportait du réconfort pour sa famille — et qu'il était heureux que l'accusé soit resté silencieux devant la cour."},
                         {"label": "Verdict", "text": "Condamnation à deux chefs de meurtre au second degré le 9 décembre 2007."}],
                     "note": "Cette citation est reproduite telle qu'elle a été rapportée par CBC News, avec le nom du père, Rick Frey. Elle montre que, dans cette salle, la parole des familles a été la dernière audition."},
              "en": {"headline": "A father's statement",
                     "items": [
                         {"label": "Disappeared", "text": "Downtown Eastside, early 2000s."},
                         {"label": "What her father asked the court", "text": "At the December 2007 sentencing, her father told the judge that the maximum sentence brought relief to his family — and that he was glad the accused had stayed silent before the court."},
                         {"label": "Verdict", "text": "Convicted on two counts of second-degree murder on 9 December 2007."}],
                     "note": "This quote is reproduced as reported by CBC News, with the father's name, Rick Frey. It shows that in that courtroom, the families' voices were the last heard."}}},

    {"order": 4, "first_name": "Georgina", "last_name": "Faith Papin", "age": "—",
     "anonymised": False, "reliability": "CONFIRMED", "source": "cbc-verdict",
     "life": {"fr": {"headline": "Enoch Cree First Nation",
                     "items": [
                         {"label": "Origine", "text": "Membre de l'Enoch Cree First Nation, près d'Edmonton, en Alberta."},
                         {"label": "Disparue", "text": "Vancouver, Downtown Eastside, début des années 2000. Elle avait quitté sa communauté et sa famille pour une autre province."},
                         {"label": "Après la condamnation", "text": "En 2024, la fille de Georgina Papin, Kristina Bateman, se exprime encore publiquement : « Je veux que ce soit complètement clos, et j'ai le sentiment que… toute la vérité n'est pas encore sortie. »"},
                         {"label": "Verdict", "text": "Condamnation à deux chefs de meurtre au second degré le 9 décembre 2007."}],
                     "note": "Georgina Papin illustre un trajet documenté dans le rapport de la Commission : partir de sa communauté pour un emploi dans une autre province, et disparaître ensuite dans un quartier où personne ne connaissait son nom."},
              "en": {"headline": "Enoch Cree First Nation",
                     "items": [
                         {"label": "Origin", "text": "A member of Enoch Cree First Nation, near Edmonton, Alberta."},
                         {"label": "Disappeared", "text": "Vancouver, Downtown Eastside, early 2000s. She had left her community and family for work in another province."},
                         {"label": "After the conviction", "text": "In 2024, Georgina Papin's daughter, Kristina Bateman, still speaks publicly: 'I want to feel like it's completely closed, and I have a feeling… the whole truth is not out yet.'"},
                         {"label": "Verdict", "text": "Convicted on two counts of second-degree murder on 9 December 2007."}],
                     "note": "Georgina Papin illustrates a documented path in the Commission's report: leaving one's community for work in another province, then disappearing in a neighbourhood where nobody knew one's name."}}},

    {"order": 5, "first_name": "Brenda", "last_name": "Wolfe", "age": "—",
     "anonymised": False, "reliability": "CONFIRMED", "source": "cbc-verdict",
     "life": {"fr": {"headline": "Une identité reconnue tardivement",
                     "items": [
                         {"label": "Disparue", "text": "Downtown Eastside, début des années 2000."},
                         {"label": "Son nom n'apparaît sur la liste publique qu'en 2003", "text": "La quatrième affiche de femmes disparues, publiée en avril 2003, est la première à faire figurer son nom — avec celui de Mona Wilson. Les familles avaient fourni des noms que la police n'avait pas encore rendus publics."},
                         {"label": "Verdict", "text": "Condamnation à deux chefs de meurtre au second degré le 9 décembre 2007."}],
                     "note": "Le délai entre la disparition, la fourniture du nom par la famille et sa publication sur une affiche publique fait partie des constats de la Commission d'enquête."},
              "en": {"headline": "A late-recognised identity",
                     "items": [
                         {"label": "Disappeared", "text": "Downtown Eastside, early 2000s."},
                         {"label": "Her name only appeared on the public list in 2003", "text": "The fourth missing women poster, released in April 2003, is the first to carry her name — along with Mona Wilson's. Families had supplied names police had not yet made public."},
                         {"label": "Verdict", "text": "Convicted on two counts of second-degree murder on 9 December 2007."}],
                     "note": "The gap between a disappearance, the family's supply of a name, and its publication on a public poster is among the findings of the Commission of Inquiry."}}},

    # --- Les femmes liées sans avoir été jugées -------------------------
    {"order": 6, "first_name": "Vingt femmes", "last_name": "— accusées, jamais jugées", "age": "—",
     "anonymised": True, "reliability": "CONFIRMED", "source": "tgm-timeline",
     "life": {"fr": {"headline": "Vingt accusations écartées en une journée",
                     "items": [
                         {"label": "Fait", "text": "Le 4 août 2010, après la confirmation de la condamnation par la Cour suprême du Canada, la Cour suprême de Colombie-Britannique suspend les vingt chefs de meurtre au premier degré restants. Motif déclaré : des condamnations supplémentaires n'augmenteraient pas la peine déjà maximale."},
                         {"label": "Conséquence", "text": "Ces vingt femmes n'ont jamais été jugées. Aucune de leurs familles n'a obtenu de verdict. Le règlement civil de 2014 ne les couvre pas : il porte sur les enfants des femmes disparues, dans le cadre de l'enquête sur les enquêtes."},
                         {"label": "Point de désaccord", "text": "Cette décision a été contestée publiquement par Cameron Ward, avocat de vingt-cinq familles : « Quand ils ont suspendu les vingt chefs sur nos filles, nous étions en colère et déçus que ces filles ne verront jamais leur jour en justice. »"}],
                     "note": "Conformément à la règle éditoriale, aucun de ces vingt noms n'est isolé ici. Le rapport de la Commission les documente individuellement ; cette application n'en fait pas une galerie."},
              "en": {"headline": "Twenty charges dropped in a single day",
                     "items": [
                         {"label": "Fact", "text": "On 4 August 2010, after the Supreme Court of Canada confirmed the conviction, the British Columbia Supreme Court stayed the twenty remaining first-degree murder counts. Stated reason: further convictions would not increase the maximum sentence already imposed."},
                         {"label": "Consequence", "text": "These twenty women were never tried. Not one of their families obtained a verdict. The 2014 civil settlement does not cover them: it concerns the children of missing women, within the inquiry into the investigations."},
                         {"label": "Point of disagreement", "text": "This decision was publicly contested by Cameron Ward, counsel to twenty-five families: 'When they stayed the 20 charges on our girls, we were angry and disappointed that these girls would never see their day in court.'"}],
                     "note": "In line with the editorial rule, none of these twenty names is singled out here. The Commission's report documents them individually; this application does not make a gallery of them."}}},

    {"order": 7, "first_name": "Trente-trois femmes", "last_name": "— ADN ou restes retrouvés sur la ferme", "age": "—",
     "anonymised": True, "reliability": "CONFIRMED", "source": "reuters-death",
     "life": {"fr": {"headline": "Ce que la science a établi, et que le droit n'a pas suivi",
                     "items": [
                         {"label": "Fait", "text": "Des restes humains partiels ou des profils ADN de 33 femmes ont été retrouvés sur la propriété de Port Coquitlam et dans des casiers de rangement hors site. Ce chiffre est donné de façon cohérente par la GRC, la presse et la Cour suprême du Canada."},
                         {"label": "L'écart avec la justice", "text": "Vingt-six femmes ont été mises en accusation, six condamnées, vingt accusations suspendues. L'ADN ne préjuge pas du fait : il relie. C'est la procédure, pas la preuve, qui a arrêté le décompte."},
                         {"label": "Le plea bargaining n'existe pas comme institution", "text": "L'affaire a été jugée sans marché de plaidoirie, contrairement à plusieurs dossiers nord-américains comparables. Le procès a duré onze mois et la cour a été entièrementGRAM réaménagée pour être entendue."}],
                     "note": "Ce chiffre de 33 est un fait d'enquête, pas un verdict. Aucune de ces femmes n'a été déclarée morte sur le plan judiciaire autrement que par l'identification de ses restes ou de son ADN."},
              "en": {"headline": "What science established, and what law did not follow",
                     "items": [
                         {"label": "Fact", "text": "Partial human remains or DNA profiles of 33 women were found on the Port Coquitlam property and in off-site storage lockers. This figure is given consistently by the RCMP, the press and the Supreme Court of Canada."},
                         {"label": "The gap with justice", "text": "Twenty-six women were charged, six convicted, twenty charges stayed. DNA does not prejudge the fact: it connects. It was procedure, not evidence, that stopped the count."},
                         {"label": "There is no plea bargaining as an institution", "text": "The case was tried without a plea bargain, unlike several comparable North American files. The trial lasted eleven months and the courtroom was fully rebuilt to be heard."}],
                     "note": "This figure of 33 is an investigative fact, not a verdict. None of these women was judicially declared dead other than through the identification of her remains or DNA."}}},

    {"order": 8, "first_name": "Les femmes disparues", "last_name": "— les autres, celles dont personne n'a compté", "age": "—",
     "anonymised": True, "reliability": "CONFIRMED", "source": "forsaken-vol4",
     "life": {"fr": {"headline": "Plus de soixante-cinq noms",
                     "items": [
                         {"label": "Périmètre", "text": "La Commission d'enquête a travaillé sur les enquêtes visant les femmes signalées disparues du Downtown Eastside entre le 23 janvier 1997 et le 5 février 2002, et son mandat portait sur plus de 65 femmes disparues et assassinées."},
                         {"label": "Première de la liste", "text": "Lillian Jean O'Dare, vue pour la dernière fois le 12 septembre 1978, est la première femme inscrite sur la liste publique des femmes disparues. La liste s'est agrandie pendant plus de vingt ans."},
                         {"label": "Le point le plus important", "text": "Le rapport de la Commission est explicite : certaines de ces femmes ont été assassinées par des personnes inconnues, et les auteurs sont probablement toujours en liberté. Cette affaire n'est pas une histoire close."},
                         {"label": "Hors périmètre", "text": "Des femmes de l'entièreté de la province ont disparu, y compris sur la route de l'Hostie — l'ancienne « Highway of Tears » en Colombie-Britannique. Le rapport documente ce cadre plus large sans en faire l'objet de sa mission principale."}],
                     "note": "Cette entrée représente toutes les femmes qui n'ont pas de fiche individuelle ici. Elle n'est pas un groupe : ce sont des personnes dont l'histoire reste ouverte."},
              "en": {"headline": "More than sixty-five names",
                     "items": [
                         {"label": "Scope", "text": "The Commission of Inquiry worked on the investigations into women reported missing from the Downtown Eastside between 23 January 1997 and 5 February 2002, and its mandate covered more than 65 missing and murdered women."},
                         {"label": "First on the list", "text": "Lillian Jean O'Dare, last seen on 12 September 1978, is the first woman on the public missing women list. The list grew for more than twenty years."},
                         {"label": "The most important point", "text": "The Commission's report is explicit: some of these women were murdered by unknown persons, and the killers are probably still at large. This case is not a closed story."},
                         {"label": "Outside the scope", "text": "Women disappeared across the province, including along what is Highway 16 in British Columbia, formerly known as the Highway of Tears. The report documents this wider frame without making it the core of its mandate."}],
                     "note": "This entry stands for all the women who have no individual file here. It is not a group: these are people whose story remains open."}}},
]

MEMORIAL = {
    "title": txt("Le rapport concluait par un mot : « Nobodies ». Le titre du volume II était « des personnes sans nom ».",
                 "The report ended on a word: 'Nobodies'. Volume II was titled after people with no name."),
    "biography": txt(
        "Entre 1978 et le début des années 2000, au moins 65 femmes ont disparu du Downtown Eastside de "
        "Vancouver, le secteur postal le plus pauvre du pays. La Commission d'enquête de 2012 aexaminé les enquêtes "
        "menées sur ces disparitions et conclu qu'elles constituaient « une défaillance manifeste », aggravée par un "
        "biais systémique. Le titre du volume central du rapport, Nobodies, a été choisi pour dire ce que ces femmes "
        "étaient devenues dans le fonctionnement des institutions : personne en particulier. Six d'entre elles ont "
        "été jugées. Vingt autres accusations ont été suspendues. Les familles des autres n'ont jamais su ce qu'il "
        "était advenu.",
        "Between 1978 and the early 2000s, at least 65 women disappeared from Vancouver's Downtown Eastside, the "
        "country's poorest postal code. The 2012 Commission of Inquiry examined the investigations into those "
        "disappearances and concluded they were a 'blatant failure', compounded by systemic bias. The central "
        "volume of the report was titled Nobodies, to say what these women had become inside institutions: nobody in "
        "particular. Six of them were tried. Twenty further charges were stayed. The families of the others never "
        "learned what happened."),
    "testimony": txt(
        "« Cette commission a échoué à découvrir les vraies raisons pour lesquelles une pareille "
        "tragédie a pu se produire », et exactement comment il se fait que le système de justice criminelle a "
        "complètement manqué de ces femmes et de leurs familles. » — Cameron Ward, avocat de 25 familles, dans ses "
        "conclusions finales devant la Commission, le 4 juin 2012. (Citation tronquée : le compte rendu de "
        "presse ne donne pas le prénom de l'oratrice.)",
        "'This commission has failed to uncover the true reasons why this enormous tragedy was allowed to happen and "
        "exactly how it was that the criminal justice system utterly failed these women and their families.' — "
        "Cameron Ward, counsel to 25 families, in final submissions before the Commission, 4 June 2012. (Quote "
        "truncated: the published account does not give the speaker's first name."),
    "memory": txt(
        "Le rapport de la Commission porte la date du 19 novembre 2012. Wally Oppal le remet au gouvernement "
        "provincial le 23 novembre. Il n'est rendu public que le 17 décembre. Entre la signature et la "
        "publication, il y a un mois — et pendant ce mois, les familles qui attendaient depuis trois ans une "
        "explication en sont encore sans. Ce décalage n'a rien d'un détail administratif : c'est la mesure exacte "
        "de ce qu'une administration fait du temps qu'on lui demande de comprendre.",
        "The Commission's report is dated 19 November 2012. Wally Oppal hands it to the provincial government on "
        "23 November. It is not made public until 17 December. Between signature and publication there is a month "
        "— and during that month, the families who had been waiting three years for an explanation are still "
        "without one. That gap is not an administrative detail: it measures exactly what an administration does "
        "with the time it is given to understand."),
}
TIMELINE = [
    fact("Lillian Jean O'Dare est vue pour la dernière fois le 12 septembre 1978. Elle est la première femme "
         "inscrite sur la liste publique des femmes disparues du Downtown Eastside.",
         "Lillian Jean O'Dare is last seen on 12 September 1978. She is the first woman on the public list of "
         "missing women from the Downtown Eastside.",
         "CONFIRMED", "vsun-timeline", "Premier nom de la liste", "First name on the list", "1978-09-12"),
    fact("Robert William Pickton, né le 24 octobre 1949 à Port Coquitlam, travaille comme chauffeur et possède "
         "avec ses frères une exploitation porcine à Port Coquitlam, à l'est de Vancouver. Il ouvre également, "
         "dans des locauxSans autorisation, un atelier de découpe et d'abattage destiné à la vente.",
         "Robert William Pickton, born 24 October 1949 in Port Coquitlam, worked as a truck driver and owned a pig "
         "farm at Port Coquitlam, east of Vancouver, with his brothers. He also ran an unlicensed slaughterhouse and "
         "cutting facility selling to local shops.",
         "CONFIRMED", "reuters-death", "L'exploitation et les hommes qui la tiennent", "The farm and the men who ran it", "1949-10-24"),
    fact("Des femmes Commencent à disparaître du Downtown Eastside. Selon l'Encyclopédie canadienne, au moins 65 "
         "femmes y seront signalées disparues entre 1978 et 2001.",
         "Women begin to disappear from the Downtown Eastside. According to the Canadian Encyclopedia, at least 65 "
         "women will be reported missing there between 1978 and 2001.",
         "CONFIRMED", "tce", "La série commence", "The series begins", "1978-2001"),
    fact("Le 23 mars 1997, une agression contre une femme dans la propriété de Port Coquitlam survit à ses "
         "blessures. Elle est désignée « Ms Anderson » dans les rapports de la Commission, sous une interdiction de "
         "publication : son nom n'est pas public et cette application ne le publie pas. Un message d'alerte est "
         "diffusé auxdetachements de la région le 29 mars 1997, indiquant que l'homme visé doit être considéré "
         "comme un danger pour les travailleuses du sexe.",
         "On 23 March 1997, an attack against a woman at the Port Coquitlam property leaves her alive. She is "
         "referred to as 'Ms Anderson' in the Commission's reports, under a publication ban: her name is not public "
         "and this application does not publish it. An advisory message is sent to detachments across the region on "
         "29 March 1997, stating that the man in question should be considered a danger to sex trade workers.",
         "CONFIRMED", "forsaken-vol4", "La première fois qu'un signal est émis", "The first time a signal is raised", "1997-03-23"),
    fact("Le 1er avril 1997, Pickton est arrêté et inculpé de tentative de meurtre, voies de fait avec_Ida_, "
         "détention illégale et coups et blessures aggravés. Il comparaît à sa demande de libération le "
         "8 avril 1997 et obtient sa liberté. Un procès est fixé du 2 au 6 février 1998.",
         "On 1 April 1997, Pickton is arrested and charged with attempted murder, assault with a weapon, unlawful "
         "confinement and aggravated assault. He appears on his bail application on 8 April 1997 and is released. A "
         "trial is set for 2 to 6 February 1998.",
         "CONFIRMED", "forsaken-es", "Quatre chefs d'accusation", "Four charges", "1997-04-01"),
    fact("Un homme lié à l'entreprise de démolition de Pickton transmet à la police, en 1998, un enregistrement "
         "audio dans lequel il rapporte que toutes les femmes qui disparaissent, tous les sacs à main et les pièces "
         "d'identité retrouvés dans la roulotte de Pickton, sont un motif d'inquiétude. Selon The Province, il "
         "affirme que Pickton avait déjà été libéré des accusations de 1997.",
         "In 1998, a man connected to Pickton's salvage company gives police an audio recording in which he says "
         "that all the women going missing, all the purses and IDs found in Pickton's trailer, are cause for "
         "concern. According to The Province, he states that Pickton had already been released on the 1997 charges.",
         "CONFIRMED", "forsaken-vol1", "Un signal enregistré", "A recorded warning", "1998"),
    fact("La Division des poursuites pénales de la Colombie-Britannique suspend la procédure le 26 ou le 27 janvier "
         "1998 — le rapport de la Commission mentionne les deux dates selon le volume. Le motif déclaré : la "
         "procureure Randi Connor jugeait la victime trop atteinte par sa dépendance pour être un témoin fiable, "
         "conclusion tirée d'une seule rencontre, moins de deux semaines avant le procès.",
         "The British Columbia Criminal Justice Branch enters a stay of proceedings on 26 or 27 January 1998 — the "
         "Commission's report gives both dates depending on the volume. The stated reason: Crown counsel Randi "
         "Connor considered the victim too impaired by her dependency to be a reliable witness, a conclusion drawn "
         "from a single meeting held less than two weeks before trial.",
         "CONFIRMED", "forsaken-es", "La décision de surseoir", "The stay decision", "1998-01-26"),
    fact("Un avis de données personnelles effacées disparaît du dossier, puis est retrouvé en 2004 : les vêtements "
         "et les bottes saisis en 1997 contenaient l'ADN de deux femmes disparues. Le rapport Oppal compte "
         "l'absence d'analyse de ce matériel parmi les erreurs de l'enquête.",
         "A personal property record goes missing from the file and is recovered in 2004: the clothing and boots "
         "seized in 1997 carried the DNA of two missing women. The Oppal report counts the failure to test this "
         "material among the investigation's errors.",
         "CONFIRMED", "forsaken-vol2b", "Des analyses qui n'ont pas eu lieu", "Analyses that did not happen", "1997-2004"),
    fact("La police de Vancouver identifie Robert Pickton comme personne d'intérêt pour des disparitions en "
         "1998. Le chef d'enquête qui a dirigé l'enquête a déclaré après le verdict que la justice n'avait pas "
         "entièrement été rendue parce qu'il aurait dû être condamné pour meurtre au premier degré.",
         "In 1998, Vancouver Police identify Robert Pickton as a person of interest in the disappearances. The "
         "lead investigator who ran the investigation said after the verdict that justice had not been fully "
         "served because he should have been convicted of first-degree murder.",
         "CONFIRMED", "cbc-inquiry", "Un suspect nommé", "A named suspect", "1998"),
    fact("Une affiche publique énumérant des femmes disparues du Downtown Eastside est publiée en 2001. D'autres "
         "suivront en février 2002, en avril 2003 et en octobre 2004 : la dernière énumère 69 noms.",
         "A public poster listing women missing from the Downtown Eastside is released in 2001. Others follow in "
         "February 2002, April 2003 and October 2004: the last lists 69 names.",
         "CONFIRMED", "forsaken-vol1", "La liste qui s'allonge", "The list that grows", "2001-2004"),
    fact("Le 4 décembre 2001, la force de tarefa mixte police- GRC déclare que 45 femmes sont disparues.",
         "On 4 December 2001, the joint VPD-RCMP task force states that 45 women are missing.",
         "CONFIRMED", "vsun-timeline", "Un décompte officiel", "An official count", "2001-12-04"),
    fact("Le 5 février 2002, des policiers de la force de tarefa Evenhanded exécutent un mandat contre la "
         "ferme de Port Coquitlam à la recherche d'armes à feu illégales. Ils y trouvent des effets personnels "
         "appartenant à des femmes disparues, dont un inhalateur d'asthme.",
         "On 5 February 2002, officers from the Project Evenhanded task force execute a search warrant at the "
         "Port Coquitlam farm looking for illegal firearms. They recover personal effects belonging to missing "
         "women, including an asthma inhaler.",
         "CONFIRMED", "tgm-charged", "La fouille", "The search", "2002-02-05"),
    fact("Le 22 février 2002, Robert Pickton, 52 ans, est arrêté à Surrey et inculpé de deux chefs de meurtre au "
         "premier degré, dans les affaires de Sereena Abotsway et Mona Wilson.",
         "On 22 February 2002, Robert Pickton, aged 52, is arrested in Surrey and charged with two counts of "
         "first-degree murder, in the cases of Sereena Abotsway and Mona Wilson.",
         "CONFIRMED", "tce", "Arrestation", "Arrest", "2002-02-22"),
    fact("Un avis sanitaire est émis à l'adresse des voisins ayant acheté de la viande de la ferme, en raison d'un "
         "risque de contamination. La fouille devient la plus vaste scène de crime jamais traitée au Canada.",
         "A public health advisory is issued to neighbours who bought meat from the farm because of a contamination "
         "risk. The search becomes the largest crime scene ever processed in Canada.",
         "CONFIRMED", "cbc-timeline", "Un risque sanitaire déclaré", "A declared health risk", "2002"),
    fact("En 18 mois, lesassentoulements fouillent 383 000 verges cubes de terre et saisissent plus de 600 000 "
         "objets. Des restes humains partiels et de l'ADN appartenant à 33 femmes sont mis au jour.",
         "Over 18 months, teams sift 383,000 cubic yards of soil and seize more than 600,000 items. Partial human "
         "remains and DNA belonging to 33 women are brought to light.",
         "CONFIRMED", "hashilthsa", "La plus grande scène de crime du pays", "The largest crime scene in the country", "2002-2003"),
    fact("Trois profils ADN non identifiés sont transmis au laboratoire. Ils ne sont jamais rattachés à un nom, "
         "comme tant d'autres dans cette affaire.",
         "Three unidentified DNA profiles are referred to the laboratory. They are never matched to a name, like so "
         "many others in this case.",
         "CONFIRMED", "guardian-trial", "Trois noms qui resteront inconnus", "Three names that will remain unknown", "2002"),
    fact("Deux ans plus tard, Pickton déclare à un codétenu infiltré par la GRC avoir tué 49 femmes et regretter "
         "de ne pas en avoir tué une de plus, pour atteindre un nombre rond. Il précise qu'il commençait à être "
         "« brouillon ». Aucune de ces déclarations n'a jamais été vérifiée.",
         "Two years later, Pickton tells an RCMP-planted cellmate that he killed 49 women and regrets not having "
         "killed one more, to reach a round number. He adds that he was starting to get 'sloppy'. None of these "
         "statements has ever been verified.",
         "PROBABLE", "tgm-timeline", "Une déclaration non vérifiée", "An unverified statement", "2002"),
    fact("Robert Pickton est reconnu formellement par un témoin d'une agression de 1997 devant la Cour. Le juge "
         "lui demande s'il a tué 49 personnes ; il répond : « Non, cette homme est sur cette photo, et je suis "
         "Robert Pickton. »",
         "Robert Pickton is formally identified by a witness to a 1997 attack before the Court. The judge asks him "
         "whether he killed 49 people; he answers: 'No, that man is in this photo, and I am Robert Pickton.'",
         "CONFIRMED", "cbc-verdict", "L'identification formelle", "The formal identification", "2007"),
    fact("Le 22 janvier 2007 s'ouvre à New Westminster le procès de six chefs de meurtre au premier degré. Il est "
         "entièrement GRAM réaménagé pour être entendu, et durera onze mois avec soixante-dix-sept décisions "
         "judiciaires rendues.",
         "On 22 January 2007, the trial on six counts of first-degree murder opens in New Westminster. It is fully "
         "rebuilt to be heard and lasts eleven months, with seventy-seven judicial rulings issued.",
         "CONFIRMED", "cbc-timeline", "Onze mois de procès", "Eleven months of trial", "2007-01-22"),
    fact("Le 9 décembre 2007, après dix jours de délibération, le jury le déclare coupable de six chefs de meurtre "
         "au second degré — et non de meurtre au premier degré, comme l'accusation l'avait government's. Les "
         "familles craignent alors que le verdict soit fragile.",
         "On 9 December 2007, after ten days of deliberation, the jury finds him guilty on six counts of "
         "second-degree murder — not first-degree, as charged. The families worry at that point that the verdict is "
         "fragile.",
         "CONFIRMED", "cbc-verdict", "Le verdict", "The verdict", "2007-12-09"),
    fact("Le 11 décembre 2007, le juge James Williams prononce six peines de réclusion à perpétuité, exécutées "
         "conjointement, avec une inéligibilité à la libération conditionnelle pendant vingt-cinq ans, le maximum "
         "possible. Il a écouté dix-huit déclarations d'impact des victimes. Sa formulation est retenue ici mot pour "
         "mot : « La conduite de M. Pickton était meurtrière, et de façon répétée. »",
         "On 11 December 2007, Justice James Williams imposes six concurrent life sentences with a 25-year "
         "parole-ineligibility period, the maximum possible. He has heard eighteen victim impact statements. His "
         "wording is kept here verbatim: 'Mr. Pickton's conduct was murderous and repeatedly so.'",
         "CONFIRMED", "cbc-verdict", "La peine", "The sentence", "2007-12-11"),
    fact("Le 25 juin 2009, la Cour d'appel de la Colombie-Britannique rejette l'appel de la défense à la "
         "majorité, estimant qu'un nouveau procès sur les vingt chefs restantes imposerait « deEEP exigences "
         "énormes » aux ressources financières et judiciaires.",
         "On 25 June 2009, the British Columbia Court of Appeal dismisses the defence appeal by a majority, "
         "holding that a new trial on the twenty remaining counts would impose 'further enormous demands on "
         "financial and judicial resources'.",
         "CONFIRMED", "tgm-timeline", "Appel rejeté", "Appeal dismissed", "2009-06-25"),
    fact("Le 30 juillet 2010, la Cour suprême du Canada rejette l'appel à l'unanimité : « preuve accablante », "
         "« ni erreur de droit, ni déni de justice ».",
         "On 30 July 2010, the Supreme Court of Canada unanimously dismisses the appeal: 'overwhelming evidence', "
         "'neither a legal error nor a miscarriage of justice'.",
         "CONFIRMED", "cbc-scc", "Le dernier recours", "The last appeal", "2010-07-30"),
    fact("Le 4 août 2010, la Cour suprême de la province suspend les vingt chefs de meurtre au premier degré "
         "restants. Le procureur général de la Couronne, Melissa Gillespie, déclare que ces condamnations "
         "n'augmenteraient pas la peine déjà subie.",
         "On 4 August 2010, the provincial Supreme Court stays the twenty remaining first-degree murder counts. "
         "Crown prosecutor Melissa Gillespie states that further convictions would not increase the sentence "
         "already being served.",
         "CONFIRMED", "tgm-timeline", "Vingt femmes sans procès", "Twenty women without trial", "2010-08-04"),
    fact("En novembre 2009, la police de Vancouver soutient publiquement, pour la première fois, la tenue d'une "
         "enquête publique. En septembre 2010, Wally Oppal est nommé à sa tête.",
         "In November 2009, Vancouver Police publicly support a public inquiry for the first time. In September "
         "2010, Wally Oppal is appointed to lead it.",
         "CONFIRMED", "vsun-timeline", "L'enquête qui viendra", "The inquiry that would come", "2009-2010"),
    fact("Le 11 octobre 2011 s'ouvre la Commission d'enquête sur les femmes disparues et assassinées. Les familles "
         "sont représentées par Cameron Ward, qui commence par parler de la façon dont la police a « balayé » leurs "
         "plaintes.",
         "On 11 October 2011, the Missing Women Commission of Inquiry opens. The families are represented by Cameron "
         "Ward, who begins by speaking of the way police 'brushed off' their complaints.",
         "CONFIRMED", "vsun-timeline", "Les audiences publiques", "The public hearings", "2011-10-11"),
    fact("Le 19 novembre 2012, le rapport de 1 445 pages est achevé. Le 23 novembre 2012, Wally Oppal le remet au "
         "gouvernement provincial. Le 17 décembre 2012, il est rendu public. Il conclut que les enquêtes ont été "
         "« une défaillance manifeste » et formule 63 recommandations et deux mesures urgentes.",
         "On 19 November 2012, the 1,445-page report is completed. On 23 November 2012, Wally Oppal hands it to the "
         "provincial government. On 17 December 2012, it is made public. It concludes that the investigations were a "
         "'blatant failure' and makes 63 recommendations and two urgent measures.",
         "CONFIRMED", "forsaken-es", "Forsaken", "Forsaken", "2012-12-17"),
    fact("En 2013, des ChiesaPreuve des enfants de femmes disparues AVCidentPrononce l'action civile contre la "
         "province de la Colombie-Britannique, la ville de Vancouver et la GRC.",
         "In 2013, the children of missing women file civil action against the province of British Columbia, the "
         "City of Vancouver and the RCMP.",
         "CONFIRMED", "cbc-civil", "La voie civile", "The civil path", "2013"),
    fact("Le 18 mars 2014, un fonds de 4,9 millions de dollars est annoncé : jusqu'à 98 enfants de femmes disparues "
         "et assassinées le partageront, à raison de 50 000 dollars chacun. La répartition est de 40 % fédéral, "
         "40 % provincial, 20 % municipal, sans reconnaissance de responsabilité.",
         "On 18 March 2014, a $4.9 million fund is announced: up to 98 children of missing and murdered women will "
         "share it, at $50,000 each. Split 40% federal, 40% provincial, 20% municipal, without admission of "
         "liability.",
         "CONFIRMED", "star-fund", "Ce que la justice civile a donné", "What civil justice provided", "2014-03-18"),
    fact("En 2019, l'Enquête nationale sur les femmes et filles autochtones assassinées et disparues publie son "
         "rapport final, Reclaiming Power and Place, avec 231 appels à la justice. Elle conclut que la violence "
         "décrite « constitue un génocide fondé sur la race ». En 2024, l'Assemblée des Premières Nations estime "
         "qu'il y a peu de progrès : de « minime à aucun » sur la majorité des appels.",
         "In 2019, the National Inquiry into Missing and Murdered Indigenous Women and Girls publishes its final "
         "report, Reclaiming Power and Place, with 231 calls for justice. It concludes that the violence described "
         "'amounts to a race-based genocide of Indigenous Peoples'. In 2024, the Assembly of First Nations assesses "
         "there is 'minimal to no' progress on the majority of the calls.",
         "CONFIRMED", "afn-mmiwg", "La suite nationale", "The national sequel", "2019-2024"),
    fact("En juin 2024, la police de Vancouver demande l'autorisation de détruire environ 14 000 objets saisis sur "
         "la ferme, dont une petite partie serait restituée aux familles. Quarante groupes et personnes s'y "
         "opposent, au motif que ces objets pourraient encore servir dans des actions civiles. En avril 2026, la "
         "Cour suprême refuse de surseoir à cette procédure.",
         "In June 2024, Vancouver Police apply to be allowed to dispose of about 14,000 items seized from the farm, "
         "a small portion of which would be returned to families. Forty groups and individuals oppose, on the "
         "grounds that the items could still be used in civil actions.",
         "CONFIRMED", "vsun-evidence", "La dernière bataille judiciaire", "The last legal battle", "2024-2026"),
    fact("Le 19 mai 2024, Robert Pickton est agressé par un codétenu à l'établissement de sécurité maximale Port-"
         "Cartier, au Québec. Il est héliporté dans un hôpital de Québec. Le 31 mai 2024, il y meurt, à 74 ans. La "
         "prison fédérale confirme avoir prévenu sa famille et les familles de victimes enregistrées.",
         "On 19 May 2024, Robert Pickton is assaulted by a fellow inmate at Port-Cartier maximum security "
         "Institution, Quebec. He is airlifted to a Quebec City hospital. On 31 May 2024, he dies there, aged 74. "
         "Correctional Service Canada confirms it notified his family and the families of registered victims.",
         "CONFIRMED", "apntn-death", "La fin", "The end", "2024-05-31"),
    fact("Le 3 juillet 2025, un codétenu de 52 ans est accusé de meurtre au premier degré dans la mort de Robert "
         "Pickton. Cette application ne commente pas l'accusé et ne traite cette information que comme la suite "
         "procédurale d'un fait documenté.",
         "On 3 July 2025, a 52-year-old fellow inmate is charged with first-degree murder in the death of Robert "
         "Pickton. This application does not comment on the accused and treats this information only as the "
         "procedural sequel to a documented fact.",
         "CONFIRMED", "cbc-death-charge", "La suite procédurale", "The procedural sequel", "2025-07-03"),
]

LOCATIONS = [
    {"kind": "region", "names": txt("Downtown Eastside, Vancouver (Colombie-Britannique)",
                                    "Downtown Eastside, Vancouver (British Columbia)"),
     "city": "Vancouver", "region": "British Columbia", "country": "CA",
     "lat": 49.2800, "lon": -123.1000, "precision": "approximate", "date": "1978-2002",
     "note": txt("Le « code postal le plus pauvre du pays ». C'est ici que les femmes vivaient, travaillaient et "
                 "disparaissaient. La carte n'affiche jamais une adresse : le rapport de la Commission insiste sur "
                 "la précision de l'échelle pour ne pas exposer les survivantes.",
                 "The 'poorest postal code in the country'. This is where the women lived, worked and disappeared. "
                 "The map never displays an address: the Commission's report stresses scale precision so as not to "
                 "expose survivors."),
     "reliability": "CONFIRMED", "source": "forsaken-vol1"},

    {"kind": "scene", "names": txt("La ferme porcine de Port Coquitlam (commune, échelle d'agglomération)",
                                    "The Port Coquitlam pig farm (commune, settlement scale)"),
     "city": "Port Coquitlam", "region": "British Columbia", "country": "CA",
     "lat": 49.2560, "lon": -122.7620, "precision": "approximate", "date": "2002-2024",
     "note": txt("Lieu de la découverte, à environ 25 km à l'est du centre de Vancouver. Conformément aux règles "
                 "éditoriales, aucune adresse exacte n'est publiée.",
                 "Place of the discovery, about 25 km east of downtown Vancouver. In line with the editorial rules, "
                 "no exact address is published."),
     "reliability": "CONFIRMED", "source": "reuters-death"},

    {"kind": "scene", "names": txt("Les locaux de stockage hors site (échelle régionale uniquement)",
                                    "The off-site storage lockers (regional scale only)"),
     "city": "", "region": "Metro Vancouver", "country": "CA",
     "lat": 49.2500, "lon": -122.8000, "precision": "region", "date": "1997-2003",
     "note": txt("Des éléments à conviction ont été conservés hors site, dont les vêtements et les bottes saisis "
                 "en 1997, analysés seulement en 2004.",
                 "Exhibit material was held off site, including the clothing and boots seized in 1997 and only "
                 "tested in 2004."),
     "reliability": "CONFIRMED", "source": "forsaken-vol2b"},

    {"kind": "court", "names": txt("Tribunal de New Westminster (bureau du juge de première instance)",
                                   "New Westminster courthouse (Supreme Court)"),
     "city": "New Westminster", "region": "British Columbia", "country": "CA",
     "lat": 49.1867, "lon": -122.8475, "precision": "city", "date": "2007-12-11",
     "note": txt("Salle d'audience du procès de 2007, entièrement réaménagée pour la durée de l'audience, "
                 "entièrement réaménagée pour la durée de l'audience.",
                 "Courtroom of the 2007 trial, fully rebuilt for the duration of the hearing."),
     "reliability": "CONFIRMED", "source": "cbc-verdict"},

    {"kind": "city", "names": txt("Surrey (Colombie-Britannique)", "Surrey (British Columbia)"),
     "city": "Surrey", "region": "British Columbia", "country": "CA",
     "lat": 49.1917, "lon": -122.9560, "precision": "city", "date": "2002-02-22",
     "note": txt("Lieu de l'arrestation, dans l'une des entreprises de l'exploitation.",
                 "Place of the arrest, at one of the farm's businesses."),
     "reliability": "CONFIRMED", "source": "cbc-timeline"},

    {"kind": "scene", "names": txt("Port-Cartier, Québec (établissement fédéral de sécurité maximale)",
                                   "Port-Cartier, Quebec (federal maximum security institution)"),
     "city": "Port-Cartier", "region": "Quebec", "country": "CA",
     "lat": 49.0217, "lon": -67.3822, "precision": "city", "date": "2024-05-19",
     "note": txt("L'établissement où il a été agressé le 19 mai 2024, transporté à l'hôpital, puis décédé le "
                 "31 mai 2024. Cette information n'est publiée que parce qu'elle met fin au parcours judiciaire et "
                 "qu'elle a été confirmée par le Service correctionnel du Canada.",
                 "The institution where he was assaulted on 19 May 2024, transported to hospital, and died on 31 May "
                 "2024. This is published only because it ends the judicial course and was confirmed by "
                 "Correctional Service Canada."),
     "reliability": "CONFIRMED", "source": "apntn-death"},
]

EVIDENCE = [
    {"kind": "dna", "weight": "decisive", "reliability": "CONFIRMED", "source": "hashilthsa",
     "title": txt("L'ADN de 33 femmes sur la propriété", "The DNA of 33 women on the property"),
     "description": txt(
         "Des restes humains partiels et des profils ADN de 33 femmes ont été retrouvés sur la ferme de Port "
         "Coquitlam et dans des casiers de rangement hors site. Ce chiffre est celui desusuaires nonempty give par "
         "la GRC, par la Cour suprême du Canada et par la presse internationale. Il ne préjuge pas du fait : il "
         "établit un lien matériel. Vingt-six femmes ont été mises en accusation, six condamnées, vingt "
         "accusations suspendues. L'écart entre 33 et 6 est l'objet même de ce dossier.",
         "Partial human remains and DNA profiles of 33 women were found on the Port Coquitlam farm and in off-site "
         "storage lockers. This figure is the one given by the RCMP, by the Supreme Court of Canada and by the "
         "international press. It does not prejudge the fact: it establishes a material link. Twenty-six women were "
         "charged, six convicted, twenty charges stayed. The gap between 33 and 6 is the very object of this "
         "dossier.")},

    {"kind": "physical", "weight": "supporting", "reliability": "CONFIRMED", "source": "forsaken-vol1",
     "title": txt("Un inhalateur d'asthme au nom de Sereena Abotsway",
                 "An asthma inhaler bearing Sereena Abotsway's name"),
     "description": txt(
         "C'est l'objet qui a fait le lien entre la propriété et une femme portée disparue. Il a été trouvé lors "
         "de la fouille de février 2002, menée à la recherche d'armes à feu illégales, et non à la recherche de "
         "victimes. La différence de motif est celle qui a geographies la différence de calendrier : l'enquête a "
         "commencé par autre chose.",
         "This is the item that linked the property to a reported missing woman. It was found during the February "
         "2002 search, carried out looking for illegal firearms, not for victims. The difference of purpose is what "
         "explains the difference of calendar: the investigation started from something else.")},

    {"kind": "dna", "weight": "decisive", "reliability": "CONFIRMED", "source": "forsaken-vol2b",
     "title": txt("Les vêtements et les bottes de 1997, analysés en 2004",
                 "The clothing and boots from 1997, tested in 2004"),
     "description": txt(
         "Les vêtements et les bottes portés lors de l'agression de mars 1997 ont été saisis puis conservés dans "
         "un casier de la GRC. Le rapport de la Commission note qu'un dossier de propriété personnelle a disparu, "
         "et que le matériel n'a pas été analysé avant 2004 — année où il s'est révélé porter l'ADN de deux femmes "
         "disparues. Sept ans de délai entre une saisie et une analyse de routine.",
         "The clothing and boots worn during the March 1997 assault were seized and then held in an RCMP locker. "
         "The Commission's report notes that a personal property record went missing, and that the material was not "
         "tested before 2004 — the year it proved to carry the DNA of two missing women. Seven years between a "
         "seizure and a routine test.")},

    {"kind": "documentary", "weight": "documented", "reliability": "PROBABLE", "source": "tgm-timeline",
     "title": txt("La déclaration des 49 victimes", "The statement of 49 victims"),
     "description": txt(
         "En 2002, Pickton déclare à un codétenu infiltré par la GRC avoir tué 49 femmes et vouloir en tuer une "
         "cinquantième. Cette déclaration n'a jamais été vérifiée : aucun des 49 faits n'a été établi, et la "
         "majorité n'a jamais été rattachée à un nom. Elle est conservée ici au niveau PROBABLE, et non "
         "CONFIRMED, précisément parce qu'elle est la partie la plus répétable de l'affaire.",
         "In 2002, Pickton tells an RCMP-planted cellmate that he killed 49 women and wanted to kill a fiftieth. "
         "This statement has never been verified: none of the 49 offences was established, and most were never "
         "matched to a name. It is kept here at PROBABLE level, not CONFIRMED, precisely because it is the most "
         "repeatable part of the case.")},

    {"kind": "documentary", "weight": "documented", "reliability": "DISPUTED", "source": "forsaken-es",
     "title": txt("L'absence de stratégie de protection des femmes du Downtown Eastside",
                 "The absence of a protection strategy for Downtown Eastside women"),
     "description": txt(
         "Le rapport conclut que la première trace d'une stratégie destinée à protéger ces femmes vulnerabilities "
         "date de 2002, quelques semaines avant l'arrestation. Les représentants de la défense d'un service de police "
         "ont contesté ces conclusions en audience. L'écart entre le constat de la Commission et les arguments de "
         "la défense est reproduit ici tel quel, non lissé.",
         "The report concludes that the first trace of a strategy to protect these vulnerable women dates from 2002, "
         "weeks before the arrest. Counsel for one police service contested these conclusions at the hearings. The "
         "gap between the Commission's finding and the police service's arguments is reproduced here as it stands, "
         "unsmoothed.")},
]

INVESTIGATION = {
    "steps": [
        {"n": 1, "date": "1978-1996", "title": txt("Des disparitions sans rapprochement",
                                                   "Disappearances without a link"),
         "body": txt("Des femmes disparaissent du Downtown Eastside. Aucune enquête ne rassemble les signalements, "
                     "ne les rapproche, et ne cherche si elles n'ont pas un dénominateur commun. La police de "
                     "Vancouver ne crée pas d'unité dédiée. Le rapport de la Commission en fera un constat "
                     "central en 2012.",
                     "Women disappear from the Downtown Eastside. No investigation pools the reports, links them, or "
                     "asks whether they share a common denominator. Vancouver Police do not create a dedicated unit. "
                     "The Commission's report makes this a central finding in 2012."),
         "reliability": "CONFIRMED", "source": "forsaken-vol2b", "premium": False},

        {"n": 2, "date": "1997-03-29", "title": txt("Un avis envoyé, un danger nommé",
                                                    "An advisory sent, a danger named"),
         "body": txt("Le 29 mars 1997, un message d'alerte est diffusé à tous les détachements du Bas-Fraser : "
                     "l'homme impliqué dans l'agression de mars 1997 doit être considéré comme un danger pour les "
                     "travailleuses du sexe. Cet avis crée un lien explicite entre une agression et une population "
                     "à risque. C'est le moment le plus net de la période documentée où le risque a été nommé "
                     "officiellement, et il ne sera suivi d'aucune stratégie de protection de cette population.",
                     "On 29 March 1997, an advisory message is sent to every detachment in the Lower Mainland: the "
                     "man involved in the March 1997 assault should be considered a danger to sex trade workers. "
                     "This advisory creates an explicit link between an assault and an at-risk population. It is the "
                     "clearest moment in the documented period when the risk was officially named, and it will not "
                     "be followed by any protection strategy for that population."),
         "reliability": "CONFIRMED", "source": "forsaken-es", "premium": False},

        {"n": 3, "date": "1997-04-01", "title": txt("Quatre chefs, une liberté",
                                                    "Four charges, one release"),
         "body": txt("Pickton est arrêté et inculpé de tentative de meurtre, voies de fait avec_Ida_, détention "
                     "illégale et coups et blessures aggravés. Le 8 avril 1997, il obtient sa liberté. La Cour "
                     "d'appel de la province notera par la suite que la libération lui a permis de reprendre "
                     "ses activités.",
                     "Pickton is arrested and charged with attempted murder, assault with a weapon, unlawful "
                     "confinement and aggravated assault. On 8 April 1997 he is released. The provincial Court of "
                     "Appeal will later note that the release allowed him to resume his activities."),
         "reliability": "CONFIRMED", "source": "forsaken-es", "premium": False},

        {"n": 4, "date": "1998-01-26", "title": txt("La décision de surseoir",
                                                    "The stay decision"),
         "body": txt("La Division des poursuites pénales suspend la procédure, motivée par l'estimation que la "
                     "victime était trop atteinte par sa dépendance pour constituer un témoin fiable. La "
                     "Commission d'enquête — saisie du cadre juridique qui l'a produite — refuse d'en commenter le "
                     "bien-fondé en vertu du principe d'indépendance du parquet, et écrit noir sur blanc que cette "
                     "décision est inexplicable à la lumière de ce qui a été appris ensuite. Dix-neuf femmes "
                     "liées à la ferme de Pickton ont disparu dans les années qui ont suivi la suspension.",
                     "The Criminal Justice Branch stays the proceedings, on the stated basis that the victim was too "
                     "impaired by her dependency to be a reliable witness. The Commission of Inquiry — bound by the "
                     "legal framework governing it — declines to comment on its merits under the principle of "
                     "prosecutorial independence, and states plainly that in light of what was learned afterwards "
                     "the decision is inexplicable. Nineteen women later linked to Pickton's farm went missing in "
                     "the years that followed."),
         "reliability": "CONFIRMED", "source": "forsaken-vol2b", "premium": True},

        {"n": 5, "date": "1998-2001", "title": txt("Un nom sur une liste, une exploitation dans le dossier",
                                                    "A name on a list, a farm in the file"),
         "body": txt("Un homme lié à l'entreprise de démolition de Pickton transmet en 1998 un enregistrement audio "
                     "où il relie explicitement les disparues, les sacs à main et les pièces d'identité trouvés "
                     "dans la roulotte. Pickton est identifié comme personne d'intérêt. La police de Vancouver a "
                     "parfois enquêté sur la ferme à propos d'infractions de zonage, sans jamais la relier aux "
                     "disparues. Deux ensembles de faits coexistent dans le système sans jamais se rencontrer.",
                     "In 1998, a man connected to Pickton's salvage company passes police an audio recording in "
                     "which he explicitly links the missing women to the purses and IDs found in the trailer. "
                     "Pickton is identified as a person of interest. Vancouver Police sometimes investigated the farm "
                     "over zoning offences without ever linking it to the disappearances. Two sets of facts coexisted "
                     "in the system without ever meeting."),
         "reliability": "CONFIRMED", "source": "forsaken-vol1", "premium": True},

        {"n": 6, "date": "2001-12-04", "title": txt("Un décompte officiel, une liste publique",
                                                    "An official count, a public list"),
         "body": txt("Le 4 décembre 2001, la force de tarefa mixte déclare que 45 femmes sont disparues. Des "
                     "affiches publiques énumèrent les noms et les photographies, se réactualisant d'année en "
                     "année jusqu'en 2004, où la liste atteint 69 entrées. C'est un acte de la police, rendu "
                     "public, qui rend visibles des femmes que les avaient rendues invisibles.",
                     "On 4 December 2001, the joint task force states that 45 women are missing. Public posters list "
                     "names and photographs, updated year after year until 2004, when the list reaches 69 entries. "
                     "It is an act by the police, made public, that rendered visible women that the police had made "
                     "invisible."),
         "reliability": "CONFIRMED", "source": "forsaken-vol1", "premium": False},

        {"n": 7, "date": "2002-02-05", "title": txt("La fouille menée pour une autre raison",
                                                    "A search carried out for another reason"),
         "body": txt("Le mandat exécuté sur la ferme de Port Coquitlam porte sur des armes à feu illégales. Les "
                     "objets personnels qui y sont trouvés ne sont pas un but de l'enquête : ce sont les indices "
                     "d'une autre. Le rapport de la Commission note que l'enquête sur les disparues aurait dû "
                     "commencer plus tôt, de quinze ans.",
                     "The warrant executed at the Port Coquitlam farm concerns illegal firearms. The personal "
                     "effects found there are not the point of the search: they are the clues of another one. The "
                     "Commission's report notes that the missing women investigation should have started fifteen "
                     "years earlier."),
         "reliability": "CONFIRMED", "source": "cbc-inquiry", "premium": False},

        {"n": 8, "date": "2002-02-22", "title": txt("Arrestation", "Arrest"),
         "body": txt("Robert Pickton, 52 ans, est arrêté à Surrey et inculpé de deux chefs de meurtre au premier "
                     "degré, dans les affaires de Sereena Abotsway et Mona Wilson. Vingt-quatre autres chefs "
                     "suivront au fil des mois, pour un total de vingt-six mises en accusation.",
                     "Robert Pickton, aged 52, is arrested in Surrey and charged with two counts of first-degree "
                     "murder, in the cases of Sereena Abotsway and Mona Wilson. Twenty-four further counts follow "
                     "over the following months, for a total of twenty-six charges."),
         "reliability": "CONFIRMED", "source": "tce", "premium": False},

        {"n": 9, "date": "2002-2003", "title": txt("Dix-huit mois de fouille", "Eighteen months of searching"),
         "body": txt("Les équipes tamisent 383 000 verges cubes de terre et saisissent plus de 600 000 objets. Des "
                     "archéologues, des biologistes, des toxicologues et des chimistes travaillent sur place. Les "
                     "méthodes de récupération mises au point après le site du World Trade Center influencent la "
                     "conduite de cette fouille, qui devient la plus vaste scène de crime traitée au Canada. Un "
                     "avis sanitaire est émis à destination des voisins ayant acheté de la viande de la ferme.",
                     "Teams sift 383,000 cubic yards of soil and seize more than 600,000 items. Archaeologists, "
                     "biologists, toxicologists and chemists work on site. Recovery methods developed after the World "
                     "Trade Center site influence how this search is run, making it the largest crime scene "
                     "processed in Canada. A public health advisory is issued to neighbours who bought meat from "
                     "the farm."),
         "reliability": "CONFIRMED", "source": "hashilthsa", "premium": False},

        {"n": 10, "date": "2002", "title": txt("La déclaration au codétenu", "The statement to the cellmate"),
         "body": txt("En 2002, Pickton déclare à un inmate infiltré par la GRC avoir tué 49 femmes et vouloir en "
                     "tuer une de plus. Cette déclaration n'a jamais été vérifiée. Elle est le seul élément "
                     "documenté qui donne un ordre de grandeur supérieur à celui des preuves matérielles, et c'est "
                     "pour cela qu'elle doit être lue avec la plus grande prudence.",
                     "In 2002, Pickton tells an RCMP-planted cellmate that he killed 49 women and wanted to kill one "
                     "more. This statement was never verified. It is the only documented element giving a magnitude "
                     "greater than the physical evidence, which is why it must be read with the greatest caution."),
         "reliability": "PROBABLE", "source": "cbc-scc", "premium": True},

        {"n": 11, "date": "2007-01-22", "title": txt("Onze mois de procès", "Eleven months of trial"),
         "body": txt("Le procès s'ouvre à New Westminster sur six chefs de meurtre au premier degré. Le parquet "
                     "prouve que Pickton a tué les six femmes, pratiqué le découpage, et éliminé les restes. La "
                     "défense présente un homme sans sophistication verbale, et suggère qu'un autre aurait pu être "
                     "le maître d'œuvre. Soixante-dix-sept décisions judiciaires sont rendues pendant "
                     "l'audience.",
                     "The trial opens in New Westminster on six counts of first-degree murder. The Crown argues that "
                     "Pickton killed the six women, dismembered them, and disposed of the remains. The defence "
                     "presents a man without verbal sophistication and suggests someone else may have been the "
                     "mastermind. Seventy-seven judicial rulings are issued during the hearing."),
         "reliability": "CONFIRMED", "source": "cbc-timeline", "premium": False},

        {"n": 12, "date": "2007-12-09", "title": txt("Le verdict, et ce qu'il ne dit pas",
                                                    "The verdict, and what it does not say"),
         "body": txt("Le jury déclare Pickton coupable de six chefs de meurtre au second degré, et non de premier "
                     "degré. La Cour d'appel de la province et la Cour suprême du CanadaEstimated ensuite que ce "
                     "verdict était improbable au vu de la preuve. Le juge de première instance, à la sentencing, "
                     "prononce le maximum de twenty-cinq ans d'inéligibilité, « parce que ce cas est unique ».",
                     "The jury finds Pickton guilty on six counts of second-degree murder, not first-degree. The "
                     "provincial Court of Appeal and the Supreme Court of Canada then found the verdict implausible "
                     "given the evidence. At sentencing, the trial judge imposes the maximum twenty-five-year "
                     "parole-ineligibility period, 'because this case is unique'."),
         "reliability": "DISPUTED", "source": "cbc-verdict", "premium": True},

        {"n": 13, "date": "2010-08-04", "title": txt("Vingt accusations suspendues", "Twenty charges stayed"),
         "body": txt("Le parquet déclare que de nouvelles condamnations ne pourraient pas augmenter la peine "
                     "déjà maximale. Le juge de première instance suspend les vingt chefs restants. La Cour "
                     "d'appel avait déjà estimé qu'un nouveau procès imposerait des exigences « énormes » aux "
                     "ressources judiciaires. Vingt femmes n'ont jamais été jugées.",
                     "The Crown states that further convictions could not increase the sentence already being served. "
                     "The trial judge stays the twenty remaining counts. The Court of Appeal had already found that a "
                     "new trial would impose 'enormous' demands on judicial resources. Twenty women were never "
                     "tried."),
         "reliability": "CONFIRMED", "source": "tgm-timeline", "premium": True},

        {"n": 14, "date": "2011-2012", "title": txt("Une enquête qui n'a pas vu les preuves",
                                                    "An inquiry that did not see the evidence"),
         "body": txt("La Commission d'enquête examine les enquêtes sur les disparues et la décision de surseoir. "
                     "Avocat de vingt-cinq familles, Cameron Ward, dénonce une « enquête sans les preuves ». "
                     "Le rapport final conclut à une « défaillance manifeste » et formule 63 recommandations.",
                     "The Commission of Inquiry examines the missing women investigations and the stay decision. "
                     "Cameron Ward, counsel to twenty-five families, denounces an 'inquiry without the evidence'. The "
                     "final report finds a 'blatant failure' and makes 63 recommendations."),
         "reliability": "CONFIRMED", "source": "tgm-families", "premium": False},
    ],
    "reality": txt(
        "L'enquête a abouti parce qu'un mandat a été exécuté pour une autre raison. Le 5 février 2002, la police "
        "cherchait des armes à feu illégales sur une ferme porcine ; ce qu'elle a trouvé était le lien entre trente-trois "
        "femmes et une propriété. Tout ce qui a suivi — la plus vaste scène de crime de l'histoire canadienne, un "
        "procès de onze mois, une enquête publique de 1 445 pages, un rapport de 63 recommandations — procède de ce "
        "hasard. Aucune de ces étapes n'a été le produit d'une stratégie visant les femmes disparues.",
        "The investigation succeeded because a warrant was executed for another reason. On 5 February 2002, police "
        "were looking for illegal firearms on a pig farm; what they found was the link between thirty-three women and "
        "a property. Everything that followed — the largest crime scene in Canadian history, an eleven-month trial, a "
        "1,445-page public inquiry, a report with 63 recommendations — follows from that accident. Not one of these "
        "steps was the product of a strategy aimed at the missing women."),
    "errors": [
        item("Le lien entre l'agression de 1997 et les disparues n'a pas été tiré en 1997 ni en 1998. Un avis "
             "officiel déclarait pourtant l'homme dangereux pour les travailleuses du sexe dès le 29 mars 1997.",
             "The link between the 1997 assault and the disappearances was not drawn in 1997 or 1998. Yet an official "
             "advisory had declared the man a danger to sex trade workers on 29 March 1997.",
             "CONFIRMED", "forsaken-es", "Lien non tiré", "Link not drawn"),
        item("La décision de surseoir du 26-27 janvier 1998 a reposé sur une appréciation de la crédibilité d'une "
             "témoin, motivée par sa dépendance. La même femme a témoigné en 2003. Vingt ans plus tard, son nom "
             "reste interdit de publication.",
             "The stay decision of 26-27 January 1998 rested on an assessment of a witness's credibility, motivated "
             "by her dependency. The same woman testified in 2003. Twenty years later, her name remains under a "
             "publication ban.",
             "CONFIRMED", "tgm-families", "Détermination qui n'a pas été réévaluée",
             "An assessment that was never revisited"),
        item("Le matériel saisi en 1997 — vêtements, bottes — n'a pas été analysé avant 2004, lorsqu'il s'est "
             "révélé porter l'ADN de deux femmes disparues. Sept ans de délai sur une analyse de routine.",
             "Material seized in 1997 — clothing, boots — was not tested before 2004, when it proved to carry the DNA "
             "of two missing women. Seven years' delay on a routine test.",
             "CONFIRMED", "forsaken-vol2b", "Preuve non exploitée", "Evidence left untested"),
        item("Un dossier de propriété personnelle a disparu des dossiers au sujet des objets saisis en 1997, et a "
             "été retrouvé des années plus tard.",
             "A personal property record went missing from the files on the items seized in 1997, and was recovered "
             "years later.",
             "CONFIRMED", "forsaken-vol2b", "Dossier égaré", "A missing file"),
        item("Aucune gestion de dossier majeur n'a été appliquée à une enquête qui comptait plus de soixante-dix "
             "victimes potentielles et deux services de police involved. La coordination entre la police de "
             "Vancouver et la GRC de Coquitlam a échoué sur la question même de la compétence.",
             "No major case management was applied to an investigation involving more than seventy potential victims "
             "and two police services. Coordination between the Vancouver Police Department and the Coquitlam RCMP "
             "failed on the very question of jurisdiction.",
             "CONFIRMED", "cbc-inquiry", "Pas de gestion de dossier majeur", "No major case management"),
        item("La police de Vancouver et la GRC ont toutes deux contesté les conclusions de la Commission en "
             "audience, et nié toute culture de biais. L'écart entre le constat d'enquête et ces contestations est "
             "reproduit ici sans être tranché.",
             "Both the Vancouver Police Department and the RCMP contested the Commission's conclusions at the "
             "hearings, denying any culture of bias. The gap between the inquiry finding and these challenges is "
             "reproduced here without being adjudicated.",
             "DISPUTED", "cbc-inquiry", "Contestation non tranchée", "An unresolved challenge"),
    ],
    "cold_case": txt(
        "Ce dossier n'est pas un cold case au sens classique : l'auteur est identified, les restes sont retrouvés, "
        "le procès a eu lieu. Ce qui reste froid, ce sont les noms. Trente-trois femmes ont été reliées à la "
        "propriété ; trois profils ADN sont restés non identifiés ; aucune famille n'a obtenu la certitude de ce "
        "qu'il était advenu de la femme qu'elle avait perdue. L'affaire est résolue au sens du droit et ouverte au "
        "sens de la mémoire.",
        "This file is not a cold case in the classical sense: the author is identified, the remains are found, the "
        "trial took place. What remains cold are the names. Thirty-three women were linked to the property; three DNA "
        "profiles stayed unidentified; no family obtained certainty about what happened to the woman they had lost. "
        "The case is resolved in law and open in memory."),
}

PSYCHOLOGY = {
    "disclaimer": txt("Aucun diagnostic n'est posé. Aucun examen psychiatrique intégral n'a été rendu public. "
                      "Les éléments ci-dessous proviennent des sources citées et sont distincts du reste.",
                      "No diagnosis is made. No full psychiatric evaluation has been made public. The elements "
                      "below come from the cited sources and are kept separate from the rest."),
    "blocks": [
        block("fact", "Ce qui a été demandé en 1997 et pourquoi", "What was asked in 1997 and why",
              "Un témoin a demandé en 1997 si Robert Pickton était « un fanatique de la torture ». La question "
              "n'est pas reprise ici comme une catégorie ; elle est rapportée parce qu'elle figure au compte rendu "
              "du procès et parce qu'elle illustre comment un jury a été conduit à recevoir une certaine "
              "description. Aucune conclusion clinique n'en découle.",
              "A witness asked in 1997 whether Robert Pickton was 'a torture fanatic'. The question is not repeated "
              "here as a category; it is reported because it appears in the trial record and because it illustrates "
              "how a jury was led to receive a certain description. No clinical conclusion follows from it.",
              "CONFIRMED", "forsaken-es"),

        block("fact", "Un homme d'une vivirie aërée", "A man with an outward life",
              "Éleveur porcin, entrepreneur, il présentait une façade d cemadan. Après sa condamnation, un livre "
              "qu'il aurait écrit en prison a été retiré de la vente en 2016, moins de deux heures après sa mise en "
              "vente, en raison d'une protestation publique. Le service correctionnel du Canada a indiqué qu'il "
              "n'avait pas terminé son livre dans les règles de sécurité pénitentiaire.",
              "A pig farmer, a businessman, he presented an outward facade. After his conviction, a book he is said "
              "to have written in prison was withdrawn from sale in 2016, less than two hours after it went on sale, "
              "amid public outcry. Correctional Service Canada said it did not comply with prison security rules.",
              "CONFIRMED", "tgm-timeline"),

        block("analysis", "Ce que la littérature scientifique ne permet pas ici",
              "What the scientific literature does not allow here",
              "La littérature sur les tueurs en série s'intéresse au recoupement entre analyse "
              "comportementale et preuve. Cette affaire illustre une limite : le dossier behavioral a été construit "
              "par desFAREd facteurs de contexte — sa profession, son accès à la propriété, sa réputation locale — "
              "plutôt que par des traces de scène. Le rapport d'enquête le dit autrement : ce n'est pas un problème "
              "de lecture du comportement, c'est un problème de nonexécution de l'enquête.",
              "The literature on serial killers focuses on the match between behavioural analysis and evidence. This "
              "case illustrates a limit: the behavioural file was built from contextual factors — his trade, his "
              "access to the property, his local standing — rather than from scene traces. The inquiry report says "
              "it differently: this is not a problem of reading behaviour, it is a problem of not running the "
              "investigation.",
              "CONFIRMED", "forsaken-vol2b"),

        block("unknown", "Ce qui n'est pas documenté", "What is not documented",
              "Aucune expertise psychiatrique, aucune évaluation de risque de récidive, aucun rapport d'observation "
              "clinique n'apparaît dans les sources consultées. Cette application n'en invente pas.",
              "No psychiatric evaluation, no recidivism risk assessment, and no clinical observation report appears "
              "in the sources consulted. This application does not invent any.",
              "UNKNOWN", None),
    ],
}

VICTIMOLOGY = {
    "ethics_note": txt("Aucune caractéristique des victimes n'explique moralement les crimes. Le rapport de la "
                       "Commission d'enquête porte sur des conditions de vie et des défaillances institutionnelles, "
                       "jamais sur une responsabilité des femmes. Cette distinction est la ligne éditoriale de ce "
                       "dossier.",
                       "No characteristic of the victims morally explains the crimes. The Commission of Inquiry "
                       "report concerns living conditions and institutional failures, never any responsibility of the "
                       "women. That distinction is the editorial line of this dossier."),
    "blocks": [
        block("context", "Un quartier décrit comme « le code postal le plus pauvre du pays »",
              "A neighbourhood described as 'the poorest postal code in the country'",
              "Le rapport d'enquête décrit le Downtown Eastside en termes de logement grossièrement inadapté, "
              "insécurité alimentaire, inégalités sanitaires, pauvreté extrême et dépendance aux drogues. Ces "
              "conditions ne causent aucun crime. Elles déterminent qui, en cas de disparition, sera cherché avec "
              "la même urgence — et qui ne le sera pas.",
              "The inquiry report describes the Downtown Eastside in terms of grossly inadequate housing, food "
              "insecurity, health inequalities, extreme poverty and drug dependency. These conditions cause no "
              "crime. They determine who, in the event of a disappearance, is searched for with the same urgency — "
              "and who is not.",
              "CONFIRMED", "forsaken-vol1"),

        block("vulnerability", "Une vulnérabilité produite, pas héritée",
              "A vulnerability produced, not inherited",
              "Le rapport identifie des facteurs situationnels documentés : logement inadapté, absence de "
              "transports, éloignement des services, conditions préjudiciables, dépendance. La Commission documente un "
              "ensemble de vulnérabilités qui sont des produits de politiques publiques. Elle ne formule aucune "
              "thèse qui rendrait ces femmes responsables.",
              "The report identifies documented situational factors: inadequate housing, lack of transport, distance "
              "from services, prejudicial conditions, dependency. The Commission documents a set of vulnerabilities "
              "that are products of public policy. It formulates no thesis making these women responsible.",
              "CONFIRMED", "forsaken-vol1"),

        block("analysis", "Le biais systémique : une conclusion d'enquête, pas une opinion",
              "Systemic bias: an inquiry finding, not an opinion",
              "La conclusion « j'ai conclu qu'il existait un biais systémique de la police » figure dans le "
              "sommaire du rapport de la Commission. Le rapport précise que trouver un biais systémique ne signifie "
              "pas que la police ne se souciait pas de ces femmes. Cette nuance est conservée : elle fait partie "
              "de la conclusion elle-même.",
              "The conclusion 'I have concluded that there was systemic bias by the police' appears in the summary "
              "of the Commission's report. The report specifies that finding systemic bias does not mean police did "
              "not care about these women. That nuance is kept: it is part of the finding itself.",
              "CONFIRMED", "forsaken-vol2b"),

        block("analysis", "Les familles, premier témoin du système",
              "Families, the system's first witness",
              "Dans l'affaire Anderson, la pièce à conviction matérielle a été constituée par un témoin extérieur, un "
              "homme lié à l'entreprise de démolition de Pickton, qui a enregistré sesconcerns en 1998 et s'est vu "
              "renvoyer. Cameron Ward, pour vingt-cinq familles, a déclaré que la police avait donné aux familles "
              "un « accueil expéditif » lorsqu'elles sont venues signaler une disparition. Le signal le plus tôt "
              "n'est pas venu d'une institution.",
              "In the Anderson matter, the material evidence was assembled by an outside witness — a man connected to "
              "Pickton's salvage company who recorded his concerns in 1998 and was sent away. Cameron Ward, for "
              "twenty-five families, said police gave families a 'brush off' when they came to report a "
              "disappearance. The earliest signal did not come from an institution.",
              "CONFIRMED", "tgm-families"),

        block("memory", "Trois signalements qui sont des noms",
              "Three testimonies that are names",
              "Lillian Jean O'Dare, première femme de la liste publique, vue pour la dernière fois le 12 septembre "
              "1978. Stephanie Lane, 20 ans, signalée disparue en 1997, dont l'ADN a été retrouvé sur la ferme et "
              "qui n'a jamais été accusée. Richard « Kellie » Little, la première personne transgenre à figurer sur "
              "une affiche publique de femmes disparues de la police de Vancouver, en 2003. Trois noms pour "
              "rappeler que chaque ligne de cette liste était une personne.",
              "Lillian Jean O'Dare, the first woman on the public list, last seen 12 September 1978. Stephanie Lane, "
              "20, reported missing in 1997, whose DNA was found on the farm and who was never charged. Richard "
              "'Kellie' Little, the first transgender person to appear on a Vancouver Police public missing women "
              "poster, in 2003. Three names to remind us that every line on that list was a person.",
              "CONFIRMED", "cbc-lane"),

        block("unknown", "Ce que la justice n'a pas rendu", "What justice did not return",
              "Vingt femmes ont été mises en accusation et n'ont pas été jugées. Des familles n'ont jamais su ce "
              "qu'il était advenu. Trois profils ADN n'ont jamais été rattachés à un nom. Ces lignes ne sont pas "
              "des zones d'ombre du dossier : ce sont des personnes dont l'histoire reste ouverte, et la question "
              "qui les concerne n'est pasriminal « qui a tué » mais « où est la preuve ».",
              "Twenty women were charged and never tried. Families never learned what happened. Three DNA profiles "
              "were never matched to a name. These are not shadows in the file: they are people whose story remains "
              "open, and the question that concerns them is not 'who killed' but 'where is the evidence'.",
              "CONFIRMED", "hashilthsa"),
    ],
}

COURT = {
    "jurisdiction": txt("Canada — Cour suprême de la Colombie-Britannique, New Westminster ; appel devant la Cour "
                        "d'appel de la province puis la Cour suprême du Canada",
                        "Canada — Supreme Court of British Columbia, New Westminster; appeal to the provincial Court "
                        "of Appeal and then the Supreme Court of Canada"),
    "verdict": txt("Culpabilité le 9 décembre 2007 sur six chefs de meurtre au second degré, après que le jury eut "
                   "refusé la qualification de meurtre au premier degré retenue par l'accusation.",
                   "Guilty on 9 December 2007 on six counts of second-degree murder, after the jury declined the "
                   "first-degree murder charge brought by the prosecution."),
    "sentence": {
        "label": txt("Six peines de réclusion à perpétuité, exécutées conjointement, avec une inéligibilité à la "
                     "libération conditionnelle pendant vingt-cinq ans",
                     "Six life sentences, served concurrently, with a twenty-five year parole-ineligibility period"),
        "pronounced": "2007-12-11",
        "requested": txt("Le parquet a réclamé le maximum de vingt-cinq ans, qui rendrait la peine équivalente à "
                         "celle d'un meurtre au premier degré. La défense sollicitait une période de quinze à vingt "
                         "ans.",
                         "The Crown sought the maximum of twenty-five years, which would make the sentence equivalent "
                         "to that for first-degree murder. The defence sought a period of fifteen to twenty years."),
        "cumul": txt("Le juge aMotifmotivation de retenir le maximum en expliquant que ce cas est unique : six "
                     "condamnations distinctes, sur une période étendue, avec une conduiteHide post-"
                     "offensive d occultation pendant des années.",
                     "The judge gave his reason for imposing the maximum by explaining that this case is unique: six "
                     "distinct convictions, over an extended period, with post-offence conduct aimed at concealment "
                     "over years."),
        "reasoning": txt("« La conduite de M. Pickton était meurtrière, et de façon répétée. » Le juge a ensuite "
                         "dit qu'il ne pouvait pas connaître les détails, mais qu'il savait ce qui s'était passé : "
                         "« c'était insensée etigned laiso, » a-t-il déclaré aux familles. Dix-huit déclarations "
                         "d'impact des victimes ont été lues avant la décision.",
                         "'Mr. Pickton's conduct was murderous and repeatedly so.' The judge then said he could not "
                         "know the details, but that he knew what happened: 'what happened to them was senseless and "
                         "despicable,' he told the families. Eighteen victim impact statements were read before the "
                         "decision."),
        "appeal": txt("Appel de la défense rejeté par la Cour d'appel de la province le 25 juin 2009 (majorité). "
                      "Appel rejeté à l'unanimité par la Cour suprême du Canada le 30 juillet 2010 : « preuve "
                      "accablante », « ni erreur de droit, ni déni de justice ». Le 4 août 2010, les vingt chefs de "
                      "meurtre au premier degré restants sont suspendus.",
                      "The defence appeal was dismissed by the provincial Court of Appeal on 25 June 2009 (majority). "
                      "The appeal was unanimously dismissed by the Supreme Court of Canada on 30 July 2010: "
                      "'overwhelming evidence', 'neither a legal error nor a miscarriage of justice'. On 4 August "
                      "2010, the twenty remaining first-degree murder counts were stayed."),
        "reliability": "DISPUTED", "source": "cbc-verdict",
    },
    "consequences": [
        item("Vingt accusations suspendues, vingt femmes jamais jugées. L'accusation avait été que la peine était "
             "déjà maximale. Les familles des vingt femmes concernées ont contesté ce dispositif.",
             "Twenty charges stayed, twenty women never tried. The prosecution argued the sentence was already "
             "maximal. The families of those twenty women contested this framing.",
             "CONFIRMED", "tgm-families"),
        item("Un rapport d'enquête de 1 445 pages, 63 recommandations et deux mesures urgentes. Le rapport conclut "
             "à une « défaillance manifeste » des enquêtes et à un biais systémique.",
             "A 1,445-page inquiry report, 63 recommendations and two urgent measures. The report finds a 'blatant "
             "failure' of the investigations and systemic bias.",
             "CONFIRMED", "forsaken-es"),
        item("Les excuses publiques de la police de Vancouver et de la GRC. La police de Vancouver a répété "
             "l'excuse : elle regrettait de ne pas avoir agi plus tôt.",
             "The public apologies of the Vancouver Police Department and the RCMP. Vancouver Police repeated the "
             "apology: it regretted not having acted sooner.",
             "CONFIRMED", "cbc-civil"),
        item("Un règlement civil de 2014 : 4,9 millions de dollars pour 98 enfants, 50 000 dollars chacun, sans "
             "reconnaissance de responsabilité. La loi de la province ne permet pas de réparer la perte d'une vie.",
             "A 2014 civil settlement: $4.9 million for 98 children, $50,000 each, without admission of liability. "
             "Provincial law does not permit compensation for the loss of a life.",
             "CONFIRMED", "star-fund"),
        item("La question de la destruction des preuves reste ouverte au-delà de la mort de l'accusé. Quarante "
             "groupes se sont opposés à la demande de la GRC, qui reste une procédure ouverte.",
             "The question of evidence disposal remains open beyond the death of the accused. Forty groups opposed "
             "the RCMP's application. In April 2026, the Court refused to stay the process.",
             "CONFIRMED", "vsun-evidence"),
    ],
}

EXPERTS = [
    {"label": txt("Lecture institutionnelle — la GRC sur sa propre fouille",
                  "Institutional reading — the RCMP on its own search"),
     "field": "forensic_science",
     "position": txt("La GRC a publié en 2024 un récit de sa propre investigation, dans lequel elle explique que "
                     "les méthodes de récupération développées après le site du World Trade Center ont eu « un "
                     "impact critique » sur la fouille de la ferme, et que l'inclusion de professionnels formés "
                     "hors du milieu judiciaire a été « la décision la plus déterminante ». Le lien entre ce que "
                     "ce que la presse appelait une « scène de crime » et ce que la GRC décrit comme un chantier "
                     "archéologique y est explicite.",
                     "In 2024 the RCMP published an account of its own investigation, explaining that recovery "
                     "methods developed after the World Trade Center site had a 'critical impact' on the farm "
                     "search, and that the inclusion of trained professionals from outside law enforcement was 'the "
                     "single most impactful decision'. The link between what the press called a 'crime scene' and "
                     "what the RCMP describes as an archaeological site is explicit.",
                     ),
     "reliability": "CONFIRMED", "source": "rcmp-gazette"},

    {"label": txt("Lecture d'enquête — le rapport de la Commission",
                  "Inquiry reading — the Commission's report"),
     "field": "judicial",
     "position": txt("Le commissaire Wally Oppal conclut que « l'initiation et la conduite des enquêtes sur les "
                     "femmes disparues et assassinées ont constitué une défaillance manifeste ». Il précise que "
                     "cette conclusion ne signifie pas que la police ne s'était pas intéressée à ces femmes, et "
                     "qu'au milieu des inadéquations systémiques, il y avait des policiersageddon individuals qui "
                     "ont reconnu la crise.",
                     "Commissioner Wally Oppal concludes that 'the initiation and conduct of the missing and "
                     "murdered women investigations were a blatant failure'. He specifies that this does not mean "
                     "police did not care about these women, and that amid the gross systemic inadequacies there "
                     "were individual police officers who acknowledged the crisis and strived.",
                     ),
     "reliability": "CONFIRMED", "source": "forsaken-es"},

    {"label": txt("Lecture victimologique — la condition autochtone",
                  "Victimological reading — the Indigenous dimension"),
     "field": "sociology",
     "position": txt("L'Enquête nationale sur les femmes et filles autochtones assassinées et disparues publie en "
                     "2019 un rapport final concluant que la violence décrite « constitue un génocide fondé sur la "
                     "race » et formule 231 appels à la justice. L'Assemblée des Premières Nations évalue en 2024 "
                     "la mise en œuvre de ces appels à « minime ou aucune » pour la majorité d'entre eux. Le lien "
                     "avec l'affaire Pickton est direct : ses victimes sont majoritairement autochtones, et la "
                     "Commission de 2012 documente la surreprésentation des femmes autochtones parmi les personnes "
                     "disparues.",
                     "The National Inquiry into Missing and Murdered Indigenous Women and Girls published a final "
                     "report in 2019 concluding that the violence described 'amounts to a race-based genocide' and "
                     "made 231 calls for justice. The Assembly of First Nations assessed in 2024 the implementation "
                     "of these calls as 'minimal to no' for the majority. The link to the Pickton case is direct: his "
                     "victims were predominantly Indigenous, and the 2012 Commission documents the "
                     "over-representation of Indigenous women among those who went missing.",
                     ),
     "reliability": "CONFIRMED", "source": "afn-mmiwg"},

    {"label": txt("Lecture critique — ce que le verdict a tranché",
                  "Critical reading — what the verdict settled"),
     "field": "judicial",
     "position": txt("Le jury a condamné pour meurtre au second degré, estimant implicitement que les faits n'étaient "
                     "ni planifiés ni délibérés. Le juge de première instance a rejeté cette lecture lors de la "
                     "sentencing, estimant le cas unique. La Cour d'appel et la Cour suprême ont considers que le "
                     "jury avait tort, sans pour autantabh że réformer les condamnations. Le désaccord sur la "
                     "qualification du crime reste l'un des points les moins résolus du dossier.",
                     "The jury convicted of second-degree murder, implicitly finding that the acts were neither "
                     "planned nor deliberate. The trial judge rejected that reading at sentencing, considering the "
                     "case unique. The Court of Appeal and the Supreme Court of Canada considered the jury to be "
                     "wrong, without reforming the convictions. The disagreement on how to characterise the crime "
                     "remains one of the least settled points in the file.",
                     ),
     "reliability": "DISPUTED", "source": "cbc-scc"},
]
EXPERTS_AGREEMENT = txt("Tous s'accordent sur un point : c'est une affaire systémique. La GRC, la Commission "
                        "d'enquête et l'Enquête nationale convergent sur le fait que l'absence de coordination, la "
                        "fragmentation et le manque de moyens ont produit un résultat, indépendamment de la "
                        "conduite d'un individu.",
                        "All agree on one point: this is a systemic case. The RCMP, the Commission of Inquiry and "
                        "the National Inquiry converge on the fact that lack of coordination, fragmentation and "
                        "insufficient resources produced the outcome, independently of any individual's conduct.")
EXPERTS_DISAGREEMENT = txt("Ils divergent sur la portée du mot « systémique ». La GRC et la police de Vancouver ont "
                           "contesté en audience que leur conduite ait été biaisée. La Commission d'enquête "
                           "conclut au contraire, et précise qu'un biais systémique ne signifie pas une absence "
                           "de préoccupation.",
                           "They differ on the scope of the word 'systemic'. The RCMP and Vancouver Police contested "
                           "before the inquiry that their conduct was biased. The Commission of Inquiry concluded "
                           "otherwise, and specifies that systemic bias does not mean a lack of concern.")
EXPERTS_UNCERTAIN = txt("Ce qui reste incertain : combien de femmes sont mortes, et lesquelles. Le chiffre de 33 "
                        "correspond à des restes ou de l'ADN, non à des personnes identifiées. Trois profils restent "
                        "sans nom.",
                        "What remains uncertain: how many women died, and which. The figure of 33 corresponds to "
                        "remains or DNA, not to identified people. Three profiles remain without a name.")

COUNTERFACTUALS = [
    counterfactual(
        "delay",
        "Et si la décision de surseoir n'avait pas été prise en janvier 1998 ?",
        "What if the stay decision had not been taken in January 1998?",
        "Le 26 ou 27 janvier 1998, la Division des poursuites pénales de la Colombie-Britannique suspend la "
        "procédure. Le 22 février 2002, Pickton est arrêté. Quatre ans et vingt-six jours séparent ces deux dates.",
        "On 26 or 27 January 1998, the British Columbia Criminal Justice Branch stays the proceedings. On 22 "
        "February 2002, Pickton is arrested. Four years and twenty-six days separate the two dates.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Décision de surseoir", "Stay decision"), "date": "1998-01-26"},
            "hypothesis": {"label": txt("Suspension de la procédure", "Proceedings stayed"), "date": "1998-01-26"},
            "scenario_event": {"label": txt("Arrestation", "Arrest"), "date": "2002-02-22"},
            "outcome_event": {"label": txt("Condamnation", "Conviction"), "date": "2007-12-09"},
            "actual_arrest": {"label": txt("Arrestation réelle", "Actual arrest"), "date": "2002-02-22"},
            "documented_offences_after": [
                {"date": "1998-09-20", "label": txt("Premier fait documenté rattaché à la ferme après la suspension",
                                                    "First documented event linked to the farm after the stay")},
            ],
            "jurisdiction_note": txt(
                "Le rapport de la Commission d'enquête compte dix-neuf femmes disparues dans les années qui ont "
                "suivi la suspension des accusations et ont été reliées à la ferme de Pickton ; un autre compte "
                "publié en 2003 en donne vingt-deux. Cet écart n'est pas lissé ici : il est affiché. Le moteur ne "
                "compte pas des vies, il mesure un intervalle. Ce qu'il ne peut pas établir, et qu'aucune source ne "
                "permet d'établir, c'est ce qu'un procès en février 1998 aurait produit. La Commission écrit "
                "elle-même qu'aucun ne peut dire avec certitude quel aurait été le résultat. Le principe "
                "d'indépendance du parquet interdit à la Commission de commenter le bien-fondé de la décision, et "
                "elle ne le fait pas.",
                "The Commission's report counts nineteen women who disappeared in the years after the charges were "
                "stayed and who were later linked to Pickton's farm; another count published in 2003 gives "
                "twenty-two. That gap is not smoothed here: it is displayed. The engine does not count lives, it "
                "measures an interval. What it cannot establish, and what no source allows to be established, is "
                "what a trial in February 1998 would have produced. The Commission itself writes that no one can "
                "say with certainty what the outcome would have been. The principle of prosecutorial independence "
                "forbids the Commission from commenting on the merits of the decision, and it does not."),
        },
        [
            {"date": "1997-03-23", "kind": "reference", "label": txt("Agression contre la survivante", "Assault on the survivor")},
            {"date": "1997-04-01", "kind": "reference", "label": txt("Arrestation et quatre chefs", "Arrest and four charges")},
            {"date": "1998-01-26", "kind": "hypothesis", "label": txt("Décision de surseoir", "Stay decision")},
            {"date": "2002-02-22", "kind": "scenario", "label": txt("Arrestation", "Arrest")},
            {"date": "2007-12-09", "kind": "fact", "label": txt("Condamnation", "Conviction")},
            {"date": "2010-08-04", "kind": "outcome", "label": txt("Vingt accusations suspendues", "Twenty charges stayed")},
        ],
        True, "forsaken-vol2b"),

    counterfactual(
        "process",
        "Et si les vêtements saisis en 1997 avaient été analysés la même année ?",
        "What if the clothing seized in 1997 had been tested the same year?",
        "Des vêtements et des bottes ont été saisis en 1997. Le rapport de la Commission note qu'ils n'ont pas "
        "été analysés avant 2004, année où ils se sont révélés porter l'ADN de deux femmes disparues. Sept ans.",
        "Clothing and boots were seized in 1997. The Commission's report notes they were not tested before 2004, "
        "the year they proved to carry the DNA of two missing women. Seven years.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Saisie du matériel", "Seizure of the material"), "date": "1997-04-01"},
            "hypothesis": {"label": txt("Analyse immédiate", "Immediate testing"), "date": "1997-04-01"},
            "scenario_event": {"label": txt("Analyse réalisée", "Testing carried out"), "date": "2004-01-01"},
            "jurisdiction_note": txt(
                "Cette question n'est pas calculable, et l'application ne pretend pas l'être. Elle est affichée "
                "comme un enchaînement de faits documentés : une saisie, un délai, un résultat. Ce que le rapport "
                "ne dit pas — et ce que cette application ne comble pas — c'est si une analyse en 1997 aurait "
                "conduit à une arrestation en 1997, en 1998, en 1999. L'un des trois profils ADN non "
                "identifiés de la ferme n'a jamais été rattaché à un nom. La question n'est pas « le système a-t-il "
                "failli » mais « combien de temps une analyse de routine a-t-elle demandé, et pourquoi ».",
                "This question is not computable, and the application does not pretend otherwise. It is displayed "
                "as a chain of documented facts: a seizure, a delay, a result. What the report does not say — and "
                "what this application does not fill in — is whether testing in 1997 would have led to an arrest in "
                "1997, 1998 or 1999. One of the three unidentified DNA profiles from the farm was never matched to a "
                "name. The question is not 'did the system almost succeed' but 'how long did a routine test take, and "
                "why'."),
        },
        [
            {"date": "1997-04-01", "kind": "reference", "label": txt("Saisie du matériel", "Seizure of the material")},
            {"date": "2004-01-01", "kind": "scenario", "label": txt("Analyse réalisée", "Testing carried out")},
            {"date": "2012-12-17", "kind": "fact", "label": txt("Rapport de la Commission", "Commission report")},
        ],
        False, "forsaken-vol2b"),
]

LESSONS = [
    item("Une enquête menée pour un autre motif peut produire le résultat qu'une enquête menée pour le bon motif "
         "avait échoué à trouver. Ici, un mandat sur des armes à feu illégales a ouvert la plus grande scène de "
         "crime de l'histoire du Canada.",
         "An investigation carried out for another purpose can produce the result that an investigation carried out "
         "for the right purpose failed to find. Here, a warrant about illegal firearms opened the largest crime "
         "scene in Canadian history.",
         "CONFIRMED", "cbc-inquiry", "Hasard institutionnel", "Institutional accident"),
    item("Une décision de surseoir prise sur une appréciation de crédibilité, non réévaluée pendant des années, "
         "peut avoir des conséquences qui durent plus longtemps que la décision elle-même.",
         "A stay decision taken on a credibility assessment, not revisited for years, can have consequences that "
         "outlast the decision itself.",
         "CONFIRMED", "forsaken-es", "Décision sans réévaluation", "An unexamined decision"),
    item("Le lien entre une preuve matérielle et un dossier peut rester invisible pendant des années sans qu'il "
         "s'agisse d'un problème de méthode, mais d'un problème d'archivage et de priorisation.",
         "The link between physical evidence and a case file can remain invisible for years without it being a "
         "method problem, but an archiving and prioritisation problem.",
         "CONFIRMED", "forsaken-vol2b", "Piste non exploitée", "Untapped lead"),
    item("Une liste publique de personnes disparues est un acte d'administration de la preuve, pas seulement de "
         "communication. En 2003, cette liste a été le premier document où figurait le nom d'une femme ensuite "
         "condamnée.",
         "A public list of missing people is an act of administering evidence, not only of communication. In 2003, "
         "that list was the first document in which appeared the name of a woman later convicted of being murdered.",
         "CONFIRMED", "forsaken-vol1", "L'affiche comme pièce", "The poster as evidence"),
    item("Le droit peut recognised un fait sans qu'une procédure ne le traduise en condamnation. Trente-trois "
         "femmes sont reliées à la propriété par la science ; six l'ont été par le droit.",
         "The law can recognise a fact without any procedure translating it into a conviction. Thirty-three women "
         "are linked to the property by science; six by law.",
         "CONFIRMED", "cbc-civil", "Écart science-droit", "The science-law gap"),
    item("Le critère « la peine est déjà maximale » est une règle de justice, pas une règle de preuve. Elle "
         "produit un résultat que le droit ne peut pas défendre une fois posé : des accusations qui ne seront "
         "jamais jugées.",
         "The criterion 'the sentence is already maximal' is a rule of justice, not a rule of evidence. It produces "
         "an outcome law cannot defend once made: charges that will never be tried.",
         "CONFIRMED", "tgm-families", "Règle de justice", "A rule of justice"),
    item("Une enquête publique peut être contestée par les institutions qu'elle interroge, et cette contestation "
         "fait partie du dossier. Elle n'annule pas le rapport ; elle en fait une pièce à deux voix.",
         "A public inquiry can be contested by the institutions it examines, and that contestation is part of the "
         "file. It does not invalidate the report; it makes it a two-voiced piece.",
         "DISPUTED", "cbc-inquiry", "Contestation conservée", "Contestation preserved"),
]

UNKNOWNS = [
    item("Le nombre exact de femmes assassinées. Le chiffre de 33 correspond à des restes ou de l'ADN ; il ne "
         "correspond pas à des personnes identifiées.",
         "The exact number of women murdered. The figure of 33 corresponds to remains or DNA; it does not correspond "
         "to identified people.",
         "CONFIRMED", "reuters-death"),
    item("L'identité des trois profils ADN non identifiés sur la ferme.",
         "The identity of the three unidentified DNA profiles from the farm.",
         "CONFIRMED", "guardian-trial"),
    item("Le sort de vingt femmes accusées et jamais jugées. Aucune n'a été déclarée morte sur le plan judiciaire.",
         "The fate of twenty women who were charged and never tried. None was judicially declared dead.",
         "CONFIRMED", "tgm-timeline"),
    item("Les femmes disparues du Downtown Eastside dont les affaires n'ont jamais été rattachées à Pickton. Le "
         "rapport de la Commission indique que leurs auteurs sont probablement toujours en liberté.",
         "The women missing from the Downtown Eastside whose cases were never linked to Pickton. The Commission's "
         "report states that their killers are probably still at large.",
         "CONFIRMED", "forsaken-es"),
    item("La déclaration des 49 victimes, jamais vérifiée. Aucune source ne permet d'en confirmer ne serait-ce "
         "qu'une partie.",
         "The statement of 49 victims, never verified. No source allows confirmation of any part of it.",
         "PROBABLE", "cbc-scc"),
    item("Le contenu d'une éventuelle expertise psychiatrique. Aucun n'a été rendu public.",
         "The content of any psychiatric evaluation. None has been made public.",
         "UNKNOWN", None),
    item("La date précise de la décision de surseoir : le rapport de la Commission mentionne le 26 janvier 1998 "
         "dans certains volumes et le 27 janvier 1998 dans d'autres. Les deux dates sont conservées.",
         "The precise date of the stay decision: the Commission's report gives 26 January 1998 in some volumes and "
         "27 January 1998 in others. Both dates are kept.",
         "DISPUTED", "forsaken-vol4"),
    item("Le nombre de femmes disparues dans les années suivant la suspension des accusations : dix-neuf selon le "
         "Globe and Mail, vingt-deux selon The Province en 2003. Écart non lissé.",
         "The number of women who disappeared in the years following the stay of charges: nineteen according to the "
         "Globe and Mail, twenty-two according to The Province in 2003. Gap not smoothed.",
         "DISPUTED", "forsaken-vol2b"),
]

SECTIONS = merge_sections(default_sections(), [
    {"key": "introduction", "blocks": [block(
        "paragraph", "Une affaire où le système est le premier auteur",
        "A case in which the system is the first author",
        "C'est le dossier le plus exigeant que nous ayons écrit sur ce sujet, parce qu'il ne parle pas d'un homme mais "
        "d'une institution. La Commission d'enquête de 2012 a employé un mot pour désigner ce qu'étaient "
        "devenues les femmes disparues du Downtown Eastside dans le fonctionnement des services de police. Ce mot "
        "est Nobodies. Il est le titre du volume central du rapport, et il est le sujet de ce dossier.",
        "This is the longest file we have written on this subject, because it is not about one man but about an "
        "institution. The 2012 Commission of Inquiry used one word to describe what the missing Downtown Eastside "
        "women had become in the way police services worked. That word is Nobodies. It is the title of the report's "
        "central volume, and it is the subject of this file.",
        "CONFIRMED", "forsaken-es")]},

    {"key": "context", "blocks": [block(
        "paragraph", "Vancouver, 1978-2002 : un quartier et une liste",
        "Vancouver, 1978-2002: a neighbourhood and a list",
        "Le Downtown Eastside, code postal le plus pauvre du pays, concentrations de logement inadapté, de pauvreté "
        "extrême et de dépendance. À partir de septembre 1978, des femmes y disparaissent. La liste publique de "
        "leurs noms s'allonge pendant vingt-cinq ans. Le rapport d'enquête décrit ces conditions sans leur "
        "attribuer aucune causalité criminelle : elles déterminent qui est cherché, et comment.",
        "The Downtown Eastside, the poorest postal code in the country, concentrations of inadequate housing, extreme "
        "poverty and dependency. From September 1978, women began to disappear there. The public list of their "
        "names grows for twenty-five years. The inquiry report describes these conditions without attributing any "
        "criminal causality to them: they determine who is searched for, and how.",
        "CONFIRMED", "forsaken-vol1")]},

    {"key": "offender", "blocks": [block(
        "paragraph", "Robert William Pickton (1949-2024)",
        "Robert William Pickton (1949-2024)",
        "Né le 24 octobre 1949 à Port Coquitlam. Éleveur porcin, chauffeur, propriétaire avec ses frères d'une "
        "exploitation à Port Coquitlam, et tenant un atelier d'abattage non autorisé approvisionnant des commerces "
        "de détail. Condamné à six chefs de meurtre au second degré en 2007. Décédé le 31 mai 2024 des suites d'une "
        "agression en prison, à 74 ans. Aucun diagnostic n'est posé dans ce dossier.",
        "Born 24 October 1949 in Port Coquitlam. A pig farmer, a truck driver, co-owner with his brothers of a farm "
        "at Port Coquitlam, and keeper of an unlicensed slaughterhouse supplying local shops. Convicted on six counts "
        "of second-degree murder in 2007. Died on 31 May 2024 following an assault in prison, aged 74. No "
        "diagnosis is made in this file.",
        "CONFIRMED", "apntn-death")]},

    {"key": "behaviour", "blocks": [block(
        "behaviour", "Ce que le dossier décrit, et ce qu'il n'interprète pas",
        "What the file describes, and what it does not interpret",
        "Le dossier documente un mode d'accès : un homme qui avait une raison professionnelle d'héberger des "
        "visiteurs, un accès direct à une propriété isolée, et une activité commerciale qui fournissait un "
        "réseau dedistribution hors du regard. Le rapport d'enquête explique que la question posée à la police "
        "n'était pas de profiler un inconnu, mais de rapprocher des faits déjà signalés. Il ne documente aucun "
        "profil de risque partagé avec d'autres affaires.",
        "The file documents a mode of access: a man with a professional reason to host visitors, direct access to an "
        "isolated property, and a commercial activity that provided a distribution network out of sight. The "
        "inquiry report explains that the question facing police was not to profile an unknown, but to connect "
        "facts already reported. It documents no risk profile shared with other cases.",
        "CONFIRMED", "forsaken-vol1")]},

    {"key": "consequences", "blocks": [block(
        "paragraph", "Soixante-trois recommandations, et ce qu'elles ont produit",
        "Sixty-three recommendations, and what they produced",
        "Le volume III du rapport porte sur l'héritage de sécurité des femmes : compensation, prévention, "
        "transports, formation des policiers, liens avec l'Enquête nationale. La province a regroupé les "
        "recommandations en quatre catégories et a publié six rapports d'avancement. Ces rapports décrivent des "
        "mesures adoptées ; ils ne décrivent pas une transformation du taux de disparitions non élucidées, qui "
        "n'est pas documenté dans les sources consultées.",
        "Volume III of the report deals with the women's safety legacy: compensation, prevention, transport, "
        "police training, and links with the National Inquiry. The province grouped the recommendations into four "
        "categories and published six progress updates. Those updates describe measures adopted; they do not "
        "describe a transformation of the rate of unresolved disappearances, which is not documented in the "
        "sources consulted.",
        "CONFIRMED", "forsaken-vol3"),
        block(
        "paragraph", "Ce qui a changé, et ce qui n'a pas changé",
        "What changed, and what did not",
        "Une enquête publique, 63 recommandations, un fonds de compensation, des excuses publiques, un rapport "
        "national en 2019. Cinq ans après ce dernier, l'Assemblée des Premières Nations évalue la mise en œuvre "
        "des appels à la justice à « minime ou aucun » pour la majorité d'entre eux. La question posée en 1997 — "
        "comment protège-t-on une population qu'une police connaît comme vulnérable — reste, dans les faits, "
        "sans réponse documentée.",
        "A public inquiry, 63 recommendations, a compensation fund, public apologies, a national report in 2019. "
        "Five years after the latter, the Assembly of First Nations assesses implementation of the calls for "
        "justice as 'minimal to no' for the majority. The question posed in 1997 — how do you protect a population "
        "police know to be vulnerable — remains, in fact, without a documented answer.",
        "CONFIRMED", "afn-mmiwg")]},
])

EPISODES = [
    {
        "number": 1,
        "title": txt("Nobodies : un quartier, une liste, vingt-cinq ans",
                      "Nobodies: a neighbourhood, a list, twenty-five years"),
        "description": txt("De septembre 1978 à 2002. Comment des femmes ont disparu d'un quartier de Vancouver, "
                           "et comment une liste de leurs noms est devenue la seule forme de preuve qui leur "
                           "reste. Narration produite par une voix de synthèse provisoire, en attendant "
                           "l'enregistrement du créateur.",
                           "From September 1978 to 2002. How women disappeared from a Vancouver neighbourhood, and "
                           "how a list of their names became the only form of evidence left to them. Narration "
                           "produced by a provisional synthetic voice, pending the creator's own recording."),
        "modes": ["documentary", "victims", "chronology", "investigation", "express", "psychology", "expert"],
        "audio_status": "produced", "voice_profile": "synthese-provisoire",
        "audio": "yanisx-robert-pickton-ep1-nobodies.mp3",
        "duration_sec": 184,
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 19, "title": txt("Le code postal le plus pauvre du pays", "The poorest postal code in the country")},
            {"at": 40, "title": txt("Le premier nom", "The first name")},
            {"at": 62, "title": txt("Un avis de danger, 29 mars 1997", "A danger advisory, 29 March 1997")},
            {"at": 113, "title": txt("Et maintenant, une question", "And now, a question")},
            {"at": 117, "title": txt("Ce que dit la Commission", "What the Commission says")},
        ],
        "transcript": {"segments": [
            {"id": "n1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X, à travers mon regard. Aujourd'hui, une affaire canadienne qui ne "
                     "raconte pas un tueur, mais une institution. Le mot que la Commission d'enquête de 2012 a "
                     "choisi pour ce dossier est un seul mot. Il est aussi le titre du volume central du rapport. "
                     "Nobodies. Des personnes sans nom.",
             "text_en": "You are on YANIS//X, through my eyes. Today, a Canadian case that is not about a killer but "
                        "about an institution. The word the 2012 Commission of Inquiry chose for this file is a "
                        "single word. It is also the title of the report's central volume. Nobodies. People with no "
                        "name."},
            {"id": "n2", "t": 19, "speaker": "yanis",
             "text": "Vancouver, dans le Downtown Eastside. Le rapport d'enquête le décrit en des termes qu'il "
                     "faut citer : logement grossièrement inadapté, insécurité alimentaire, inégalités "
                     "sanitaires, pauvreté extrême. Ce n'est pas un décor. C'est une chaîne de conditions qui "
                     "détermine, ensuite, qui sera cherché avec la même urgence, et qui ne le sera pas.",
             "text_en": "Vancouver, in the Downtown Eastside. The inquiry report describes it in terms that must be "
                        "quoted: grossly inadequate housing, food insecurity, health inequalities, extreme "
                        "poverty. This is not scenery. It is a chain of conditions that then determines who will be "
                        "searched for with the same urgency, and who will not."},
            {"id": "n3", "t": 40, "speaker": "yanis",
             "text": "Le douze septembre 1978, Lillian Jean O'Dare est vue pour la dernière fois. Elle est la "
                     "première femme de cette liste. La liste s'allongera pendant vingt-cinq ans. En 2004, la "
                     "dernière affiche de la police de Vancouver énumère soixante-neuf noms. Chacun de ces noms "
                     "était une personne qui avait une famille, un endroit où dormir, un travail parfois.",
             "text_en": "On 12 September 1978, Lillian Jean O'Dare is last seen. She is the first woman on this "
                        "list. The list will grow for twenty-five years. In 2004, the last Vancouver Police poster "
                        "lists sixty-nine names. Each of those names was a person who had a family, a place to "
                        "sleep, sometimes a job."},
            {"id": "n4", "t": 62, "speaker": "yanis",
             "text": "Le 29 mars 1997, la GRC envoie un message d'alerte à tous les détachements du Bas-Fraser. "
                     "Un homme du Lower Mainland avait "
                     "agressé une femme. Le message dit : il doit être considéré comme un danger pour les "
                     "travailleuses du sexe. C'est un moment rare. Le risque a été nommé, noir sur blanc, par une "
                     "institution, à une population entière.",
             "text_en": "On 29 March 1997, the RCMP sends an advisory to every detachment in the Lower Mainland. A "
                        "man in the Lower Mainland had assaulted a woman. The message says: he should be considered "
                        "a danger to sex trade workers. This is a rare moment. The risk was named, in writing, by an "
                        "institution, to an entire population."},
            {"id": "n5", "t": 85, "speaker": "yanis",
             "text": "Un mois plus tard, il est arrêté. Quatre chefs d'accusation. Un avis de libération. Un "
                     "procès est fixé pour février 1998. Le 26 janvier, le parquet décide de surseoir. Le motif "
                     "déclaré : la témoin était trop atteinte par sa dépendance pour constituer un témoin "
                     "fiable. C'était une conclusion tirée d'une seule rencontre, moins de deux semaines avant le "
                     "procès. Cette femme témoignerait en 2003. Son nom, lui, reste interdit de publication "
                     "vingt-cinq ans plus tard.",
             "text_en": "A month later, he is arrested. Four charges. A release on bail. A trial is set for February "
                        "1998. On 26 January, the Crown decides to stay the proceedings. The stated reason: the "
                        "witness was too impaired by her dependency to be a reliable witness. It was a conclusion "
                        "drawn from a single meeting held less than two weeks before trial. That woman would testify "
                        "in 2003. Her name, meanwhile, remains under a publication ban twenty-five years later."},
            {"id": "n6", "t": 113, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "n7", "t": 117, "speaker": "yanis",
             "text": "La Commission d'enquête a elle-même refusé de commenter le bien-fondé de cette décision, "
                     "parce que le principe d'indépendance du parquet l'y oblige. Elle a dit autre chose, dans "
                     "d'autres mots : qu'en lumière de ce qui a été appris ensuite, la décision est inexplicable. "
                     "Un mot. Inexpliquable. Après. Une décision se juge toujours deux fois : une fois au moment "
                     "où on la prend, et une fois dans la lumière de ce que l'on sait ensuite.",
             "text_en": "The Commission of Inquiry itself declined to comment on the merits of that decision, because "
                        "the principle of prosecutorial independence requires it. It said something else, in other "
                        "words: that in light of what was learned afterwards, the decision is inexplicable. One "
                        "word. Inexplicable. Afterwards. A decision is always judged twice: once at the moment it is "
                        "taken, and once in the light of what is known afterwards."},
            {"id": "n8", "t": 142, "speaker": "yanis",
             "text": "En 1998, un homme lié à l'entreprise de démolition de Robert Pickton enregistre une "
                     "conversation. Il y relie les femmes qui disparaissent, et les sacs à main et les pièces "
                     "d'identité retrouvés dans la roulotte de Pickton. Il donne cette bande à la police. On lui dit "
                     "merci. Puis plus rien. L'enquête officielle ne commencera qu'en février 2002, pour une autre "
                     "raison : on cherchait des armes.",
             "text_en": "In 1998, a man connected to Robert Pickton's salvage company records a conversation. In it "
                        "he links the women who are disappearing to the purses and IDs found in Pickton's trailer. "
                        "He gives the tape to police. He is thanked. Then nothing. The official investigation will "
                        "not begin until February 2002, for another reason: they were looking for firearms."},
            {"id": "n9", "t": 165, "speaker": "yanis",
             "text": "Écouter cette histoire, c'est entendre le moment précis où une institution qui sait quelque "
                     "chose choisit de ne pas en faire une enquête. Puis le moment où elle le fait — pour une "
                     "autre raison, dans un autre dossier, sous un autre motif. Ce sont ces deux dates, et non la "
                     "condamnation, qui font le plus mal aux familles.",
             "text_en": "Listening to this story is to hear the precise moment when an institution that knows "
                        "something chooses not to make it an investigation. Then the moment when it does — for "
                        "another reason, in another file, under another heading. It is those two dates, not the "
                        "conviction, that hurt the families most."},
        ]},
    },
    {
        "number": 2,
        "title": txt("Trente-trois, six, et les vingt qui n'ont pas vu un tribunal",
                      "Thirty-three, six, and the twenty who never saw a courtroom"),
        "description": txt("2002-2014. La plus grande scène de crime de l'histoire canadienne, un procès de onze "
                           "mois, un verdict contesté par les deux cours d'appel, et vingt accusations suspendues "
                           "parce que la peine était déjà maximale.",
                           "2002-2014. The largest crime scene in Canadian history, an eleven-month trial, a "
                           "verdict contested by two appellate courts, and twenty charges stayed because the "
                           "sentence was already maximal."),
        "modes": ["investigation", "documentary", "chronology", "expert", "express", "psychology", "victims"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 80, "title": txt("Cinq février 2002", "Five February 2002")},
            {"at": 240, "title": txt("Dix-huit mois", "Eighteen months")},
            {"at": 420, "title": txt("Le procès", "The trial")},
            {"at": 600, "title": txt("Et maintenant, une question", "And now, a question")},
            {"at": 660, "title": txt("Le quatre août 2010", "Four August 2010")},
            {"at": 840, "title": txt("Ce que la justice civile a donné", "What civil justice provided")},
        ],
        "transcript": {"segments": [
            {"id": "t1", "t": 0, "speaker": "yanis",
             "text": "Le cinq février 2002, la police de Vancouver entre sur une ferme porcine de Port Coquitlam. "
                     "Elle ne cherche pas des victimes. Elle cherche des armes à feu illégales. Ce qu'elle trouve "
                     "est autre chose : des effets personnels appartenant à des femmes déclarées disparues. "
                     "L'inquiry note que cette enquête aurait dû commencer quinze ans plus tôt.",
             "text_en": "On 5 February 2002, Vancouver Police enter a pig farm in Port Coquitlam. They are not looking "
                        "for victims. They are looking for illegal firearms. What they find is something else: "
                        "personal effects belonging to women reported missing. The inquiry notes this investigation "
                        "should have begun fifteen years earlier."},
            {"id": "t2", "t": 80, "speaker": "yanis",
             "text": "La fouille dure dix-huit mois. On tamise trois cent quatre-vingt-trois mille verges cubes de "
                     "terre. On saisit plus de six cent mille objets. Les archéologues, les biologistes, les "
                     "toxicologues et les chimistes travaillent ensemble. C'est la plus vaste scène de crime "
                     "jamais traitée au Canada. Un avis sanitaire est envoyé aux voisins qui ont acheté de la "
                     "viande de la ferme.",
             "text_en": "The search lasts eighteen months. Three hundred and eighty-three thousand cubic yards of "
                        "soil are sifted. More than six hundred thousand items are seized. Archaeologists, "
                        "biologists, toxicologists and chemists work together. It is the largest crime scene ever "
                        "processed in Canada. A public health advisory goes out to neighbours who bought meat from "
                        "the farm."},
            {"id": "t3", "t": 240, "speaker": "yanis",
             "text": "Des restes humains partiels. Et de l'ADN. En tout, le chiffre trente-trois est donné par la "
                     "GRC, par la Cour suprême du Canada et par la presse internationale. Trente-trois femmes "
                     "reliées à cette propriété. Vingt-six sont mises en accusation. Six seront jugées. Et il y a "
                     "des choses que l'ADN ne fait pas : il relie. Il ne dit pas qui a tué.",
             "text_en": "Partial human remains. And DNA. In total, the figure thirty-three is given by the RCMP, by "
                        "the Supreme Court of Canada and by the international press. Thirty-three women linked to "
                        "this property. Twenty-six are charged. Six will be tried. And there are things DNA does not "
                        "do: it links. It does not say who killed."},
            {"id": "t4", "t": 420, "speaker": "yanis",
             "text": "Le procès s'ouvre en janvier 2007, à New Westminster. Onze mois. Soixante-dix-sept décisions "
                     "judiciaires. Le neuf décembre, le jury déclare Robert Pickton coupable de six chefs de "
                     "meurtre au second degré. Pas au premier degré. Aux termes de cette qualification, les faits "
                     "n'étaient ni planifiés ni délibérés. Le juge de première instance, à la sentencing, dit que ce "
                     "cas est unique. Les deux cours d'appel, ensuite, jugeront que le jury s'est trompé sur ce "
                     "point — sans pour autant réformer les condamnations.",
             "text_en": "The trial opens in January 2007, in New Westminster. Eleven months. Seventy-seven judicial "
                        "rulings. On 9 December, the jury finds Robert Pickton guilty on six counts of "
                        "second-degree murder. Not first-degree. On that characterisation, the acts were neither "
                        "planned nor deliberate. The trial judge, at sentencing, says this case is unique. The two "
                        "appellate courts then hold that the jury got that point wrong — without reforming the "
                        "convictions."},
            {"id": "t5", "t": 600, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "t6", "t": 660, "speaker": "yanis",
             "text": "Le quatre août 2010, vingt accusations de meurtre au premier degré sont suspendues. Le "
                     "raisonnement : la peine est déjà maximale, de nouvelles condamnations n'ajouteraient rien. "
                     "C'est un raisonnement de justice, pas un raisonnement de preuve. Et il produit un résultat "
                     "que le droit ne peut pas défendre une fois posé : vingt femmes qui n'entreront jamais dans "
                     "une salle d'audience. Leurs familles ne obtiendront jamais un verdict. Elles newere pas "
                     "disparues — elles sont dans un état juridique permanent.",
             "text_en": "On 4 August 2010, twenty first-degree murder charges are stayed. The reasoning: the "
                        "sentence is already maximal, further convictions would add nothing. It is a reasoning of "
                        "justice, not a reasoning of evidence. And it produces an outcome the law cannot defend once "
                        "made: twenty women who will never enter a courtroom. Their families will never get a "
                        "verdict. They are not missing — they are in a permanent legal state."},
            {"id": "t7", "t": 840, "speaker": "yanis",
             "text": "Un an de plus, et c'est une somme d'argent : quatre virgule neuf millions de dollars, cent "
                     "quatre-vingt-huit enfants, cinquante mille dollars chacun. La loi de la province ne permet "
                     "pas de réparer une vie. Elle permet de réparer un manque financier. C'est déjà quelque chose. "
                     "Ce n'est pas ce qui s'est passé.",
             "text_en": "A year later, and it is a sum of money: $4.9 million, ninety-eight children, fifty "
                        "thousand dollars each. Provincial law does not permit repairing a life. It permits "
                        "repairing a financial loss. That is already something. It is not what happened."},
            {"id": "t8", "t": 1010, "speaker": "yanis",
             "text": "Trente-trois femmes sont reliées à cette ferme par la science. Six le sont par le droit. "
                     "Entre ces deux nombres, il n'y a pas un mystère. Il y a une procédure. Et c'est cela que ce "
                     "dossier veut laisser : non pas une histoire qui se termine mal, mais une histoire dont on sait "
                     "exactement où elle a failli, et pourquoi.",
             "text_en": "Thirty-three women are linked to this farm by science. Six are linked by law. Between those "
                        "two numbers there is not a mystery. There is a procedure. And that is what this file wants "
                        "to leave: not a story that ends badly, but a story of which we know exactly where it came "
                        "close, and why."},
        ]},
    },
]

QUESTIONS = [
    question("1", 113, "system",
             "Le 29 mars 1997, un avis de police désigne nommément un homme comme un danger pour les "
             "travailleuses du sexe. Qu'est-ce qui manque, dans les mois qui suivent, pour que cet avis devienne "
             "une stratégie ?",
             "On 29 March 1997, a police advisory names a man as a danger to sex trade workers. What is missing in "
             "the months that follow for that advisory to become a strategy?",
             [("a", "Des moyens supplémentaires", "Additional resources"),
              ("b", "Le rapprochement des disparues avec l'agression connue, et une protection de la population "
                    "citée", "Linking the disappearances to the known assault, and protecting the cited population"),
              ("c", "La condamnation préalable de l'auteur", "A prior conviction of the author"),
              ("d", "Une expertise psychologique", "A psychological assessment")],
             {"fr": {"whatInvestigatorsKnew": "Le 23 mars 1997, une agression contre une femme dans la propriété de Port Coquitlam est connue. Le 29 mars, un message d'alerte est diffusé à tous les détachements du Bas-Fraser. L'auteur est connu, la victime est identifiée, la population à risque est nommée dans un document officiel.",
                     "whatExpertsProposed": "Le rapport de la Commission d'enquête conclut que la première trace d'une stratégie destinée à protéger les femmes du Downtown Eastside date de 2002 — quelques semaines avant l'arrestation. L'écart entre l'avis et la stratégie est de cinq ans.",
                     "documented": "Le sommaire du rapport Forsaken et le volume II documentent cette chronologie.",
                     "hypothetical": "Ce qu'une protection ciblée de la population nommée dans l'avis aurait produit — hypothèse que le rapport se refuse à formuler, faute de base.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir qu'un objet saisi en 1997 — un vêtement, une botte — porterait l'ADN de deux femmes disparues, et qu'il resterait sept ans sans être analysé.",
                     "answer_note": "La réponse attendue est B. L'avis n'est pas un défaut d'information : c'est l'absence de décision qui en découle."},
              "en": {"whatInvestigatorsKnew": "On 23 March 1997, an assault against a woman at the Port Coquitlam property is known. On 29 March, an advisory is sent to every detachment in the Lower Mainland. The author is known, the victim is identified, the at-risk population is named in an official document.",
                     "whatExpertsProposed": "The Commission's report finds the first trace of a strategy to protect Downtown Eastside women dates from 2002 — weeks before the arrest. The gap between the advisory and the strategy is five years.",
                     "documented": "The Forsaken executive summary and volume II document this chronology.",
                     "hypothetical": "What targeted protection of the population named in the advisory would have produced — a hypothesis the report declines to formulate, having no basis for it.",
                     "whatYouCouldNotKnow": "You could not know that an item seized in 1997 — a garment, a boot — carried the DNA of two missing women, and would go seven years without being tested.",
                     "answer_note": "The expected answer is B. The advisory is not an information failure: it is the absence of any decision following from it."}},
             "forsaken-es"),

    question("2", 330, "evidence",
             "Des restes ou de l'ADN de 33 femmes sont retrouvés sur la propriété. Vingt-six femmes sont mises en "
             "accusation. Pourquoi l'ADN n'a-t-il pas suffi ?",
             "Remains or DNA from 33 women are found on the property. Twenty-six women are charged. Why was the DNA "
             "not enough?",
             [("a", "Parce que l'ADN a été mal prélevé", "Because the DNA was badly collected"),
              ("b", "Parce que l'ADN établit un lien, pas une intention : l'acte strengths punishable doit être établi "
                    "séparément pour chaque victime", "Because DNA establishes a link, not an intention: the punishable act must be established separately for each victim"),
              ("c", "Parce que la loi canadienne l'interdit", "Because Canadian law forbids it"),
              ("d", "Parce que le laboratoire n'a pas eu les moyens", "Because the laboratory lacked the means")],
             {"fr": {"whatInvestigatorsKnew": "Trente-trois femmes sont reliées matériellement à la propriété. Vingt-six ont été mises en accusation, six jugées, vingt suspendues. Trois profils ADN sont restés non identifiés.",
                     "whatExpertsProposed": "La doctrine de l'enchaînement desUu preuves exige qu'un lien matériel soit établi pour identifier une victime, et qu'un acte coupable soit établi pour la condamner. Le lien et l'acte sont deux questions distinctes dans une procédure criminelle.",
                     "documented": "Le chiffre de 33 est documenté de façon cohérente par la GRC et par la Cour suprême du Canada ; l'écart avec les 6 condamnations est documenté par le Globe and Mail.",
                     "hypothetical": "Ce qu'une procédure de jugement accéléré aurait produit — hypothèse qu'aucune source ne permet d'établir.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir que la décision de suspendre les vingt chefs serait fondée non sur un doute sur les faits, mais sur un constat de droit : la peine était déjà maximale.",
                     "answer_note": "La réponse attendue est B. C'est la distinction centrale de tout le dossier : 33 femmes sont prouvées présentes, 6 sont prouvées assassinées par un jugement."},
              "en": {"whatInvestigatorsKnew": "Thirty-three women are materially linked to the property. Twenty-six are charged, six tried, twenty stayed. Three DNA profiles remain unidentified.",
                     "whatExpertsProposed": "The doctrine of the chain of evidence requires a material link to identify a victim, and a culpable act to convict. The link and the act are two distinct questions in a criminal proceeding.",
                     "documented": "The figure of 33 is documented consistently by the RCMP and by the Supreme Court of Canada; the gap with the 6 convictions is documented by the Globe and Mail.",
                     "hypothetical": "What a different procedure would have produced — a hypothesis no source allows to be established.",
                     "whatYouCouldNotKnow": "You could not know that the decision to stay the twenty counts would be founded not on any doubt about the facts, but on a point of law: the sentence was already maximal.",
                     "answer_note": "The expected answer is B. It is the central distinction of the whole file: 33 women are proved present, 6 are proved murdered by a judgment."}},
             "cbc-civil"),

    question("2", 660, "justice",
             "Le 4 août 2010, vingt accusations de meurtre au premier degré sont suspendues. Sur quel raisonnement ?",
             "On 4 August 2010, twenty first-degree murder charges are stayed. On what reasoning?",
             [("a", "Sur un doute raisonnable", "On a reasonable doubt"),
              ("b", "Sur une insuffisance de preuves", "On insufficient evidence"),
              ("c", "Sur un motif d'ordre public : la peine déjà prononcée étant maximale, de nouvelles "
                    "condamnations n'y changeraient rien", "On grounds of public policy: the sentence already imposed being maximal, further convictions would change nothing"),
              ("d", "Sur la pression des familles", "On pressure from the families")],
             {"fr": {"whatInvestigatorsKnew": "La Cour d'appel avait déjà jugé qu'un nouveau procès sur les vingt chefs imposerait des exigences « énormes » aux ressources financières et judiciaires.",
                     "whatExpertsProposed": "Un critère fondé sur la peine déjà prononcée est un critère d'équité et de gestion, pas un critère probatoire. Il n'exprime aucun doute sur les faits.",
                     "documented": "Le Global and Mail documente la décision du 4 août 2010 et la déclaration du parquet ; l'Enquête nationale de 2019 rappelle que le problème n'est pas la preuve mais le décompte.",
                     "hypothetical": "Ce qu'un régime de peines consécutives aurait permis — le droit canadien ne le prévoit pas pour cette infraction, ce qui explique en partie la décision.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir, en 2010, qu'en 2024 la GRC demanderait à détruire environ 14 000 pièces de l'enquête, et que cette demande serait contestée par les familles et les associations.",
                     "answer_note": "La réponse attendue est C. C'est la raison donnée, et elle dit quelque chose sur le système de sanctions autant que sur cette affaire."},
              "en": {"whatInvestigatorsKnew": "The Court of Appeal had already held that a new trial on the twenty counts would impose 'enormous' demands on financial and judicial resources.",
                     "whatExpertsProposed": "A criterion founded on the sentence already imposed is a criterion of fairness and management, not an evidential one. It expresses no doubt about the facts.",
                     "documented": "The Globe and Mail documents the decision of 4 August 2010 and the Crown's statement; the 2019 National Inquiry recalls that the problem is not proof but counting.",
                     "hypothetical": "What a regime of consecutive sentences would have permitted — Canadian law does not provide for it for this offence, which partly explains the decision.",
                     "whatYouCouldNotKnow": "You could not know, in 2010, that in 2024 the RCMP would apply to dispose of about 14,000 items from the investigation, and that the question would remain open after the accused's death.",
                     "answer_note": "The expected answer is C. It is the reason given, and it says something about the sentencing system as much as about this case."}},
             "tgm-timeline"),
]

CASE = {
    "id": CASE_ID,
    "title": txt("Robert Pickton — les disparues du Downtown Eastside",
                  "Robert Pickton — the missing women of the Downtown Eastside"),
    "subtitle": txt("Vancouver, 1978-2012. Soixante-cinq femmes disparues, un avis de danger émis en 1997 et "
                    "ignoré, une scène de crime ouverte en 2002 pour une autre raison, et un rapport "
                    "d'enquête qui a employé le mot « Nobodies ».",
                    "Vancouver, 1978-2012. Sixty-five missing women, a danger advisory issued in 1997 and set "
                    "aside, a crime scene opened in 2002 for another reason, and an inquiry report that used the "
                    "word 'Nobodies'."),
    "country": "CA", "region": "Colombie-Britannique", "city": "Vancouver",
    "year_start": 1978, "year_end": 2024, "period_label": txt("1978 – 2024", "1978 – 2024"),
    "status": "RESOLVED", "type": "serial",
    "tags": ["serial_killer", "systemic_failure", "missing_women", "inquiry", "canada", "dtes",
             "indigenous_women", "victimology", "unresolved_identities"],
    "tier": "PREMIUM", "editorial": "yanis", "published_at": "2026-09-28", "sensitive": True,
    "triggers": txt("Disparitions, executions, violenceagainst des femmes autochtones et marginalisées ; ampleur "
                    "des faits évoquée sans aucun détail graphique.",
                    "Disappearances, killings, violence against Indigenous and marginalised women; the scale of the "
                    "offences is evoked with no graphic detail."),
    "lat": 49.2800, "lon": -123.1000, "cover": "cover-pickton",
    "stats": {
        "victims_convicted": 6, "victims_charged": 26, "victims_dna_linked": 33,
        "victims_claimed": 49, "missing_women_dtes": 65, "inquiry_pages": 1445,
        "inquiry_recommendations": 63, "stay_decision_years": 4, "duration_years": 46,
    },
    "summary": txt(
        "Entre septembre 1978 et le début des années 2000, au moins 65 femmes disparaissent du Downtown Eastside de "
        "Vancouver, le code postal le plus pauvre du pays. Le 23 mars 1997, une femme agressée dans la propriété de "
        "Port Coquitlam survit. Le 29 mars, la GRC envoie un avis nommant l'homme comme un danger pour les "
        "travailleuses du sexe. Il est arrêté le 1er avril, libéré le 8, et le 26 janvier 1998 le parquet suspend "
        "la procédure, estimant la témoin trop atteinte par sa dépendance. Des vêtements saisis ce jour-là ne sont "
        "analysés qu'en 2004 : ils portent l'ADN de deux femmes disparues. En 1998, un homme lié à l'entreprise de "
        "démolition de Pickton enregistre ses observations et les donne à la police. Le 5 février 2002, un mandat "
        "portant sur des armes à feu illégales ouvre la plus vaste scène de crime de l'histoire canadienne : 383 000 "
        "verges cubes tamisées, plus de 600 000 objets saisis, et les restes ou l'ADN de 33 femmes. Robert Pickton "
        "est arrêté le 22 février 2002, condamné le 9 décembre 2007 à six peines de réclusion à vie sans libération "
        "possible pendant vingt-cinq ans. Le 4 août 2010, vingt accusations de meurtre au premier degré sont "
        "suspendues au motif que la peine est déjà maximale. La Commission d'enquête sur les femmes disparues et "
        "assassinées publie le 17 décembre 2012 un rapport de 1 445 pages concluant que les enquêtes ont constitué "
        "« une défaillance manifeste » et qu'il existait un « biais systémique ». En 2014, un fonds de 4,9 millions "
        "de dollars est versé à 98 enfants. Robert Pickton meurt le 31 mai 2024 des suites d'une agression en "
        "prison. Vingt femmes n'ont jamais été jugées, et trois profils ADN n'ont jamais reçu de nom.",
        "Between September 1978 and the early 2000s, at least 65 women disappeared from Vancouver's Downtown "
        "Eastside, the poorest postal code in the country. On 23 March 1997, a woman assaulted at the Port Coquitlam "
        "property survives. On 29 March, the RCMP sends an advisory naming the man as a danger to sex trade "
        "workers. He is arrested on 1 April, released on the 8th, and on 26 January 1998 the Crown stays the "
        "proceedings, considering the witness too impaired by her dependency. Clothing seized that day is not tested "
        "until 2004: it carries the DNA of two missing women. In 1998, a man connected to Pickton's salvage company "
        "records his observations and gives them to police. On 5 February 2002, a warrant concerning illegal "
        "firearms opens the largest crime scene in Canadian history: 383,000 cubic yards sifted, more than 600,000 "
        "items seized, and the remains or DNA of 33 women. Robert Pickton is arrested on 22 February 2002, "
        "convicted on 9 December 2007 to six life sentences with no possibility of parole for twenty-five years. On "
        "4 August 2010, twenty first-degree murder charges are stayed on the ground that the sentence is already "
        "maximal. The Missing Women Commission of Inquiry publishes on 17 December 2012 a 1,445-page report finding "
        "that the investigations were a 'blatant failure' and that 'systemic bias' existed. In 2014, a $4.9 million "
        "fund is paid to 98 children. Robert Pickton dies on 31 May 2024 following an assault in prison. Twenty women "
        "were never tried, and three DNA profiles never received a name."),
    "sources": SOURCES, "victims": VICTIMS, "memorial": MEMORIAL, "timeline": TIMELINE, "locations": LOCATIONS,
    "evidence": EVIDENCE, "investigation": INVESTIGATION, "psychology": PSYCHOLOGY, "victimology": VICTIMOLOGY,
    "court": COURT, "experts": EXPERTS, "experts_agreement": EXPERTS_AGREEMENT,
    "experts_disagreement": EXPERTS_DISAGREEMENT, "experts_uncertain": EXPERTS_UNCERTAIN,
    "counterfactuals": COUNTERFACTUALS, "lessons": LESSONS, "unknowns": UNKNOWNS, "sections": SECTIONS,
    "episodes": EPISODES, "questions": QUESTIONS,
}
