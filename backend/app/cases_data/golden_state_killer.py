"""
DOSSIER 05 — LE GOLDEN STATE KILLER / JOSEPH DEANGELO (États-Unis, Californie, 1974-2020)

Sources publiques vérifiées le 2026-09-24.
"""
from ..case_template import (block, counterfactual, default_sections, fact, item,
                             merge_sections, question, source, txt)

CASE_ID = "golden-state-killer"
V = "2026-09-24"

SOURCES = [
    source("aetv-gsk", CASE_ID, "Case File: Joseph DeAngelo", "Case File: Joseph DeAngelo",
           "A&E", "Redaction", "https://www.aetv.com/articles/golden-state-killer-joseph-deangelo",
           "2026", "press", "CONFIRMED", V,
           "Synthèse détaillée : périodes, nombre de faits, méthode d'identification, procédure et condamnation.",
           "Detailed synthesis: periods, number of offences, identification method, procedure and sentence."),
    source("abc-timeline", CASE_ID, "The 'Golden State Killer': Inside the timeline of crimes",
           "The 'Golden State Killer': Inside the timeline of crimes",
           "ABC News", "Redaction", "https://abcnews.com/US/inside-timeline-crimes-golden-state-killer/story?id=54744307",
           "2020-10-30", "press", "CONFIRMED", V,
           "Chronologie de l'affaire, arrestation de 2018, plaidoyer de 2020, auditions des victimes.",
           "Case chronology, 2018 arrest, 2020 plea, victim hearings."),
    source("guardian-plea", CASE_ID, "Golden State Killer: former police officer pleads guilty to string of murders",
           "Golden State Killer: former police officer pleads guilty to string of murders",
           "The Guardian", "Redaction", "https://www.theguardian.com/us-news/2020/jun/29/golden-state-killer-joseph-deangelo-guilty-plea",
           "2020-06-29", "press", "CONFIRMED", V,
           "Plaidoyer de culpabilité, chefs d'accusation, prescription des viols et cambriolages, déclarations du parquet.",
           "Guilty plea, charges, statute of limitations on rapes and burglaries, prosecution statements."),
    source("bbc-sentence", CASE_ID, "Golden State Killer sentenced to life in prison",
           "Golden State Killer sentenced to life in prison",
           "BBC News", "Redaction", "https://www.bbc.com/news/election-us-2020-53828154",
           "2020-08-21", "press", "CONFIRMED", V,
           "Condamnation du 21 août 2020, ampleur retenue par l'accusation, impact sur d'autres affaires.",
           "Sentencing of 21 August 2020, scale retained by the prosecution, impact on other cases."),
    source("rossmo-2023", CASE_ID,
           "Behavioral Profiling in the Golden State Killer Investigation: A Comparative Analysis",
           "Behavioral Profiling in the Golden State Killer Investigation: A Comparative Analysis",
           "Trauma, Violence, & Abuse (SAGE) — D. Kim Rossmo", "D. Kim Rossmo",
           "https://journals.sagepub.com/doi/10.1177/10887679231201801",
           "2023-10-17", "scientific", "CONFIRMED", V,
           "Article scientifique : éléments biographiques, méthode d'identification, rôle de Paul Holes.",
           "Scientific article: biographical elements, identification method, role of Paul Holes."),
]

VICTIMS = [

    {"order": 0, "first_name": "Victimes", "last_name": "— 13 meurtres retenus", "age": "—",
     "anonymised": True, "reliability": "CONFIRMED", "source": "aetv-gsk",
     "life": {
         "fr": {"headline": "Treize meurtres, cinquante agressions sexuelles, cent vingt cambriolages",
                "items": [
                    {"label": "Ampleur retenue par l'accusation", "text": "87 victimes et 53 scènes de crime dans 11 comtés de Californie."},
                    {"label": "Chef d'accusation", "text": "13 chefs de meurtre au premier degré et 13 chefs liés à des enlèvements ; les viols et cambriolages des années 1970-1980 étaient prescrits."},
                    {"label": "Un exemple documenté", "text": "Lyman Smith et son épouse Charlene ont été tués à leur domicile de Ventura en 1980. Leur fille Carole avait 18 ans ; leur fils de 12 ans a découvert les corps. La famille n'a appris que vingt ans plus tard que ces meurtres relevaient d'une série."},
                    {"label": "Identités", "text": "Les noms de l'ensemble des victimes ne figurent pas dans les sources consultées. Cette application ne publie pas de liste non sourcée."}],
                "note": "Conformément à la règle éditoriale (§11), aucune victime n'est réduite à un numéro : lorsqu'une identité n'est pas documentée dans les sources consultées, l'absence est affichée plutôt que comblée."},
         "en": {"headline": "Thirteen murders, fifty sexual assaults, one hundred and twenty burglaries",
                "items": [
                    {"label": "Scale retained by the prosecution", "text": "87 victims and 53 crime scenes across 11 California counties."},
                    {"label": "Charges", "text": "13 counts of first-degree murder and 13 kidnapping-related counts; the rapes and burglaries of the 1970s-1980s were time-barred."},
                    {"label": "One documented example", "text": "Lyman Smith and his wife Charlene were killed at their Ventura home in 1980. Their daughter Carole was 18; their 12-year-old son found the bodies. The family learned only twenty years later that these murders belonged to a series."},
                    {"label": "Identities", "text": "The names of all the victims do not appear in the sources consulted. This application does not publish an unsourced list."}],
                "note": "In line with the editorial rule (§11), no victim is reduced to a number: when an identity is not documented in the sources consulted, the absence is displayed rather than filled."}},
     "disappearance": {
         "fr": {"items": [
             {"label": "Période", "text": "1974-1986 selon les synthèses, avec un premier fait retenu en 1975."},
             {"label": "Zones", "text": "Nord et sud de la Californie, 11 comtés."},
             {"label": "Auditions", "text": "Du 18 au 20 août 2020, survivantes, proches et familles des personnes tuées se sont exprimées devant la cour, dans une salle aménagée à l'université d'État de Sacramento."}]},
         "en": {"items": [
             {"label": "Period", "text": "1974-1986 according to syntheses, with a first offence retained in 1975."},
             {"label": "Areas", "text": "Northern and Southern California, 11 counties."},
             {"label": "Hearings", "text": "From 18 to 20 August 2020, survivors, relatives and families of those killed addressed the court, in a room fitted out at Sacramento State University."}]}}},
]

MEMORIAL = {
    "title": txt("87 victimes, 53 scènes, 11 comtés", "87 victims, 53 scenes, 11 counties"),
    "biography": txt(
        "L'accusation a retenu une ampleur de 87 victimes et 53 scènes de crime dans 11 comtés de Californie. Parmi "
        "elles, des personnes tuées chez elles, des survivantes d'agressions sexuelles, des familles qui ont appris "
        "des décennies plus tard que leur affaire appartenait à une série. Trois jours d'audience, du 18 au 20 août "
        "2020, leur ont été consacrés avant le prononcé de la peine.",
        "The prosecution retained a scale of 87 victims and 53 crime scenes in 11 California counties. Among them, "
        "people killed in their homes, survivors of sexual assaults, families who learned decades later that their "
        "case belonged to a series. Three days of hearing, from 18 to 20 August 2020, were devoted to them before "
        "sentencing.",
    ),
    "testimony": txt(
        "La procureure du comté de Sacramento, Anne Marie Schubert, a déclaré après la condamnation : « I don't "
        "believe we will ever know the magnitude of what Mr DeAngelo did », indiquant que des victimes pourraient "
        "rester non identifiées.",
        "Sacramento County District Attorney Anne Marie Schubert said after sentencing: 'I don't believe we will ever "
        "know the magnitude of what Mr DeAngelo did', indicating that victims might remain unidentified.",
    ),
    "memory": txt(
        "Une survivante a écrit qu'elle avait fait confiance à son mari lorsqu'il disait travailler tard, chasser ou "
        "partir en déplacement à des centaines de kilomètres. Le couple était séparé au moment de l'arrestation en "
        "2018 ; le divorce a été prononcé un an plus tard. Ce témoignage, lu à l'audience, dit ce que quarante ans "
        "d'inconnu ont coûté à des familles qui ne savaient pas.",
        "One survivor wrote that she had trusted her husband when he said he was working late, hunting, or travelling "
        "hundreds of miles away. The couple was separated at the time of the 2018 arrest; the divorce was finalised a "
        "year later. That testimony, read at the hearing, says what forty years of not knowing cost families who did "
        "not know.",
    ),
}

