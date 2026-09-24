"""
DOSSIER 01 — L'AFFAIRE ESTELLE MOUZIN (France, Seine-et-Marne, 2003-2025)

All facts below are drawn from the public sources listed in SOURCES and were
verified on 2026-09-24. Every entry carries a reliability level:
CONFIRMED / PROBABLE / DISPUTED / UNKNOWN (§23). Nothing here is invented.
"""
from ..case_template import block, counterfactual, fact, item, question, source, txt

CASE_ID = "estelle-mouzin"
VERIFIED_AT = "2026-09-24"

SOURCES = [
    source(
        "monde-5dates", CASE_ID,
        "Michel Fourniret : de la disparition d'Estelle Mouzin aux aveux, dix-sept ans d'enquête en cinq dates-clés",
        "Michel Fourniret: from Estelle Mouzin's disappearance to his confession, seventeen years of investigation in five key dates",
        "Le Monde", "Journalists of Le Monde", "https://www.lemonde.fr/societe/article/2020-10-09/de-la-disparition-d-estelle-mouzin-aux-aveux-de-michel-fourniret-dix-sept-ans-d-enquete-en-cinq-dates-clefs_6055485_3224.html",
        "2020-10-09", "press", "CONFIRMED", VERIFIED_AT,
        "Chronologie de référence publiée par un quotidien national.",
        "Reference chronology published by a national daily.",
    ),
    source(
        "franceinfo-chronologie", CASE_ID,
        "Estelle Mouzin — chronologie et suivi de l'affaire",
        "Estelle Mouzin — chronology and case coverage",
        "franceinfo (Radio France)", "Redaction", "https://www.ici.fr/personnes/estelle-mouzin",
        "2025", "press", "CONFIRMED", VERIFIED_AT,
        "Fiche personne et chronologie ; mentions de l'ADN partiel retrouvé en août 2020.",
        "Person file and chronology; mentions the partial DNA found in August 2020.",
    ),
    source(
        "rtl-faute-lourde", CASE_ID,
        "Meurtre d'Estelle Mouzin : l'État condamné pour faute lourde dans l'enquête sur sa disparition",
        "Estelle Mouzin murder: the State condemned for gross negligence in the investigation",
        "RTL", "Redaction", "https://www.rtl.fr/actu/justice-faits-divers/meurtre-d-estelle-mouzin-l-etat-condamne-pour-faute-lourde-dans-l-enquete-sur-sa-disparition-7900537297",
        "2025-09-03", "press", "CONFIRMED", VERIFIED_AT,
        "Compte rendu du jugement du tribunal judiciaire de Paris du 3 septembre 2025.",
        "Report on the Paris judicial court ruling of 3 September 2025.",
    ),
    source(
        "franceinfo-olivier-2023", CASE_ID,
        "Procès de Monique Olivier : condamnée à la réclusion à perpétuité pour complicité dans trois meurtres, dont celui d'Estelle Mouzin",
        "Monique Olivier trial: sentenced to life imprisonment for complicity in three murders, including Estelle Mouzin's",
        "franceinfo (Radio France)", "Redaction", "https://www.franceinfo.fr/societe/justice/michel-fourniret/proces-de-monique-olivier-l-ex-femme-de-michel-fourniret-condamnee-a-la-prison-a-perpetuite-pour-complicite-dans-trois-meurtres-dont-celui-d-estelle-mouzin_6254334.html",
        "2023-12-19", "press", "CONFIRMED", VERIFIED_AT,
        "Verdict, motivations de la cour, audiences du 28 novembre au 19 décembre 2023.",
        "Verdict, court reasoning, hearings from 28 November to 19 December 2023.",
    ),
    source(
        "marieclaire-temps-forts", CASE_ID,
        "Estelle Mouzin : les temps forts d'une affaire qui a bouleversé la France",
        "Estelle Mouzin: the key moments of a case that shook France",
        "Marie Claire", "Redaction", "https://www.marieclaire.fr/l-affaire-estelle-mouzin,1373771.asp",
        "2025-01-09", "press", "PROBABLE", VERIFIED_AT,
        "Presse magazine : détails sur l'alibi téléphonique et le contenu informatique, à recouper avec les actes d'instruction.",
        "Magazine press: details on the phone alibi and computer content, to be cross-checked with investigative acts.",
    ),
    source(
        "ouestfrance-reconstitution", CASE_ID,
        "Affaire Estelle Mouzin. Monique Olivier a confirmé « l'implication » de Michel Fourniret",
        "Estelle Mouzin case: Monique Olivier confirmed Michel Fourniret's involvement",
        "Ouest-France", "Redaction", "https://www.ouest-france.fr/societe/justice/affaire-estelle-mouzin-monique-olivier-a-confirme-l-implication-de-michel-fourniret-7016457",
        "2020-10-15", "press", "CONFIRMED", VERIFIED_AT,
        "Compte rendu de la reconstitution du 15 octobre 2020 à Guermantes.",
        "Report on the reconstruction of 15 October 2020 in Guermantes.",
    ),
]

# ------------------------------------------------------------------ CASE ----
CASE = {
    "id": CASE_ID,
    "title": txt("L'affaire Estelle Mouzin", "The Estelle Mouzin case"),
    "subtitle": txt(
        "Guermantes, 9 janvier 2003. Neuf ans, un trajet de quelques centaines de mètres, et dix-sept ans d'enquête.",
        "Guermantes, 9 January 2003. Nine years old, a journey of a few hundred metres, and seventeen years of investigation.",
    ),
    "country": "FR",
    "region": "Île-de-France / Seine-et-Marne",
    "city": "Guermantes",
    "year_start": 2003,
    "year_end": 2025,
    "period_label": txt("2003 – 2025", "2003 – 2025"),
    "status": "PARTIALLY_RESOLVED",
    "status_note": txt(
        "Une condamnation pour complicité a été prononcée en 2023 ; l'auteur principal est décédé en détention en 2021 sans avoir été jugé pour ces faits, et le corps n'a jamais été retrouvé.",
        "A conviction for complicity was handed down in 2023; the principal author died in custody in 2021 without being tried for these facts, and the body was never found.",
    ),
    "type": "disappearance",
    "tags": ["child_victim", "cold_case", "dna", "france", "judicial_failures", "serial_link"],
    "tier": "FREE",
    "editorial": "yanis",
    "published_at": "2026-09-24",
    "sensitive": True,
    "triggers": txt(
        "Enlèvement et mort d'un enfant, violences sexuelles évoquées sans description, défaillances institutionnelles.",
        "Abduction and death of a child, sexual violence mentioned without description, institutional failures.",
    ),
    "lat": 48.87,
    "lon": 2.7,
    "cover": "cover-mouzin",
    "stats": {
        "victims_documented": 1,
        "duration_years": 22,
        "magistrates_succession": 10,
    },
    "summary": txt(
        "Le 9 janvier 2003, Estelle Mouzin, 9 ans, ne rentre pas de l'école à Guermantes, en Seine-et-Marne. "
        "Les recherches sont immédiates et massives : les habitants sont entendus, les logements perquisitionnés, "
        "les bois ratissés. Une information judiciaire est ouverte à Meaux. La piste d'un tueur en série déjà "
        "incarcéré, Michel Fourniret, est envisagée dès 2003 puis écartée au profit d'un alibi téléphonique. "
        "Il faudra attendre 2019, le dépaysement du dossier à Paris et le travail d'une nouvelle juge d'instruction "
        "pour que cette piste redevienne centrale. Les aveux partiels de Fourniret en 2020, ceux de son ex-épouse "
        "Monique Olivier, une trace d'ADN partiel retrouvée sur un matelas saisi en 2003, une reconstitution, "
        "des fouilles : le corps ne sera jamais retrouvé. En décembre 2023, Monique Olivier est condamnée à la "
        "réclusion criminelle à perpétuité pour complicité. Le 3 septembre 2025, l'État est condamné pour faute "
        "lourde dans la conduite de l'enquête.",
        "On 9 January 2003, Estelle Mouzin, 9, did not come home from school in Guermantes, Seine-et-Marne. "
        "The search was immediate and massive: residents were heard, homes searched, woods combed. A judicial "
        "investigation was opened in Meaux. The lead of a serial killer already imprisoned, Michel Fourniret, "
        "was considered as early as 2003 and then discarded in favour of a telephone alibi. It took until 2019, "
        "the transfer of the file to Paris and the work of a new investigating judge, for that lead to become "
        "central again. Fourniret's partial confessions in 2020, those of his ex-wife Monique Olivier, a partial "
        "DNA trace found on a mattress seized in 2003, a reconstruction, searches: the body was never recovered. "
        "In December 2023, Monique Olivier was sentenced to life imprisonment for complicity. On 3 September 2025, "
        "the State was condemned for gross negligence in the conduct of the investigation.",
    ),
    "sources": SOURCES,
}

# -------------------------------------------------------------- VICTIMS ----
VICTIMS = [

{
        "order": 0,
        "first_name": "Estelle",
        "last_name": "Mouzin",
        "age": "9",
        "anonymised": False,
        "reliability": "CONFIRMED",
        "source": "franceinfo-chronologie",
        "life": {
            "fr": {
                "headline": "Qui était Estelle avant le 9 janvier 2003 ?",
                "items": [
                    {"label": "Prénom", "text": "Estelle."},
                    {"label": "Âge", "text": "9 ans au moment de sa disparition."},
                    {"label": "Lieu de vie", "text": "Guermantes, petite commune de Seine-et-Marne d'environ 1 400 habitants."},
                    {"label": "Scolarité", "text": "Élève à l'école de Guermantes ; le trajet école-domicile se faisait à pied."},
                    {"label": "Famille", "text": "Son père, Éric Mouzin, a mené pendant plus de vingt ans les démarches pour faire reconnaître les manquements de l'enquête."},
                ],
                "note": "Cette fiche est volontairement incomplète : les éléments de vie personnelle (passions, amis, projets) relèvent de la famille et ne figurent pas dans les sources publiques consultées. L'application n'invente rien pour combler un vide.",
            },
            "en": {
                "headline": "Who was Estelle before 9 January 2003?",
                "items": [
                    {"label": "First name", "text": "Estelle."},
                    {"label": "Age", "text": "9 years old at the time of her disappearance."},
                    {"label": "Place of life", "text": "Guermantes, a small Seine-et-Marne commune of about 1,400 inhabitants."},
                    {"label": "Schooling", "text": "Pupil at the Guermantes school; the school-to-home journey was made on foot."},
                    {"label": "Family", "text": "Her father, Éric Mouzin, pursued for over twenty years the steps needed to have the investigation's failures recognised."},
                ],
                "note": "This file is deliberately incomplete: personal details (passions, friends, projects) belong to the family and do not appear in the public sources consulted. The application invents nothing to fill a gap.",
            },
        },
        "disappearance": {
            "fr": {
                "items": [
                    {"label": "Date", "text": "9 janvier 2003, au retour de l'école, entre l'école et le domicile."},
                    {"label": "Premières recherches", "text": "Les quelque 1 400 habitants de la commune sont interrogés, les logements perquisitionnés, les bois environnants ratissés."},
                    {"label": "Cadre judiciaire", "text": "Information judiciaire ouverte à Meaux pour enlèvement et séquestration de mineur de 15 ans."},
                    {"label": "Découverte", "text": "Le corps n'a jamais été retrouvé."},
                    {"label": "Identification", "text": "En août 2020, une trace d'ADN partiel de l'enfant est retrouvée sur un matelas saisi en 2003 dans une maison de Ville-sur-Lumes (Ardennes)."},
                ],
            },
            "en": {
                "items": [
                    {"label": "Date", "text": "9 January 2003, on the way home from school, between the school and the house."},
                    {"label": "First searches", "text": "The commune's roughly 1,400 inhabitants were questioned, homes searched, surrounding woods combed."},
                    {"label": "Judicial frame", "text": "Judicial investigation opened in Meaux for abduction and confinement of a minor under 15."},
                    {"label": "Discovery", "text": "The body was never recovered."},
                    {"label": "Identification", "text": "In August 2020, a partial DNA trace of the child was found on a mattress seized in 2003 in a house in Ville-sur-Lumes (Ardennes)."},
                ],
            },
        },
    },
]

