"""
DOSSIER 04 — DENNIS RADER, DIT « BTK » (États-Unis, Kansas, 1974-2005)

Sources publiques vérifiées le 2026-09-24.
"""
from ..case_template import (block, counterfactual, default_sections, fact, item,
                             merge_sections, question, source, txt)

CASE_ID = "btk-rader"
V = "2026-09-24"

SOURCES = [
    source("wiki-rader", CASE_ID, "Dennis Rader", "Dennis Rader",
           "Wikipedia (English)", "Contributors", "https://en.wikipedia.org/wiki/Dennis_Rader",
           "2026", "public_archive", "PROBABLE", V,
           "Encyclopédie collaborative : données recoupées avec la presse ; niveau PROBABLE par prudence.",
           "Collaborative encyclopaedia: data cross-checked with the press; PROBABLE level as a precaution."),
    source("biography-rader", CASE_ID, "Dennis Rader — Who Is the BTK Killer?", "Dennis Rader — Who Is the BTK Killer?",
           "Biography.com", "Redaction", "https://www.biography.com/crime/dennis-rader",
           "2025-01-21", "press", "CONFIRMED", V,
           "Éléments biographiques, découverte des corps, réémergence de 2004, aveux et condamnation.",
           "Biographical elements, discovery of the bodies, 2004 re-emergence, guilty plea and sentence."),
    source("creed-btk", CASE_ID, "The BTK Killer: How Dennis Rader Was Finally Caught",
           "The BTK Killer: How Dennis Rader Was Finally Caught",
           "Cassian Creed", "Cassian Creed", "https://cassiancreed.com/post/the-btk-killer-how-dennis-rader-was-finally-caught/",
           "2026-05-20", "press", "PROBABLE", V,
           "Blog de synthèse : dates d'arrestation, de plaidoyer et de condamnation recoupées avec Wikipedia.",
           "Summary blog: arrest, plea and sentencing dates cross-checked with Wikipedia."),
]

VICTIMS = [

    {"order": 0, "first_name": "Joseph", "last_name": "Otero", "age": "38", "reliability": "PROBABLE", "source": "biography-rader",
     "life": {"fr": {"headline": "Joseph Otero", "items": [
         {"label": "Situation", "text": "Père de famille, tué à son domicile de Wichita avec son épouse et deux de leurs enfants le 15 janvier 1974."},
         {"label": "Découverte", "text": "Les corps sont retrouvés le lendemain matin par leur fils Charlie, 15 ans, en rentrant."}]},
        "en": {"headline": "Joseph Otero", "items": [
         {"label": "Situation", "text": "A father, killed at his Wichita home with his wife and two of their children on 15 January 1974."},
         {"label": "Discovery", "text": "The bodies were found the next morning by their son Charlie, 15, coming home."}]}},
     "disappearance": {"fr": {"items": [{"label": "Date", "text": "15 janvier 1974 — premier fait de la série."}]},
                       "en": {"items": [{"label": "Date", "text": "15 January 1974 — first offence of the series."}]}}},


    {"order": 1, "first_name": "Josephine", "last_name": "Otero", "age": "34", "reliability": "PROBABLE", "source": "biography-rader",
     "life": {"fr": {"headline": "Josephine Otero", "items": [{"label": "Situation", "text": "Épouse de Joseph Otero, mère de famille, tuée le 15 janvier 1974."}]},
             "en": {"headline": "Josephine Otero", "items": [{"label": "Situation", "text": "Wife of Joseph Otero, a mother, killed on 15 January 1974."}]}},
     "disappearance": {"fr": {"items": [{"label": "Date", "text": "15 janvier 1974."}]},
                       "en": {"items": [{"label": "Date", "text": "15 January 1974."}]}}},


    {"order": 2, "first_name": "Joseph", "last_name": "Otero Jr", "age": "9", "reliability": "PROBABLE", "source": "biography-rader",
     "life": {"fr": {"headline": "Joseph Otero Jr", "items": [{"label": "Âge", "text": "9 ans."}, {"label": "Situation", "text": "Enfant de la famille Otero, tué au domicile familial."}]},
             "en": {"headline": "Joseph Otero Jr", "items": [{"label": "Age", "text": "9."}, {"label": "Situation", "text": "Child of the Otero family, killed at the family home."}]}},
     "disappearance": {"fr": {"items": [{"label": "Date", "text": "15 janvier 1974."}]},
                       "en": {"items": [{"label": "Date", "text": "15 January 1974."}]}}},


    {"order": 3, "first_name": "Josephine", "last_name": "Otero (Jo)", "age": "11", "reliability": "PROBABLE", "source": "biography-rader",
     "life": {"fr": {"headline": "Josephine « Jo » Otero", "items": [{"label": "Âge", "text": "11 ans."}, {"label": "Situation", "text": "Enfant de la famille Otero."}]},
             "en": {"headline": "Josephine 'Jo' Otero", "items": [{"label": "Age", "text": "11."}, {"label": "Situation", "text": "Child of the Otero family."}]}},
     "disappearance": {"fr": {"items": [{"label": "Date", "text": "15 janvier 1974."}]},
                       "en": {"items": [{"label": "Date", "text": "15 January 1974."}]}}},


    {"order": 4, "first_name": "Kevin", "last_name": "Bright", "age": "—", "reliability": "CONFIRMED", "source": "wiki-rader",
     "life": {"fr": {"headline": "Kevin Bright, survivant", "items": [
         {"label": "Statut", "text": "Survivant. Il a décrit l'agresseur comme « un type de taille moyenne, moustache fournie, des yeux “psychotiques” », selon un article de TIME cité par Biography.com."}]},
        "en": {"headline": "Kevin Bright, survivor", "items": [
         {"label": "Status", "text": "Survivor. He described the attacker as 'an average-sized guy, bushy mustache, “psychotic” eyes', according to a TIME article cited by Biography.com."}]}},
     "disappearance": {"fr": {"items": [{"label": "Élément", "text": "Son signalement n'a pas conduit à une identification à l'époque."}]},
                       "en": {"items": [{"label": "Element", "text": "His description did not lead to an identification at the time."}]}}},
]