TIMELINE = [
    fact("Naissance de Joseph James DeAngelo Jr à Bath, État de New York. Sa famille s'installe ensuite en "
         "Californie ; il est scolarisé à Rancho Cordova puis à Folsom.",
         "Joseph James DeAngelo Jr is born in Bath, New York State. His family later moves to California; he is "
         "schooled in Rancho Cordova then Folsom.",
         "CONFIRMED", "rossmo-2023", "Naissance", "Birth", "1945-11-08"),
    fact("Il est policier à Exeter de 1973 à 1976. Son activité criminelle débute dans cette période, selon les "
         "synthèses publiées.",
         "He is a police officer in Exeter from 1973 to 1976. His criminal activity begins in that period, according "
         "to published syntheses.",
         "CONFIRMED", "guardian-plea", "Première période", "First period", "1973"),
    fact("Il est renvoyé de la police d'Auburn en 1979, après avoir été soupçonné d'avoir volé du répulsif pour "
         "chien et un marteau dans un magasin.",
         "He is dismissed from the Auburn police in 1979, after being suspected of stealing dog repellent and a hammer "
         "from a store.",
         "CONFIRMED", "guardian-plea", "Renvoi", "Dismissal", "1979"),
    fact("La série de faits s'étend jusqu'en 1986. Les cambriolages, agressions sexuelles et meurtres sont répartis "
         "dans le nord puis le sud de la Californie.",
         "The series of offences extends until 1986. Burglaries, sexual assaults and murders are spread across "
         "northern then southern California.",
         "CONFIRMED", "aetv-gsk", "Période des faits", "Period of offences", "1986"),
    fact("Il travaille comme mécanicien poids lourds dans un centre de distribution de supermarché à Roseville, de "
         "1990 à sa retraite en 2017.",
         "He works as a truck mechanic in a supermarket distribution centre in Roseville, from 1990 until his "
         "retirement in 2017.",
         "CONFIRMED", "rossmo-2023", "Vie professionnelle", "Working life", "1990"),
    fact("Le dossier est ancien et froid. Les affaires du nord et du sud de la Californie ont mis des années à être "
         "rapprochées par les enquêteurs.",
         "The file is old and cold. The northern and southern California cases took years to be linked by "
         "investigators.",
         "CONFIRMED", "guardian-plea", "Dossier froid", "Cold file", "1990-2017"),
    fact("Un profil ADN issu d'un kit de prélèvement d'un viol commis dans le comté de Ventura est déposé sur "
         "GEDmatch, site de généalogie génétique ouvert. Un arbre généalogique de plus de mille noms est construit, "
         "puis réduit à trois individus.",
         "A DNA profile from a rape kit taken in Ventura County is uploaded to GEDmatch, an open genetic genealogy "
         "site. A family tree of more than a thousand names is built, then reduced to three individuals.",
         "CONFIRMED", "aetv-gsk", "Généalogie génétique", "Genetic genealogy", "2018"),
    fact("Deux échantillons sont recueillis de manière discrète : l'un sur la poignée de voiture qu'il conduisait, "
         "l'autre sur un mouchoir pris dans sa poubelle. Les deux sont compatibles avec les profils des comtés "
         "d'Orange et de Ventura.",
         "Two samples are covertly collected: one from the door handle of a car he was driving, the other from a "
         "tissue taken from his bin. Both are consistent with the Orange and Ventura County profiles.",
         "CONFIRMED", "rossmo-2023", "Confirmation ADN", "DNA confirmation", "2018-04"),
    fact("Joseph DeAngelo est arrêté à son domicile de Citrus Heights, sans résistance. Il est âgé de 72 ans.",
         "Joseph DeAngelo is arrested at his Citrus Heights home, without resistance. He is 72 years old.",
         "CONFIRMED", "aetv-gsk", "Arrestation", "Arrest", "2018-04-24"),
    fact("Plaidoyer de culpabilité sur 13 chefs de meurtre au premier degré et 13 chefs liés à des enlèvements, "
         "devant une salle d'audience aménagée à l'université d'État de Sacramento. Il admet également des dizaines "
         "d'agressions sexuelles pour lesquelles la prescription empêche toute poursuite. La peine de mort est "
         "écartée dans le cadre de l'accord.",
         "Guilty plea to 13 counts of first-degree murder and 13 kidnapping-related counts, before a hearing room "
         "fitted out at Sacramento State University. He also admits dozens of sexual assaults for which the statute "
         "of limitations prevents prosecution. The death penalty is taken off the table as part of the deal.",
         "CONFIRMED", "guardian-plea", "Plaidoyer", "Plea", "2020-06-29"),
    fact("Du 18 au 20 août 2020, survivantes et familles s'expriment devant la cour. Le 21 août, il est condamné à "
         "onze peines consécutives de réclusion à perpétuité sans possibilité de libération conditionnelle, plus "
         "quinze peines concurrentes et des durées pour des chefs liés aux armes. Le juge Bowman déclare avoir "
         "prononcé le maximum autorisé par la loi.",
         "From 18 to 20 August 2020, survivors and families address the court. On 21 August, he is sentenced to "
         "eleven consecutive life terms without possibility of parole, plus fifteen concurrent life sentences and "
         "additional time for weapons charges. Judge Bowman states he imposed the maximum allowed by law.",
         "CONFIRMED", "bbc-sentence", "Condamnation", "Sentencing", "2020-08-21"),
    fact("Depuis cette identification, la généalogie génétique a permis d'identifier plus de 150 suspects selon ABC "
         "News ; le parquet a évoqué près de 100 affaires supplémentaires résolues.",
         "Since that identification, genetic genealogy has allowed more than 150 suspects to be identified according "
         "to ABC News; the prosecution mentioned nearly 100 additional solved cases.",
         "CONFIRMED", "abc-timeline", "Portée de la méthode", "Reach of the method", "2020"),
]

LOCATIONS = [
    {"kind": "region", "names": txt("Californie — 11 comtés", "California — 11 counties"),
     "city": "", "region": "California", "country": "US", "lat": 37.5, "lon": -121.0, "precision": "region",
     "date": "1974-1986",
     "note": txt("Les faits sont répartis entre le nord et le sud de l'État. La carte affiche l'échelle du comté, "
                "jamais une adresse.",
                "The offences are spread between the north and south of the state. The map displays county scale, "
                "never an address."),
     "reliability": "CONFIRMED", "source": "bbc-sentence"},
    {"kind": "city", "names": txt("Exeter (Californie)", "Exeter (California)"),
     "city": "Exeter", "region": "California", "country": "US", "lat": 36.29, "lon": -119.14, "precision": "city",
     "date": "1973-1976", "note": txt("Affectation comme policier.", "Assignment as a police officer."),
     "reliability": "CONFIRMED", "source": "guardian-plea"},
    {"kind": "city", "names": txt("Citrus Heights (Californie)", "Citrus Heights (California)"),
     "city": "Citrus Heights", "region": "California / Sacramento County", "country": "US",
     "lat": 38.70, "lon": -121.28, "precision": "city", "date": "2018-04-24",
     "note": txt("Lieu de l'arrestation.", "Place of arrest."), "reliability": "CONFIRMED", "source": "aetv-gsk"},
    {"kind": "city", "names": txt("Sacramento — université d'État", "Sacramento — State University"),
     "city": "Sacramento", "region": "California", "country": "US", "lat": 38.56, "lon": -121.42, "precision": "city",
     "date": "2020-08-21",
     "note": txt("Salle d'audience aménagée pour accueillir survivants et familles.",
                 "Hearing room fitted out to accommodate survivors and families."),
     "reliability": "CONFIRMED", "source": "bbc-sentence"},
]