MEMORIAL = {
    "title": txt("Estelle Mouzin (2003)", "Estelle Mouzin (2003)"),
    "biography": txt(
        "Estelle Mouzin avait 9 ans. Elle vivait à Guermantes et rentrait de l'école à pied le 9 janvier 2003. "
        "Elle n'est jamais arrivée chez elle. Son père, Éric Mouzin, est devenu l'une des figures publiques de la "
        "lutte contre l'oubli judiciaire : marches blanches, demandes d'actes, assignation de l'État. Le 3 septembre "
        "2025, le tribunal judiciaire de Paris a reconnu une faute lourde de l'État dans la conduite de l'enquête et "
        "lui a accordé 50 000 euros au titre du préjudice moral.",
        "Estelle Mouzin was 9 years old. She lived in Guermantes and walked home from school on 9 January 2003. "
        "She never arrived. Her father, Éric Mouzin, became one of the public figures of the fight against judicial "
        "oblivion: white marches, requests for investigative acts, suing the State. On 3 September 2025, the Paris "
        "judicial court recognised gross negligence by the State in the conduct of the investigation and awarded him "
        "50,000 euros for moral damages.",
    ),
    "testimony": txt(
        "« L'essentiel, c'est de retrouver le corps d'Estelle Mouzin. C'est désormais la seule énigme du dossier. » "
        "— Me Richard Delgenes, avocat de Monique Olivier, octobre 2020 (propos rapportés par la presse).",
        "'The essential thing is to find Estelle Mouzin's body. That is now the only enigma in the file.' "
        "— Richard Delgenes, Monique Olivier's lawyer, October 2020 (as reported by the press).",
    ),
    "memory": txt(
        "Ce dossier rappelle une chose simple : une enquête peut être relancée, un auteur peut avouer, une complice "
        "peut être condamnée, et la famille rester sans sépulture. La mémoire d'Estelle Mouzin ne se réduit pas à la "
        "résolution judiciaire.",
        "This case recalls something simple: an investigation can be reopened, an author can confess, an accomplice "
        "can be convicted, and the family can remain without a grave. Estelle Mouzin's memory is not reduced to the "
        "judicial outcome.",
    ),
    "reliability": "CONFIRMED",
}

# ------------------------------------------------------------- TIMELINE ----
TIMELINE = [
    fact(
        "Estelle Mouzin, 9 ans, disparaît sur le chemin du retour de l'école à Guermantes (Seine-et-Marne).",
        "Estelle Mouzin, 9, disappears on her way home from school in Guermantes (Seine-et-Marne).",
        "CONFIRMED", "franceinfo-chronologie",
        "Disparition", "Disappearance", "2003-01-09",
    ),
    fact(
        "Une information judiciaire pour enlèvement et séquestration de mineur de 15 ans est ouverte à Meaux. "
        "Les habitants de la commune sont interrogés, les logements perquisitionnés, les bois ratissés.",
        "A judicial investigation for abduction and confinement of a minor under 15 is opened in Meaux. "
        "Residents are questioned, homes searched, woods combed.",
        "CONFIRMED", "franceinfo-chronologie",
        "Premières investigations", "First investigations", "2003-01",
    ),
    fact(
        "La piste de Michel Fourniret, tueur en série déjà incarcéré, est envisagée. Des éléments matériels sont "
        "découverts lors de perquisitions : une cassette vidéo contenant un reportage sur la disparition, et des "
        "photographies de l'enfant sur son ordinateur.",
        "The lead of Michel Fourniret, a serial killer already imprisoned, is considered. Material elements are found "
        "during searches: a video cassette containing a report on the disappearance, and photographs of the child on his computer.",
        "PROBABLE", "marieclaire-temps-forts",
        "Une piste ouverte", "A lead opened", "2003",
    ),
    fact(
        "Fourniret dispose d'un alibi : un appel passé le soir du 9 janvier 2003 depuis son domicile belge de "
        "Sart-Custinne, à environ 250 kilomètres de Guermantes, pour souhaiter un bon anniversaire à son fils. "
        "Les relevés téléphoniques l'attestent. Les enquêteurs estiment l'alibi solide et la piste est écartée.",
        "Fourniret has an alibi: a call placed on the evening of 9 January 2003 from his Belgian home in "
        "Sart-Custinne, about 250 kilometres from Guermantes, to wish his son a happy birthday. Phone records attest it. "
        "Investigators considered the alibi solid and the lead was set aside.",
        "CONFIRMED", "monde-5dates",
        "L'alibi", "The alibi", "2003",
    ),
    fact(
        "Le dossier est dépaysé à Paris. L'instruction est reprise par la juge Sabine Kheris.",
        "The file is transferred to Paris. The investigation is taken over by judge Sabine Kheris.",
        "CONFIRMED", "marieclaire-temps-forts",
        "Dépaysement", "Transfer of jurisdiction", "2019",
    ),
    fact(
        "Entendu sur une autre affaire, Michel Fourniret évoque l'affaire Estelle Mouzin et dit avoir des "
        "« explications » à donner. Il ne formule aucun aveu à ce stade.",
        "Heard in another case, Michel Fourniret mentions the Estelle Mouzin case and says he has "
        "'explanations' to give. He makes no confession at this stage.",
        "CONFIRMED", "marieclaire-temps-forts",
        "Première mention", "First mention", "2019-03-14",
    ),
    fact(
        "Monique Olivier, ex-épouse de Michel Fourniret, accuse ce dernier d'avoir enlevé, violé puis étranglé "
        "Estelle Mouzin. Elle est mise en examen pour complicité d'enlèvement et séquestration suivis de mort.",
        "Monique Olivier, Michel Fourniret's ex-wife, accuses him of having abducted, raped then strangled "
        "Estelle Mouzin. She is indicted for complicity in abduction and confinement followed by death.",
        "CONFIRMED", "monde-5dates",
        "Accusation", "Accusation", "2020-01",
    ),
    fact(
        "Michel Fourniret reconnaît sa responsabilité devant la juge d'instruction : « Je reconnais là un être qui "
        "n'est plus là par ma faute. » Il estime « pertinent » que le corps puisse se trouver dans l'une de ses "
        "anciennes propriétés, sans préciser les conditions de l'enlèvement ni celles de la mort.",
        "Michel Fourniret acknowledges his responsibility before the investigating judge: 'I acknowledge here a being "
        "who is no longer there through my fault.' He considers it 'relevant' that the body might be on one of his "
        "former properties, without specifying the conditions of the abduction or of the death.",
        "CONFIRMED", "monde-5dates",
        "Aveux partiels", "Partial confession", "2020-03",
    ),
    fact(
        "À l'issue d'une nouvelle expertise, une trace d'ADN partiel de l'enfant est retrouvée sur un matelas saisi "
        "en 2003 dans la maison de Ville-sur-Lumes (Ardennes), ancienne propriété de la sœur défunte de Michel Fourniret.",
        "Following a new expert examination, a partial DNA trace of the child is found on a mattress seized in 2003 "
        "in the Ville-sur-Lumes house (Ardennes), former property of Michel Fourniret's late sister.",
        "CONFIRMED", "franceinfo-chronologie",
        "Trace biologique", "Biological trace", "2020-08-21",
    ),
    fact(
        "Reconstitution de six heures à Guermantes. Monique Olivier confirme « l'implication » de Michel Fourniret, "
        "qui reconnaît Estelle sur une photographie mais refuse de donner des précisions.",
        "Six-hour reconstruction in Guermantes. Monique Olivier confirms Michel Fourniret's 'involvement'; "
        "he recognises Estelle in a photograph but refuses to give details.",
        "CONFIRMED", "ouestfrance-reconstitution",
        "Reconstitution", "Reconstruction", "2020-10-15",
    ),
    fact(
        "Fouilles dans les Ardennes, notamment à Issancourt-et-Rumel, sur des lieux désignés. Le corps n'est pas retrouvé.",
        "Searches in the Ardennes, notably at Issancourt-et-Rumel, on designated sites. The body is not found.",
        "CONFIRMED", "franceinfo-chronologie",
        "Fouilles", "Searches", "2020-10",
    ),
    fact(
        "Monique Olivier reconnaît avoir joué un rôle dans la séquestration et avoir transporté le corps.",
        "Monique Olivier acknowledges having played a role in the confinement and having transported the body.",
        "CONFIRMED", "franceinfo-chronologie",
        "Aveux de la complice", "Accomplice's admissions", "2021-04",
    ),
    fact(
        "Michel Fourniret meurt en détention à 79 ans. En droit français, la mort éteint l'action publique : il ne "
        "sera pas jugé pour les faits concernant Estelle Mouzin.",
        "Michel Fourniret dies in custody aged 79. Under French law, death extinguishes public prosecution: he will "
        "not be tried for the facts concerning Estelle Mouzin.",
        "CONFIRMED", "actu-guermantes",
        "Décès de l'auteur", "Death of the author", "2021-05-10",
    ),
    fact(
        "De nouvelles fouilles sont menées dans les Ardennes en 2021 et 2022. Aucune trace du corps.",
        "Further searches are carried out in the Ardennes in 2021 and 2022. No trace of the body.",
        "CONFIRMED", "marieclaire-temps-forts",
        "Recherches renouvelées", "Renewed searches", "2022",
    ),
    fact(
        "Procès de Monique Olivier devant la cour d'assises des Hauts-de-Seine à Nanterre, du 28 novembre au "
        "19 décembre 2023. Verdict : réclusion criminelle à perpétuité, assortie d'une période de sûreté de 20 ans, "
        "pour complicité dans l'enlèvement, la séquestration et la mort d'Estelle Mouzin, de Joanna Parrish et de "
        "Marie-Angèle Domèce. La cour relève une implication « totale » et une personnalité « sans empathie ».",
        "Trial of Monique Olivier before the Hauts-de-Seine assize court in Nanterre, from 28 November to "
        "19 December 2023. Verdict: life imprisonment with a 20-year minimum term, for complicity in the abduction, "
        "confinement and death of Estelle Mouzin, Joanna Parrish and Marie-Angèle Domèce. The court notes 'total' "
        "involvement and a personality 'without empathy'.",
        "CONFIRMED", "franceinfo-olivier-2023",
        "Procès et verdict", "Trial and verdict", "2023-12-19",
    ),
    fact(
        "Le tribunal judiciaire de Paris condamne l'État pour faute lourde dans l'enquête : 50 000 euros de "
        "préjudice moral à Éric Mouzin. Le jugement vise le manque de moyens humains, les dysfonctionnements, la "
        "succession de dix magistrats, l'absence de procès-verbal de synthèse et un dossier jamais coté. Il souligne "
        "aussi que des actes d'investigation d'une ampleur exceptionnelle ont été réalisés.",
        "The Paris judicial court condemns the State for gross negligence in the investigation: 50,000 euros in moral "
        "damages to Éric Mouzin. The ruling targets the lack of human resources, the dysfunctions, the succession of "
        "ten magistrates, the absence of a synthesis report and a file never paginated. It also notes that "
        "investigative acts of exceptional scale were carried out.",
        "CONFIRMED", "rtl-faute-lourde",
        "Faute lourde de l'État", "Gross negligence of the State", "2025-09-03",
    ),
]

TIMELINE_PHASES = [
    ("2003-01-09", "disappearance"), ("2003-01", "investigation"), ("2003", "investigation"),
    ("2003", "investigation"), ("2019", "investigation"), ("2019-03-14", "investigation"),
    ("2020-01", "investigation"), ("2020-03", "investigation"), ("2020-08-21", "evidence"),
    ("2020-10-15", "investigation"), ("2020-10", "investigation"), ("2021-04", "investigation"),
    ("2021-05-10", "after"), ("2022", "investigation"), ("2023-12-19", "trial"),
    ("2025-09-03", "after"),
]