MEMORIAL = {
    "title": txt("Dix victimes, Sedgwick County 1974-1991", "Ten victims, Sedgwick County 1974-1991"),
    "biography": txt(
        "Dix personnes ont été tuées dans le comté de Sedgwick entre le 15 janvier 1974 et le 19 janvier 1991. Quatre "
        "d'entre elles appartenaient à la même famille, les Otero : un père, une mère et deux enfants de 9 et 11 ans. "
        "Leur fils aîné, Charlie, 15 ans, a découvert les corps en rentrant. Une autre personne, Kevin Bright, a "
        "survécu et a livré un signalement.",
        "Ten people were killed in Sedgwick County between 15 January 1974 and 19 January 1991. Four of them belonged "
        "to the same family, the Oteros: a father, a mother and two children aged 9 and 11. Their eldest son, Charlie, "
        "15, found the bodies on coming home. Another person, Kevin Bright, survived and gave a description.",
    ),
    "testimony": txt(
        "À l'audience de condamnation du 18 août 2005, les familles des victimes se sont exprimées avant le prononcé "
        "de la peine. Ces déclarations ont précédé le monologue de l'accusé, que le procureur a comparé à un discours "
        "de remise de prix.",
        "At the sentencing hearing of 18 August 2005, victims' families spoke before the sentence was pronounced. "
        "Those statements preceded the accused's monologue, which the prosecutor compared to an awards acceptance "
        "speech.",
    ),
    "memory": txt(
        "L'homme condamné occupait des fonctions sociales visibles : responsable de troupe scoute, président du "
        "conseil de sa paroisse, employé municipal. Cette dissimulation sociale a duré trente ans. Elle n'efface pas "
        "les dix personnes tuées, dont deux enfants.",
        "The convicted man held visible social roles: scout troop leader, president of his church council, city "
        "employee. That social concealment lasted thirty years. It does not erase the ten people killed, including "
        "two children.",
    ),
}

TIMELINE = [
    fact("Naissance de Dennis Lynn Rader à Pittsburg (Kansas). Il grandit à Wichita.",
         "Dennis Lynn Rader is born in Pittsburg (Kansas). He grows up in Wichita.",
         "CONFIRMED", "wiki-rader", "Naissance", "Birth", "1945-03-09"),
    fact("Quatre membres de la famille Otero sont tués à leur domicile de Wichita. Le lendemain matin, leur fils "
         "Charlie, 15 ans, découvre les corps.",
         "Four members of the Otero family are killed at their Wichita home. The next morning, their son Charlie, 15, "
         "discovers the bodies.",
         "CONFIRMED", "biography-rader", "Premier fait", "First offence", "1974-01-15"),
    fact("Une lettre revendiquant le meurtre des Otero est déposée dans un livre d'une bibliothèque publique.",
         "A letter claiming the Otero murders is placed in a public library book.",
         "CONFIRMED", "biography-rader", "Première revendication", "First claim", "1974-10"),
    fact("Kevin Bright survit à une agression et décrit son agresseur : taille moyenne, moustache fournie, regard "
         "décrit comme « psychotique ». Le signalement ne conduit pas à une identification.",
         "Kevin Bright survives an attack and describes his attacker: average height, bushy moustache, gaze described "
         "as 'psychotic'. The description does not lead to an identification.",
         "CONFIRMED", "biography-rader", "Un survivant", "A survivor", "1974"),
    fact("La série se poursuit jusqu'au 19 janvier 1991, date à laquelle Dolores Davis est enlevée à son domicile : "
         "dernière victime connue.",
         "The series continues until 19 January 1991, when Dolores Davis is taken from her home: the last known victim.",
         "CONFIRMED", "biography-rader", "Dernier fait connu", "Last known offence", "1991-01-19"),
    fact("Après treize ans de silence, l'auteur des lettres reprend contact avec les médias et les enquêteurs, à la "
         "faveur de la couverture du trentième anniversaire des meurtres Otero.",
         "After thirteen years of silence, the author of the letters resumes contact with media and investigators, in "
         "the wake of coverage of the thirtieth anniversary of the Otero murders.",
         "CONFIRMED", "wiki-rader", "Réémergence", "Re-emergence", "2004"),
    fact("Il demande à la police si une disquette pouvait être tracée. Les enquêteurs répondent par voie de presse "
         "que non. Cette réponse était fausse.",
         "He asks the police whether a floppy disk could be traced. Investigators answer through the media that it "
         "could not. That answer was false.",
         "CONFIRMED", "creed-btk", "Le piège", "The trap", "2005-01"),
    fact("Une disquette envoyée par courrier contient un document Word supprimé dont les métadonnées mentionnent "
         "« Christ Lutheran Church » et un dernier modificateur nommé « Dennis ». Une recherche en ligne montre qu'un "
         "« Dennis Rader » est président du conseil de cette paroisse.",
         "A floppy disk sent by mail contains a deleted Word document whose metadata mention 'Christ Lutheran Church' "
         "and a last modifier named 'Dennis'. An online search shows a 'Dennis Rader' is president of that "
         "congregation's council.",
         "CONFIRMED", "wiki-rader", "Métadonnées", "Metadata", "2005-02-16"),
    fact("Un lien familial est confirmé par comparaison entre l'ADN de scènes et un échantillon obtenu à partir de "
         "dossier médical concernant sa fille.",
         "A family link is confirmed by comparing scene DNA with a sample obtained from medical records concerning "
         "his daughter.",
         "CONFIRMED", "creed-btk", "ADN familial", "Familial DNA", "2005-02"),
    fact("Dennis Rader est arrêté au volant près de son domicile de Park City, peu après midi. Les perquisitions "
         "concernent son domicile, son véhicule, sa paroisse, son bureau et la bibliothèque municipale.",
         "Dennis Rader is arrested while driving near his Park City home, shortly after noon. Searches concern his "
         "home, his vehicle, his church, his office and the municipal library.",
         "CONFIRMED", "wiki-rader", "Arrestation", "Arrest", "2005-02-25"),
    fact("Il est inculpé de dix meurtres au premier degré devant la district court du comté de Sedgwick.",
         "He is charged with ten counts of first-degree murder before the Sedgwick County district court.",
         "CONFIRMED", "wiki-rader", "Inculpation", "Indictment", "2005-02-28"),
    fact("À la date prévue pour son procès, il plaide coupable des dix meurtres et décrit les faits devant la cour, "
         "qu'il qualifie de « projets », sans exprimer d'excuses.",
         "On the date set for his trial, he pleads guilty to the ten murders and describes the facts before the court, "
         "calling them 'projects', without expressing apologies.",
         "CONFIRMED", "wiki-rader", "Plaidoyer de culpabilité", "Guilty plea", "2005-06-27"),
    fact("Condamnation à dix peines de réclusion à perpétuité consécutives, avec un minimum de 175 ans. La peine de "
         "mort n'était pas applicable : le Kansas l'a rétablie en 1994, après les faits.",
         "Sentenced to ten consecutive life terms, with a minimum of 175 years. The death penalty was not applicable: "
         "Kansas reinstated it in 1994, after the facts.",
         "CONFIRMED", "wiki-rader", "Condamnation", "Sentencing", "2005-08-18"),
    fact("Il est incarcéré à l'El Dorado Correctional Facility.",
         "He is imprisoned at El Dorado Correctional Facility.",
         "CONFIRMED", "wiki-rader", "Détention", "Detention", "2005"),
]

LOCATIONS = [
    {"kind": "city", "names": txt("Wichita et Park City (Kansas)", "Wichita and Park City (Kansas)"),
     "city": "Wichita", "region": "Kansas / Sedgwick County", "country": "US", "lat": 37.69, "lon": -97.34,
     "precision": "city", "date": "1974-1991",
     "note": txt("Secteur des faits et domicile de l'auteur. Aucune adresse privée n'est affichée.",
                 "Area of the facts and the author's home. No private address is displayed."),
     "reliability": "CONFIRMED", "source": "wiki-rader"},
    {"kind": "court", "names": txt("District Court du comté de Sedgwick", "Sedgwick County District Court"),
     "city": "Wichita", "region": "Kansas", "country": "US", "lat": 37.69, "lon": -97.34, "precision": "city",
     "date": "2005-08-18", "note": txt("Juridiction de jugement.", "Trial court."),
     "reliability": "CONFIRMED", "source": "wiki-rader"},
]