EVIDENCE = [
    {"kind": "dna", "weight": "decisive", "reliability": "CONFIRMED", "source": "aetv-gsk",
     "title": txt("Profil ADN d'un kit de prélèvement", "DNA profile from a rape kit"),
     "description": txt(
         "Le profil issu d'un kit de prélèvement d'un viol commis dans le comté de Ventura a été déposé sur GEDmatch. "
         "Le site renvoie des apparentés selon le degré de partage de marqueurs génétiques. Un arbre de plus de mille "
         "noms a été construit, puis croisé avec l'âge, la localisation et d'autres données pour aboutir à trois "
         "individus.",
         "The profile from a rape kit taken in a Ventura County rape was uploaded to GEDmatch. The site returns "
         "relatives according to the degree of shared genetic markers. A tree of more than a thousand names was "
         "built, then crossed with age, location and other data to arrive at three individuals.")},
    {"kind": "dna", "weight": "decisive", "reliability": "CONFIRMED", "source": "rossmo-2023",
     "title": txt("Deux prélèvements discrets", "Two covert samples"),
     "description": txt(
         "Un échantillon a été recueilli sur la poignée d'une voiture qu'il conduisait, un second sur un mouchoir "
         "récupéré dans sa poubelle. Les deux se sont révélés compatibles avec les profils des comtés d'Orange et de "
         "Ventura.",
         "One sample was collected from the door handle of a car he was driving, a second from a tissue recovered from "
         "his bin. Both proved consistent with the Orange and Ventura County profiles.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "guardian-plea",
     "title": txt("La prescription comme limite", "The statute of limitations as a limit"),
     "description": txt(
         "Les viols et cambriolages commis dans les années 1970 et 1980 étaient prescrits : les poursuites ont porté "
         "sur 13 meurtres et 13 chefs liés à des enlèvements. L'accusé a admis des dizaines d'agressions sexuelles "
         "sans qu'elles puissent être poursuivies.",
         "The rapes and burglaries committed in the 1970s and 1980s were time-barred: prosecutions covered 13 murders "
         "and 13 kidnapping-related counts. The accused admitted dozens of sexual assaults that could not be "
         "prosecuted.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "guardian-plea",
     "title": txt("Un passé de policier", "A police background"),
     "description": txt(
         "Il a été policier à Exeter de 1973 à 1976, puis renvoyé de la police d'Auburn en 1979 après des "
         "soupçons de vol en magasin. Cette situation professionnelle a coïncidé avec le début de la période des faits.",
         "He was a police officer in Exeter from 1973 to 1976, then dismissed from the Auburn police in 1979 after "
         "shoplifting suspicions. That professional situation coincided with the start of the period of offences.")},
]

INVESTIGATION = {
    "steps": [
        {"n": 1, "date": "1974-1979", "title": txt("Des cambriolages et des agressions", "Burglaries and assaults"),
         "body": txt("Une première série de faits est commise dans le nord de la Californie, pendant que l'auteur "
                     "exerce comme policier à Exeter puis à Auburn.",
                     "A first series of offences is committed in northern California, while the author works as a "
                     "police officer in Exeter then Auburn."),
         "reliability": "CONFIRMED", "source": "guardian-plea", "premium": False},
        {"n": 2, "date": "1979-1986", "title": txt("Des meurtres dans le sud", "Murders in the south"),
         "body": txt("Des meurtres sont commis dans le sud de la Californie, dont celui de Lyman et Charlene Smith à "
                     "Ventura en 1980. Le rapprochement entre les deux zones prendra des années.",
                     "Murders are committed in southern California, including that of Lyman and Charlene Smith in "
                     "Ventura in 1980. Linking the two areas would take years."),
         "reliability": "CONFIRMED", "source": "guardian-plea", "premium": False},
        {"n": 3, "date": "1986", "title": txt("Le dernier fait connu", "The last known offence"),
         "body": txt("La série s'arrête en 1986. Le dossier devient froid, et le reste pendant plus de trente ans.",
                     "The series stops in 1986. The file goes cold, and stays so for more than thirty years.",),
         "reliability": "CONFIRMED", "source": "aetv-gsk", "premium": False},
        {"n": 4, "date": "1990-2017", "title": txt("Une vie ordinaire", "An ordinary life"),
         "body": txt("L'auteur travaille comme mécanicien poids lourds dans un centre de distribution à Roseville "
                     "jusqu'à sa retraite en 2017. Il vit à Citrus Heights.",
                     "The author works as a truck mechanic in a distribution centre in Roseville until retiring in "
                     "2017. He lives in Citrus Heights."),
         "reliability": "CONFIRMED", "source": "rossmo-2023", "premium": True},
        {"n": 5, "date": "2018", "title": txt("Un profil déposé sur une base ouverte", "A profile uploaded to an open database"),
         "body": txt("Un profil ADN issu d'un kit de prélèvement du comté de Ventura est déposé sur GEDmatch. La "
                     "méthode consiste à identifier des apparentés, puis à construire un arbre généalogique croisé "
                     "avec l'âge et la géographie.",
                     "A DNA profile from a Ventura County rape kit is uploaded to GEDmatch. The method consists of "
                     "identifying relatives, then building a family tree crossed with age and geography."),
         "reliability": "CONFIRMED", "source": "aetv-gsk", "premium": False},
        {"n": 6, "date": "2018-04", "title": txt("De mille noms à trois, puis à un", "From a thousand names to three, then to one"),
         "body": txt("L'arbre de plus de mille noms est réduit à trois individus, dont Joseph DeAngelo et son frère. "
                     "Deux prélèvements discrets — poignée de voiture et mouchoir dans une poubelle — confirment la "
                     "correspondance.",
                     "The tree of more than a thousand names is reduced to three individuals, including Joseph "
                     "DeAngelo and his brother. Two covert samples — a car door handle and a tissue from a bin — "
                     "confirm the match."),
         "reliability": "CONFIRMED", "source": "rossmo-2023", "premium": True},
        {"n": 7, "date": "2018-04-24", "title": txt("Arrestation", "Arrest"),
         "body": txt("Il est arrêté à son domicile de Citrus Heights, sans résistance, à 72 ans. C'est la première "
                     "arrestation publique obtenue par généalogie génétique.",
                     "He is arrested at his Citrus Heights home, without resistance, aged 72. It is the first public "
                     "arrest obtained through genetic genealogy."),
         "reliability": "CONFIRMED", "source": "abc-timeline", "premium": False},
        {"n": 8, "date": "2020-06-29", "title": txt("Un accord pour éviter la peine de mort", "A deal to avoid the death penalty"),
         "body": txt("Il plaide coupable. Le parquet, qui avait requis la peine capitale, accepte l'accord en citant "
                     "la complexité du dossier et l'âge avancé de nombreuses victimes et témoins.",
                     "He pleads guilty. The prosecution, which had sought the death penalty, accepts the deal citing "
                     "the complexity of the file and the advanced age of many victims and witnesses."),
         "reliability": "CONFIRMED", "source": "guardian-plea", "premium": True},
        {"n": 9, "date": "2020-08-21", "title": txt("Le maximum légal", "The legal maximum"),
         "body": txt("Après trois jours d'auditions de survivants et de familles, il est condamné à onze peines "
                     "consécutives de réclusion à perpétuité sans possibilité de libération conditionnelle, plus "
                     "quinze peines concurrentes. Le juge déclare avoir prononcé le maximum autorisé.",
                     "After three days of hearings of survivors and families, he is sentenced to eleven consecutive "
                     "life terms without possibility of parole, plus fifteen concurrent sentences. The judge states "
                     "he imposed the maximum allowed."),
         "reliability": "CONFIRMED", "source": "bbc-sentence", "premium": False},
    ],
    "reality": txt(
        "L'affaire s'est résolue par une méthode nouvelle appliquée à des traces anciennes : la généalogie génétique. "
        "Elle ne désigne pas un coupable, elle produit des apparentés, puis un arbre, puis des hypothèses réduites par "
        "l'âge et la géographie, enfin une confirmation ADN directe. Depuis, la méthode a permis d'identifier plus de "
        "150 suspects.",
        "The case was solved by a new method applied to old traces: genetic genealogy. It does not name a culprit, it "
        "produces relatives, then a tree, then hypotheses reduced by age and geography, and finally a direct DNA "
        "confirmation. Since then, the method has identified more than 150 suspects."),
    "errors": [
        item("Le rapprochement entre les affaires du nord et du sud de la Californie a pris des années, alors que des "
             "traces existaient.",
             "Linking the northern and southern California cases took years, although traces existed.",
             "CONFIRMED", "guardian-plea", "Cloisonnement géographique", "Geographic compartmentalisation"),
        item("L'auteur a exercé comme policier pendant la première période des faits ; cette circonstance n'a pas "
             "permis son identification à l'époque.",
             "The author worked as a police officer during the first period of offences; that circumstance did not "
             "lead to his identification at the time.",
             "CONFIRMED", "guardian-plea", "Angle non exploré", "Unexplored angle"),
    ],
    "cold_case": {
        "what_we_know": [
            item("13 meurtres retenus, des dizaines d'agressions sexuelles admises, 120 cambriolages évoqués.",
                 "13 murders retained, dozens of admitted sexual assaults, 120 burglaries mentioned.",
                 "CONFIRMED", "aetv-gsk"),
            item("Identification par généalogie génétique, confirmée par deux prélèvements discrets.",
                 "Identification through genetic genealogy, confirmed by two covert samples.", "CONFIRMED", "rossmo-2023"),
        ],
        "what_is_probable": [
            item("Des victimes pourraient rester non identifiées, selon la déclaration de la procureure après la "
                 "condamnation.",
                 "Victims may remain unidentified, according to the District Attorney's statement after sentencing.",
                 "PROBABLE", "bbc-sentence"),
        ],
        "what_is_disputed": [
            item("La lecture du profilage comportemental dans cette affaire fait l'objet d'une analyse comparative "
                 "publiée par D. Kim Rossmo en 2023, qui discute la place réelle du profilage par rapport à la preuve "
                 "génétique.",
                 "The reading of behavioural profiling in this case is the subject of a comparative analysis published "
                 "by D. Kim Rossmo in 2023, which discusses the real place of profiling relative to genetic evidence.",
                 "DISPUTED", "rossmo-2023"),
        ],
        "what_is_unknown": [
            item("Le nombre total de faits : « I don't believe we will ever know the magnitude of what Mr DeAngelo "
                 "did », a déclaré la procureure.",
                 "The total number of offences: 'I don't believe we will ever know the magnitude of what Mr DeAngelo "
                 "did', the District Attorney said.", "UNKNOWN", "bbc-sentence"),
        ],
        "latest_progress": [
            item("2020 : condamnation définitive à la perpétuité sans possibilité de libération conditionnelle.",
                 "2020: final sentence of life without possibility of parole.", "CONFIRMED", "bbc-sentence"),
        ],
        "leads": [], "limits": [
            item("La prescription a empêché toute poursuite pour les viols et cambriolages des années 1970-1980.",
                 "The statute of limitations prevented any prosecution for the rapes and burglaries of the 1970s-1980s.",
                 "CONFIRMED", "guardian-plea"),
        ],
    },
}

PSYCHOLOGY = {
    "disclaimer": txt("Aucun diagnostic n'est posé. Les éléments ci-dessous proviennent des sources citées.",
                      "No diagnosis is made. The elements below come from the cited sources."),
    "blocks": [
        block("fact", "Une position d'autorité pendant la première période", "A position of authority during the first period",
              "Il était policier à Exeter de 1973 à 1976, période au cours de laquelle l'activité criminelle débute "
              "selon les synthèses publiées. Il a été renvoyé en 1979 de la police d'Auburn pour des soupçons de vol.",
              "He was a police officer in Exeter from 1973 to 1976, the period during which the criminal activity "
              "begins according to published syntheses. He was dismissed in 1979 from the Auburn police on suspicion "
              "of theft.",
              "CONFIRMED", "guardian-plea"),
        block("fact", "Une déclaration enregistrée après l'arrestation", "A statement recorded after the arrest",
              "Après son arrestation, il a été entendu se dire à lui-même, dans une salle d'interrogatoire : « I did "
              "all those things. I destroyed all those lives. » Le parquet a rapporté cette déclaration à l'audience. "
              "Il a également évoqué une force interne qu'il ne contrôlait pas : « I didn't want to do those things. »",
              "After his arrest, he was heard telling himself, in an interview room: 'I did all those things. I "
              "destroyed all those lives.' The prosecution reported that statement at the hearing. He also referred to "
              "an internal force he could not control: 'I didn't want to do those things.'",
              "CONFIRMED", "abc-timeline"),
        block("analysis", "Ce que l'article scientifique discute", "What the scientific article discusses",
              "L'analyse comparative publiée par D. Kim Rossmo en 2023 porte sur la place du profilage comportemental "
              "dans cette enquête, et la compare à la preuve génétique qui a effectivement permis l'identification. "
              "C'est une analyse d'expert publiée, pas un fait de dossier.",
              "The comparative analysis published by D. Kim Rossmo in 2023 concerns the place of behavioural profiling "
              "in this investigation, and compares it with the genetic evidence that actually enabled identification. "
              "This is published expert analysis, not a case fact.",
              "CONFIRMED", "rossmo-2023"),
        block("unknown", "Ce qui n'est pas documenté", "What is not documented",
              "Les motivations, l'existence éventuelle d'autres faits, et le contenu d'éventuelles expertises "
              "psychiatriques ne figurent pas dans les sources consultées.",
              "Motivations, the possible existence of other offences, and the content of any psychiatric "
              "evaluations do not appear in the sources consulted.",
              "UNKNOWN", None),
    ],
}

VICTIMOLOGY = {
    "ethics_note": txt("Aucune caractéristique des victimes n'explique moralement les crimes.",
                       "No characteristic of the victims morally explains the crimes."),
    "blocks": [
        block("context", "Des domiciles, de nuit, dans onze comtés", "Homes, at night, across eleven counties",
              "Les faits sont commis au domicile des victimes, dans un large périmètre couvrant le nord et le sud de "
              "la Californie. L'accusation a retenu 87 victimes et 53 scènes dans 11 comtés.",
              "The offences are committed at victims' homes, over a wide area covering northern and southern "
              "California. The prosecution retained 87 victims and 53 scenes in 11 counties.",
              "CONFIRMED", "bbc-sentence"),
        block("analysis", "Des familles qui n'ont pas su", "Families who did not know",
              "La famille Smith n'a appris que vingt ans après les faits que le meurtre de Lyman et Charlene Smith "
              "relevait d'une série. Une survivante a décrit avoir cru, pendant des années, aux explications de son "
              "mari sur ses absences. La victimologie, ici, documente aussi l'ignorance dans laquelle les proches ont "
              "vécu.",
              "The Smith family learned only twenty years after the facts that the murder of Lyman and Charlene Smith "
              "belonged to a series. One survivor described believing, for years, her husband's explanations for his "
              "absences. Victimology here also documents the ignorance in which relatives lived.",
              "CONFIRMED", "guardian-plea"),
        block("vulnerability", "Une vulnérabilité de situation", "A situational vulnerability",
              "Les victimes ont été surprises chez elles, parfois en couple, avec un mode opératoire incluant la "
              "contrainte. C'est un facteur situationnel documenté, sans lien avec une responsabilité des victimes.",
              "Victims were surprised in their homes, sometimes as couples, with a method including restraint. This "
              "is a documented situational factor, unrelated to any responsibility of the victims.",
              "CONFIRMED", "aetv-gsk"),
    ],
}

COURT = {
    "jurisdiction": txt("États-Unis — Sacramento County Superior Court (audience délocalisée à Sacramento State University)",
                        "United States — Sacramento County Superior Court (hearing relocated to Sacramento State University)"),
    "verdict": txt("Plaidoyer de culpabilité sur 13 chefs de meurtre au premier degré et 13 chefs liés à des "
                   "enlèvements, le 29 juin 2020.",
                   "Guilty plea to 13 counts of first-degree murder and 13 kidnapping-related counts, on 29 June 2020."),
    "sentence": {
        "label": txt("Onze peines consécutives de réclusion à perpétuité sans possibilité de libération conditionnelle",
                     "Eleven consecutive life sentences without possibility of parole"),
        "pronounced": "2020-08-21",
        "requested": txt("Le parquet avait initialement requis la peine de mort ; elle a été écartée dans le cadre de "
                         "l'accord de plaidoyer, notamment en raison de la complexité du dossier et de l'âge avancé "
                         "de nombreuses victimes et témoins.",
                         "The prosecution had initially sought the death penalty; it was set aside as part of the plea "
                         "deal, notably because of the complexity of the file and the advanced age of many victims "
                         "and witnesses."),
        "cumul": txt("À ces onze peines consécutives s'ajoutent quinze peines concurrentes de réclusion à perpétuité "
                     "et des durées pour des chefs liés aux armes.",
                     "To these eleven consecutive terms are added fifteen concurrent life sentences and time for "
                     "weapons-related counts."),
        "reasoning": txt("Le juge Bowman a déclaré avoir prononcé le « maximum absolu » autorisé par la loi.",
                         "Judge Bowman stated he imposed the 'absolute maximum' allowed by law."),
        "appeal": txt("Pas de procès : le plaidoyer de culpabilité a mis fin à la procédure. Les auditions des "
                      "victimes se sont tenues du 18 au 20 août 2020.",
                      "No trial: the guilty plea ended the proceedings. Victim hearings were held from 18 to 20 "
                      "August 2020."),
        "reliability": "CONFIRMED", "source": "bbc-sentence",
    },
    "consequences": [
        item("La méthode d'identification a été reprise : plus de 150 suspects identifiés depuis 2018 selon ABC News, "
             "près de 100 affaires supplémentaires résolues selon le parquet.",
             "The identification method has been reused: more than 150 suspects identified since 2018 according to "
             "ABC News, nearly 100 additional solved cases according to the prosecution.",
             "CONFIRMED", "abc-timeline"),
        item("L'affaire a ouvert un débat public sur l'usage des bases de généalogie génétique ouvertes, le "
             "consentement des personnes qui y déposent leur ADN, et l'encadrement juridique de cette technique.",
             "The case opened a public debate on the use of open genetic genealogy databases, the consent of people "
             "who upload their DNA, and the legal framework of the technique.",
             "PROBABLE", "aetv-gsk"),
        item("La prescription a privé de poursuite des dizaines d'agressions sexuelles admises à l'audience.",
             "The statute of limitations deprived dozens of sexual assaults admitted at the hearing of prosecution.",
             "CONFIRMED", "guardian-plea"),
    ],
}

EXPERTS = [
    {"label": txt("Lecture scientifique — la généalogie génétique", "Scientific reading — genetic genealogy"),
     "field": "forensic_science",
     "position": txt("Paul Holes, scientifique légiste et enquêteur cold case retraité du sheriff du comté de Contra "
                     "Costa, a joué un rôle clé dans l'identification. La méthode repose sur la recherche "
                     "d'apparentés puis sur la réduction d'un arbre généalogique.",
                     "Paul Holes, forensic scientist and retired cold-case investigator for the Contra Costa County "
                     "Sheriff's Office, played a key role in the identification. The method relies on finding "
                     "relatives then reducing a family tree.",),
     "reliability": "CONFIRMED", "source": "rossmo-2023"},
    {"label": txt("Lecture critique — la place du profilage", "Critical reading — the place of profiling"),
     "field": "behavioural_analysis",
     "position": txt("D. Kim Rossmo publie en 2023 une analyse comparative du profilage comportemental dans cette "
                     "enquête, en le confrontant à la preuve génétique réellement déterminante.",
                     "D. Kim Rossmo published a comparative analysis of behavioural profiling in this investigation "
                     "in 2023, confronting it with the genuinely decisive genetic evidence.",),
     "reliability": "CONFIRMED", "source": "rossmo-2023"},
    {"label": txt("Lecture du parquet — l'ampleur inconnue", "Prosecution reading — the unknown scale"),
     "field": "judicial",
     "position": txt("La procureure Anne Marie Schubert a déclaré ne pas croire que l'ampleur réelle des faits sera "
                     "jamais connue, et a évoqué la possibilité de victimes non identifiées.",
                     "District Attorney Anne Marie Schubert said she did not believe the true scale of the offences "
                     "would ever be known, and mentioned the possibility of unidentified victims.",),
     "reliability": "CONFIRMED", "source": "bbc-sentence"},
]
EXPERTS_AGREEMENT = txt("Tous s'accordent sur le fait que l'identification est venue de la génétique, pas du profil.",
                        "All agree that identification came from genetics, not from the profile.")
EXPERTS_DISAGREEMENT = txt("Ils divergent sur la valeur rétrospective à accorder aux analyses comportementales produites pendant l'enquête.",
                           "They differ on the retrospective value to give to behavioural analyses produced during the investigation.")
EXPERTS_UNCERTAIN = txt("Ce qui reste incertain : le nombre total de faits et de victimes.",
                        "What remains uncertain: the total number of offences and victims.")

COUNTERFACTUALS = [
    counterfactual(
        "technology",
        "Et si la généalogie génétique avait existé en 1986 ?",
        "What if genetic genealogy had existed in 1986?",
        "Le dernier fait connu date de 1986. L'identification par généalogie génétique est intervenue en 2018. "
        "Trente-deux ans séparent les deux dates.",
        "The last known offence dates from 1986. Identification through genetic genealogy occurred in 2018. "
        "Thirty-two years separate the two dates.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Dernier fait connu", "Last known offence"), "date": "1986-05-04"},
            "hypothesis": {"label": txt("Technique inexistante", "Technique non-existent"), "date": "1986-05-04"},
            "scenario_event": {"label": txt("Identification par généalogie génétique", "Identification through genetic genealogy"), "date": "2018-04-24"},
            "outcome_event": {"label": txt("Condamnation", "Sentencing"), "date": "2020-08-21"},
            "documented_offences_after": [],
            "jurisdiction_note": txt(
                "La généalogie génétique suppose des bases de données ouvertes de génomique personnelle, qui "
                "n'existaient pas avant les années 2010. Aucune victime ultérieure n'étant documentée après 1986, le "
                "scénario ne permet pas de compter des vies : il mesure un écart de temps et une capacité technique. "
                "Il soulève aussi une question de droit : l'usage de ces bases pose des questions de consentement et "
                "de protection des données, dont l'encadrement varie selon les États.",
                "Genetic genealogy requires open personal genomics databases, which did not exist before the 2010s. "
                "Since no later victim is documented after 1986, the scenario does not allow lives to be counted: it "
                "measures a time gap and a technical capability. It also raises a legal question: the use of these "
                "databases poses consent and data-protection questions, whose framework varies by state."),
        },
        [
            {"date": "1974-01-01", "kind": "offence", "label": txt("Début de la période des faits", "Start of the offence period")},
            {"date": "1986-05-04", "kind": "reference", "label": txt("Dernier fait connu", "Last known offence")},
            {"date": "2018-04-24", "kind": "scenario", "label": txt("Identification", "Identification")},
            {"date": "2020-06-29", "kind": "fact", "label": txt("Plaidoyer de culpabilité", "Guilty plea")},
            {"date": "2020-08-21", "kind": "outcome", "label": txt("Condamnation", "Sentencing")},
        ],
        True, "rossmo-2023"),
    counterfactual(
        "professional_position",
        "Et si le passé de policier avait été examiné comme une piste ?",
        "What if the police background had been examined as a lead?",
        "L'auteur a été policier à Exeter de 1973 à 1976, puis renvoyé de la police d'Auburn en 1979. La première "
        "période des faits coïncide avec cette affectation.",
        "The author was a police officer in Exeter from 1973 to 1976, then dismissed from the Auburn police in 1979. "
        "The first period of offences coincides with that assignment.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Affectation à Exeter", "Assignment to Exeter"), "date": "1973-01-01"},
            "hypothesis": {"label": txt("Renvoi d'Auburn", "Dismissal from Auburn"), "date": "1979-01-01"},
            "scenario_event": {"label": txt("Identification", "Identification"), "date": "2018-04-24"},
            "jurisdiction_note": txt(
                "Aucune source consultée n'établit que les services d'enquête aient ou non examiné les effectifs de "
                "police de la région à l'époque. Cette question contrefactuelle porte donc sur une hypothèse non "
                "documentée : l'application affiche l'écart de temps sans affirmer ce qu'une vérification aurait "
                "produit.",
                "No source consulted establishes whether or not investigative services examined regional police "
                "staff at the time. This counterfactual question therefore concerns an undocumented hypothesis: the "
                "application displays the time gap without asserting what a check would have produced."),
        },
        [
            {"date": "1973-01-01", "kind": "reference", "label": txt("Policier à Exeter", "Police officer in Exeter")},
            {"date": "1979-01-01", "kind": "fact", "label": txt("Renvoyé de la police d'Auburn", "Dismissed from Auburn police")},
            {"date": "1986-05-04", "kind": "offence", "label": txt("Dernier fait connu", "Last known offence")},
            {"date": "2018-04-24", "kind": "scenario", "label": txt("Identification", "Identification")},
        ],
        False, "guardian-plea"),
]