# ------------------------------------------------------------- LOCATIONS ----
LOCATIONS = [
    {
        "kind": "city", "names": txt("Guermantes (Seine-et-Marne)", "Guermantes (Seine-et-Marne)"),
        "city": "Guermantes", "region": "Seine-et-Marne", "country": "FR",
        "lat": 48.87, "lon": 2.70, "precision": "city", "date": "2003-01-09",
        "note": txt(
            "Lieu de la disparition. Conformément à la charte éditoriale, aucune adresse privée exacte n'est affichée : "
            "seule la commune est géolocalisée.",
            "Place of the disappearance. In line with the editorial charter, no exact private address is displayed: "
            "only the commune is geolocated.",
        ),
        "reliability": "CONFIRMED", "source": "franceinfo-chronologie",
    },
    {
        "kind": "city", "names": txt("Ville-sur-Lumes (Ardennes)", "Ville-sur-Lumes (Ardennes)"),
        "city": "Ville-sur-Lumes", "region": "Ardennes", "country": "FR",
        "lat": 49.79, "lon": 4.79, "precision": "city", "date": "2020-08-21",
        "note": txt(
            "Maison de la sœur défunte de Michel Fourniret, désignée par Monique Olivier ; un matelas y avait été saisi en 2003.",
            "House of Michel Fourniret's late sister, designated by Monique Olivier; a mattress had been seized there in 2003.",
        ),
        "reliability": "CONFIRMED", "source": "monde-5dates",
    },
    {
        "kind": "city", "names": txt("Sart-Custinne (Belgique)", "Sart-Custinne (Belgium)"),
        "city": "Sart-Custinne", "region": "Namur", "country": "BE",
        "lat": 50.20, "lon": 4.98, "precision": "city", "date": "2003-01-09",
        "note": txt("Domicile belge invoqué dans l'alibi téléphonique de 2003.", "Belgian home invoked in the 2003 telephone alibi."),
        "reliability": "CONFIRMED", "source": "monde-5dates",
    },
    {
        "kind": "court", "names": txt("Cour d'assises des Hauts-de-Seine, Nanterre", "Hauts-de-Seine Assize Court, Nanterre"),
        "city": "Nanterre", "region": "Hauts-de-Seine", "country": "FR",
        "lat": 48.89, "lon": 2.20, "precision": "city", "date": "2023-12-19",
        "note": txt("Procès de Monique Olivier, 28 novembre – 19 décembre 2023.", "Trial of Monique Olivier, 28 November – 19 December 2023."),
        "reliability": "CONFIRMED", "source": "franceinfo-olivier-2023",
    },
]

# -------------------------------------------------------------- EVIDENCE ----
EVIDENCE = [
    {
        "kind": "digital", "weight": "documented", "reliability": "PROBABLE", "source": "marieclaire-temps-forts",
        "title": txt("Reportage vidéo et photographies", "Video report and photographs"),
        "description": txt(
            "Lors de perquisitions, une cassette vidéo contenant un reportage sur la disparition d'Estelle Mouzin est "
            "retrouvée, ainsi que des photographies de l'enfant sur un ordinateur. Michel Fourniret nie toute "
            "implication et évoque un intérêt pour cette disparition.",
            "During searches, a video cassette containing a report on Estelle Mouzin's disappearance was found, as well "
            "as photographs of the child on a computer. Michel Fourniret denied any involvement and spoke of an interest "
            "in the disappearance.",
        ),
    },
    {
        "kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "monde-5dates",
        "title": txt("Relevés téléphoniques du 9 janvier 2003", "Phone records of 9 January 2003"),
        "description": txt(
            "Un appel passé le soir du 9 janvier 2003 depuis Sart-Custinne (Belgique) vers le fils de Michel Fourniret "
            "a longtemps constitué l'alibi central. Les relevés attestent l'appel ; leur portée géographique exacte au "
            "regard du trajet a été un enjeu d'instruction ultérieur.",
            "A call placed on the evening of 9 January 2003 from Sart-Custinne (Belgium) to Michel Fourniret's son long "
            "constituted the central alibi. Records attest the call; their exact geographic scope in relation to the "
            "journey became a later investigative issue.",
        ),
    },
    {
        "kind": "dna", "weight": "decisive", "reliability": "CONFIRMED", "source": "franceinfo-chronologie",
        "title": txt("Trace d'ADN partiel sur un matelas", "Partial DNA trace on a mattress"),
        "description": txt(
            "Le 21 août 2020, une nouvelle expertise révèle une trace d'ADN partiel d'Estelle Mouzin sur un matelas "
            "saisi dès 2003 dans la maison de Ville-sur-Lumes. L'objet était conservé depuis dix-sept ans.",
            "On 21 August 2020, a new expert examination revealed a partial DNA trace of Estelle Mouzin on a mattress "
            "seized as early as 2003 in the Ville-sur-Lumes house. The item had been kept for seventeen years.",
        ),
    },
    {
        "kind": "testimony", "weight": "decisive", "reliability": "CONFIRMED", "source": "monde-5dates",
        "title": txt("Déclarations de Monique Olivier", "Statements by Monique Olivier"),
        "description": txt(
            "En janvier 2020, Monique Olivier accuse Michel Fourniret. En août 2020, elle précise qu'il a séquestré, "
            "violé et tué l'enfant dans la maison de Ville-sur-Lumes. En avril 2021, elle reconnaît avoir transporté "
            "le corps. Ces déclarations ont été faites devant la juge d'instruction puis à l'audience.",
            "In January 2020, Monique Olivier accused Michel Fourniret. In August 2020, she specified that he confined, "
            "raped and killed the child in the Ville-sur-Lumes house. In April 2021, she acknowledged transporting the "
            "body. These statements were made before the investigating judge and then at the hearing.",
        ),
    },
    {
        "kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "rtl-faute-lourde",
        "title": txt("Jugement du 3 septembre 2025", "Ruling of 3 September 2025"),
        "description": txt(
            "Le tribunal judiciaire de Paris retient la faute lourde de l'État : manque de moyens humains, "
            "dysfonctionnements, succession de dix magistrats, absence de procès-verbal de synthèse, dossier jamais "
            "coté. Le même jugement constate des actes d'investigation d'une ampleur exceptionnelle et relève que rien "
            "ne permet de démontrer que la culpabilité du couple aurait pu être établie bien avant les aveux.",
            "The Paris judicial court found gross negligence by the State: lack of human resources, dysfunctions, "
            "succession of ten magistrates, absence of a synthesis report, file never paginated. The same ruling notes "
            "investigative acts of exceptional scale and that nothing shows the couple's guilt could have been "
            "established long before the admissions.",
        ),
    },
]