EVIDENCE = [
    {"kind": "digital", "weight": "decisive", "reliability": "CONFIRMED", "source": "wiki-rader",
     "title": txt("Métadonnées d'un document supprimé", "Metadata of a deleted document"),
     "description": txt(
         "Une disquette envoyée en 2005 contenait un document Word supprimé mais encore présent. Ses métadonnées "
         "indiquaient « Christ Lutheran Church » et un dernier modificateur nommé « Dennis ». Une recherche sur le "
         "site de la paroisse a fait apparaître un Dennis Rader, président du conseil paroissial.",
         "A floppy disk sent in 2005 contained a deleted but still present Word document. Its metadata indicated "
         "'Christ Lutheran Church' and a last modifier named 'Dennis'. A search on the church website revealed a "
         "Dennis Rader, president of the congregation council.")},
    {"kind": "dna", "weight": "decisive", "reliability": "CONFIRMED", "source": "creed-btk",
     "title": txt("Comparaison ADN familiale", "Familial DNA comparison"),
     "description": txt(
         "Un échantillon obtenu à partir de matériel médical concernant sa fille a permis d'établir un lien familial "
         "avec l'ADN conservé des scènes. Ce lien a confirmé l'identification suggérée par les métadonnées.",
         "A sample obtained from medical material concerning his daughter established a family link with DNA kept from "
         "the scenes. That link confirmed the identification suggested by the metadata.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "biography-rader",
     "title": txt("Les lettres et revendications", "The letters and claims"),
     "description": txt(
         "Dès octobre 1974, des communications sont déposées ou envoyées, dont une lettre glissée dans un livre de "
         "bibliothèque publique revendiquant les meurtres des Otero. La réémergence de 2004 a produit une nouvelle "
         "série de courriers.",
         "From October 1974, communications were deposited or sent, including a letter slipped into a public library "
         "book claiming the Otero murders. The 2004 re-emergence produced a new series of letters.")},
    {"kind": "testimony", "weight": "documented", "reliability": "CONFIRMED", "source": "biography-rader",
     "title": txt("Le signalement d'un survivant", "A survivor's description"),
     "description": txt(
         "Kevin Bright a décrit un homme de taille moyenne, à moustache fournie, au regard qualifié de « psychotique ». "
         "Ce signalement, rapporté par TIME, n'a pas permis d'identification à l'époque.",
         "Kevin Bright described an average-sized man with a bushy moustache and a gaze called 'psychotic'. That "
         "description, reported by TIME, did not allow identification at the time.")},
    {"kind": "physical", "weight": "documented", "reliability": "CONFIRMED", "source": "wiki-rader",
     "title": txt("Objets saisis lors des perquisitions", "Items seized during searches"),
     "description": txt(
         "Les perquisitions ont porté sur le domicile, le véhicule, la paroisse, le bureau de l'intéressé et la "
         "bibliothèque municipale de Park City ; du matériel informatique et des objets ont été saisis.",
         "Searches covered the home, the vehicle, the church, the person's office and the Park City municipal library; "
         "computer equipment and objects were seized.")},
]

INVESTIGATION = {
    "steps": [
        {"n": 1, "date": "1974-01-15", "title": txt("Quatre morts dans une maison", "Four dead in a house"),
         "body": txt("Quatre membres de la famille Otero sont retrouvés morts le lendemain matin par leur fils de 15 "
                     "ans. L'enquête porte sur un quadruple homicide au domicile.",
                     "Four members of the Otero family are found dead the next morning by their 15-year-old son. The "
                     "investigation concerns a quadruple homicide at the home."),
         "reliability": "CONFIRMED", "source": "biography-rader", "premium": False},
        {"n": 2, "date": "1974-10", "title": txt("Une revendication dans un livre", "A claim inside a book"),
         "body": txt("Une lettre revendiquant les faits est déposée dans un livre de bibliothèque publique. C'est le "
                     "début d'une relation épistolaire avec la police et les médias.",
                     "A letter claiming the facts is placed in a public library book. It is the start of an "
                     "epistolary relationship with police and media."),
         "reliability": "CONFIRMED", "source": "biography-rader", "premium": False},
        {"n": 3, "date": "1974-1991", "title": txt("Une série et un survivant", "A series and a survivor"),
         "body": txt("Les faits s'échelonnent jusqu'en janvier 1991. Un signalement est fourni par Kevin Bright, "
                     "survivant d'une agression, sans conduire à une identification.",
                     "The offences run until January 1991. A description is given by Kevin Bright, survivor of an "
                     "attack, without leading to an identification."),
         "reliability": "CONFIRMED", "source": "biography-rader", "premium": True},
        {"n": 4, "date": "1991-2004", "title": txt("Treize ans de silence", "Thirteen years of silence"),
         "body": txt("Plus aucune communication. L'homme occupe des fonctions sociales visibles : responsable de "
                     "troupe scoute, président du conseil paroissial, agent de conformité municipale.",
                     "No further communication. The man holds visible social roles: scout troop leader, president of "
                     "the church council, municipal compliance officer."),
         "reliability": "CONFIRMED", "source": "biography-rader", "premium": False},
        {"n": 5, "date": "2004", "title": txt("La réémergence", "The re-emergence"),
         "body": txt("La couverture médiatique du trentième anniversaire des meurtres Otero est suivie d'une reprise "
                     "des envois de lettres, avec des allusions à d'autres faits.",
                     "Media coverage of the thirtieth anniversary of the Otero murders is followed by a resumption of "
                     "letters, with allusions to other facts."),
         "reliability": "CONFIRMED", "source": "wiki-rader", "premium": True},
        {"n": 6, "date": "2005-01", "title": txt("Une question posée à la police", "A question put to the police"),
         "body": txt("Il demande si une disquette peut être tracée. Les enquêteurs font répondre par voie de presse "
                     "que non. La réponse est fausse, et il y croit.",
                     "He asks whether a floppy disk can be traced. Investigators have it answered through the media "
                     "that it cannot. The answer is false, and he believes it."),
         "reliability": "CONFIRMED", "source": "creed-btk", "premium": False},
        {"n": 7, "date": "2005-02-16", "title": txt("Deux mots dans des métadonnées", "Two words in metadata"),
         "body": txt("« Christ Lutheran Church » et « Dennis ». Une recherche en ligne donne un nom : Dennis Rader, "
                     "président du conseil paroissial.",
                     "'Christ Lutheran Church' and 'Dennis'. An online search yields a name: Dennis Rader, president "
                     "of the congregation council."),
         "reliability": "CONFIRMED", "source": "wiki-rader", "premium": True},
        {"n": 8, "date": "2005-02", "title": txt("La confirmation biologique", "The biological confirmation"),
         "body": txt("Un échantillon obtenu à partir de matériel médical concernant sa fille établit un lien familial "
                     "avec l'ADN des scènes. La piste devient une identification.",
                     "A sample obtained from medical material concerning his daughter establishes a family link with "
                     "scene DNA. The lead becomes an identification."),
         "reliability": "CONFIRMED", "source": "creed-btk", "premium": True},
        {"n": 9, "date": "2005-02-25", "title": txt("Arrestation", "Arrest"),
         "body": txt("Il est arrêté au volant près de son domicile de Park City. Le chef de la police de Wichita "
                     "déclare le lendemain : « The bottom line: BTK is arrested. »",
                     "He is arrested while driving near his Park City home. The Wichita police chief declares the next "
                     "day: 'The bottom line: BTK is arrested.'"),
         "reliability": "CONFIRMED", "source": "wiki-rader", "premium": False},
        {"n": 10, "date": "2005-08-18", "title": txt("Dix peines consécutives", "Ten consecutive sentences"),
         "body": txt("Après un plaidoyer de culpabilité le 27 juin 2005, il est condamné à dix peines de réclusion à "
                     "perpétuité consécutives, avec un minimum de 175 ans. La peine de mort n'était pas applicable aux "
                     "faits, antérieurs au rétablissement de 1994 au Kansas.",
                     "After a guilty plea on 27 June 2005, he is sentenced to ten consecutive life terms with a "
                     "minimum of 175 years. The death penalty was not applicable to the facts, which predate Kansas's "
                     "1994 reinstatement."),
         "reliability": "CONFIRMED", "source": "wiki-rader", "premium": True},
    ],
    "reality": txt(
        "L'affaire ne s'est pas résolue par le profilage ni par le signalement d'un survivant, mais par une erreur de "
        "l'auteur : une question posée à la police, une réponse fausse donnée volontairement, puis deux mots retrouvés "
        "dans les métadonnées d'un fichier supprimé, confirmés par une comparaison ADN familiale.",
        "The case was not solved by profiling or by a survivor's description, but by the author's mistake: a question "
        "put to the police, a deliberately false answer, then two words found in the metadata of a deleted file, "
        "confirmed by a familial DNA comparison."),
    "errors": [
        item("Le signalement fourni par un survivant en 1974 n'a conduit à aucune identification : il n'a pas été "
             "rapproché utilement des autres éléments.",
             "The description given by a survivor in 1974 led to no identification: it was not usefully linked to "
             "other elements.", "CONFIRMED", "biography-rader", "Exploitation d'un témoignage", "Use of testimony"),
        item("Les communications de l'auteur ont été reçues pendant des années sans que le support permette une "
             "identification technique : il a fallu attendre le support numérique de 2005.",
             "The author's communications were received for years without the medium allowing technical "
             "identification: it took the 2005 digital medium.",
             "CONFIRMED", "creed-btk", "Limites techniques", "Technical limits"),
    ],
    "cold_case": {
        "what_we_know": [
            item("Dix meurtres entre le 15 janvier 1974 et le 19 janvier 1991 dans le comté de Sedgwick.",
                 "Ten murders between 15 January 1974 and 19 January 1991 in Sedgwick County.", "CONFIRMED", "wiki-rader"),
            item("Identification par métadonnées puis confirmation par ADN familial.",
                 "Identification through metadata then confirmation by familial DNA.", "CONFIRMED", "creed-btk"),
        ],
        "what_is_probable": [
            item("Après son arrestation, une source anonyme citée par l'Associated Press a évoqué des aveux portant sur "
                 "d'autres meurtres ; le procureur du comté de Sedgwick a démenti et n'a pas confirmé l'existence de "
                 "telles déclarations.",
                 "After his arrest, an anonymous source cited by the Associated Press mentioned confessions to other "
                 "murders; the Sedgwick County district attorney denied it and did not confirm such statements.",
                 "PROBABLE", "wiki-rader"),
        ],
        "what_is_disputed": [
            item("L'existence de faits non jugés : démentie par le parquet, elle n'est ni établie ni définitivement "
                 "écartée dans les sources consultées.",
                 "The existence of untried offences: denied by the prosecution, it is neither established nor "
                 "definitively ruled out in the sources consulted.", "DISPUTED", "wiki-rader"),
        ],
        "what_is_unknown": [
            item("Les raisons de l'interruption de treize ans entre 1991 et 2004.",
                 "The reasons for the thirteen-year interruption between 1991 and 2004.", "UNKNOWN", "wiki-rader"),
        ],
        "latest_progress": [],
        "leads": [], "limits": [],
    },
}

PSYCHOLOGY = {
    "disclaimer": txt("Aucun diagnostic n'est posé par l'application. Une expertise psychologique a été réalisée à la "
                      "demande de la défense après le plaidoyer de culpabilité ; ses conclusions ne sont pas "
                      "reproduites ici faute de publication accessible dans les sources consultées.",
                      "No diagnosis is made by the application. A psychological evaluation was carried out at the "
                      "defence's request after the guilty plea; its conclusions are not reproduced here for lack of "
                      "accessible publication in the sources consulted."),
    "blocks": [
        block("fact", "Une double vie sociale documentée", "A documented double social life",
              "Pendant la période des faits puis après, l'intéressé a occupé des fonctions sociales visibles : "
              "responsable de troupe scoute, président du conseil de sa paroisse, employé municipal. Ce sont des faits "
              "rapportés par plusieurs sources concordantes.",
              "During and after the offences, the person held visible social roles: scout troop leader, president of "
              "his church council, municipal employee. These are facts reported by several concordant sources.",
              "CONFIRMED", "biography-rader"),
        block("behaviour", "Le besoin de nommer", "The need to name",
              "L'auteur a produit des lettres, des revendications, un auto-surnom et, en 2004, une reprise des envois. "
              "Le comportement documenté est celui d'une recherche de reconnaissance publique de ses actes. Son "
              "interprétation relève de l'analyse, pas du fait.",
              "The author produced letters, claims, a self-given nickname and, in 2004, a resumption of mailings. The "
              "documented behaviour is one of seeking public recognition of his acts. Its interpretation belongs to "
              "analysis, not to fact.",
              "CONFIRMED", "wiki-rader"),
        block("behaviour", "La mise en scène de la procédure", "Staging of the proceedings",
              "Devant la cour, il a décrit les faits en les qualifiant de « projets », sans excuses, puis a prononcé "
              "un monologue d'une trentaine de minutes à l'audience de condamnation, comparé par le procureur à un "
              "discours de remise de prix.",
              "Before the court, he described the facts calling them 'projects', without apologies, then delivered a "
              "thirty-minute monologue at the sentencing hearing, compared by the prosecutor to an awards acceptance "
              "speech.",
              "CONFIRMED", "wiki-rader"),
        block("unknown", "L'expertise de la défense", "The defence evaluation",
              "Un psychologue du Massachusetts, Robert Mendoza, a été mandaté par la défense après le plaidoyer de "
              "culpabilité du 27 juin 2005 pour examiner l'opportunité d'une défense fondée sur la démence. Le "
              "contenu de cette évaluation n'est pas accessible dans les sources consultées.",
              "A Massachusetts psychologist, Robert Mendoza, was instructed by the defence after the guilty plea of "
              "27 June 2005 to examine whether an insanity-based defence was viable. The content of that evaluation "
              "is not accessible in the sources consulted.",
              "UNKNOWN", "wiki-rader"),
    ],
}

VICTIMOLOGY = {
    "ethics_note": txt("Aucune caractéristique des victimes n'explique moralement les crimes.",
                       "No characteristic of the victims morally explains the crimes."),
    "blocks": [
        block("context", "Des victimes à domicile", "Victims at home",
              "La première série de faits concerne une famille entière à son domicile. Dolores Davis, dernière victime "
              "connue, a été enlevée chez elle en janvier 1991. Le domicile est un lieu récurrent.",
              "The first series of offences concerns an entire family at its home. Dolores Davis, the last known "
              "victim, was taken from her home in January 1991. The home is a recurring place.",
              "CONFIRMED", "biography-rader"),
        block("analysis", "Un périmètre géographique restreint", "A restricted geographic perimeter",
              "Les faits sont concentrés dans le comté de Sedgwick, autour de Wichita et Park City, sur dix-sept ans. "
              "Cette concentration spatiale est un fait de dossier ; elle n'a pas conduit à une identification à "
              "l'époque.",
              "The offences are concentrated in Sedgwick County, around Wichita and Park City, over seventeen years. "
              "This spatial concentration is a case fact; it did not lead to identification at the time.",
              "CONFIRMED", "wiki-rader"),
    ],
}

COURT = {
    "jurisdiction": txt("États-Unis — District Court du comté de Sedgwick, Kansas",
                        "United States — Sedgwick County District Court, Kansas"),
    "verdict": txt("Plaidoyer de culpabilité sur dix chefs de meurtre au premier degré, le 27 juin 2005.",
                   "Guilty plea to ten counts of first-degree murder, on 27 June 2005."),
    "sentence": {
        "label": txt("Dix peines de réclusion à perpétuité consécutives, minimum 175 ans",
                     "Ten consecutive life sentences, minimum 175 years"),
        "pronounced": "2005-08-18",
        "requested": txt("La peine de mort n'était pas applicable : le Kansas l'a rétablie en 1994, après la "
                         "commission des faits.",
                         "The death penalty was not applicable: Kansas reinstated it in 1994, after the offences were "
                         "committed."),
        "cumul": txt("Les dix peines sont consécutives, avec un minimum cumulé de 175 ans avant toute possibilité "
                     "d'examen.",
                     "The ten sentences are consecutive, with a cumulative minimum of 175 years before any possibility "
                     "of review."),
        "reasoning": txt("Les familles des victimes se sont exprimées avant le prononcé. L'accusé a ensuite prononcé "
                         "un long monologue.",
                         "Victims' families spoke before sentencing. The accused then delivered a long monologue."),
        "appeal": txt("Pas de procès : le plaidoyer de culpabilité a mis fin à la procédure contradictoire.",
                      "No trial: the guilty plea ended the adversarial proceedings."),
        "reliability": "CONFIRMED", "source": "wiki-rader",
    },
    "consequences": [
        item("L'affaire est devenue une référence en matière d'exploitation des métadonnées et d'ADN familial.",
             "The case became a reference for the exploitation of metadata and familial DNA.",
             "CONFIRMED", "creed-btk"),
    ],
}

EXPERTS = [
    {"label": txt("Lecture technique — la trace numérique", "Technical reading — the digital trace"),
     "field": "digital_forensics",
     "position": txt("Un fichier supprimé reste présent sur son support ; ses métadonnées ont fourni un nom et une "
                     "institution. La confirmation est venue d'une comparaison ADN familiale.",
                     "A deleted file remains present on its medium; its metadata provided a name and an institution. "
                     "Confirmation came from a familial DNA comparison."),
     "reliability": "CONFIRMED", "source": "wiki-rader"},
    {"label": txt("Lecture comportementale — la reprise de contact", "Behavioural reading — the resumption of contact"),
     "field": "behavioural_analysis",
     "position": txt("Le silence de treize ans a pris fin avec la couverture médiatique d'un anniversaire. La reprise "
                     "des envois a fourni le support qui a permis l'identification.",
                     "The thirteen-year silence ended with media coverage of an anniversary. The resumption of "
                     "mailings provided the medium that allowed identification."),
     "reliability": "CONFIRMED", "source": "wiki-rader"},
]
EXPERTS_AGREEMENT = txt("Les deux lectures convergent : c'est l'auteur qui a produit l'élément décisif.",
                        "Both readings converge: it is the author who produced the decisive element.")
EXPERTS_DISAGREEMENT = txt("Elles divergent sur la part de chance et celle de méthode dans l'exploitation de la disquette.",
                           "They differ on the share of luck and of method in exploiting the floppy disk.")
EXPERTS_UNCERTAIN = txt("Ce qui reste incertain : l'existence éventuelle d'autres faits, démentie par le parquet.",
                        "What remains uncertain: the possible existence of other offences, denied by the prosecution.")

COUNTERFACTUALS = [
    counterfactual(
        "communication",
        "Et si les communications de 1974 avaient pu être tracées ?",
        "What if the 1974 communications had been traceable?",
        "L'auteur a communiqué par lettres papier dès octobre 1974. L'identification n'est intervenue qu'en février "
        "2005, grâce aux métadonnées d'un fichier numérique. Entre ces deux dates, six victimes documentées ont été "
        "tuées après la première lettre.",
        "The author communicated by paper letters from October 1974. Identification came only in February 2005, "
        "through the metadata of a digital file. Between those two dates, six documented victims were killed after "
        "the first letter.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Première lettre revendiquée", "First claiming letter"), "date": "1974-10-01"},
            "hypothesis": {"label": txt("Support papier non traçable", "Paper medium not traceable"), "date": "1974-10-01"},
            "scenario_event": {"label": txt("Identification par métadonnées", "Identification through metadata"), "date": "2005-02-16"},
            "outcome_event": {"label": txt("Arrestation", "Arrest"), "date": "2005-02-25"},
            "documented_offences_after": [
                {"date": "1977-01-01", "label": txt("Victimes ultérieures documentées (dates précises non établies dans les sources consultées)", "Later documented victims (precise dates not established in the sources consulted)"), "reliability": "PROBABLE"},
                {"date": "1991-01-19", "label": txt("Dolores Davis, dernière victime connue", "Dolores Davis, last known victim"), "reliability": "CONFIRMED"},
            ],
            "jurisdiction_note": txt(
                "En 1974, aucune technique d'exploitation des métadonnées numériques n'existait, et l'ADN n'était pas "
                "utilisé en criminalistique. Le scénario étudié porte donc sur une technologie inexistante à "
                "l'époque : l'application peut mesurer l'écart de temps, elle ne peut pas établir ce qui se serait "
                "produit.",
                "In 1974, no technique for exploiting digital metadata existed, and DNA was not used in forensic "
                "science. The scenario studied therefore concerns a technology that did not exist at the time: the "
                "application can measure the time gap, it cannot establish what would have happened."),
        },
        [
            {"date": "1974-01-15", "kind": "offence", "label": txt("Famille Otero (4 victimes)", "Otero family (4 victims)")},
            {"date": "1974-10-01", "kind": "reference", "label": txt("Première lettre", "First letter")},
            {"date": "1991-01-19", "kind": "offence", "label": txt("Dolores Davis", "Dolores Davis")},
            {"date": "2004-01-01", "kind": "fact", "label": txt("Réémergence", "Re-emergence")},
            {"date": "2005-02-16", "kind": "scenario", "label": txt("Métadonnées exploitées", "Metadata exploited")},
            {"date": "2005-02-25", "kind": "outcome", "label": txt("Arrestation", "Arrest")},
        ],
        True, "creed-btk"),
]