LESSONS = [
    item("Une technique nouvelle ne relit pas seulement les dossiers récents : elle relit des scellés anciens. Ici, "
         "un kit de prélèvement des années 1980 a identifié un homme en 2018.",
         "A new technique does not only reread recent files: it rereads old exhibits. Here, a 1980s rape kit "
         "identified a man in 2018.",
         "CONFIRMED", "aetv-gsk", "Science différée", "Deferred science"),
    item("La généalogie génétique produit des apparentés, pas des coupables : la confirmation exige un prélèvement "
         "direct comparé.",
         "Genetic genealogy produces relatives, not culprits: confirmation requires a directly compared sample.",
         "CONFIRMED", "rossmo-2023", "Chaîne probatoire", "Evidential chain"),
    item("La prescription peut rendre impossible la poursuite de faits admis à l'audience : des dizaines "
         "d'agressions sexuelles reconnues n'ont pas pu être jugées.",
         "The statute of limitations can make it impossible to prosecute offences admitted at the hearing: dozens of "
         "acknowledged sexual assaults could not be tried.",
         "CONFIRMED", "guardian-plea", "Droit", "Law"),
    item("Un accord de plaidoyer peut écarter la peine de mort pour des raisons pratiques : complexité du dossier, "
         "âge des victimes et des témoins.",
         "A plea deal can rule out the death penalty for practical reasons: complexity of the file, age of victims "
         "and witnesses.",
         "CONFIRMED", "guardian-plea", "Procédure", "Procedure"),
    item("L'ampleur d'une série peut rester inconnue même après une condamnation : la procureure a déclaré qu'elle ne "
         "serait probablement jamais établie.",
         "The scale of a series can remain unknown even after a conviction: the District Attorney said it would "
         "probably never be established.",
         "CONFIRMED", "bbc-sentence", "Limites", "Limits"),
    item("Le profilage comportemental a été discuté scientifiquement après coup : son rôle réel dans cette enquête "
         "fait l'objet d'une publication comparative.",
         "Behavioural profiling was scientifically discussed afterwards: its real role in this investigation is the "
         "subject of a comparative publication.",
         "CONFIRMED", "rossmo-2023", "Esprit critique", "Critical thinking"),
]