# --------------------------------------------------------- INVESTIGATION ----
INVESTIGATION = {
    "steps": [
        {
            "n": 1, "date": "2003-01-09",
            "title": txt("Une enfant ne rentre pas", "A child does not come home"),
            "body": txt(
                "Le 9 janvier 2003, Estelle Mouzin, 9 ans, ne revient pas de l'école à Guermantes. Le signalement est "
                "immédiat. Ce que les enquêteurs savent à cet instant : un trajet court et habituel, une heure de "
                "disparition resserrée, une commune de petite taille, une météo hivernale.",
                "On 9 January 2003, Estelle Mouzin, 9, did not return from school in Guermantes. The report was "
                "immediate. What investigators knew at that moment: a short, routine journey, a narrow window of "
                "disappearance, a small commune, winter weather.",
            ),
            "reliability": "CONFIRMED", "source": "franceinfo-chronologie", "premium": False,
        },
        {
            "n": 2, "date": "2003-01",
            "title": txt("Une commune entière passée au crible", "An entire commune put through the sieve"),
            "body": txt(
                "Les quelque 1 400 habitants sont interrogés, les logements perquisitionnés, les bois ratissés. "
                "Une information judiciaire est ouverte à Meaux. Ce travail de masse produit un volume considérable "
                "d'auditions sans aboutir à une identification.",
                "The roughly 1,400 inhabitants were questioned, homes searched, woods combed. A judicial investigation "
                "was opened in Meaux. This mass work produced a considerable volume of statements without leading to an "
                "identification.",
            ),
            "reliability": "CONFIRMED", "source": "franceinfo-chronologie", "premium": False,
        },
        {
            "n": 3, "date": "2003",
            "title": txt("Une piste déjà connue de la justice", "A lead already known to the justice system"),
            "body": txt(
                "La piste de Michel Fourniret est envisagée dès 2003. Des perquisitions mettent au jour un reportage "
                "vidéo sur la disparition et des photographies de l'enfant sur son ordinateur. Il nie et invoque un "
                "intérêt pour l'affaire.",
                "The Michel Fourniret lead was considered as early as 2003. Searches uncovered a video report on the "
                "disappearance and photographs of the child on his computer. He denied it and claimed an interest in the case.",
            ),
            "reliability": "PROBABLE", "source": "marieclaire-temps-forts", "premium": True,
        },
        {
            "n": 4, "date": "2003",
            "title": txt("L'alibi téléphonique", "The telephone alibi"),
            "body": txt(
                "Un appel passé depuis la Belgique le soir du 9 janvier 2003 place Michel Fourniret à environ 250 "
                "kilomètres de Guermantes. Les relevés téléphoniques l'attestent. Les enquêteurs estiment l'alibi "
                "solide ; la piste est écartée, et Guermantes ne correspond pas au secteur habituel de ses crimes.",
                "A call placed from Belgium on the evening of 9 January 2003 put Michel Fourniret about 250 kilometres "
                "from Guermantes. Phone records attest it. Investigators deemed the alibi solid; the lead was set "
                "aside, and Guermantes did not correspond to the usual area of his crimes.",
            ),
            "reliability": "CONFIRMED", "source": "monde-5dates", "premium": False,
        },
        {
            "n": 5, "date": "2004-2018",
            "title": txt("Quinze ans de sommeil du dossier", "Fifteen years of the file asleep"),
            "body": txt(
                "Le dossier est instruit à Meaux puis connaît une succession de magistrats. Le jugement de 2025 "
                "constatera : dix magistrats successifs, aucun procès-verbal de synthèse, un dossier jamais coté, "
                "c'est-à-dire dont aucune page n'était numérotée.",
                "The file was investigated in Meaux and then saw a succession of magistrates. The 2025 ruling would "
                "find: ten successive magistrates, no synthesis report, a file never paginated, meaning no page was numbered.",
            ),
            "reliability": "CONFIRMED", "source": "rtl-faute-lourde", "premium": True,
        },
        {
            "n": 6, "date": "2019",
            "title": txt("Le dépaysement", "The transfer"),
            "body": txt(
                "En 2019, le dossier est dépaysé à Paris, avec l'objectif affiché de favoriser la manifestation de la "
                "vérité avant que l'âge et la mémoire de Michel Fourniret ne l'empêchent définitivement. L'instruction "
                "est reprise par la juge Sabine Kheris.",
                "In 2019, the file was transferred to Paris, with the stated aim of facilitating the discovery of truth "
                "before Michel Fourniret's age and memory prevented it for good. Judge Sabine Kheris took over.",
            ),
            "reliability": "CONFIRMED", "source": "monde-5dates", "premium": False,
        },
        {
            "n": 7, "date": "2020-01",
            "title": txt("Une parole qui change le dossier", "A statement that changes the file"),
            "body": txt(
                "Monique Olivier accuse son ex-mari d'avoir enlevé, violé puis étranglé Estelle Mouzin. Elle est mise "
                "en examen pour complicité d'enlèvement et séquestration suivis de mort.",
                "Monique Olivier accused her ex-husband of abducting, raping and strangling Estelle Mouzin. She was "
                "indicted for complicity in abduction and confinement followed by death.",
            ),
            "reliability": "CONFIRMED", "source": "monde-5dates", "premium": True,
        },
        {
            "n": 8, "date": "2020-03",
            "title": txt("Des aveux à sa façon", "A confession in his own way"),
            "body": txt(
                "Michel Fourniret déclare : « Je reconnais là un être qui n'est plus là par ma faute. » Il n'indique "
                "ni les conditions de l'enlèvement, ni celles de la mort, ni le lieu du corps. Ses déclarations "
                "alambiquées et ses problèmes de mémoire ont constamment compliqué le travail des enquêteurs.",
                "Michel Fourniret declared: 'I acknowledge here a being who is no longer there through my fault.' He "
                "gave neither the conditions of the abduction, nor of the death, nor the location of the body. His "
                "convoluted statements and memory problems constantly complicated investigators' work.",
            ),
            "reliability": "CONFIRMED", "source": "monde-5dates", "premium": False,
        },
        {
            "n": 9, "date": "2020-08-21",
            "title": txt("Une trace conservée dix-sept ans", "A trace kept for seventeen years"),
            "body": txt(
                "Une nouvelle expertise révèle une trace d'ADN partiel d'Estelle Mouzin sur un matelas saisi en 2003. "
                "L'objet était sous main de justice depuis dix-sept ans : la science a changé, la scellé était resté.",
                "A new expert examination revealed a partial DNA trace of Estelle Mouzin on a mattress seized in 2003. "
                "The item had been in judicial custody for seventeen years: the science had changed, the seal had stayed.",
            ),
            "reliability": "CONFIRMED", "source": "franceinfo-chronologie", "premium": True,
        },
        {
            "n": 10, "date": "2020-10-15",
            "title": txt("Reconstitution et fouilles", "Reconstruction and searches"),
            "body": txt(
                "Une reconstitution de six heures se tient à Guermantes. Des fouilles suivent dans les Ardennes, sur "
                "des sites désignés, notamment Issancourt-et-Rumel. Elles ne permettent pas de retrouver le corps.",
                "A six-hour reconstruction was held in Guermantes. Searches followed in the Ardennes, on designated "
                "sites including Issancourt-et-Rumel. They did not recover the body.",
            ),
            "reliability": "CONFIRMED", "source": "ouestfrance-reconstitution", "premium": False,
        },
        {
            "n": 11, "date": "2023-12-19",
            "title": txt("Un procès sans l'auteur principal", "A trial without the principal author"),
            "body": txt(
                "Michel Fourniret étant décédé en 2021, l'action publique est éteinte à son égard. Monique Olivier "
                "comparaît seule. Elle est condamnée à la réclusion criminelle à perpétuité, avec 20 ans de sûreté.",
                "Michel Fourniret having died in 2021, public prosecution was extinguished with respect to him. Monique "
                "Olivier appeared alone. She was sentenced to life imprisonment with a 20-year minimum term.",
            ),
            "reliability": "CONFIRMED", "source": "franceinfo-olivier-2023", "premium": True,
        },
        {
            "n": 12, "date": "2025-09-03",
            "title": txt("L'État face à ses dysfonctionnements", "The State confronted with its dysfunctions"),
            "body": txt(
                "Le tribunal judiciaire de Paris condamne l'État pour faute lourde et accorde 50 000 euros à Éric "
                "Mouzin. Le jugement reconnaît les manquements tout en constatant l'ampleur exceptionnelle de "
                "certains actes d'investigation.",
                "The Paris judicial court condemned the State for gross negligence and awarded 50,000 euros to Éric "
                "Mouzin. The ruling recognised the failures while noting the exceptional scale of certain "
                "investigative acts.",
            ),
            "reliability": "CONFIRMED", "source": "rtl-faute-lourde", "premium": False,
        },
    ],
    "reality": txt(
        "Voici comment l'enquête s'est réellement déroulée : une piste envisagée dès 2003, écartée sur la foi d'un "
        "alibi téléphonique, puis reprise seize ans plus tard après un dépaysement, et conclue par des aveux "
        "successifs, une trace biologique retrouvée sur un scellé ancien, une condamnation pour complicité et une "
        "décision civile reconnaissant la faute lourde de l'État. Le corps n'a jamais été retrouvé.",
        "This is how the investigation actually unfolded: a lead considered as early as 2003, set aside on the strength "
        "of a telephone alibi, then taken up sixteen years later after a transfer of jurisdiction, and concluded by "
        "successive confessions, a biological trace found on an old exhibit, a conviction for complicity and a civil "
        "decision recognising gross negligence by the State. The body was never recovered.",
    ),
    "errors": [
        item(
            "Une piste écartée trop vite : la piste Fourniret, envisagée en 2003, a été abandonnée au profit d'un "
            "alibi téléphonique que l'instruction ultérieure a remis en perspective.",
            "A lead set aside too quickly: the Fourniret lead, considered in 2003, was abandoned in favour of a "
            "telephone alibi that later investigation put into perspective.",
            "CONFIRMED", "rtl-faute-lourde", "Écart de piste", "Discarded lead",
        ),
        item(
            "Absence de procès-verbal de synthèse : aucun document ne résumait l'enquête pour les magistrats suivants.",
            "Absence of a synthesis report: no document summarised the investigation for the following magistrates.",
            "CONFIRMED", "rtl-faute-lourde", "Perte d'information", "Loss of information",
        ),
        item(
            "Dossier jamais coté : aucune page n'était numérotée, ce que le jugement de 2025 décrit comme un dossier "
            "impossible à lire méthodiquement.",
            "File never paginated: no page was numbered, which the 2025 ruling describes as a file impossible to read "
            "methodically.",
            "CONFIRMED", "rtl-faute-lourde", "Désordre procédural", "Procedural disorder",
        ),
        item(
            "Succession de dix magistrats sans transmission structurée.",
            "Succession of ten magistrates without structured handover.",
            "CONFIRMED", "rtl-faute-lourde", "Continuité", "Continuity",
        ),
        item(
            "Un scellé décisif est resté dix-sept ans sans exploitation au niveau atteint en 2020 : le matelas saisi "
            "en 2003 n'a livré une trace d'ADN partiel qu'après une nouvelle expertise.",
            "A decisive exhibit remained seventeen years without exploitation at the level reached in 2020: the "
            "mattress seized in 2003 yielded a partial DNA trace only after a new examination.",
            "CONFIRMED", "franceinfo-chronologie", "Science différée", "Deferred science",
        ),
    ],
    "cold_case": {
        "what_we_know": [
            item("Estelle Mouzin, 9 ans, a disparu le 9 janvier 2003 à Guermantes.",
                 "Estelle Mouzin, 9, disappeared on 9 January 2003 in Guermantes.", "CONFIRMED", "franceinfo-chronologie"),
            item("Michel Fourniret a reconnu sa responsabilité en mars 2020.",
                 "Michel Fourniret acknowledged his responsibility in March 2020.", "CONFIRMED", "monde-5dates"),
            item("Une trace d'ADN partiel a été identifiée en août 2020 sur un matelas saisi en 2003.",
                 "A partial DNA trace was identified in August 2020 on a mattress seized in 2003.", "CONFIRMED", "franceinfo-chronologie"),
            item("Monique Olivier a été condamnée pour complicité le 19 décembre 2023.",
                 "Monique Olivier was convicted of complicity on 19 December 2023.", "CONFIRMED", "franceinfo-olivier-2023"),
        ],
        "what_is_probable": [
            item("Selon les déclarations de Monique Olivier, la séquestration s'est déroulée à Ville-sur-Lumes et le "
                 "corps a été transporté puis enfoui par Michel Fourniret.",
                 "According to Monique Olivier's statements, the confinement took place in Ville-sur-Lumes and the body "
                 "was transported then buried by Michel Fourniret.", "PROBABLE", "monde-5dates"),
        ],
        "what_is_disputed": [
            item("La portée réelle de l'alibi téléphonique de 2003 : l'appel est attesté, son articulation avec un "
                 "déplacement reste un point d'instruction discuté.",
                 "The actual scope of the 2003 telephone alibi: the call is attested, its articulation with a journey "
                 "remains a debated investigative point.", "DISPUTED", "monde-5dates"),
        ],
        "what_is_unknown": [
            item("Le lieu où se trouve le corps.", "The place where the body lies.", "UNKNOWN", "franceinfo-chronologie"),
            item("Les circonstances précises de l'enlèvement et de la mort, jamais détaillées par Michel Fourniret.",
                 "The precise circumstances of the abduction and death, never detailed by Michel Fourniret.",
                 "UNKNOWN", "monde-5dates"),
        ],
        "latest_progress": [
            item("3 septembre 2025 : condamnation de l'État pour faute lourde par le tribunal judiciaire de Paris.",
                 "3 September 2025: the State condemned for gross negligence by the Paris judicial court.",
                 "CONFIRMED", "rtl-faute-lourde"),
            item("Fouilles 2021-2022 dans les Ardennes : sans résultat.",
                 "2021-2022 searches in the Ardennes: no result.", "CONFIRMED", "marieclaire-temps-forts"),
        ],
        "leads": [
            item("Les anciennes propriétés du couple Fourniret-Olivier, dont certaines ont fait l'objet de fouilles.",
                 "The former properties of the Fourniret-Olivier couple, some of which were searched.",
                 "PROBABLE", "franceinfo-chronologie"),
        ],
        "limits": [
            item("L'auteur principal est décédé : plus aucune audience ne permettra de l'interroger.",
                 "The principal author is dead: no hearing will ever allow him to be questioned.",
                 "CONFIRMED", "actu-guermantes"),
        ],
    },
}

# ------------------------------------------------------------ PSYCHOLOGY ----
PSYCHOLOGY = {
    "disclaimer": txt(
        "Aucun diagnostic psychiatrique n'est posé ici. Les éléments ci-dessous distinguent systématiquement le fait "
        "documenté, l'hypothèse, l'analyse d'expert et l'inconnu.",
        "No psychiatric diagnosis is made here. The elements below systematically distinguish documented fact, "
        "hypothesis, expert analysis and unknown.",
    ),
    "blocks": [
        block(
            "fact", "Ce que l'on sait du parcours judiciaire antérieur",
            "What is known of the prior judicial history",
            "Michel Fourniret avait été condamné en mai 2008 par la cour d'assises des Ardennes à la réclusion "
            "criminelle à perpétuité, assortie d'une période de sûreté de 28 ans, pour les meurtres de sept jeunes "
            "femmes ou adolescentes commis entre 1987 et 2001, puis en 2018 à 20 ans de réclusion pour un "
            "assassinat crapuleux. Il était donc incarcéré au moment de l'intérêt porté à l'affaire Estelle Mouzin.",
            "Michel Fourniret had been sentenced in May 2008 by the Ardennes assize court to life imprisonment with a "
            "28-year minimum term for the murders of seven young women or teenagers committed between 1987 and 2001, "
            "then in 2018 to 20 years for a mercenary assassination. He was therefore imprisoned at the time interest "
            "was taken in the Estelle Mouzin case.",
            "CONFIRMED", "franceinfo-olivier-2023",
        ),
        block(
            "behaviour", "Le contrôle de la parole", "Control of speech",
            "", "", "CONFIRMED", "monde-5dates",
            items=[
                item("Des aveux formulés de manière partielle et différée : reconnaissance de responsabilité sans "
                     "récit des circonstances.",
                     "Confessions formulated in a partial and delayed way: acknowledgement of responsibility without "
                     "an account of the circumstances.", "CONFIRMED", "monde-5dates"),
                item("Des déclarations décrites comme alambiquées, accompagnées de problèmes de mémoire.",
                     "Statements described as convoluted, accompanied by memory problems.", "PROBABLE", "monde-5dates"),
                item("Une dénégation initiale accompagnée d'une justification : un « intérêt » pour la disparition.",
                     "An initial denial accompanied by a justification: an 'interest' in the disappearance.",
                     "PROBABLE", "marieclaire-temps-forts"),
            ],
        ),
        block(
            "expert", "Ce que la cour a retenu de la personnalité de la complice",
            "What the court retained about the accomplice's personality",
            "Dans ses motivations, la cour d'assises des Hauts-de-Seine a décrit Monique Olivier comme une « complice "
            "active » et non comme une épouse « passive » ou « soumise » telle que certains experts-psychologues "
            "l'avaient décrite, et a relevé une personnalité « sans empathie » ni « affect pour des victimes "
            "déshumanisées ». C'est une appréciation juridictionnelle, pas un diagnostic médical.",
            "In its reasoning, the Hauts-de-Seine assize court described Monique Olivier as an 'active accomplice' and "
            "not as a 'passive' or 'submissive' wife as some expert psychologists had described her, and noted a "
            "personality 'without empathy' or 'affect for dehumanised victims'. This is a judicial assessment, not a "
            "medical diagnosis.",
            "CONFIRMED", "franceinfo-olivier-2023",
        ),
        block(
            "unknown", "Ce que l'on ne saura pas", "What we will not know",
            "Les conditions de l'enlèvement, le déroulé de la séquestration et les circonstances de la mort n'ont "
            "jamais été décrits par l'auteur. Aucune audience ne permettra de l'interroger.",
            "The conditions of the abduction, the course of the confinement and the circumstances of death were never "
            "described by the author. No hearing will allow him to be questioned.",
            "UNKNOWN", "monde-5dates",
        ),
    ],
}