LESSONS = [
    item("Un support change ce qu'une enquête peut faire : le papier n'a rien livré pendant trente ans, le fichier "
         "numérique a livré un nom en quelques jours.",
         "A medium changes what an investigation can do: paper yielded nothing for thirty years, the digital file "
         "yielded a name in days.",
         "CONFIRMED", "wiki-rader", "Support et trace", "Medium and trace"),
    item("Une métadonnée oriente, elle n'identifie pas : la confirmation est venue d'une comparaison ADN familiale.",
         "Metadata orientates, it does not identify: confirmation came from a familial DNA comparison.",
         "CONFIRMED", "creed-btk", "Chaîne probatoire", "Evidential chain"),
    item("Un signalement de survivant peut être exact et rester inexploité : la description de 1974 correspondait à "
         "l'homme arrêté en 2005.",
         "A survivor's description can be accurate and remain unexploited: the 1974 description matched the man "
         "arrested in 2005.",
         "CONFIRMED", "biography-rader", "Témoignage", "Testimony"),
    item("Une apparence sociale ordinaire n'est pas un indice d'innocence, et n'est pas non plus une preuve : elle "
         "explique seulement pourquoi la suspicion ne s'est pas portée sur lui.",
         "An ordinary social appearance is not an indication of innocence, and is not evidence either: it only "
         "explains why suspicion did not fall on him.",
         "CONFIRMED", "biography-rader", "Représentations", "Representations"),
    item("Une réponse volontairement fausse donnée par les enquêteurs a produit un comportement exploitable. C'est "
         "une technique documentée, qui interroge sur ses conditions d'emploi.",
         "A deliberately false answer given by investigators produced exploitable behaviour. This is a documented "
         "technique, which raises questions about its conditions of use.",
         "CONFIRMED", "creed-btk", "Stratégie d'enquête", "Investigative strategy"),
]