UNKNOWNS = [
    item("Le nombre total de faits et de victimes.", "The total number of offences and victims.", "UNKNOWN", "bbc-sentence"),
    item("Les raisons de l'arrêt de la série en 1986.", "The reasons the series stopped in 1986.", "UNKNOWN", "aetv-gsk"),
    item("Le contenu des éventuelles expertises psychiatriques.", "The content of any psychiatric evaluations.", "UNKNOWN", None),
    item("Si les effectifs de police de la région ont été examinés comme piste pendant l'enquête.",
         "Whether regional police staff were examined as a lead during the investigation.", "UNKNOWN", None),
]

SECTIONS = merge_sections(default_sections(), [
    {"key": "introduction", "blocks": [block(
        "paragraph", "Le premier cold case résolu par généalogie génétique", "The first cold case solved by genetic genealogy",
        "Plus de trente ans après le dernier fait connu, un profil ADN déposé sur une base de généalogie ouverte a "
        "permis de construire un arbre, de le réduire à trois noms, puis de confirmer une identité par deux "
        "prélèvements discrets.",
        "More than thirty years after the last known offence, a DNA profile uploaded to an open genealogy database "
        "allowed a tree to be built, reduced to three names, then an identity confirmed by two covert samples.",
        "CONFIRMED", "aetv-gsk")]},
    {"key": "context", "blocks": [block(
        "paragraph", "La Californie, 1974-1986", "California, 1974-1986",
        "Onze comtés, deux zones distinctes — le nord puis le sud de l'État —, et des années avant que les enquêteurs "
        "ne les rapprochent.",
        "Eleven counties, two distinct areas — north then south of the state — and years before investigators linked "
        "them.",
        "CONFIRMED", "guardian-plea")]},
    {"key": "offender", "blocks": [block(
        "paragraph", "Joseph James DeAngelo Jr (né en 1945)", "Joseph James DeAngelo Jr (born 1945)",
        "Né le 8 novembre 1945 à Bath, État de New York. Policier à Exeter de 1973 à 1976, renvoyé de la police "
        "d'Auburn en 1979, puis mécanicien poids lourds à Roseville de 1990 à sa retraite en 2017. Ancien militaire "
        "de l'US Navy, vétéran du Vietnam, père de trois enfants.",
        "Born 8 November 1945 in Bath, New York State. Police officer in Exeter from 1973 to 1976, dismissed from the "
        "Auburn police in 1979, then truck mechanic in Roseville from 1990 until his retirement in 2017. Former US "
        "Navy serviceman, Vietnam veteran, father of three.",
        "CONFIRMED", "rossmo-2023")]},
    {"key": "behaviour", "blocks": [block(
        "behaviour", "Intrusion au domicile et contrainte", "Home intrusion and restraint",
        "Les faits documentés se caractérisent par une intrusion au domicile, la contrainte des occupants et une "
        "répartition géographique large. La description relève du dossier ; son interprétation comportementale est "
        "discutée dans la littérature scientifique.",
        "The documented offences are characterised by intrusion into the home, restraint of occupants and a wide "
        "geographic spread. The description belongs to the file; its behavioural interpretation is discussed in the "
        "scientific literature.",
        "CONFIRMED", "rossmo-2023")]},
    {"key": "consequences", "blocks": [block(
        "paragraph", "Une méthode qui s'est généralisée", "A method that became widespread",
        "Depuis 2018, plus de 150 suspects ont été identifiés par généalogie génétique selon ABC News. Le débat "
        "public porte désormais sur le consentement des personnes déposant leur ADN sur ces plateformes.",
        "Since 2018, more than 150 suspects have been identified through genetic genealogy according to ABC News. "
        "Public debate now concerns the consent of people uploading their DNA to these platforms.",
        "CONFIRMED", "abc-timeline")]},
])