# ---------------------------------------------------------- VICTIMOLOGY ----
VICTIMOLOGY = {
    "ethics_note": txt(
        "Les éléments ci-dessous décrivent un contexte documenté. Aucune caractéristique de la victime n'explique ni "
        "ne justifie moralement le crime : la responsabilité appartient exclusivement à l'auteur.",
        "The elements below describe a documented context. No characteristic of the victim explains or morally "
        "justifies the crime: responsibility belongs exclusively to the author.",
    ),
    "blocks": [
        block("context", "Un trajet court et habituel", "A short, routine journey",
              "Estelle Mouzin rentrait de l'école à pied, sur un parcours familier, dans une commune de petite "
              "taille où les habitants se connaissent. La disparition intervient en fin de journée, en hiver.",
              "Estelle Mouzin walked home from school along a familiar route, in a small commune where residents know "
              "each other. The disappearance occurred at the end of the day, in winter.",
              "CONFIRMED", "franceinfo-chronologie"),
        block("vulnerability", "Une vulnérabilité d'âge", "An age-based vulnerability",
              "Une enfant de 9 ans circulant seule dispose d'une capacité de résistance et d'alerte limitée. C'est un "
              "facteur situationnel documenté, pas une caractéristique personnelle imputable à la victime.",
              "A 9-year-old child moving alone has limited capacity to resist or raise an alarm. This is a documented "
              "situational factor, not a personal characteristic attributable to the victim.",
              "CONFIRMED", "franceinfo-chronologie"),
        block("analysis", "Ce que la victimologie apporte à l'enquête", "What victimology brings to the investigation",
              "Dans ce dossier, la victimologie a surtout servi à établir que la disparition n'entrait pas dans le "
              "secteur géographique habituellement retenu pour Michel Fourniret — un argument qui a pesé dans "
              "l'abandon de la piste en 2003. L'instruction ultérieure a montré qu'un auteur pouvait agir hors de sa "
              "zone habituelle.",
              "In this file, victimology mainly served to establish that the disappearance did not fall within the "
              "geographic area usually associated with Michel Fourniret — an argument that weighed in abandoning the "
              "lead in 2003. Later investigation showed that an author could act outside his usual area.",
              "CONFIRMED", "marieclaire-temps-forts"),
    ],
}

# ---------------------------------------------------------------- COURT ----
COURT = {
    "jurisdiction": txt("France — cour d'assises des Hauts-de-Seine (Nanterre) ; tribunal judiciaire de Paris",
                        "France — Hauts-de-Seine Assize Court (Nanterre); Paris judicial court"),
    "verdict": txt(
        "Monique Olivier déclarée coupable de complicité dans l'enlèvement, la séquestration et la mort d'Estelle "
        "Mouzin, de Joanna Parrish et de Marie-Angèle Domèce (19 décembre 2023). Michel Fourniret, décédé le 10 mai "
        "2021, n'a pas été jugé pour ces faits : la mort éteint l'action publique.",
        "Monique Olivier found guilty of complicity in the abduction, confinement and death of Estelle Mouzin, Joanna "
        "Parrish and Marie-Angèle Domèce (19 December 2023). Michel Fourniret, who died on 10 May 2021, was not tried "
        "for these facts: death extinguishes public prosecution.",
    ),
    "sentence": {
        "label": txt("Réclusion criminelle à perpétuité, période de sûreté de 20 ans",
                     "Life imprisonment with a 20-year minimum term"),
        "pronounced": "2023-12-19",
        "requested": txt("Le parquet avait requis la perpétuité assortie de 22 ans de sûreté.",
                         "The prosecution had requested life imprisonment with a 22-year minimum term."),
        "cumul": txt(
            "Cette peine se confond avec les condamnations antérieures : perpétuité avec 28 ans de sûreté en 2008 "
            "(cour d'assises des Ardennes), 20 ans en 2018 (assises des Yvelines). Selon le calcul du parquet, la "
            "condamnée ne sera pas libérable avant 2035.",
            "This sentence merges with previous convictions: life with a 28-year minimum term in 2008 (Ardennes assize "
            "court), 20 years in 2018 (Yvelines assize court). According to the prosecution's calculation, the "
            "convict will not be eligible for release before 2035.",
        ),
        "reasoning": txt(
            "La cour a qualifié la peine de « juste, adéquate et proportionnée à l'extrême gravité des faits où son "
            "implication est totale ».",
            "The court described the sentence as 'fair, adequate and proportionate to the extreme gravity of facts in "
            "which her involvement is total'.",
        ),
        "appeal": txt("La défense a indiqué ne pas faire appel pour ne pas « infliger un second procès aux parties civiles ».",
                      "The defence stated it would not appeal so as not to 'inflict a second trial on the civil parties'."),
        "reliability": "CONFIRMED",
        "source": "franceinfo-olivier-2023",
    },
    "consequences": [
        item("3 septembre 2025 : l'État est condamné pour faute lourde à verser 50 000 euros à Éric Mouzin au titre "
             "du préjudice moral.",
             "3 September 2025: the State is condemned for gross negligence to pay 50,000 euros to Éric Mouzin for "
             "moral damages.", "CONFIRMED", "rtl-faute-lourde"),
        item("Le jugement retient le manque de moyens humains et les dysfonctionnements, tout en constatant des actes "
             "d'investigation d'une ampleur exceptionnelle.",
             "The ruling cites the lack of human resources and the dysfunctions, while noting investigative acts of "
             "exceptional scale.", "CONFIRMED", "rtl-faute-lourde"),
        item("Le corps n'a jamais été retrouvé : pour la famille, l'affaire reste ouverte sur ce point.",
             "The body was never recovered: for the family, the case remains open on that point.",
             "CONFIRMED", "franceinfo-chronologie"),
    ],
}

# -------------------------------------------------------------- EXPERTS ----
EXPERTS = [
    {
        "label": txt("Analyse A — l'alibi comme élément suffisant (2003)", "Analysis A — the alibi as a sufficient element (2003)"),
        "field": "investigation",
        "position": txt(
            "Position retenue par les enquêteurs en 2003 : un relevé téléphonique attestant un appel à environ 250 km "
            "le soir des faits constitue un alibi solide ; le secteur géographique ne correspond pas aux crimes "
            "habituels de l'intéressé.",
            "Position held by investigators in 2003: a phone record attesting a call about 250 km away on the evening "
            "of the facts constitutes a solid alibi; the geographic area does not correspond to the person's usual crimes.",
        ),
        "reliability": "CONFIRMED", "source": "monde-5dates",
    },
    {
        "label": txt("Analyse B — la piste devait être maintenue", "Analysis B — the lead should have been maintained"),
        "field": "judicial_criticism",
        "position": txt(
            "Position portée par la famille et son avocat : la piste Fourniret a été envisagée dès 2003 et abandonnée "
            "trop vite ; le jugement civil de 2025 reconnaît une faute lourde de l'État dans la conduite de l'enquête.",
            "Position carried by the family and its lawyer: the Fourniret lead was considered as early as 2003 and "
            "abandoned too quickly; the 2025 civil ruling recognises gross negligence by the State in the conduct of "
            "the investigation.",
        ),
        "reliability": "CONFIRMED", "source": "rtl-faute-lourde",
    },
    {
        "label": txt("Point de nuance du même jugement", "Nuance in the same ruling"),
        "field": "judicial",
        "position": txt(
            "Le tribunal souligne aussi que des actes d'investigation d'une ampleur exceptionnelle ont été réalisés et "
            "que, compte tenu des manœuvres du couple, rien ne permet de démontrer que leur culpabilité aurait pu être "
            "établie bien avant les aveux de Monique Olivier.",
            "The court also stresses that investigative acts of exceptional scale were carried out and that, given the "
            "couple's manoeuvres, nothing shows their guilt could have been established long before Monique Olivier's admissions.",
        ),
        "reliability": "CONFIRMED", "source": "rtl-faute-lourde",
    },
]
EXPERTS_AGREEMENT = txt(
    "Les deux lectures s'accordent sur un point : une piste existait en 2003 et elle a été écartée.",
    "Both readings agree on one point: a lead existed in 2003 and it was set aside.",
)
EXPERTS_DISAGREEMENT = txt(
    "Elles divergent sur la portée de cet écart : alibi suffisant d'un côté, abandon prématuré de l'autre. Le "
    "jugement de 2025 tranche sur la faute de l'État sans établir qu'une issue différente était certaine.",
    "They differ on the significance of that step: sufficient alibi on one side, premature abandonment on the other. "
    "The 2025 ruling settles the question of State negligence without establishing that a different outcome was certain.",
)
EXPERTS_UNCERTAIN = txt(
    "Ce qui reste incertain : ce qu'une exploitation plus précoce de la piste aurait produit concrètement.",
    "What remains uncertain: what earlier exploitation of the lead would concretely have produced.",
)