UNKNOWNS = [
    item("Les raisons exactes de l'interruption de treize ans.", "The exact reasons for the thirteen-year interruption.",
         "UNKNOWN", "wiki-rader"),
    item("L'existence d'autres faits : évoquée par une source anonyme, démentie par le parquet.",
         "The existence of other offences: mentioned by an anonymous source, denied by the prosecution.",
         "DISPUTED", "wiki-rader"),
    item("Le contenu de l'expertise psychologique demandée par la défense.",
         "The content of the psychological evaluation requested by the defence.", "UNKNOWN", "wiki-rader"),
]

SECTIONS = merge_sections(default_sections(), [
    {"key": "introduction", "blocks": [block(
        "paragraph", "Trente ans, dix victimes, une disquette", "Thirty years, ten victims, a floppy disk",
        "Entre 1974 et 1991, dix personnes sont tuées dans le comté de Sedgwick, au Kansas. L'auteur écrit à la police "
        "et aux médias, se donne un surnom, puis se tait pendant treize ans. Son identification viendra d'un support "
        "qu'il a lui-même choisi d'envoyer.",
        "Between 1974 and 1991, ten people are killed in Sedgwick County, Kansas. The author writes to police and "
        "media, gives himself a nickname, then falls silent for thirteen years. His identification would come from a "
        "medium he chose to send himself.",
        "CONFIRMED", "wiki-rader")]},
    {"key": "context", "blocks": [block(
        "paragraph", "Wichita et Park City", "Wichita and Park City",
        "Les faits se déroulent dans une agglomération du Kansas, sur un périmètre restreint, pendant une période où "
        "ni les fichiers génétiques ni l'exploitation des supports numériques n'existaient en criminalistique.",
        "The offences take place in a Kansas metropolitan area, over a restricted perimeter, during a period when "
        "neither genetic databases nor the exploitation of digital media existed in forensic science.",
        "CONFIRMED", "creed-btk")]},
    {"key": "offender", "blocks": [block(
        "paragraph", "Dennis Lynn Rader (né en 1945)", "Dennis Lynn Rader (born 1945)",
        "Né le 9 mars 1945 à Pittsburg (Kansas), grandi à Wichita. Études au Butler County Community College puis à "
        "Wichita State University. Responsable de troupe scoute, président du conseil de sa paroisse, employé "
        "municipal. Arrêté le 25 février 2005.",
        "Born 9 March 1945 in Pittsburg (Kansas), raised in Wichita. Studied at Butler County Community College then "
        "Wichita State University. Scout troop leader, president of his church council, municipal employee. Arrested "
        "on 25 February 2005.",
        "CONFIRMED", "wiki-rader")]},
    {"key": "behaviour", "blocks": [block(
        "behaviour", "Écrire pour exister", "Writing to exist",
        "Le comportement central documenté est la production de communications : lettres, revendications, envois "
        "renouvelés en 2004. Cette production a été, en définitive, le vecteur de son identification.",
        "The central documented behaviour is the production of communications: letters, claims, mailings renewed in "
        "2004. That production was, ultimately, the vector of his identification.",
        "CONFIRMED", "wiki-rader")]},
    {"key": "consequences", "blocks": [block(
        "paragraph", "Un précédent technique", "A technical precedent",
        "L'affaire est citée comme l'un des premiers exemples d'identification par métadonnées numériques couplée à "
        "une comparaison ADN familiale. Elle pose aussi la question des techniques d'enquête impliquant une réponse "
        "fausse délibérée.",
        "The case is cited as one of the first examples of identification through digital metadata coupled with a "
        "familial DNA comparison. It also raises the question of investigative techniques involving a deliberate "
        "false answer.",
        "CONFIRMED", "creed-btk")]},
])