EPISODES = [
    {
        "number": 1,
        "title": txt("L'arbre aux mille noms", "The tree of a thousand names"),
        "description": txt("Californie, 1974-2018. Comment un profil ADN déposé sur une base généalogique ouverte a "
                           "mis fin à plus de trente ans de dossier froid.",
                           "California, 1974-2018. How a DNA profile uploaded to an open genealogy database ended more "
                           "than thirty years of cold file."),
        "modes": ["documentary", "investigation", "expert", "chronology", "express", "psychology", "victims"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 70, "title": txt("Onze comtés", "Eleven counties")},
            {"at": 250, "title": txt("Le dossier refroidit", "The file goes cold")},
            {"at": 420, "title": txt("Un profil déposé sur GEDmatch", "A profile uploaded to GEDmatch")},
            {"at": 600, "title": txt("Et maintenant, une question", "And now, a question")},
            {"at": 640, "title": txt("Trois jours d'auditions", "Three days of hearings")},
        ],
        "transcript": {"segments": [
            {"id": "k1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X, à travers mon regard. Aujourd'hui, une affaire américaine qui a changé "
                     "la manière de rouvrir les dossiers froids.",
             "text_en": "You are on YANIS//X, through my eyes. Today, an American case that changed how cold files are "
                        "reopened."},
            {"id": "k2", "t": 70, "speaker": "yanis",
             "text": "Californie, entre 1974 et 1986. Des cambriolages, des agressions sexuelles, des meurtres. Onze "
                     "comtés. Cinquante-trois scènes. L'accusation retiendra quatre-vingt-sept victimes. D'abord le "
                     "nord de l'État, puis le sud. Il faudra des années aux enquêteurs pour rapprocher les deux zones.",
             "text_en": "California, between 1974 and 1986. Burglaries, sexual assaults, murders. Eleven counties. "
                        "Fifty-three scenes. The prosecution would retain eighty-seven victims. First the north of the "
                        "state, then the south. It would take investigators years to link the two areas."},
            {"id": "k3", "t": 250, "speaker": "yanis",
             "text": "En 1980, à Ventura, Lyman Smith et son épouse Charlene sont tués chez eux. Leur fille Carole a "
                     "dix-huit ans. Leur fils de douze ans découvre les corps. La famille ne saura que vingt ans plus "
                     "tard que ces meurtres appartenaient à une série.",
             "text_en": "In 1980, in Ventura, Lyman Smith and his wife Charlene are killed at their home. Their "
                        "daughter Carole is eighteen. Their twelve-year-old son finds the bodies. The family would "
                        "learn only twenty years later that these murders belonged to a series."},
            {"id": "k4", "t": 420, "speaker": "yanis",
             "text": "Puis le dossier refroidit. En 2018, un profil ADN issu d'un kit de prélèvement du comté de "
                     "Ventura est déposé sur GEDmatch, une plateforme ouverte de généalogie génétique. Le site ne "
                     "désigne personne : il renvoie des apparentés. Les enquêteurs construisent un arbre de plus de "
                     "mille noms. Ils le réduisent en croisant l'âge, la localisation, d'autres données. Trois "
                     "individus restent, dont deux frères.",
             "text_en": "Then the file goes cold. In 2018, a DNA profile from a Ventura County rape kit is uploaded to "
                        "GEDmatch, an open genetic genealogy platform. The site names no one: it returns relatives. "
                        "Investigators build a tree of more than a thousand names. They reduce it by crossing age, "
                        "location, other data. Three individuals remain, including two brothers."},
            {"id": "k5", "t": 560, "speaker": "yanis",
             "text": "Deux prélèvements discrets : une poignée de voiture, un mouchoir dans une poubelle. Les deux "
                     "sont compatibles avec les profils des comtés d'Orange et de Ventura. Le 24 avril 2018, Joseph "
                     "DeAngelo est arrêté à son domicile de Citrus Heights. Il a soixante-douze ans. Il était policier "
                     "à Exeter entre 1973 et 1976.",
             "text_en": "Two covert samples: a car door handle, a tissue in a bin. Both are consistent with the Orange "
                        "and Ventura County profiles. On 24 April 2018, Joseph DeAngelo is arrested at his Citrus "
                        "Heights home. He is seventy-two. He was a police officer in Exeter between 1973 and 1976."},
            {"id": "k6", "t": 600, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "k7", "t": 640, "speaker": "yanis",
             "text": "Le 29 juin 2020, il plaide coupable de treize meurtres et de treize chefs liés à des "
                     "enlèvements. Il admet des dizaines d'agressions sexuelles que la prescription empêche de "
                     "poursuivre. La peine de mort, initialement requise, est écartée dans l'accord. Du 18 au 20 août, "
                     "les survivantes et les familles parlent. Le 21 août, le juge Bowman prononce onze peines "
                     "consécutives de réclusion à perpétuité sans possibilité de libération : le maximum autorisé par "
                     "la loi, dit-il.",
             "text_en": "On 29 June 2020, he pleads guilty to thirteen murders and thirteen kidnapping-related "
                        "counts. He admits dozens of sexual assaults that the statute of limitations prevents from "
                        "being prosecuted. The death penalty, initially sought, is set aside in the deal. From 18 to "
                        "20 August, survivors and families speak. On 21 August, Judge Bowman imposes eleven "
                        "consecutive life terms without possibility of parole: the maximum allowed by law, he says."},
            {"id": "k8", "t": 840, "speaker": "yanis",
             "text": "Après la condamnation, la procureure Anne Marie Schubert a dit une chose que cette application "
                     "retient : « Je ne crois pas que nous saurons jamais l'ampleur de ce que M. DeAngelo a fait. » "
                     "Certaines affaires ne se referment pas. Elles s'arrêtent.",
             "text_en": "After sentencing, District Attorney Anne Marie Schubert said something this application keeps: "
                        "'I don't believe we will ever know the magnitude of what Mr DeAngelo did.' Some cases do not "
                        "close. They stop."},
            {"id": "k9", "t": 940, "speaker": "yanis",
             "text": "Écouter les histoires. Comprendre les affaires. Ne jamais oublier les victimes — y compris "
                     "celles dont nous ne connaîtrons pas le nom.",
             "text_en": "Listen to the stories. Understand the cases. Never forget the victims — including those whose "
                        "names we will never know."},
        ]},
    },
]