# ------------------------------------------------------------ ET SI ? (§51) ----
COUNTERFACTUALS = [
    counterfactual(
        "lead_not_pursued",
        "Et si la piste de 2003 avait été maintenue ?",
        "What if the 2003 lead had been maintained?",
        "La piste Michel Fourniret a été envisagée en 2003 puis écartée au profit d'un alibi téléphonique. Elle est "
        "revenue au centre du dossier en 2019, après le dépaysement à Paris. Entre ces deux dates, que peut-on "
        "établir à partir de la chronologie documentée ?",
        "The Michel Fourniret lead was considered in 2003 then set aside in favour of a telephone alibi. It returned "
        "to the centre of the file in 2019, after the transfer to Paris. Between those two dates, what can be "
        "established from the documented chronology?",
        {
            "unit": "years",
            "reference_event": {
                "label": txt("Piste envisagée", "Lead considered"),
                "date": "2003-01-09",
            },
            "hypothesis": {
                "label": txt("Piste écartée (alibi téléphonique)", "Lead set aside (telephone alibi)"),
                "date": "2003-12-31",
            },
            "scenario_event": {
                "label": txt("Piste reprise après dépaysement", "Lead resumed after transfer"),
                "date": "2019-01-01",
            },
            "outcome_event": {
                "label": txt("Condamnation pour complicité", "Conviction for complicity"),
                "date": "2023-12-19",
            },
            "jurisdiction_note": txt(
                "En droit français, un alibi vérifié est un motif légitime d'écarter une piste. Aucune règle "
                "n'imposait de la maintenir ; la question porte sur les conséquences documentées de cet écart, "
                "non sur sa légalité.",
                "In French law, a verified alibi is a legitimate ground for setting a lead aside. No rule required it "
                "to be maintained; the question concerns the documented consequences of that step, not its legality.",
            ),
        },
        [
            {"date": "2003-01-09", "kind": "fact", "label": txt("Disparition", "Disappearance")},
            {"date": "2003-12-31", "kind": "hypothesis", "label": txt("Piste écartée", "Lead set aside")},
            {"date": "2019-01-01", "kind": "scenario", "label": txt("Piste reprise", "Lead resumed")},
            {"date": "2020-03-01", "kind": "fact", "label": txt("Aveux partiels de M. Fourniret", "M. Fourniret's partial confession")},
            {"date": "2020-08-21", "kind": "fact", "label": txt("ADN partiel sur un matelas saisi en 2003", "Partial DNA on a mattress seized in 2003")},
            {"date": "2021-05-10", "kind": "fact", "label": txt("Décès de M. Fourniret en détention", "Death of M. Fourniret in custody")},
            {"date": "2023-12-19", "kind": "outcome", "label": txt("Condamnation de M. Olivier", "Conviction of M. Olivier")},
            {"date": "2025-09-03", "kind": "fact", "label": txt("Faute lourde de l'État reconnue", "Gross negligence of the State recognised")},
        ],
        True, "rtl-faute-lourde",
    ),
    counterfactual(
        "technology",
        "Et si l'expertise de 2020 avait été possible en 2003 ?",
        "What if the 2020 examination had been possible in 2003?",
        "Le matelas saisi en 2003 à Ville-sur-Lumes n'a livré une trace d'ADN partiel d'Estelle Mouzin qu'en août "
        "2020, à la faveur d'une nouvelle expertise. Dix-sept ans séparent la saisie de la lecture.",
        "The mattress seized in 2003 in Ville-sur-Lumes yielded a partial DNA trace of Estelle Mouzin only in August "
        "2020, thanks to a new expert examination. Seventeen years separate the seizure from the reading.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Saisie du matelas", "Seizure of the mattress"), "date": "2003-12-31"},
            "hypothesis": {"label": txt("Lecture scientifique impossible à l'époque", "Scientific reading impossible at the time"), "date": "2003-12-31"},
            "scenario_event": {"label": txt("Trace d'ADN partiel identifiée", "Partial DNA trace identified"), "date": "2020-08-21"},
            "jurisdiction_note": txt(
                "La sensibilité des techniques d'analyse génétique a progressé entre 2003 et 2020. Dire qu'une "
                "lecture équivalente « aurait » été possible plus tôt suppose des conditions techniques qui ne sont "
                "pas documentées dans les sources consultées : l'application se limite donc à mesurer l'écart de temps.",
                "The sensitivity of genetic analysis techniques progressed between 2003 and 2020. Saying that an "
                "equivalent reading 'would' have been possible earlier assumes technical conditions that are not "
                "documented in the sources consulted: the application therefore limits itself to measuring the time gap.",
            ),
        },
        [
            {"date": "2003-12-31", "kind": "reference", "label": txt("Matelas sous scellé", "Mattress under seal")},
            {"date": "2020-08-21", "kind": "scenario", "label": txt("Trace d'ADN partiel", "Partial DNA trace")},
        ],
        True, "franceinfo-chronologie",
    ),
]

# ---------------------------------------------------------- LESSONS (§33) ----
LESSONS = [
    item("Un alibi attesté n'est pas une démonstration d'impossibilité : il établit un appel, pas l'intégralité d'un "
         "emploi du temps.",
         "An attested alibi is not a demonstration of impossibility: it establishes a call, not an entire schedule.",
         "CONFIRMED", "monde-5dates", "Portée d'un alibi", "Scope of an alibi"),
    item("La conservation des scellés est un investissement : un objet saisi en 2003 a parlé en 2020.",
         "Preserving exhibits is an investment: an item seized in 2003 spoke in 2020.",
         "CONFIRMED", "franceinfo-chronologie", "Science différée", "Deferred science"),
    item("La continuité d'un dossier dépend d'outils modestes : cotation des pages, procès-verbal de synthèse, "
         "transmission entre magistrats.",
         "The continuity of a file depends on modest tools: pagination, synthesis report, handover between magistrates.",
         "CONFIRMED", "rtl-faute-lourde", "Procédure", "Procedure"),
    item("La persistance d'une famille peut modifier le cours d'une instruction : ici, elle a conduit à une décision "
         "civile reconnaissant la faute de l'État.",
         "A family's persistence can change the course of an investigation: here, it led to a civil decision "
         "recognising the State's negligence.",
         "CONFIRMED", "rtl-faute-lourde", "Rôle des familles", "Role of families"),
    item("Un auteur peut agir hors de la zone géographique que l'on associe à ses autres crimes : la géographie "
         "criminelle ordonne des priorités, elle n'exclut rien.",
         "An author can act outside the geographic area associated with his other crimes: criminal geography orders "
         "priorities, it excludes nothing.",
         "CONFIRMED", "marieclaire-temps-forts", "Géographie", "Geography"),
    item("La mort d'un auteur éteint l'action publique mais n'éteint pas le dossier : la complicité reste jugée, et "
         "la recherche du corps se poursuit.",
         "The death of an author extinguishes public prosecution but not the file: complicity is still tried, and the "
         "search for the body continues.",
         "CONFIRMED", "actu-guermantes", "Droit", "Law"),
    item("Reconnaître une faute institutionnelle et reconnaître l'ampleur des actes accomplis ne s'excluent pas : le "
         "jugement de 2025 fait les deux.",
         "Recognising institutional failure and recognising the scale of acts performed are not mutually exclusive: "
         "the 2025 ruling does both.",
         "CONFIRMED", "rtl-faute-lourde", "Nuance", "Nuance"),
]

# ----------------------------------------------------------- UNKNOWN ZONES ----
UNKNOWNS = [
    item("Le lieu où se trouve le corps d'Estelle Mouzin.", "The place where Estelle Mouzin's body lies.",
         "UNKNOWN", "franceinfo-chronologie"),
    item("Les circonstances précises de l'enlèvement et de la mort.", "The precise circumstances of the abduction and death.",
         "UNKNOWN", "monde-5dates"),
    item("Le rôle exact de Monique Olivier le 9 janvier 2003, au-delà de la complicité retenue par la cour.",
         "Monique Olivier's exact role on 9 January 2003, beyond the complicity found by the court.",
         "UNKNOWN", "franceinfo-olivier-2023"),
    item("Ce qu'une instruction continue, dotée d'un dossier coté et d'un procès-verbal de synthèse, aurait produit "
         "entre 2004 et 2018.",
         "What continuous investigation, with a paginated file and a synthesis report, would have produced between 2004 and 2018.",
         "UNKNOWN", "rtl-faute-lourde"),
]

# --------------------------------------------------------- DOSSIER (§9) ----
SECTIONS = [
    {"key": "introduction", "title": txt("Introduction", "Introduction"), "tier": "FREE",
     "blocks": [block("paragraph", "Un trajet de quelques centaines de mètres", "A journey of a few hundred metres",
                      "Le 9 janvier 2003, à Guermantes, une enfant de 9 ans ne rentre pas de l'école. Ce qui suit est "
                      "l'histoire d'une enquête de dix-sept ans, d'une trace conservée dans un scellé, d'aveux tardifs "
                      "et d'une décision de justice reconnaissant la faute lourde de l'État.",
                      "On 9 January 2003, in Guermantes, a 9-year-old child did not come home from school. What follows "
                      "is the story of a seventeen-year investigation, a trace kept in an exhibit, late confessions and "
                      "a court decision recognising gross negligence by the State.",
                      "CONFIRMED", "franceinfo-chronologie")]},
    {"key": "context", "title": txt("Contexte", "Context"), "tier": "FREE",
     "blocks": [block("paragraph", "Une commune de 1 400 habitants", "A commune of 1,400 inhabitants",
                      "Guermantes est une petite commune de Seine-et-Marne. La disparition d'un enfant y déclenche un "
                      "dispositif de masse : tous les habitants entendus, tous les logements perquisitionnés, les bois "
                      "ratissés. Le volume d'actes est considérable ; l'identification, elle, n'advient pas.",
                      "Guermantes is a small commune in Seine-et-Marne. A child's disappearance there triggered a mass "
                      "operation: all inhabitants heard, all homes searched, woods combed. The volume of acts was "
                      "considerable; the identification did not come.",
                      "CONFIRMED", "franceinfo-chronologie")]},
    {"key": "offender", "title": txt("Auteur", "Author"), "tier": "PREMIUM",
     "blocks": [block("paragraph", "Michel Fourniret (1942-2021)", "Michel Fourniret (1942-2021)",
                      "Tueur en série déjà condamné à la perpétuité en 2008 pour les meurtres de sept jeunes femmes ou "
                      "adolescentes commis entre 1987 et 2001, puis à 20 ans de réclusion en 2018. Il a reconnu en "
                      "mars 2020 sa responsabilité dans la mort d'Estelle Mouzin. Décédé en détention le 10 mai 2021, "
                      "il n'a pas été jugé pour ces faits.",
                      "A serial killer already sentenced to life in 2008 for the murders of seven young women or "
                      "teenagers committed between 1987 and 2001, then to 20 years in 2018. In March 2020 he "
                      "acknowledged his responsibility for Estelle Mouzin's death. He died in custody on 10 May 2021 "
                      "and was not tried for these facts.",
                      "CONFIRMED", "franceinfo-olivier-2023")]},
    {"key": "victims", "title": txt("Victime", "Victim"), "tier": "FREE", "blocks": []},
    {"key": "timeline", "title": txt("Chronologie", "Chronology"), "tier": "FREE", "blocks": []},
    {"key": "investigation", "title": txt("Enquête", "Investigation"), "tier": "FREE", "blocks": []},
    {"key": "clues", "title": txt("Indices et preuves", "Clues and evidence"), "tier": "PREMIUM", "blocks": []},
    {"key": "behaviour", "title": txt("Analyse comportementale", "Behavioural analysis"), "tier": "PREMIUM",
     "blocks": [block("behaviour", "Parler peu, parler tard", "Speaking little, speaking late",
                      "Le comportement documenté de l'auteur dans ce dossier est un comportement de contrôle de "
                      "l'information : dénégation initiale, aveu de responsabilité sans récit, refus de préciser les "
                      "circonstances, désignation de lieux sans résultats. Ce schéma a contraint l'instruction à "
                      "travailler sur des traces et sur la parole d'un tiers plutôt que sur un récit vérifiable.",
                      "The author's documented behaviour in this file is one of information control: initial denial, "
                      "acknowledgement of responsibility without narrative, refusal to specify circumstances, "
                      "designation of places without results. This pattern forced the investigation to work on traces "
                      "and on a third party's speech rather than on a verifiable account.",
                      "CONFIRMED", "monde-5dates")]},
    {"key": "psychology", "title": txt("Psychologie", "Psychology"), "tier": "PREMIUM", "blocks": []},
    {"key": "victimology", "title": txt("Victimologie", "Victimology"), "tier": "FREE", "blocks": []},
    {"key": "geography", "title": txt("Géographie", "Geography"), "tier": "FREE", "blocks": [
        block("paragraph", "Trois lieux, deux pays", "Three places, two countries",
              "Guermantes (lieu de la disparition), Ville-sur-Lumes (lieu désigné de la séquestration), "
              "Sart-Custinne en Belgique (lieu de l'appel d'alibi). La distance entre les deux premiers est d'environ "
              "250 kilomètres — c'est cette distance qui a pesé dans l'écart de la piste en 2003.",
              "Guermantes (place of disappearance), Ville-sur-Lumes (designated place of confinement), Sart-Custinne "
              "in Belgium (place of the alibi call). The distance between the first two is about 250 kilometres — it "
              "was this distance that weighed in setting the lead aside in 2003.",
              "CONFIRMED", "monde-5dates")]},
    {"key": "arrest", "title": txt("Mise en cause", "Indictment"), "tier": "FREE", "blocks": [
        block("paragraph", "Une mise en examen tardive", "A late indictment",
              "Michel Fourniret a été mis en examen pour enlèvement et séquestration suivis de mort dans ce dossier ; "
              "Monique Olivier a été mise en examen pour complicité en 2020.",
              "Michel Fourniret was indicted for abduction and confinement followed by death in this file; Monique "
              "Olivier was indicted for complicity in 2020.",
              "CONFIRMED", "ouestfrance-reconstitution")]},
    {"key": "trial", "title": txt("Procès", "Trial"), "tier": "FREE", "blocks": []},
    {"key": "justice", "title": txt("Justice", "Justice"), "tier": "FREE", "blocks": []},
    {"key": "consequences", "title": txt("Conséquences", "Consequences"), "tier": "FREE",
     "blocks": [block("paragraph", "Après le verdict", "After the verdict",
                      "L'affaire a produit une décision civile inédite pour la famille : la reconnaissance de la faute "
                      "lourde de l'État, le 3 septembre 2025. Elle a aussi alimenté le débat public sur la "
                      "continuité de l'instruction et sur le traitement des dossiers de disparition d'enfants.",
                      "The case produced an unprecedented civil decision for the family: recognition of gross "
                      "negligence by the State, on 3 September 2025. It also fed public debate on the continuity of "
                      "investigations and on the handling of child disappearance files.",
                      "CONFIRMED", "rtl-faute-lourde")]},
    {"key": "archives", "title": txt("Archives", "Archives"), "tier": "PREMIUM", "blocks": []},
    {"key": "sources", "title": txt("Sources", "Sources"), "tier": "FREE", "blocks": []},
    {"key": "memorial", "title": txt("Mémoire", "Memory"), "tier": "FREE", "blocks": []},
    {"key": "unknowns", "title": txt("Zones d'ombre", "Unknown zones"), "tier": "FREE", "blocks": []},
    {"key": "lessons", "title": txt("Ce que l'affaire nous apprend", "What the case teaches us"), "tier": "FREE", "blocks": []},
]