EPISODES = [
    {
        "number": 1,
        "title": txt("Le fichier supprimé", "The deleted file"),
        "description": txt("Kansas, 1974-2005. Trente ans de lettres, treize ans de silence, et deux mots retrouvés "
                           "dans les métadonnées d'un document effacé.",
                           "Kansas, 1974-2005. Thirty years of letters, thirteen years of silence, and two words found "
                           "in the metadata of an erased document."),
        "modes": ["documentary", "investigation", "chronology", "express", "expert", "psychology", "victims"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 60, "title": txt("15 janvier 1974", "15 January 1974")},
            {"at": 220, "title": txt("Les lettres", "The letters")},
            {"at": 380, "title": txt("Treize ans de silence", "Thirteen years of silence")},
            {"at": 520, "title": txt("La question posée à la police", "The question put to the police")},
            {"at": 640, "title": txt("Et maintenant, une question", "And now, a question")},
        ],
        "transcript": {"segments": [
            {"id": "b1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X, à travers mon regard. Aujourd'hui, une affaire américaine qui s'est "
                     "terminée par un détail technique : un fichier que l'on croyait effacé.",
             "text_en": "You are on YANIS//X, through my eyes. Today, an American case that ended with a technical "
                        "detail: a file believed to be erased."},
            {"id": "b2", "t": 60, "speaker": "yanis",
             "text": "15 janvier 1974, Wichita, Kansas. Quatre membres de la famille Otero sont tués à leur domicile. "
                     "Le lendemain matin, leur fils Charlie, quinze ans, rentre et découvre les corps. C'est le "
                     "premier fait d'une série qui comptera dix victimes, jusqu'au 19 janvier 1991.",
             "text_en": "15 January 1974, Wichita, Kansas. Four members of the Otero family are killed at their home. "
                        "The next morning, their son Charlie, fifteen, comes home and finds the bodies. It is the "
                        "first offence of a series that would count ten victims, until 19 January 1991."},
            {"id": "b3", "t": 220, "speaker": "yanis",
             "text": "En octobre 1974, une lettre revendiquant ces meurtres est déposée dans un livre d'une "
                     "bibliothèque publique. Un survivant, Kevin Bright, décrit son agresseur : taille moyenne, "
                     "moustache fournie, un regard qu'il qualifie de psychotique. Le signalement ne donnera rien.",
             "text_en": "In October 1974, a letter claiming these murders is placed in a public library book. A "
                        "survivor, Kevin Bright, describes his attacker: average height, bushy moustache, a gaze he "
                        "calls psychotic. The description yields nothing."},
            {"id": "b4", "t": 380, "speaker": "yanis",
             "text": "Puis treize ans de silence. Pendant ce temps, l'homme est responsable d'une troupe scoute, "
                     "président du conseil de sa paroisse, employé municipal. Rien, dans sa vie sociale visible, ne le "
                     "désigne.",
             "text_en": "Then thirteen years of silence. During that time, the man leads a scout troop, presides over "
                        "his church council, works for the city. Nothing in his visible social life points to him."},
            {"id": "b5", "t": 520, "speaker": "yanis",
             "text": "En 2004, la couverture du trentième anniversaire des meurtres Otero est suivie d'une reprise "
                     "des envois. En janvier 2005, il pose une question à la police : une disquette peut-elle être "
                     "tracée ? Les enquêteurs font répondre par voie de presse que non. Cette réponse était fausse. Il "
                     "y a cru.",
             "text_en": "In 2004, coverage of the thirtieth anniversary of the Otero murders is followed by a "
                        "resumption of mailings. In January 2005, he puts a question to the police: can a floppy disk "
                        "be traced? Investigators have it answered through the media that it cannot. That answer was "
                        "false. He believed it."},
            {"id": "b6", "t": 640, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "b7", "t": 680, "speaker": "yanis",
             "text": "Le 16 février 2005, dans une disquette reçue par courrier, un document Word supprimé est encore "
                     "présent. Ses métadonnées contiennent deux indications : « Christ Lutheran Church », et un "
                     "dernier modificateur nommé « Dennis ». Une recherche en ligne montre qu'un Dennis Rader est "
                     "président du conseil de cette paroisse. Un échantillon obtenu à partir d'un dossier médical "
                     "concernant sa fille confirme un lien familial avec l'ADN des scènes. Le 25 février, il est "
                     "arrêté au volant près de chez lui.",
             "text_en": "On 16 February 2005, in a floppy disk received by mail, a deleted Word document is still "
                        "present. Its metadata contain two indications: 'Christ Lutheran Church', and a last modifier "
                        "named 'Dennis'. An online search shows a Dennis Rader is president of that congregation's "
                        "council. A sample obtained from medical records concerning his daughter confirms a family "
                        "link with the scene DNA. On 25 February, he is arrested while driving near his home."},
            {"id": "b8", "t": 860, "speaker": "yanis",
             "text": "Le 27 juin 2005, il plaide coupable de dix meurtres. Le 18 août, il est condamné à dix peines "
                     "de réclusion à perpétuité consécutives, avec un minimum de cent soixante-quinze ans. La peine "
                     "de mort n'était pas applicable : le Kansas ne l'avait rétablie qu'en 1994, après les faits.",
             "text_en": "On 27 June 2005, he pleads guilty to ten murders. On 18 August, he is sentenced to ten "
                        "consecutive life terms, with a minimum of one hundred and seventy-five years. The death "
                        "penalty was not applicable: Kansas had reinstated it only in 1994, after the facts."},
            {"id": "b9", "t": 980, "speaker": "yanis",
             "text": "Dix personnes ont été tuées. Quatre d'entre elles portaient le même nom : Otero. Deux étaient "
                     "des enfants de neuf et onze ans. Écouter les histoires. Comprendre les affaires. Ne jamais "
                     "oublier les victimes.",
             "text_en": "Ten people were killed. Four of them bore the same name: Otero. Two were children of nine and "
                        "eleven. Listen to the stories. Understand the cases. Never forget the victims."},
        ]},
    },
]