QUESTIONS = [
    question("1", 600, "evidence",
             "Une base de généalogie génétique renvoie des apparentés à partir d'un profil de scène. Que produit cette étape, à elle seule ?",
             "A genetic genealogy database returns relatives from a scene profile. What does this step alone produce?",
             [("a", "L'identification du coupable", "Identification of the culprit"),
              ("b", "Un ensemble d'hypothèses nominatives à réduire puis à confirmer", "A set of named hypotheses to reduce then confirm"),
              ("c", "Une preuve recevable devant la cour", "Admissible evidence before the court"),
              ("d", "Rien d'exploitable", "Nothing usable")],
             {"fr": {"whatInvestigatorsKnew": "Le dépôt du profil sur GEDmatch a renvoyé des apparentés par degré de partage de marqueurs. Un arbre de plus de mille noms a été construit, réduit à trois individus, dont Joseph DeAngelo et son frère.",
                     "whatExpertsProposed": "La généalogie génétique ne désigne pas un individu : elle construit un ensemble de candidats. La confirmation exige une comparaison directe, ici deux prélèvements discrets compatibles avec les profils des scènes.",
                     "documented": "La chaîne complète est documentée par A&E et par l'article de D. Kim Rossmo.",
                     "hypothetical": "Ce que l'affaire aurait donné si les deux prélèvements discrets n'avaient pas été possibles.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir que l'usage de bases ouvertes soulèverait ensuite un débat sur le consentement et la protection des données.",
                     "answer_note": "La réponse attendue est B. A et C confondent piste et preuve."},
              "en": {"whatInvestigatorsKnew": "Uploading the profile to GEDmatch returned relatives by degree of shared markers. A tree of more than a thousand names was built, reduced to three individuals, including Joseph DeAngelo and his brother.",
                     "whatExpertsProposed": "Genetic genealogy does not name an individual: it builds a set of candidates. Confirmation requires a direct comparison, here two covert samples consistent with scene profiles.",
                     "documented": "The full chain is documented by A&E and by D. Kim Rossmo's article.",
                     "hypothetical": "What the case would have produced had the two covert samples not been possible.",
                     "whatYouCouldNotKnow": "You could not know that the use of open databases would later raise a debate on consent and data protection.",
                     "answer_note": "The expected answer is B. A and C confuse lead with evidence."}},
             "rossmo-2023"),
    question("1", 780, "chronology",
             "Des dizaines d'agressions sexuelles ont été admises à l'audience sans pouvoir être poursuivies. Pourquoi ?",
             "Dozens of sexual assaults were admitted at the hearing without being prosecutable. Why?",
             [("a", "Parce que les victimes ne voulaient pas témoigner", "Because victims did not want to testify"),
              ("b", "Parce que les faits étaient prescrits", "Because the offences were time-barred"),
              ("c", "Parce que l'accord de plaidoyer l'interdisait", "Because the plea deal forbade it"),
              ("d", "Parce qu'aucune preuve n'existait", "Because no evidence existed")],
             {"fr": {"whatInvestigatorsKnew": "Les viols et cambriolages commis dans les années 1970 et 1980 étaient prescrits : les poursuites ont porté sur 13 meurtres et 13 chefs liés à des enlèvements.",
                     "whatExpertsProposed": "La prescription est une règle de droit qui limite dans le temps l'exercice de l'action publique. Elle peut conduire à ce que des faits admis ne soient pas jugés.",
                     "documented": "The Guardian documente la prescription et le contenu du plaidoyer.",
                     "hypothetical": "Ce qu'aurait produit une législation différente à l'époque des faits.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir si d'autres victimes resteraient non identifiées : la procureure l'a elle-même indiqué après la condamnation.",
                     "answer_note": "La réponse attendue est B. C'est un point de droit, pas un choix des victimes."},
              "en": {"whatInvestigatorsKnew": "The rapes and burglaries committed in the 1970s and 1980s were time-barred: prosecutions covered 13 murders and 13 kidnapping-related counts.",
                     "whatExpertsProposed": "The statute of limitations is a rule of law limiting in time the exercise of public prosecution. It can lead to admitted facts not being tried.",
                     "documented": "The Guardian documents the prescription and the content of the plea.",
                     "hypothetical": "What different legislation at the time of the facts would have produced.",
                     "whatYouCouldNotKnow": "You could not know whether other victims would remain unidentified: the District Attorney said so herself after sentencing.",
                     "answer_note": "The expected answer is B. It is a point of law, not a choice by the victims."}},
             "guardian-plea"),
]