# -------------------------------------------------------------- PODCAST ----
SIGNATURE_INTRO_FR = (
    "Vous êtes sur YANIS//X, à travers mon regard. Aujourd'hui, nous allons revenir sur une affaire française qui a "
    "duré dix-sept ans. Une enfant de neuf ans, un trajet de quelques centaines de mètres, et une question qui n'a "
    "jamais cessé : pourquoi a-t-il fallu si longtemps ?"
)
SIGNATURE_INTRO_EN = (
    "You are on YANIS//X, through my eyes. Today we return to a French case that lasted seventeen years. A nine-year-old "
    "child, a journey of a few hundred metres, and a question that never stopped: why did it take so long?"
)

EPISODES = [
    {
        "number": 1,
        "title": txt("Le trajet", "The journey"),
        "description": txt(
            "9 janvier 2003, Guermantes. Ce que l'on sait dans les premières heures, ce que l'on cherche, et la piste "
            "que l'on va écarter.",
            "9 January 2003, Guermantes. What is known in the first hours, what is searched for, and the lead that "
            "will be set aside.",
        ),
        "modes": ["documentary", "investigation", "chronology", "victims", "express", "psychology", "expert"],
        "audio_status": "produced",
        "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 60, "title": txt("17 h : l'absence", "5 p.m.: the absence")},
            {"at": 180, "title": txt("Une commune au crible", "A commune under the sieve")},
            {"at": 300, "title": txt("Une piste déjà connue", "A lead already known")},
            {"at": 420, "title": txt("L'alibi", "The alibi")},
            {"at": 540, "title": txt("Et maintenant, une question", "And now, a question")},
        ],
        "transcript": {
            "segments": [
                {"id": "s1", "t": 0, "speaker": "yanis", "text": SIGNATURE_INTRO_FR, "text_en": SIGNATURE_INTRO_EN},
                {"id": "s2", "t": 60, "speaker": "yanis",
                 "text": "Le 9 janvier 2003, à Guermantes, en Seine-et-Marne, Estelle Mouzin a neuf ans. Elle rentre "
                         "de l'école à pied. Le trajet est court, connu, quotidien. Elle n'arrivera pas chez elle.",
                 "text_en": "On 9 January 2003, in Guermantes, Seine-et-Marne, Estelle Mouzin is nine years old. She "
                            "walks home from school. The journey is short, known, daily. She will not arrive home."},
                {"id": "s3", "t": 180, "speaker": "yanis",
                 "text": "Ce soir-là, la réponse est massive. Les quelque mille quatre cents habitants de la commune "
                         "sont interrogés. Les logements sont perquisitionnés. Les bois autour de Guermantes sont "
                         "ratissés. Une information judiciaire est ouverte à Meaux pour enlèvement et séquestration "
                         "de mineur de quinze ans.",
                 "text_en": "That evening, the response is massive. The commune's roughly fourteen hundred inhabitants "
                            "are questioned. Homes are searched. The woods around Guermantes are combed. A judicial "
                            "investigation is opened in Meaux for abduction and confinement of a minor under fifteen."},
                {"id": "s4", "t": 300, "speaker": "yanis",
                 "text": "Et très tôt, une piste apparaît. Elle porte le nom d'un homme déjà connu de la justice : "
                         "Michel Fourniret. Lors des perquisitions, on trouve une cassette vidéo contenant un "
                         "reportage sur la disparition d'Estelle. Sur son ordinateur, des photographies de l'enfant. "
                         "Il nie, et parle d'un intérêt pour cette disparition.",
                 "text_en": "And very early, a lead appears. It bears the name of a man already known to the justice "
                            "system: Michel Fourniret. During searches, a video cassette containing a report on "
                            "Estelle's disappearance is found. On his computer, photographs of the child. He denies it, "
                            "and speaks of an interest in the disappearance."},
                {"id": "s5", "t": 420, "speaker": "yanis",
                 "text": "Puis vient l'alibi. Le soir du 9 janvier 2003, un appel est passé depuis Sart-Custinne, en "
                         "Belgique, à environ deux cent cinquante kilomètres de Guermantes. Michel Fourniret souhaite "
                         "un bon anniversaire à son fils. Les relevés téléphoniques attestent cet appel. Les "
                         "enquêteurs estiment l'alibi solide. La piste est écartée.",
                 "text_en": "Then comes the alibi. On the evening of 9 January 2003, a call is placed from "
                            "Sart-Custinne, in Belgium, about two hundred and fifty kilometres from Guermantes. Michel "
                            "Fourniret wishes his son a happy birthday. Phone records attest this call. Investigators "
                            "deem the alibi solid. The lead is set aside."},
                {"id": "s6", "t": 540, "speaker": "yanis",
                 "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
                 "text_en": "And now, a question. Not a judgement. A reflection."},
                {"id": "s7", "t": 560, "speaker": "yanis",
                 "text": "Seize ans plus tard, en 2019, le dossier est dépaysé à Paris. En 2020, Michel Fourniret "
                         "déclare devant la juge d'instruction : « Je reconnais là un être qui n'est plus là par ma "
                         "faute. » En août 2020, une trace d'ADN partiel d'Estelle est retrouvée sur un matelas saisi "
                         "en 2003. Le corps, lui, n'a jamais été retrouvé.",
                 "text_en": "Sixteen years later, in 2019, the file is transferred to Paris. In 2020, Michel Fourniret "
                            "declares before the investigating judge: 'I acknowledge here a being who is no longer "
                            "there through my fault.' In August 2020, a partial DNA trace of Estelle is found on a "
                            "mattress seized in 2003. The body was never recovered."},
                {"id": "s8", "t": 700, "speaker": "yanis",
                 "text": "Le 19 décembre 2023, Monique Olivier est condamnée à la réclusion criminelle à perpétuité, "
                         "assortie d'une période de sûreté de vingt ans, pour complicité. Le 3 septembre 2025, l'État "
                         "est condamné pour faute lourde dans la conduite de l'enquête. Le jugement cite le manque de "
                         "moyens humains, la succession de dix magistrats, l'absence de procès-verbal de synthèse, et "
                         "un dossier jamais coté. Il dit aussi autre chose : des actes d'investigation d'une ampleur "
                         "exceptionnelle ont été réalisés.",
                 "text_en": "On 19 December 2023, Monique Olivier is sentenced to life imprisonment with a twenty-year "
                            "minimum term, for complicity. On 3 September 2025, the State is condemned for gross "
                            "negligence in the conduct of the investigation. The ruling cites the lack of human "
                            "resources, the succession of ten magistrates, the absence of a synthesis report, and a "
                            "file never paginated. It also says something else: investigative acts of exceptional "
                            "scale were carried out."},
                {"id": "s9", "t": 860, "speaker": "yanis",
                 "text": "Estelle Mouzin avait neuf ans. Avant d'être un dossier, elle était une élève, une fille, "
                         "une enfant qui rentrait chez elle. C'est cela que cette application retient d'abord.",
                 "text_en": "Estelle Mouzin was nine years old. Before being a file, she was a pupil, a daughter, a "
                            "child walking home. That is what this application holds onto first."},
            ],
        },
    },
    {
        "number": 2,
        "title": txt("Dix-sept ans de scellés", "Seventeen years of exhibits"),
        "description": txt(
            "Comment un matelas saisi en 2003 a parlé en 2020. La science, la procédure, et ce que le dossier a perdu "
            "en route.",
            "How a mattress seized in 2003 spoke in 2020. Science, procedure, and what the file lost along the way.",
        ),
        "modes": ["documentary", "investigation", "expert", "chronology", "express"],
        "audio_status": "script_only",
        "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 60, "title": txt("Un dossier sans numéro de page", "A file without page numbers")},
            {"at": 240, "title": txt("Le dépaysement", "The transfer")},
            {"at": 420, "title": txt("Le matelas", "The mattress")},
        ],
        "transcript": {
            "segments": [
                {"id": "e2s1", "t": 0, "speaker": "yanis",
                 "text": "Vous êtes sur YANIS//X, à travers mon regard. Cet épisode ne parle pas d'un crime. Il parle "
                         "d'un objet : un matelas, saisi en 2003, conservé dix-sept ans sous main de justice.",
                 "text_en": "You are on YANIS//X, through my eyes. This episode is not about a crime. It is about an "
                            "object: a mattress, seized in 2003, kept for seventeen years in judicial custody."},
                {"id": "e2s2", "t": 60, "speaker": "yanis",
                 "text": "Pour comprendre ce qu'il a fallu pour le faire parler, il faut regarder le dossier. Le "
                         "jugement du 3 septembre 2025 décrit une succession de dix magistrats. Aucun procès-verbal "
                         "de synthèse. Aucune page numérotée. Un dossier, écrit le tribunal, impossible à lire comme "
                         "un livre.",
                 "text_en": "To understand what it took to make it speak, one must look at the file. The ruling of 3 "
                            "September 2025 describes a succession of ten magistrates. No synthesis report. No "
                            "numbered page. A file, the court writes, impossible to read like a book."},
                {"id": "e2s3", "t": 240, "speaker": "yanis",
                 "text": "En 2019, le dossier est dépaysé à Paris. L'objectif est écrit noir sur blanc : favoriser la "
                         "manifestation de la vérité avant que l'âge et la mémoire de Michel Fourniret ne l'empêchent "
                         "définitivement.",
                 "text_en": "In 2019, the file is transferred to Paris. The objective is written plainly: to "
                            "facilitate the discovery of truth before Michel Fourniret's age and memory prevent it "
                            "for good."},
                {"id": "e2s4", "t": 420, "speaker": "yanis",
                 "text": "Le 21 août 2020, une nouvelle expertise révèle sur ce matelas une trace d'ADN partiel "
                         "d'Estelle Mouzin. Dix-sept ans après la saisie. La technique avait changé. Le scellé, lui, "
                         "avait attendu.",
                 "text_en": "On 21 August 2020, a new expert examination revealed on that mattress a partial DNA trace "
                            "of Estelle Mouzin. Seventeen years after the seizure. The technique had changed. The "
                            "exhibit had waited."},
            ],
        },
    },
    {
        "number": 3,
        "title": txt("Estelle", "Estelle"),
        "description": txt(
            "Épisode Mémoire. Pas d'enquête, pas d'analyse : la personne. Ce que l'on sait d'elle, ce que la famille "
            "a porté, et ce que l'on ne saura pas.",
            "Memory episode. No investigation, no analysis: the person. What is known of her, what the family carried, "
            "and what will never be known.",
        ),
        "modes": ["victims", "documentary", "express"],
        "audio_status": "produced",
        "voice_profile": "yanis-real",
        "chapters": [{"at": 0, "title": txt("Qui était Estelle ?", "Who was Estelle?")}],
        "transcript": {
            "segments": [
                {"id": "e3s1", "t": 0, "speaker": "yanis",
                 "text": "Cet épisode n'est pas une enquête. Il n'y a pas de question à la fin. Il y a un prénom : "
                         "Estelle. Elle avait neuf ans. Elle vivait à Guermantes. Elle rentrait de l'école à pied.",
                 "text_en": "This episode is not an investigation. There is no question at the end. There is a first "
                            "name: Estelle. She was nine years old. She lived in Guermantes. She walked home from school."},
                {"id": "e3s2", "t": 60, "speaker": "yanis",
                 "text": "Les sources publiques consultées ne décrivent pas ses passions, ses amis, ses projets. Cette "
                         "application ne les inventera pas. Ce silence dans le dossier est aussi une information : il "
                         "dit ce qui appartient à une famille et ce qui appartient à la justice.",
                 "text_en": "The public sources consulted do not describe her passions, her friends, her plans. This "
                            "application will not invent them. That silence in the file is also information: it says "
                            "what belongs to a family and what belongs to justice."},
                {"id": "e3s3", "t": 150, "speaker": "yanis",
                 "text": "Ce que l'on sait, c'est ce que son père a fait pendant plus de vingt ans : des marches, des "
                         "demandes d'actes, une assignation de l'État. Le 3 septembre 2025, le tribunal judiciaire de "
                         "Paris a reconnu une faute lourde et lui a accordé cinquante mille euros au titre du "
                         "préjudice moral. Le corps d'Estelle n'a jamais été retrouvé.",
                 "text_en": "What is known is what her father did for more than twenty years: marches, requests for "
                            "investigative acts, a suit against the State. On 3 September 2025, the Paris judicial "
                            "court recognised gross negligence and awarded him fifty thousand euros for moral damages. "
                            "Estelle's body was never recovered."},
                {"id": "e3s4", "t": 280, "speaker": "yanis",
                 "text": "Écouter les histoires. Comprendre les affaires. Ne jamais oublier les victimes.",
                 "text_en": "Listen to the stories. Understand the cases. Never forget the victims."},
            ],
        },
    },
]