QUESTIONS = [
    question("1", 640, "evidence",
             "Une disquette contient un document supprimé dont les métadonnées donnent un prénom et une institution. Que peut-on en déduire à ce stade ?",
             "A floppy disk contains a deleted document whose metadata give a first name and an institution. What can be deduced at this stage?",
             [("a", "L'identité de l'auteur des faits", "The identity of the author of the offences"),
              ("b", "Une piste nominative à vérifier par un élément indépendant", "A named lead to be verified by an independent element"),
              ("c", "Une preuve suffisante pour condamner", "Evidence sufficient to convict"),
              ("d", "Rien : les métadonnées sont modifiables", "Nothing: metadata can be modified")],
             {"fr": {"whatInvestigatorsKnew": "Les métadonnées indiquaient « Christ Lutheran Church » et un dernier modificateur nommé « Dennis ». Une recherche en ligne a fait apparaître un Dennis Rader, président du conseil paroissial.",
                     "whatExpertsProposed": "Une métadonnée est une déclaration technique enregistrée par un logiciel : elle oriente, mais elle doit être confirmée. Ici, la confirmation est venue d'une comparaison ADN familiale.",
                     "documented": "La chaîne est documentée : métadonnées, recherche en ligne, prélèvement familial, arrestation le 25 février 2005.",
                     "hypothetical": "Ce que l'affaire aurait donné sans la confirmation biologique.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir que les enquêteurs avaient volontairement donné une réponse fausse sur la traçabilité des disquettes.",
                     "answer_note": "La réponse attendue est B. Les métadonnées ne sont pas une preuve d'identité, elles sont une piste — ici confirmée."},
              "en": {"whatInvestigatorsKnew": "The metadata indicated 'Christ Lutheran Church' and a last modifier named 'Dennis'. An online search revealed a Dennis Rader, president of the congregation council.",
                     "whatExpertsProposed": "Metadata is a technical statement recorded by software: it orientates but must be confirmed. Here, confirmation came from a familial DNA comparison.",
                     "documented": "The chain is documented: metadata, online search, family sample, arrest on 25 February 2005.",
                     "hypothetical": "What the case would have produced without biological confirmation.",
                     "whatYouCouldNotKnow": "You could not know that investigators had deliberately given a false answer about the traceability of floppy disks.",
                     "answer_note": "The expected answer is B. Metadata is not proof of identity; it is a lead — confirmed here."}},
             "wiki-rader"),
    question("1", 300, "bias",
             "Un survivant décrit l'agresseur en 1974 : taille moyenne, moustache fournie. Trente et un ans plus tard, l'homme arrêté correspond à ce signalement. Que révèle cet écart ?",
             "A survivor describes the attacker in 1974: average height, bushy moustache. Thirty-one years later, the arrested man matches that description. What does that gap reveal?",
             [("a", "Que les témoignages sont inutiles", "That testimonies are useless"),
              ("b", "Qu'un témoignage exact peut rester inexploité faute de support de comparaison", "That an accurate testimony can remain unexploited for lack of a comparison medium"),
              ("c", "Que l'auteur n'a pas changé d'apparence", "That the author did not change appearance"),
              ("d", "Que la police a négligé le survivant", "That the police neglected the survivor")],
             {"fr": {"whatInvestigatorsKnew": "Le signalement de Kevin Bright est documenté et correspond à l'homme arrêté en 2005.",
                     "whatExpertsProposed": "Un signalement ne vaut que s'il peut être confronté à un ensemble de candidats. Sans fichier, sans rapprochement possible, il reste une description.",
                     "documented": "Le signalement figure dans la presse de l'époque citée par Biography.com.",
                     "hypothetical": "Ce qu'un rapprochement systématique aurait produit à l'époque.",
                     "whatYouCouldNotKnow": "Vous ne pouvez pas connaître l'ensemble des signalements recueillis par la police de Wichita entre 1974 et 1991.",
                     "answer_note": "La réponse attendue est B. Les options A et D sont des jugements non documentés."},
              "en": {"whatInvestigatorsKnew": "Kevin Bright's description is documented and matches the man arrested in 2005.",
                     "whatExpertsProposed": "A description is worth something only if it can be matched against a set of candidates. Without a database, without possible linkage, it remains a description.",
                     "documented": "The description appears in the press of the time cited by Biography.com.",
                     "hypothetical": "What systematic matching would have produced at the time.",
                     "whatYouCouldNotKnow": "You cannot know the full set of descriptions collected by Wichita police between 1974 and 1991.",
                     "answer_note": "The expected answer is B. Options A and D are undocumented judgements."}},
             "biography-rader"),
]