CASE = {
    "id": CASE_ID,
    "title": txt("Le Golden State Killer", "The Golden State Killer"),
    "subtitle": txt("Californie, 1974-1986. Onze comtés, cinquante-trois scènes, et une identification en 2018 par "
                    "généalogie génétique.",
                    "California, 1974-1986. Eleven counties, fifty-three scenes, and an identification in 2018 through "
                    "genetic genealogy."),
    "country": "US", "region": "Californie", "city": "Sacramento",
    "year_start": 1974, "year_end": 2020, "period_label": txt("1974 – 2020", "1974 – 2020"),
    "status": "RESOLVED", "type": "serial",
    "tags": ["serial_killer", "cold_case", "genetic_genealogy", "dna", "usa", "police_offender", "statute_of_limitations"],
    "tier": "PREMIUM", "editorial": "yanis", "published_at": "2026-09-24", "sensitive": True,
    "triggers": txt("Agressions sexuelles, meurtres au domicile ; ampleur des faits évoquée sans détail graphique.",
                    "Sexual assaults, murders at home; scale of the offences mentioned without graphic detail."),
    "lat": 37.5, "lon": -121.0, "cover": "cover-gsk",
    "stats": {"victims_documented": 13, "victims_prosecution_scale": 87, "scenes": 53, "counties": 11, "duration_years": 46},
    "summary": txt(
        "Entre 1974 et 1986, une série de cambriolages, d'agressions sexuelles et de meurtres est commise dans le "
        "nord puis le sud de la Californie. L'accusation retiendra 87 victimes et 53 scènes dans 11 comtés. Le "
        "dossier reste froid pendant plus de trente ans. En 2018, un profil ADN issu d'un kit de prélèvement du comté "
        "de Ventura est déposé sur GEDmatch : un arbre généalogique de plus de mille noms est construit, réduit à "
        "trois individus, puis confirmé par deux prélèvements discrets. Joseph James DeAngelo, ancien policier âgé de "
        "72 ans, est arrêté le 24 avril 2018 à Citrus Heights. Il plaide coupable le 29 juin 2020 de 13 meurtres et "
        "13 chefs liés à des enlèvements, la peine de mort étant écartée par l'accord. Le 21 août 2020, après trois "
        "jours d'auditions des victimes et des familles, il est condamné à onze peines consécutives de réclusion à "
        "perpétuité sans possibilité de libération conditionnelle.",
        "Between 1974 and 1986, a series of burglaries, sexual assaults and murders is committed in northern then "
        "southern California. The prosecution would retain 87 victims and 53 scenes in 11 counties. The file remains "
        "cold for more than thirty years. In 2018, a DNA profile from a Ventura County rape kit is uploaded to "
        "GEDmatch: a family tree of more than a thousand names is built, reduced to three individuals, then confirmed "
        "by two covert samples. Joseph James DeAngelo, a former police officer aged 72, is arrested on 24 April 2018 "
        "in Citrus Heights. He pleads guilty on 29 June 2020 to 13 murders and 13 kidnapping-related counts, the "
        "death penalty being set aside by the deal. On 21 August 2020, after three days of victim and family "
        "hearings, he is sentenced to eleven consecutive life terms without possibility of parole."),
    "sources": SOURCES, "victims": VICTIMS, "memorial": MEMORIAL, "timeline": TIMELINE, "locations": LOCATIONS,
    "evidence": EVIDENCE, "investigation": INVESTIGATION, "psychology": PSYCHOLOGY, "victimology": VICTIMOLOGY,
    "court": COURT, "experts": EXPERTS, "experts_agreement": EXPERTS_AGREEMENT,
    "experts_disagreement": EXPERTS_DISAGREEMENT, "experts_uncertain": EXPERTS_UNCERTAIN,
    "counterfactuals": COUNTERFACTUALS, "lessons": LESSONS, "unknowns": UNKNOWNS, "sections": SECTIONS,
    "episodes": EPISODES, "questions": QUESTIONS,
}