# ------------------------------------------------------- QUESTIONS (§26) ----
QUESTIONS = [
    question(
        "1", 540, "investigation",
        "À ce stade de l'enquête, en 2003, que feriez-vous de la piste Michel Fourniret ?",
        "At this stage of the investigation, in 2003, what would you do with the Michel Fourniret lead?",
        [
            ("a", "L'écarter : l'alibi téléphonique est attesté par des relevés", "Set it aside: the phone alibi is attested by records"),
            ("b", "La maintenir ouverte et la documenter, sans agir publiquement", "Keep it open and document it, without acting publicly"),
            ("c", "La traiter comme prioritaire et placer l'intéressé en garde à vue", "Treat it as a priority and detain the person"),
            ("d", "Impossible à déterminer avec les éléments de 2003", "Impossible to determine with 2003 elements"),
        ],
        {
            "fr": {
                "whatInvestigatorsKnew": "En 2003, les enquêteurs disposent de relevés téléphoniques attestant un appel passé depuis Sart-Custinne, en Belgique, à environ 250 km, le soir des faits. Ils disposent aussi d'un reportage vidéo et de photographies de l'enfant retrouvés lors des perquisitions.",
                "whatExpertsProposed": "La piste est écartée : l'alibi est estimé solide et Guermantes ne correspond pas au secteur habituel des crimes alors imputés à Michel Fourniret.",
                "documented": "L'appel est attesté par les relevés. La présence de la cassette et des photographies est rapportée par la presse à partir des perquisitions.",
                "hypothetical": "Ce qu'une conservation active de la piste aurait changé. Le jugement civil de 2025 souligne d'ailleurs que rien ne permet de démontrer que la culpabilité du couple aurait pu être établie bien avant les aveux.",
                "whatYouCouldNotKnow": "Vous ne pouviez pas savoir, en 2003, qu'en août 2020 une trace d'ADN partiel serait identifiée sur un matelas saisi cette même année 2003, ni que l'auteur reconnaîtrait sa responsabilité en 2020.",
                "answer_note": "Aucune réponse n'est « fausse ». La réponse retenue par les enquêteurs à l'époque correspond à l'option A ; l'option B décrit ce que la décision civile de 2025 a posteriori interroge.",
            },
            "en": {
                "whatInvestigatorsKnew": "In 2003, investigators had phone records attesting a call placed from Sart-Custinne, Belgium, about 250 km away, on the evening of the facts. They also had a video report and photographs of the child found during searches.",
                "whatExpertsProposed": "The lead was set aside: the alibi was deemed solid and Guermantes did not correspond to the usual area of the crimes then attributed to Michel Fourniret.",
                "documented": "The call is attested by records. The presence of the cassette and photographs is reported by the press from the searches.",
                "hypothetical": "What actively keeping the lead would have changed. The 2025 civil ruling stresses that nothing shows the couple's guilt could have been established long before the admissions.",
                "whatYouCouldNotKnow": "You could not know, in 2003, that in August 2020 a partial DNA trace would be identified on a mattress seized that same year, nor that the author would acknowledge his responsibility in 2020.",
                "answer_note": "No answer is 'wrong'. The answer held by investigators at the time corresponds to option A; option B describes what the 2025 civil decision questions after the fact.",
            },
        },
        "monde-5dates",
    ),
    question(
        "2", 200, "evidence",
        "Un matelas est saisi en 2003 et conservé sous scellé. Dix-sept ans plus tard, une expertise y révèle une trace d'ADN partiel. Que peut-on déduire de cette trace ?",
        "A mattress is seized in 2003 and kept under seal. Seventeen years later, an examination reveals a partial DNA trace. What can be deduced from that trace?",
        [
            ("a", "Que l'enfant a été présente dans cette maison", "That the child was present in that house"),
            ("b", "Que l'ADN de l'enfant s'y trouve, sans que le moment ni le mode de dépôt soient établis", "That the child's DNA is there, without the moment or mode of deposition being established"),
            ("c", "Que les personnes mises en cause sont coupables", "That the persons indicted are guilty"),
            ("d", "Rien : un profil partiel n'a aucune valeur", "Nothing: a partial profile has no value"),
        ],
        {
            "fr": {
                "whatInvestigatorsKnew": "La trace est identifiée le 21 août 2020 sur un matelas saisi en 2003 dans la maison de Ville-sur-Lumes, ancienne propriété de la sœur défunte de Michel Fourniret.",
                "whatExpertsProposed": "Une trace partielle établit une correspondance génétique avec un profil de référence ; elle n'établit ni la date ni le mode de dépôt, et sa force dépend du nombre de marqueurs exploitables.",
                "documented": "La présence de la trace et sa date d'identification sont documentées par la presse à partir de l'instruction.",
                "hypothetical": "L'usage probatoire exact qui en a été fait à l'audience de 2023 n'est pas détaillé dans les sources consultées.",
                "whatYouCouldNotKnow": "Vous ne pouvez pas connaître les seuils techniques de l'expertise de 2020 : les sources consultées parlent d'« ADN partiel » sans préciser le nombre de marqueurs.",
                "answer_note": "La réponse la plus prudente et la plus exacte au regard des sources est B.",
            },
            "en": {
                "whatInvestigatorsKnew": "The trace was identified on 21 August 2020 on a mattress seized in 2003 in the Ville-sur-Lumes house, former property of Michel Fourniret's late sister.",
                "whatExpertsProposed": "A partial trace establishes a genetic match with a reference profile; it establishes neither the date nor the mode of deposition, and its strength depends on the number of usable markers.",
                "documented": "The presence of the trace and its identification date are documented by the press from the investigation.",
                "hypothetical": "The exact evidential use made of it at the 2023 hearing is not detailed in the sources consulted.",
                "whatYouCouldNotKnow": "You cannot know the technical thresholds of the 2020 examination: the sources consulted speak of 'partial DNA' without specifying the number of markers.",
                "answer_note": "The most cautious and accurate answer given the sources is B.",
            },
        },
        "franceinfo-chronologie",
    ),
    question(
        "3", 780, "bias",
        "Un jugement reconnaît à la fois une faute lourde de l'État et des actes d'investigation d'une ampleur exceptionnelle. Quel biais évite-t-on en tenant les deux ensemble ?",
        "A ruling recognises both gross negligence by the State and investigative acts of exceptional scale. Which bias is avoided by holding both together?",
        [
            ("a", "Le biais de confirmation", "Confirmation bias"),
            ("b", "L'effet de halo", "The halo effect"),
            ("c", "Le récit unique rétrospectif", "The single retrospective narrative"),
            ("d", "L'ancrage", "Anchoring"),
        ],
        {
            "fr": {
                "whatInvestigatorsKnew": "Le jugement du 3 septembre 2025 retient le manque de moyens humains et des dysfonctionnements, et constate dans le même temps l'ampleur exceptionnelle de certains actes.",
                "whatExpertsProposed": "Tenir ensemble deux constats opposés empêche de reconstruire après coup un récit unique — « tout a mal été fait » ou « tout a bien été fait » — qui effacerait la complexité réelle du dossier.",
                "documented": "Les deux constats figurent dans le compte rendu du jugement.",
                "hypothetical": "Aucune. Il s'agit ici d'une notion de raisonnement, pas d'un fait d'espèce.",
                "whatYouCouldNotKnow": "Rien : la question porte sur la méthode de lecture d'une décision, pas sur un élément caché.",
                "answer_note": "La réponse attendue est C. Les autres biais existent mais ne décrivent pas cette situation précise.",
            },
            "en": {
                "whatInvestigatorsKnew": "The ruling of 3 September 2025 cites a lack of human resources and dysfunctions, and at the same time notes the exceptional scale of certain acts.",
                "whatExpertsProposed": "Holding two opposing findings together prevents reconstructing after the fact a single narrative — 'everything was done badly' or 'everything was done well' — which would erase the real complexity of the file.",
                "documented": "Both findings appear in the report of the ruling.",
                "hypothetical": "None. This is a reasoning concept, not a case fact.",
                "whatYouCouldNotKnow": "Nothing: the question concerns the method of reading a decision, not a hidden element.",
                "answer_note": "The expected answer is C. The other biases exist but do not describe this precise situation.",
            },
        },
        "rtl-faute-lourde",
    ),
]

CASE.update(
    {
        "victims": VICTIMS,
        "memorial": MEMORIAL,
        "timeline": TIMELINE,
        "timeline_phases": TIMELINE_PHASES,
        "locations": LOCATIONS,
        "evidence": EVIDENCE,
        "investigation": INVESTIGATION,
        "psychology": PSYCHOLOGY,
        "victimology": VICTIMOLOGY,
        "court": COURT,
        "experts": EXPERTS,
        "experts_agreement": EXPERTS_AGREEMENT,
        "experts_disagreement": EXPERTS_DISAGREEMENT,
        "experts_uncertain": EXPERTS_UNCERTAIN,
        "counterfactuals": COUNTERFACTUALS,
        "lessons": LESSONS,
        "unknowns": UNKNOWNS,
        "sections": SECTIONS,
        "episodes": EPISODES,
        "questions": QUESTIONS,
    }
)