CASE = {
    "id": CASE_ID,
    "title": txt("Dennis Rader, dit « BTK »", "Dennis Rader, known as 'BTK'"),
    "subtitle": txt("Comté de Sedgwick, Kansas, 1974-1991. Dix victimes, treize ans de silence, et un fichier que l'on croyait effacé.",
                    "Sedgwick County, Kansas, 1974-1991. Ten victims, thirteen years of silence, and a file believed erased."),
    "country": "US", "region": "Kansas / Sedgwick County", "city": "Wichita",
    "year_start": 1974, "year_end": 2005, "period_label": txt("1974 – 2005", "1974 – 2005"),
    "status": "RESOLVED", "type": "serial",
    "tags": ["serial_killer", "metadata", "familial_dna", "usa", "survivors", "digital_forensics"],
    "tier": "PREMIUM", "editorial": "yanis", "published_at": "2026-09-24", "sensitive": True,
    "triggers": txt("Meurtres dont ceux de deux enfants ; violences décrites sans détail graphique.",
                    "Murders including those of two children; violence described without graphic detail."),
    "lat": 37.69, "lon": -97.34, "cover": "cover-btk",
    "stats": {"victims_documented": 10, "survivors_documented": 1, "duration_years": 31},
    "summary": txt(
        "Entre le 15 janvier 1974 et le 19 janvier 1991, dix personnes sont tuées dans le comté de Sedgwick, au "
        "Kansas. Quatre membres de la famille Otero comptent parmi les premières victimes ; leur fils de 15 ans "
        "découvre les corps. L'auteur communique par lettres avec la police et les médias, puis observe treize ans de "
        "silence. En 2004, il reprend contact. En janvier 2005, il demande si une disquette peut être tracée ; les "
        "enquêteurs font répondre que non. Le 16 février 2005, les métadonnées d'un document supprimé sur une "
        "disquette reçue livrent deux indications — « Christ Lutheran Church » et un modificateur nommé « Dennis » — "
        "qui conduisent à Dennis Rader, président du conseil paroissial. Un lien familial est confirmé par comparaison "
        "ADN. Il est arrêté le 25 février 2005, plaide coupable le 27 juin, et est condamné le 18 août à dix peines "
        "consécutives de réclusion à perpétuité, avec un minimum de 175 ans.",
        "Between 15 January 1974 and 19 January 1991, ten people were killed in Sedgwick County, Kansas. Four members "
        "of the Otero family are among the first victims; their 15-year-old son found the bodies. The author "
        "communicated by letter with police and media, then observed thirteen years of silence. In 2004, he resumed "
        "contact. In January 2005, he asked whether a floppy disk could be traced; investigators had it answered that "
        "it could not. On 16 February 2005, the metadata of a deleted document on a received floppy disk yielded two "
        "indications — 'Christ Lutheran Church' and a modifier named 'Dennis' — leading to Dennis Rader, president of "
        "the congregation council. A family link was confirmed by DNA comparison. He was arrested on 25 February 2005, "
        "pleaded guilty on 27 June, and was sentenced on 18 August to ten consecutive life terms with a minimum of "
        "175 years."),
    "sources": SOURCES, "victims": VICTIMS, "memorial": MEMORIAL, "timeline": TIMELINE, "locations": LOCATIONS,
    "evidence": EVIDENCE, "investigation": INVESTIGATION, "psychology": PSYCHOLOGY, "victimology": VICTIMOLOGY,
    "court": COURT, "experts": EXPERTS, "experts_agreement": EXPERTS_AGREEMENT,
    "experts_disagreement": EXPERTS_DISAGREEMENT, "experts_uncertain": EXPERTS_UNCERTAIN,
    "counterfactuals": COUNTERFACTUALS, "lessons": LESSONS, "unknowns": UNKNOWNS, "sections": SECTIONS,
    "episodes": EPISODES, "questions": QUESTIONS,
}
