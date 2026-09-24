"""
DOSSIER 06 — PETER SUTCLIFFE (Royaume-Uni, Yorkshire, 1975-2020)

Le surnom médiatique « Yorkshire Ripper » est traité ici comme un objet
d'étude (son origine, ses effets sur l'enquête), jamais comme une identité
valorisante (§44). Sources publiques vérifiées le 2026-09-24.
"""
from ..case_template import (block, counterfactual, default_sections, fact, item,
                             merge_sections, question, source, txt)

CASE_ID = "yorkshire-sutcliffe"
V = "2026-09-24"

SOURCES = [
    source("ap-death", CASE_ID,
           "UK's 'Yorkshire Ripper' serial killer Peter Sutcliffe dies",
           "UK's 'Yorkshire Ripper' serial killer Peter Sutcliffe dies",
           "Associated Press (via KCRG)", "Associated Press",
           "https://www.kcrg.com/2020-11-13/uks-yorkshire-ripper-serial-killer-peter-sutcliffe-dies/",
           "2020-11-13", "press", "CONFIRMED", V,
           "Décès, verdict de 1981, canular ayant trompé les enquêteurs, défaillances du système de fiches.",
           "Death, 1981 verdict, hoax that misled investigators, failures of the card indexing system."),
    source("policyline-facts", CASE_ID,
           "Peter Sutcliffe: Verified Facts, Timeline, and Official Sources",
           "Peter Sutcliffe: Verified Facts, Timeline, and Official Sources",
           "policyline.uk", "Redaction", "https://policyline.uk/tech/peter-sutcliffe-verified-facts-timeline/",
           "2026-07-26", "press", "PROBABLE", V,
           "Synthèse de faits avec renvois à la BBC et à Crime + Investigation ; niveau PROBABLE car site secondaire.",
           "Fact synthesis with references to the BBC and Crime + Investigation; PROBABLE level as a secondary site."),
    source("serialkillercalendar", CASE_ID,
           "Serial killer Peter William Sutcliffe", "Serial killer Peter William Sutcliffe",
           "Serial Killer Calendar", "Redaction", "https://serialkillercalendar.com/Peter%20William%20SUTCLIFFE.php",
           "2026", "press", "PROBABLE", V,
           "Liste nominative des victimes retenues au procès, avec dates et âges ; à recouper avec les décisions de justice.",
           "Named list of victims retained at trial, with dates and ages; to be cross-checked with court decisions."),
    source("wikipedia-simple", CASE_ID, "Peter Sutcliffe", "Peter Sutcliffe",
           "Simple English Wikipedia", "Contributors", "https://simple.wikipedia.org/wiki/Peter_Sutcliffe",
           "2026", "public_archive", "PROBABLE", V,
           "Éléments biographiques de synthèse ; encyclopédie collaborative.",
           "Summary biographical elements; collaborative encyclopaedia."),
]


def _v(order, first, last, age, date, source_key, reliability, life_fr, life_en, dis_fr, dis_en):
    return {
        "order": order, "first_name": first, "last_name": last, "age": age,
        "source": source_key, "reliability": reliability, "anonymised": False,
        "life": {"fr": {"headline": f"{first} {last}", "items": life_fr},
                 "en": {"headline": f"{first} {last}", "items": life_en}},
        "disappearance": {"fr": {"items": dis_fr}, "en": {"items": dis_en}},
    }


NOTE = txt(
    "Les informations biographiques détaillées (profession, famille, projets) ne figurent pas dans les sources "
    "consultées pour la majorité des victimes. L'application affiche cette absence plutôt que de la combler.",
    "Detailed biographical information (occupation, family, plans) does not appear in the sources consulted for most "
    "victims. The application displays that absence rather than filling it.",
)

VICTIMS = [
    _v(0, "Wilma", "McCann", "28", "30 octobre 1975", "serialkillercalendar", "PROBABLE",
       [{"label": "Âge", "text": "28 ans."}, {"label": "Faits", "text": "Première victime retenue au procès, le 30 octobre 1975."},
        {"label": "Biographie", "text": "Non documentée dans les sources consultées."}],
       [{"label": "Age", "text": "28."}, {"label": "Facts", "text": "First victim retained at trial, on 30 October 1975."},
        {"label": "Biography", "text": "Not documented in the sources consulted."}],
       [{"label": "Date", "text": "30 octobre 1975."}], [{"label": "Date", "text": "30 October 1975."}]),
    _v(1, "Emily", "Jackson", "42", "20 janvier 1976", "serialkillercalendar", "PROBABLE",
       [{"label": "Âge", "text": "42 ans."}, {"label": "Biographie", "text": "Non documentée dans les sources consultées."}],
       [{"label": "Age", "text": "42."}, {"label": "Biography", "text": "Not documented in the sources consulted."}],
       [{"label": "Date", "text": "20 janvier 1976."}], [{"label": "Date", "text": "20 January 1976."}]),
    _v(2, "Irene", "Richardson", "28", "5 février 1977", "serialkillercalendar", "PROBABLE",
       [{"label": "Âge", "text": "28 ans."}, {"label": "Biographie", "text": "Non documentée dans les sources consultées."}],
       [{"label": "Age", "text": "28."}, {"label": "Biography", "text": "Not documented in the sources consulted."}],
       [{"label": "Date", "text": "5 février 1977."}], [{"label": "Date", "text": "5 February 1977."}]),
    _v(3, "Patricia", "Atkinson", "32", "23 avril 1977", "serialkillercalendar", "PROBABLE",
       [{"label": "Âge", "text": "32 ans."}, {"label": "Biographie", "text": "Non documentée dans les sources consultées."}],
       [{"label": "Age", "text": "32."}, {"label": "Biography", "text": "Not documented in the sources consulted."}],
       [{"label": "Date", "text": "23 avril 1977."}], [{"label": "Date", "text": "23 April 1977."}]),
    _v(4, "Jayne", "MacDonald", "16", "26 juin 1977", "serialkillercalendar", "PROBABLE",
       [{"label": "Âge", "text": "16 ans — la plus jeune victime retenue au procès."},
        {"label": "Biographie", "text": "Non documentée dans les sources consultées."}],
       [{"label": "Age", "text": "16 — the youngest victim retained at trial."},
        {"label": "Biography", "text": "Not documented in the sources consulted."}],
       [{"label": "Date", "text": "26 juin 1977."}], [{"label": "Date", "text": "26 June 1977."}]),
    _v(5, "Jacqueline", "Hill", "—", "17 novembre 1980", "policyline-facts", "CONFIRMED",
       [{"label": "Faits", "text": "Treizième et dernière victime retenue au procès, le 17 novembre 1980."},
        {"label": "Biographie", "text": "Non documentée dans les sources consultées."}],
       [{"label": "Facts", "text": "Thirteenth and last victim retained at trial, on 17 November 1980."},
        {"label": "Biography", "text": "Not documented in the sources consulted."}],
       [{"label": "Date", "text": "17 novembre 1980."}], [{"label": "Date", "text": "17 November 1980."}]),
]

MEMORIAL = {
    "title": txt("Treize femmes, 1975-1980", "Thirteen women, 1975-1980"),
    "biography": txt(
        "Treize femmes ont été tuées dans le Yorkshire et le nord-ouest de l'Angleterre entre le 30 octobre 1975 et "
        "le 17 novembre 1980. Sept autres ont survécu à des tentatives de meurtre. Leurs noms, pour huit d'entre "
        "elles, figurent dans les listes publiées par la presse ; les informations biographiques détaillées ne sont "
        "pas disponibles dans les sources consultées et ne sont pas reconstituées ici.",
        "Thirteen women were killed in Yorkshire and north-west England between 30 October 1975 and 17 November 1980. "
        "Seven others survived attempted murder. Their names, for eight of them, appear in lists published by the "
        "press; detailed biographical information is not available in the sources consulted and is not reconstructed "
        "here.",
    ),
    "testimony": txt(
        "Un rapport publié deux décennies après les faits a conclu que l'auteur avait probablement commis davantage "
        "de crimes que ceux pour lesquels il a été condamné. Ce constat porte sur l'ampleur des faits, pas sur les "
        "victimes déjà identifiées.",
        "A report published two decades after the facts concluded that the author probably committed more crimes than "
        "those for which he was convicted. That finding concerns the scale of the offences, not the victims already "
        "identified.",
    ),
    "memory": txt(
        "Le surnom donné par la presse a contribué à orienter l'enquête vers certaines victimes plutôt que d'autres, "
        "et a durablement marqué la mémoire publique. Cette application nomme les personnes et traite le surnom comme "
        "un objet d'analyse : ce qu'il a produit sur l'enquête est documenté, ce qu'il a produit sur la mémoire des "
        "victimes aussi.",
        "The nickname given by the press helped steer the investigation towards certain victims rather than others, "
        "and durably marked public memory. This application names the persons and treats the nickname as an object of "
        "analysis: what it produced on the investigation is documented, and so is what it produced on the victims' "
        "memory.",
    ),
}

TIMELINE = [
    fact("Naissance de Peter William Sutcliffe dans le West Yorkshire (Shipley selon l'Associated Press, Bingley "
         "selon d'autres notices).",
         "Peter William Sutcliffe is born in West Yorkshire (Shipley according to the Associated Press, Bingley "
         "according to other entries).",
         "DISPUTED", "ap-death", "Naissance", "Birth", "1946-06-02"),
    fact("Première victime retenue au procès : Wilma McCann, 28 ans, le 30 octobre 1975.",
         "First victim retained at trial: Wilma McCann, 28, on 30 October 1975.",
         "PROBABLE", "serialkillercalendar", "Premier fait jugé", "First offence tried", "1975-10-30"),
    fact("Les faits s'échelonnent jusqu'au 17 novembre 1980, date du meurtre de Jacqueline Hill, treizième victime "
         "retenue.",
         "The offences run until 17 November 1980, the date of the murder of Jacqueline Hill, thirteenth victim "
         "retained.",
         "PROBABLE", "policyline-facts", "Période des faits", "Period of offences", "1980-11-17"),
    fact("Des lettres et une cassette sonore revendiquant les faits sont adressées à la police. Elles émanent d'un "
         "autre homme et portent sur un accent du Wearside. Des responsables de l'enquête s'y fient et orientent les "
         "recherches en conséquence.",
         "Letters and an audio tape claiming the offences are sent to the police. They come from another man and "
         "concern a Wearside accent. Senior officers rely on them and steer the searches accordingly.",
         "CONFIRMED", "ap-death", "Le canular", "The hoax", "1978"),
    fact("Peter Sutcliffe est arrêté le 2 janvier 1981 à Sheffield, lors d'un contrôle routier. Il est trouvé en "
         "compagnie d'une prostituée dans sa voiture. Il reconnaît être l'auteur des faits au cours d'un entretien de "
         "vingt-quatre heures, après avoir été entendu neuf fois au cours de l'enquête sans être identifié.",
         "Peter Sutcliffe is arrested on 2 January 1981 in Sheffield, during a traffic stop. He is found with a "
         "prostitute in his car. He admits being the author during a twenty-four hour interview, after having been "
         "interviewed nine times during the investigation without being identified.",
         "CONFIRMED", "ap-death", "Arrestation", "Arrest", "1981-01-02"),
    fact("Procès à l'Old Bailey, ouvert le 5 mai 1981. Il plaide non coupable des meurtres mais coupable "
         "d'homicides involontaires pour responsabilité atténuée, invoquant des voix qu'il attribuait à Dieu. Le jury "
         "écarte cette défense.",
         "Trial at the Old Bailey, opened on 5 May 1981. He pleads not guilty to murder but guilty of manslaughter on "
         "grounds of diminished responsibility, invoking voices he attributed to God. The jury rejects that defence.",
         "CONFIRMED", "serialkillercalendar", "Procès", "Trial", "1981-05-05"),
    fact("Le 22 mai 1981, il est déclaré coupable de treize meurtres et de sept tentatives de meurtre, et condamné à "
         "vingt peines de réclusion à perpétuité concurrentes. Le juge recommande un minimum de trente ans et "
         "déclare espérer qu'il ne sorte jamais.",
         "On 22 May 1981, he is found guilty of thirteen murders and seven attempted murders, and sentenced to twenty "
         "concurrent life terms. The judge recommends a minimum of thirty years and states he hopes he will never be "
         "released.",
         "CONFIRMED", "ap-death", "Verdict", "Verdict", "1981-05-22"),
    fact("Il est hospitalisé à Broadmoor, établissement de haute sécurité. Des psychiatres ont retenu un diagnostic "
         "de schizophrénie paranoïde ; ce diagnostic est distinct du verdict du jury.",
         "He is hospitalised at Broadmoor, a high-security establishment. Psychiatrists retained a diagnosis of "
         "paranoid schizophrenia; that diagnosis is distinct from the jury's verdict.",
         "PROBABLE", "wikipedia-simple", "Hospitalisation", "Hospitalisation", "1984"),
    fact("Une décision de la High Court en 2010 confirme qu'il purgera une peine incompressible (whole life tariff) "
         "et ne sera jamais libéré.",
         "A High Court decision in 2010 confirms he will serve a whole life tariff and never be released.",
         "PROBABLE", "serialkillercalendar", "Peine incompressible", "Whole life tariff", "2010-08-04"),
    fact("Transféré à HMP Frankland en 2016, jugé suffisamment stable pour être détenu en prison.",
         "Transferred to HMP Frankland in 2016, deemed stable enough to be held in prison.",
         "CONFIRMED", "ap-death", "Transfert", "Transfer", "2016"),
    fact("Il meurt à l'hôpital le 13 novembre 2020, à 74 ans, après avoir refusé des soins à la suite d'un test "
         "positif au Covid-19. Il avait changé de nom en détention (Peter Coonan).",
         "He dies in hospital on 13 November 2020, aged 74, after refusing treatment following a positive Covid-19 "
         "test. He had changed his name in custody (Peter Coonan).",
         "CONFIRMED", "ap-death", "Décès", "Death", "2020-11-13"),
]

LOCATIONS = [
    {"kind": "region", "names": txt("Yorkshire et nord-ouest de l'Angleterre", "Yorkshire and north-west England"),
     "city": "", "region": "Yorkshire", "country": "GB", "lat": 53.8, "lon": -1.6, "precision": "region",
     "date": "1975-1980",
     "note": txt("Les faits sont répartis sur un large périmètre. Aucune adresse n'est publiée.",
                 "The offences are spread over a wide area. No address is published."),
     "reliability": "CONFIRMED", "source": "ap-death"},
    {"kind": "city", "names": txt("Sheffield (arrestation)", "Sheffield (arrest)"),
     "city": "Sheffield", "region": "South Yorkshire", "country": "GB", "lat": 53.38, "lon": -1.47,
     "precision": "city", "date": "1981-01-02", "note": txt("Contrôle routier du 2 janvier 1981.", "Traffic stop of 2 January 1981."),
     "reliability": "CONFIRMED", "source": "ap-death"},
    {"kind": "court", "names": txt("Old Bailey, Londres", "Old Bailey, London"),
     "city": "Londres", "region": "Grand Londres", "country": "GB", "lat": 51.516, "lon": -0.102,
     "precision": "city", "date": "1981-05-22", "note": txt("Procès du 5 au 22 mai 1981.", "Trial from 5 to 22 May 1981."),
     "reliability": "CONFIRMED", "source": "serialkillercalendar"},
]

EVIDENCE = [
    {"kind": "documentary", "weight": "disputed", "reliability": "CONFIRMED", "source": "ap-death",
     "title": txt("Lettres et cassette du « Wearside Jack »", "The 'Wearside Jack' letters and tape"),
     "description": txt(
         "Des communications revendiquant les faits proviennent d'un autre homme et mettent en avant un accent du "
         "Wearside. Des responsables de l'enquête s'y fient, ce qui oriente les recherches vers une zone et un profil "
         "vocal qui ne correspondaient pas à l'auteur réel.",
         "Communications claiming the offences come from another man and put forward a Wearside accent. Senior "
         "officers rely on them, steering searches towards an area and a vocal profile that did not correspond to the "
         "actual author.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "ap-death",
     "title": txt("Un système de fiches mal croisé", "A poorly cross-referenced card system"),
     "description": txt(
         "La police, submergée par le volume d'informations, avait mis en place un système de fiches. Il était mal "
         "croisé : des éléments clés ont été égarés. Des détails d'apparence — un écart entre les dents, une pointure "
         "— n'ont pas été signalés comme pertinents.",
         "Police, overwhelmed by the volume of information, had set up a card system. It was poorly cross-referenced: "
         "key elements were misplaced. Appearance details — a gap in the teeth, a shoe size — were not flagged as "
         "relevant.")},
    {"kind": "testimony", "weight": "documented", "reliability": "CONFIRMED", "source": "ap-death",
     "title": txt("Neuf entretiens sans identification", "Nine interviews without identification"),
     "description": txt(
         "L'homme a été entendu neuf fois au cours de l'enquête. Il n'a été identifié qu'à l'occasion d'un contrôle "
         "routier sans lien avec l'affaire. À l'audience, il a lui-même exprimé sa surprise d'avoir pu agir aussi "
         "longtemps : « It was just a miracle they did not apprehend me earlier — they had all the facts. »",
         "The man was interviewed nine times during the investigation. He was identified only during a traffic stop "
         "unrelated to the case. At the hearing, he himself expressed surprise at having gone on so long: 'It was "
         "just a miracle they did not apprehend me earlier — they had all the facts.'")},
    {"kind": "testimony", "weight": "documented", "reliability": "CONFIRMED", "source": "serialkillercalendar",
     "title": txt("Une défense fondée sur des voix", "A defence based on voices"),
     "description": txt(
         "À l'audience, l'accusé a invoqué des voix qu'il attribuait à Dieu, déclarant les avoir entendues alors "
         "qu'il travaillait comme fossoyeur, et les avoir rattachées à une pierre tombale. Des psychiatres ont retenu "
         "une schizophrénie paranoïde ; le jury a écarté la responsabilité atténuée.",
         "At the hearing, the accused invoked voices he attributed to God, stating he heard them while working as a "
         "gravedigger, and linked them to a headstone. Psychiatrists retained paranoid schizophrenia; the jury "
         "rejected diminished responsibility.")},
]

INVESTIGATION = {
    "steps": [
        {"n": 1, "date": "1975-10-30", "title": txt("Un premier meurtre dans le Yorkshire", "A first murder in Yorkshire"),
         "body": txt("Wilma McCann, 28 ans, est tuée le 30 octobre 1975. Rien ne relie encore ce fait à une série.",
                     "Wilma McCann, 28, is killed on 30 October 1975. Nothing yet links this offence to a series.",),
         "reliability": "PROBABLE", "source": "serialkillercalendar", "premium": False},
        {"n": 2, "date": "1976-1977", "title": txt("La constitution d'une série", "The formation of a series"),
         "body": txt("Des meurtres successifs sont commis dans le Yorkshire et le nord-ouest. L'enquête devient l'une "
                     "des plus vastes et des plus coûteuses de l'histoire britannique.",
                     "Successive murders are committed in Yorkshire and the north-west. The investigation becomes one "
                     "of the largest and most expensive in British history.",),
         "reliability": "CONFIRMED", "source": "ap-death", "premium": False},
        {"n": 3, "date": "1978", "title": txt("Un canular qui oriente l'enquête", "A hoax that steers the investigation"),
         "body": txt("Des lettres puis une cassette revendiquant les faits parviennent à la police. Elles émanent "
                     "d'un autre homme. Des responsables s'y fient : les recherches sont orientées vers un accent du "
                     "Wearside, alors que l'auteur réel ne l'avait pas.",
                     "Letters then a tape claiming the offences reach the police. They come from another man. Senior "
                     "officers rely on them: searches are steered towards a Wearside accent, which the actual author "
                     "did not have.",),
         "reliability": "CONFIRMED", "source": "ap-death", "premium": True},
        {"n": 4, "date": "1978-1980", "title": txt("Neuf entretiens, aucune identification", "Nine interviews, no identification"),
         "body": txt("L'homme est entendu neuf fois pendant l'enquête. Le système de fiches, mal croisé, égare des "
                     "éléments ; des détails physiques ne sont pas rapprochés.",
                     "The man is interviewed nine times during the investigation. The card system, poorly "
                     "cross-referenced, misplaces elements; physical details are not linked.",),
         "reliability": "CONFIRMED", "source": "ap-death", "premium": True},
        {"n": 5, "date": "1981-01-02", "title": txt("Un contrôle routier", "A traffic stop"),
         "body": txt("À Sheffield, lors d'un contrôle sans lien avec l'affaire, il est trouvé en compagnie d'une "
                     "prostituée dans sa voiture. Il est arrêté. Au cours d'un entretien de vingt-quatre heures, il "
                     "reconnaît les faits.",
                     "In Sheffield, during a stop unrelated to the case, he is found with a prostitute in his car. He "
                     "is arrested. During a twenty-four hour interview, he admits the facts.",),
         "reliability": "CONFIRMED", "source": "ap-death", "premium": False},
        {"n": 6, "date": "1981-05-22", "title": txt("Le verdict", "The verdict"),
         "body": txt("Le jury écarte la responsabilité atténuée et le déclare coupable de treize meurtres et sept "
                     "tentatives. Vingt peines de réclusion à perpétuité concurrentes sont prononcées.",
                     "The jury rejects diminished responsibility and finds him guilty of thirteen murders and seven "
                     "attempts. Twenty concurrent life terms are pronounced.",),
         "reliability": "CONFIRMED", "source": "ap-death", "premium": False},
        {"n": 7, "date": "2010-08-04", "title": txt("Une peine incompressible confirmée", "A whole life tariff confirmed"),
         "body": txt("Une décision de la High Court confirme qu'il ne sera jamais libéré.",
                     "A High Court decision confirms he will never be released.",),
         "reliability": "PROBABLE", "source": "serialkillercalendar", "premium": True},
    ],
    "reality": txt(
        "L'enquête a disposé des éléments avant de pouvoir les assembler : neuf entretiens, des détails physiques "
        "relevés, un volume massif d'informations. Ce n'est pas une absence de données qui a retardé l'identification, "
        "c'est leur traitement — et une communication falsifiée qui a orienté les recherches ailleurs.",
        "The investigation had the elements before being able to assemble them: nine interviews, recorded physical "
        "details, a massive volume of information. It was not an absence of data that delayed identification, but "
        "their handling — and a falsified communication that steered searches elsewhere."),
    "errors": [
        item("Foi accordée à des lettres et à une cassette provenant d'un canular, orientant les recherches vers un "
             "accent et une zone erronés.",
             "Faith placed in letters and a tape from a hoax, steering searches towards a wrong accent and area.",
             "CONFIRMED", "ap-death", "Communication falsifiée", "Falsified communication"),
        item("Système de fiches mal croisé : des éléments clés ont été égarés malgré leur existence.",
             "Poorly cross-referenced card system: key elements were misplaced despite existing.",
             "CONFIRMED", "ap-death", "Gestion de l'information", "Information management"),
        item("Détails physiques (écart dentaire, pointure) non signalés comme pertinents lors des entretiens.",
             "Physical details (gap in the teeth, shoe size) not flagged as relevant during interviews.",
             "CONFIRMED", "ap-death", "Rapprochement", "Linkage"),
    ],
    "cold_case": {
        "what_we_know": [
            item("Treize meurtres et sept tentatives retenus au procès de 1981.",
                 "Thirteen murders and seven attempts retained at the 1981 trial.", "CONFIRMED", "ap-death"),
            item("Neuf entretiens avant l'identification ; arrestation lors d'un contrôle routier.",
                 "Nine interviews before identification; arrest during a traffic stop.", "CONFIRMED", "ap-death"),
        ],
        "what_is_probable": [
            item("Un rapport publié deux décennies plus tard conclut qu'il a probablement commis d'autres crimes que "
                 "ceux jugés.",
                 "A report published two decades later concludes he probably committed other crimes than those tried.",
                 "PROBABLE", "ap-death"),
        ],
        "what_is_disputed": [
            item("Le lieu de naissance : Shipley selon l'Associated Press, Bingley selon d'autres notices.",
                 "Place of birth: Shipley according to the Associated Press, Bingley according to other entries.",
                 "DISPUTED", "ap-death"),
            item("L'articulation entre le diagnostic psychiatrique de schizophrénie paranoïde et le verdict de "
                 "culpabilité pour meurtre : ce sont deux actes distincts.",
                 "The articulation between the psychiatric diagnosis of paranoid schizophrenia and the murder "
                 "conviction: they are two distinct acts.", "DISPUTED", "wikipedia-simple"),
        ],
        "what_is_unknown": [
            item("Le nombre exact de faits non jugés.", "The exact number of untried offences.", "UNKNOWN", "ap-death"),
        ],
        "latest_progress": [
            item("Décès en détention le 13 novembre 2020 ; une enquête du coroner a été ouverte.",
                 "Death in custody on 13 November 2020; a coroner's investigation was opened.",
                 "CONFIRMED", "ap-death"),
        ],
        "leads": [], "limits": [],
    },
}

PSYCHOLOGY = {
    "disclaimer": txt("Un diagnostic de schizophrénie paranoïde a été retenu par des psychiatres et publié dans la "
                      "presse ; le jury a néanmoins écarté la responsabilité atténuée. L'application présente les "
                      "deux éléments sans les confondre et ne pose elle-même aucun diagnostic.",
                      "A diagnosis of paranoid schizophrenia was retained by psychiatrists and published in the "
                      "press; the jury nevertheless rejected diminished responsibility. The application presents "
                      "both elements without conflating them and makes no diagnosis itself."),
    "blocks": [
        block("fact", "Un récit de voix", "An account of voices",
              "À l'audience, l'accusé a déclaré avoir entendu des voix qu'il attribuait à Dieu, et les avoir "
              "rattachées à une pierre tombale alors qu'il travaillait comme fossoyeur. C'est une déclaration "
              "d'audience, pas un constat clinique.",
              "At the hearing, the accused said he had heard voices he attributed to God, and linked them to a "
              "headstone while working as a gravedigger. This is a statement made at the hearing, not a clinical "
              "finding.",
              "CONFIRMED", "serialkillercalendar"),
        block("expert", "Diagnostic psychiatrique et verdict", "Psychiatric diagnosis and verdict",
              "Des psychiatres ont retenu une schizophrénie paranoïde. Le jury a écarté la défense de responsabilité "
              "atténuée et prononcé un verdict de culpabilité pour meurtre sur les treize chefs. En droit anglais, "
              "ces deux éléments coexistent : un diagnostic ne détermine pas automatiquement l'issue pénale.",
              "Psychiatrists retained paranoid schizophrenia. The jury rejected the diminished responsibility defence "
              "and returned a guilty verdict for murder on all thirteen counts. Under English law, these two elements "
              "coexist: a diagnosis does not automatically determine the criminal outcome.",
              "CONFIRMED", "ap-death"),
        block("behaviour", "Un comportement d'opportunité et de dissimulation", "A behaviour of opportunity and concealment",
              "Il a été entendu neuf fois sans être identifié, ce qui documente une capacité à ne pas éveiller la "
              "suspicion lors d'entretiens de police. Ce constat porte sur l'enquête, pas sur une structure "
              "psychique.",
              "He was interviewed nine times without being identified, which documents a capacity not to arouse "
              "suspicion during police interviews. That finding concerns the investigation, not a psychic structure.",
              "CONFIRMED", "ap-death"),
        block("unknown", "Ce qui n'est pas documenté", "What is not documented",
              "Les motivations, le déroulé interne des faits et l'existence de victimes supplémentaires ne sont pas "
              "établis par les sources consultées.",
              "Motivations, the internal course of the offences and the existence of further victims are not "
              "established by the sources consulted.",
              "UNKNOWN", None),
    ],
}

VICTIMOLOGY = {
    "ethics_note": txt("La catégorisation des victimes par la presse et par une partie de l'enquête est un objet "
                      "d'analyse. Elle ne fonde aucune hiérarchie entre les personnes tuées.",
                      "The categorisation of victims by the press and by part of the investigation is an object of "
                      "analysis. It establishes no hierarchy between the persons killed."),
    "blocks": [
        block("context", "Treize femmes, un large périmètre", "Thirteen women, a wide area",
              "Les victimes étaient des femmes tuées dans le Yorkshire et le nord-ouest de l'Angleterre entre 1975 et "
              "1980. Les âges retenus dans les listes publiées vont de 16 à 42 ans pour les victimes dont l'âge est "
              "documenté dans les sources consultées.",
              "The victims were women killed in Yorkshire and north-west England between 1975 and 1980. The ages "
              "given in published lists range from 16 to 42 for those documented in the sources consulted.",
              "PROBABLE", "serialkillercalendar"),
        block("analysis", "Ce que la victimologie révèle ici", "What victimology reveals here",
              "Les faits ont d'abord visé des femmes prostituées, puis des jeunes femmes sans lien avec cette "
              "situation. Cette évolution est documentée par la presse de l'époque et par les synthèses ultérieures. "
              "Elle montre que la catégorisation initiale des victimes a conduit à sous-estimer le périmètre réel de "
              "la série.",
              "The offences first targeted women working as prostitutes, then young women with no connection to that "
              "situation. This evolution is documented by the press of the time and by later syntheses. It shows that "
              "the initial categorisation of victims led to underestimating the real perimeter of the series.",
              "PROBABLE", "ap-death"),
    ],
}

COURT = {
    "jurisdiction": txt("Royaume-Uni — Central Criminal Court (Old Bailey), Londres",
                        "United Kingdom — Central Criminal Court (Old Bailey), London"),
    "verdict": txt("Coupable de treize meurtres et de sept tentatives de meurtre, le 22 mai 1981. La défense de "
                   "responsabilité atténuée a été écartée par le jury.",
                   "Guilty of thirteen murders and seven attempted murders, on 22 May 1981. The diminished "
                   "responsibility defence was rejected by the jury."),
    "sentence": {
        "label": txt("Vingt peines de réclusion à perpétuité concurrentes ; peine incompressible confirmée en 2010",
                     "Twenty concurrent life sentences; whole life tariff confirmed in 2010"),
        "pronounced": "1981-05-22",
        "requested": txt("Le juge a recommandé un minimum de trente ans avant tout examen d'une libération et a "
                         "déclaré espérer qu'il ne sorte jamais de prison.",
                         "The judge recommended a minimum of thirty years before any release review and stated he "
                         "hoped he would never leave prison."),
        "cumul": txt("Les vingt peines sont concurrentes, et non consécutives.",
                     "The twenty sentences are concurrent, not consecutive."),
        "reasoning": txt("Le juge a déclaré que l'accusé était « beyond redemption ».",
                         "The judge stated that the accused was 'beyond redemption'."),
        "appeal": txt("Une décision de la High Court du 4 août 2010 a confirmé le caractère incompressible de la peine.",
                      "A High Court decision of 4 August 2010 confirmed the whole life character of the sentence."),
        "reliability": "CONFIRMED", "source": "ap-death",
    },
    "consequences": [
        item("L'enquête a fait l'objet de critiques publiques durables sur la gestion de l'information et sur la "
             "confiance accordée à une communication falsifiée.",
             "The investigation was the subject of lasting public criticism over information management and over the "
             "trust placed in a falsified communication.",
             "CONFIRMED", "ap-death"),
        item("Le traitement médiatique et la catégorisation des victimes ont alimenté un débat public sur la manière "
             "de nommer les affaires criminelles.",
             "Media treatment and the categorisation of victims fed a public debate on how to name criminal cases.",
             "PROBABLE", "ap-death"),
    ],
}

EXPERTS = [
    {"label": txt("Lecture psychiatrique", "Psychiatric reading"), "field": "psychiatry",
     "position": txt("Des psychiatres ont retenu une schizophrénie paranoïde, fondement de la défense de "
                     "responsabilité atténuée.",
                     "Psychiatrists retained paranoid schizophrenia, the basis of the diminished responsibility defence."),
     "reliability": "PROBABLE", "source": "wikipedia-simple"},
    {"label": txt("Lecture du jury", "The jury's reading"), "field": "judicial",
     "position": txt("Le jury a écarté la responsabilité atténuée et retenu la culpabilité pour meurtre sur les "
                     "treize chefs.",
                     "The jury rejected diminished responsibility and found guilt for murder on all thirteen counts."),
     "reliability": "CONFIRMED", "source": "serialkillercalendar"},
    {"label": txt("Lecture policière rétrospective", "Retrospective police reading"), "field": "investigation",
     "position": txt("Un rapport publié deux décennies plus tard a conclu qu'il avait probablement commis davantage "
                     "de crimes que ceux jugés, et a mis en cause la gestion de l'information.",
                     "A report published two decades later concluded he probably committed more crimes than those "
                     "tried, and criticised information management."),
     "reliability": "CONFIRMED", "source": "ap-death"},
]
EXPERTS_AGREEMENT = txt("Tous s'accordent sur la chronologie et sur le fait que l'identification est intervenue tardivement.",
                        "All agree on the chronology and on the late identification.")
EXPERTS_DISAGREEMENT = txt("Ils divergent sur l'articulation entre diagnostic psychiatrique et responsabilité pénale.",
                           "They differ on how psychiatric diagnosis articulates with criminal responsibility.")
EXPERTS_UNCERTAIN = txt("Ce qui reste incertain : l'ampleur réelle des faits non jugés.",
                        "What remains uncertain: the real scale of untried offences.")

COUNTERFACTUALS = [
    counterfactual(
        "hoax_believed",
        "Et si les lettres et la cassette du canular n'avaient pas été crues ?",
        "What if the hoax letters and tape had not been believed?",
        "Des lettres puis une cassette revendiquant les faits, émanant d'un autre homme et mettant en avant un accent "
        "du Wearside, ont orienté les recherches. Des meurtres retenus au procès ont été commis après l'arrivée de ces "
        "communications.",
        "Letters then a tape claiming the offences, coming from another man and putting forward a Wearside accent, "
        "steered the searches. Murders retained at trial were committed after those communications arrived.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Premières communications du canular", "First hoax communications"), "date": "1978-06-01"},
            "hypothesis": {"label": txt("Communications tenues pour authentiques", "Communications held to be authentic"), "date": "1978-06-30"},
            "scenario_event": {"label": txt("Arrestation lors d'un contrôle routier", "Arrest during a traffic stop"), "date": "1981-01-02"},
            "outcome_event": {"label": txt("Condamnation", "Conviction"), "date": "1981-05-22"},
            "documented_offences_after": [
                {"date": "1980-11-17", "label": txt("Jacqueline Hill, treizième victime retenue", "Jacqueline Hill, thirteenth victim retained"), "reliability": "PROBABLE"},
            ],
            "jurisdiction_note": txt(
                "Les dates précises de plusieurs meurtres intermédiaires ne figurent pas dans les sources consultées "
                "pour toutes les victimes : le décompte affiché ne porte que sur les faits dont la date est établie "
                "après l'événement de référence. L'application n'extrapole pas.",
                "The precise dates of several intermediate murders do not appear in the sources consulted for all "
                "victims: the displayed count concerns only offences whose date is established after the reference "
                "event. The application does not extrapolate."),
        },
        [
            {"date": "1975-10-30", "kind": "offence", "label": txt("Wilma McCann", "Wilma McCann")},
            {"date": "1977-06-26", "kind": "offence", "label": txt("Jayne MacDonald, 16 ans", "Jayne MacDonald, 16")},
            {"date": "1978-06-01", "kind": "reference", "label": txt("Canular reçu", "Hoax received")},
            {"date": "1980-11-17", "kind": "offence", "label": txt("Jacqueline Hill", "Jacqueline Hill")},
            {"date": "1981-01-02", "kind": "scenario", "label": txt("Arrestation", "Arrest")},
            {"date": "1981-05-22", "kind": "outcome", "label": txt("Condamnation", "Conviction")},
        ],
        True, "ap-death"),
    counterfactual(
        "investigation_orientation",
        "Et si les neuf entretiens avaient été rapprochés ?",
        "What if the nine interviews had been linked?",
        "L'auteur a été entendu neuf fois au cours de l'enquête. Le système de fiches était mal croisé et des détails "
        "physiques n'ont pas été signalés comme pertinents. Il a déclaré à l'audience : « They had all the facts. »",
        "The author was interviewed nine times during the investigation. The card system was poorly cross-referenced "
        "and physical details were not flagged as relevant. He told the court: 'They had all the facts.'",
        {
            "unit": "years",
            "reference_event": {"label": txt("Premiers entretiens", "First interviews"), "date": "1977-01-01"},
            "hypothesis": {"label": txt("Fiches mal croisées", "Poorly cross-referenced cards"), "date": "1979-01-01"},
            "scenario_event": {"label": txt("Arrestation fortuite", "Chance arrest"), "date": "1981-01-02"},
            "jurisdiction_note": txt(
                "Aucune source consultée ne date chacun des neuf entretiens. Le calcul d'un écart précis est donc "
                "impossible avec une fiabilité suffisante : l'application affiche la période et non un nombre de mois.",
                "No source consulted dates each of the nine interviews. Computing a precise gap is therefore "
                "impossible with sufficient reliability: the application displays the period, not a number of months."),
        },
        [
            {"date": "1977-01-01", "kind": "reference", "label": txt("Entretiens (non datés individuellement)", "Interviews (not individually dated)")},
            {"date": "1980-11-17", "kind": "offence", "label": txt("Dernière victime retenue", "Last victim retained")},
            {"date": "1981-01-02", "kind": "scenario", "label": txt("Arrestation", "Arrest")},
        ],
        False, "ap-death"),
]

LESSONS = [
    item("Une communication revendicative doit être testée avant d'orienter une enquête : ici, un canular a déplacé "
         "les recherches.",
         "A claiming communication must be tested before steering an investigation: here, a hoax displaced the "
         "searches.",
         "CONFIRMED", "ap-death", "Authentification", "Authentication"),
    item("Le volume d'information ne protège pas : sans croisement, un système de fiches égare les éléments qu'il "
         "contient.",
         "Volume of information does not protect: without cross-referencing, a card system misplaces the elements it "
         "contains.",
         "CONFIRMED", "ap-death", "Gestion de l'information", "Information management"),
    item("Un diagnostic psychiatrique et un verdict pénal sont deux actes distincts : les deux ont coexisté ici.",
         "A psychiatric diagnosis and a criminal verdict are two distinct acts: both coexisted here.",
         "CONFIRMED", "ap-death", "Droit et psychiatrie", "Law and psychiatry"),
    item("La catégorisation des victimes a réduit le périmètre perçu de la série : les premières victimes ont été "
         "traitées différemment des suivantes.",
         "The categorisation of victims reduced the perceived perimeter of the series: the first victims were treated "
         "differently from the later ones.",
         "PROBABLE", "ap-death", "Victimologie", "Victimology"),
    item("Un surnom de presse n'est pas une identité : il oriente la perception publique et peut orienter l'enquête.",
         "A press nickname is not an identity: it steers public perception and can steer the investigation.",
         "CONFIRMED", "ap-death", "Médias", "Media"),
]

UNKNOWNS = [
    item("Le nombre de faits non jugés.", "The number of untried offences.", "UNKNOWN", "ap-death"),
    item("Les dates précises de plusieurs meurtres intermédiaires, dans les sources consultées.",
         "The precise dates of several intermediate murders, in the sources consulted.", "UNKNOWN", "serialkillercalendar"),
    item("Le lieu de naissance exact : les sources divergent.", "The exact place of birth: sources diverge.",
         "DISPUTED", "ap-death"),
]

SECTIONS = merge_sections(default_sections(), [
    {"key": "introduction", "blocks": [block(
        "paragraph", "Treize meurtres, neuf entretiens, un canular", "Thirteen murders, nine interviews, a hoax",
        "Entre 1975 et 1980, treize femmes sont tuées dans le Yorkshire et le nord-ouest de l'Angleterre. L'auteur est "
        "entendu neuf fois sans être identifié. Une communication falsifiée oriente l'enquête vers une autre région. "
        "L'arrestation survient à l'occasion d'un contrôle routier sans lien avec l'affaire.",
        "Between 1975 and 1980, thirteen women are killed in Yorkshire and north-west England. The author is "
        "interviewed nine times without being identified. A falsified communication steers the investigation towards "
        "another region. The arrest comes during a traffic stop unrelated to the case.",
        "CONFIRMED", "ap-death")]},
    {"key": "context", "blocks": [block(
        "paragraph", "La plus grande chasse à l'homme britannique de son temps", "The largest British manhunt of its time",
        "L'enquête est décrite comme l'une des plus vastes et des plus coûteuses de l'histoire britannique. Elle a "
        "produit un volume d'informations que les outils de l'époque ne permettaient pas de croiser efficacement.",
        "The investigation is described as one of the largest and most expensive in British history. It produced a "
        "volume of information that the tools of the time did not allow to cross-reference effectively.",
        "CONFIRMED", "ap-death")]},
    {"key": "offender", "blocks": [block(
        "paragraph", "Peter William Sutcliffe (1946-2020)", "Peter William Sutcliffe (1946-2020)",
        "Né le 2 juin 1946 dans le West Yorkshire. A notamment travaillé comme fossoyeur. Condamné le 22 mai 1981 à "
        "vingt peines de réclusion à perpétuité concurrentes. Hospitalisé à Broadmoor, transféré à HMP Frankland en "
        "2016, mort le 13 novembre 2020. Il avait changé de nom en détention.",
        "Born 2 June 1946 in West Yorkshire. Worked notably as a gravedigger. Sentenced on 22 May 1981 to twenty "
        "concurrent life terms. Hospitalised at Broadmoor, transferred to HMP Frankland in 2016, died on 13 November "
        "2020. He had changed his name in custody.",
        "CONFIRMED", "ap-death")]},
    {"key": "behaviour", "blocks": [block(
        "behaviour", "Passer neuf fois à travers l'entretien", "Getting through nine interviews",
        "Le comportement documenté n'est pas celui d'une mise en scène élaborée, mais celui d'une capacité à ne pas "
        "éveiller la suspicion lors d'entretiens répétés. C'est un fait d'enquête, établi par les synthèses "
        "ultérieures.",
        "The documented behaviour is not that of elaborate staging, but of a capacity not to arouse suspicion during "
        "repeated interviews. That is an investigation fact, established by later syntheses.",
        "CONFIRMED", "ap-death")]},
    {"key": "consequences", "blocks": [block(
        "paragraph", "Ce que l'affaire a laissé", "What the case left behind",
        "Des critiques publiques durables sur la gestion de l'information, un rapport concluant à une ampleur "
        "probablement supérieure à celle jugée, et un débat sur la manière dont la presse nomme les affaires et "
        "catégorise les victimes.",
        "Lasting public criticism of information management, a report concluding the scale was probably greater than "
        "that tried, and a debate on how the press names cases and categorises victims.",
        "CONFIRMED", "ap-death")]},
])

EPISODES = [
    {
        "number": 1,
        "title": txt("Neuf entretiens", "Nine interviews"),
        "description": txt("Yorkshire, 1975-1981. Une enquête massive, une communication falsifiée, et un homme "
                           "entendu neuf fois sans être identifié.",
                           "Yorkshire, 1975-1981. A massive investigation, a falsified communication, and a man "
                           "interviewed nine times without being identified."),
        "modes": ["documentary", "investigation", "chronology", "express", "expert", "psychology", "victims"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 70, "title": txt("1975-1980", "1975-1980")},
            {"at": 240, "title": txt("Les lettres et la cassette", "The letters and the tape")},
            {"at": 420, "title": txt("Un système de fiches", "A card system")},
            {"at": 580, "title": txt("Et maintenant, une question", "And now, a question")},
            {"at": 620, "title": txt("Old Bailey, mai 1981", "Old Bailey, May 1981")},
        ],
        "transcript": {"segments": [
            {"id": "s1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X, à travers mon regard. Aujourd'hui, une affaire britannique qui pose une "
                     "question inconfortable : que se passe-t-il quand une enquête dispose de tout, et ne parvient "
                     "pas à l'assembler ?",
             "text_en": "You are on YANIS//X, through my eyes. Today, a British case that asks an uncomfortable "
                        "question: what happens when an investigation has everything, and cannot assemble it?"},
            {"id": "s2", "t": 70, "speaker": "yanis",
             "text": "Entre le 30 octobre 1975 et le 17 novembre 1980, treize femmes sont tuées dans le Yorkshire et "
                     "le nord-ouest de l'Angleterre. Sept autres survivent à des tentatives. La première victime "
                     "retenue au procès s'appelait Wilma McCann, elle avait vingt-huit ans. La plus jeune, Jayne "
                     "MacDonald, avait seize ans. La dernière, Jacqueline Hill, a été tuée le 17 novembre 1980.",
             "text_en": "Between 30 October 1975 and 17 November 1980, thirteen women are killed in Yorkshire and "
                        "north-west England. Seven others survive attempts. The first victim retained at trial was "
                        "called Wilma McCann; she was twenty-eight. The youngest, Jayne MacDonald, was sixteen. The "
                        "last, Jacqueline Hill, was killed on 17 November 1980."},
            {"id": "s3", "t": 240, "speaker": "yanis",
             "text": "Pendant l'enquête, des lettres parviennent à la police, puis une cassette sonore. Elles "
                     "revendiquent les meurtres. Elles mettent en avant un accent du Wearside. Elles n'émanent pas de "
                     "l'auteur des faits : c'est un canular. Des responsables de l'enquête s'y fient. Les recherches "
                     "sont orientées vers une zone et un profil vocal qui ne correspondent pas.",
             "text_en": "During the investigation, letters reach the police, then an audio tape. They claim the "
                        "murders. They put forward a Wearside accent. They do not come from the author of the "
                        "offences: it is a hoax. Senior officers rely on them. Searches are steered towards an area "
                        "and a vocal profile that do not match."},
            {"id": "s4", "t": 420, "speaker": "yanis",
             "text": "Parallèlement, la police est submergée par le volume d'informations. Un système de fiches est "
                     "mis en place. Il est mal croisé : des éléments clés sont égarés. Des détails d'apparence — un "
                     "écart entre les dents, une pointure — ne sont pas signalés comme pertinents. Et l'homme est "
                     "entendu neuf fois pendant l'enquête. Neuf fois, sans être identifié.",
             "text_en": "Meanwhile, police are overwhelmed by the volume of information. A card system is set up. It "
                        "is poorly cross-referenced: key elements are misplaced. Appearance details — a gap in the "
                        "teeth, a shoe size — are not flagged as relevant. And the man is interviewed nine times "
                        "during the investigation. Nine times, without being identified."},
            {"id": "s5", "t": 580, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "s6", "t": 620, "speaker": "yanis",
             "text": "Le 2 janvier 1981, à Sheffield, un contrôle routier sans lien avec l'affaire. Il est trouvé en "
                     "compagnie d'une prostituée dans sa voiture. Il est arrêté. Au cours d'un entretien de "
                     "vingt-quatre heures, il reconnaît les faits. À l'audience, il dira lui-même : « It was just a "
                     "miracle they did not apprehend me earlier — they had all the facts. »",
             "text_en": "On 2 January 1981, in Sheffield, a traffic stop unrelated to the case. He is found with a "
                        "prostitute in his car. He is arrested. During a twenty-four hour interview, he admits the "
                        "facts. At the hearing, he would himself say: 'It was just a miracle they did not apprehend "
                        "me earlier — they had all the facts.'"},
            {"id": "s7", "t": 780, "speaker": "yanis",
             "text": "Le procès s'ouvre à l'Old Bailey le 5 mai 1981. Il plaide non coupable des meurtres, coupable "
                     "d'homicides involontaires pour responsabilité atténuée, invoquant des voix qu'il attribuait à "
                     "Dieu. Des psychiatres retiennent une schizophrénie paranoïde. Le jury écarte cette défense. Le "
                     "22 mai 1981, il est déclaré coupable de treize meurtres et de sept tentatives, et condamné à "
                     "vingt peines de réclusion à perpétuité concurrentes. En 2010, la High Court confirme qu'il ne "
                     "sera jamais libéré. Il meurt en détention le 13 novembre 2020.",
             "text_en": "The trial opens at the Old Bailey on 5 May 1981. He pleads not guilty to murder, guilty of "
                        "manslaughter on grounds of diminished responsibility, invoking voices he attributed to God. "
                        "Psychiatrists retain paranoid schizophrenia. The jury rejects that defence. On 22 May 1981, "
                        "he is found guilty of thirteen murders and seven attempts, and sentenced to twenty concurrent "
                        "life terms. In 2010, the High Court confirms he will never be released. He dies in custody on "
                        "13 November 2020."},
            {"id": "s8", "t": 960, "speaker": "yanis",
             "text": "Cette affaire porte un surnom de presse. Ce surnom n'est pas une identité : il a orienté des "
                     "recherches et marqué une mémoire. Ici, les personnes s'appellent Wilma, Emily, Irene, Patricia, "
                     "Jayne, Jacqueline — et sept autres dont les noms figurent au verdict de 1981. Écouter les "
                     "histoires. Comprendre les affaires. Ne jamais oublier les victimes.",
             "text_en": "This case carries a press nickname. That nickname is not an identity: it steered searches and "
                        "marked a memory. Here, the persons are called Wilma, Emily, Irene, Patricia, Jayne, "
                        "Jacqueline — and seven others whose names appear in the 1981 verdict. Listen to the stories. "
                        "Understand the cases. Never forget the victims."},
        ]},
    },
]

QUESTIONS = [
    question("1", 580, "bias",
             "Des lettres et une cassette revendiquent les faits et décrivent un accent. Quelle est la première vérification à opérer ?",
             "Letters and a tape claim the offences and describe an accent. What is the first verification to carry out?",
             [("a", "Comparer l'accent décrit avec celui des personnes déjà entendues", "Compare the described accent with that of persons already interviewed"),
              ("b", "Tester l'authenticité de la communication elle-même", "Test the authenticity of the communication itself"),
              ("c", "Élargir la zone de recherche à la région décrite", "Extend the search area to the described region"),
              ("d", "Diffuser la cassette pour susciter des appels", "Broadcast the tape to generate calls")],
             {"fr": {"whatInvestigatorsKnew": "Des lettres puis une cassette revendiquant les faits sont parvenues à la police ; elles émanaient d'un autre homme.",
                     "whatExpertsProposed": "Une communication revendicative est un élément à authentifier avant d'être un élément d'orientation. L'authentification porte sur le support, la langue, la cohérence avec les scènes, et l'origine.",
                     "documented": "L'Associated Press documente que des responsables de l'enquête ont été trompés et ont orienté les recherches en conséquence.",
                     "hypothetical": "Ce qu'aurait produit une authentification immédiate.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir que l'auteur réel avait déjà été entendu plusieurs fois sans être identifié.",
                     "answer_note": "La réponse attendue est B. Les options A et C présupposent l'authenticité de la communication."},
              "en": {"whatInvestigatorsKnew": "Letters then a tape claiming the offences reached the police; they came from another man.",
                     "whatExpertsProposed": "A claiming communication is an element to authenticate before being an element of orientation. Authentication concerns the medium, the language, consistency with the scenes, and the origin.",
                     "documented": "The Associated Press documents that senior officers were misled and steered searches accordingly.",
                     "hypothetical": "What immediate authentication would have produced.",
                     "whatYouCouldNotKnow": "You could not know that the actual author had already been interviewed several times without being identified.",
                     "answer_note": "The expected answer is B. Options A and C presuppose the authenticity of the communication."}},
             "ap-death"),
    question("1", 400, "investigation",
             "Un volume massif d'informations est collecté, avec un système de fiches. Qu'est-ce qui rend ce système inefficace ?",
             "A massive volume of information is collected, with a card system. What makes that system ineffective?",
             [("a", "Le nombre de fiches", "The number of cards"),
              ("b", "L'absence de croisement entre les fiches", "The absence of cross-referencing between cards"),
              ("c", "Le manque de personnel", "The lack of staff"),
              ("d", "La nature des informations", "The nature of the information")],
             {"fr": {"whatInvestigatorsKnew": "La police était submergée par le volume d'informations ; le système de fiches créé était mal croisé, ce qui a égaré des faits clés.",
                     "whatExpertsProposed": "Un système d'information d'enquête vaut par sa capacité de rapprochement, non par sa capacité de stockage. Des détails physiques existaient et n'ont pas été rapprochés.",
                     "documented": "L'Associated Press documente le mauvais croisement et l'absence de signalement de détails pertinents.",
                     "hypothetical": "Ce qu'un croisement systématique aurait produit, et à quelle date.",
                     "whatYouCouldNotKnow": "Vous ne pouvez pas connaître le contenu détaillé de chaque fiche.",
                     "answer_note": "La réponse attendue est B. C'est un problème d'organisation de l'information, pas de volume."},
              "en": {"whatInvestigatorsKnew": "Police were overwhelmed by the volume of information; the card system created was poorly cross-referenced, which misplaced key facts.",
                     "whatExpertsProposed": "An investigative information system is worth its capacity for linkage, not its capacity for storage. Physical details existed and were not linked.",
                     "documented": "The Associated Press documents the poor cross-referencing and the failure to flag relevant details.",
                     "hypothetical": "What systematic cross-referencing would have produced, and on what date.",
                     "whatYouCouldNotKnow": "You cannot know the detailed content of each card.",
                     "answer_note": "The expected answer is B. It is an information organisation problem, not a volume one."}},
             "ap-death"),
]

CASE = {
    "id": CASE_ID,
    "title": txt("Peter Sutcliffe — Yorkshire, 1975-1981", "Peter Sutcliffe — Yorkshire, 1975-1981"),
    "subtitle": txt("Treize femmes tuées, sept tentatives, neuf entretiens sans identification, et un canular qui a "
                    "orienté l'enquête.",
                    "Thirteen women killed, seven attempts, nine interviews without identification, and a hoax that "
                    "steered the investigation."),
    "country": "GB", "region": "Yorkshire / Angleterre du Nord", "city": "Leeds",
    "year_start": 1975, "year_end": 2020, "period_label": txt("1975 – 2020", "1975 – 2020"),
    "status": "RESOLVED", "type": "serial",
    "tags": ["serial_killer", "uk", "hoax", "information_management", "media_naming", "whole_life_tariff"],
    "tier": "PREMIUM", "editorial": "yanis", "published_at": "2026-09-24", "sensitive": True,
    "triggers": txt("Meurtres de treize femmes ; débats sur la catégorisation des victimes ; diagnostic "
                    "psychiatrique évoqué.",
                    "Murders of thirteen women; debates on the categorisation of victims; psychiatric diagnosis "
                    "mentioned."),
    "lat": 53.8, "lon": -1.6, "cover": "cover-yorkshire",
    "stats": {"victims_documented": 13, "attempts_documented": 7, "interviews": 9, "duration_years": 45},
    "summary": txt(
        "Entre le 30 octobre 1975 et le 17 novembre 1980, treize femmes sont tuées dans le Yorkshire et le nord-ouest "
        "de l'Angleterre ; sept autres survivent à des tentatives. L'enquête, l'une des plus vastes de l'histoire "
        "britannique, est orientée par des lettres et une cassette revendicatives qui émanent en réalité d'un autre "
        "homme et mettent en avant un accent du Wearside. Le système de fiches mis en place est mal croisé et égare "
        "des éléments clés. L'auteur est entendu neuf fois sans être identifié. Il est arrêté le 2 janvier 1981 à "
        "Sheffield lors d'un contrôle routier sans lien avec l'affaire. Le 22 mai 1981, l'Old Bailey le déclare "
        "coupable de treize meurtres et de sept tentatives, après avoir écarté la défense de responsabilité atténuée "
        "fondée sur des voix qu'il attribuait à Dieu ; vingt peines de réclusion à perpétuité concurrentes sont "
        "prononcées. En 2010, la High Court confirme le caractère incompressible de la peine. Il meurt en détention "
        "le 13 novembre 2020.",
        "Between 30 October 1975 and 17 November 1980, thirteen women are killed in Yorkshire and north-west England; "
        "seven others survive attempts. The investigation, one of the largest in British history, is steered by "
        "claiming letters and a tape that in fact come from another man and put forward a Wearside accent. The card "
        "system set up is poorly cross-referenced and misplaces key elements. The author is interviewed nine times "
        "without being identified. He is arrested on 2 January 1981 in Sheffield during a traffic stop unrelated to "
        "the case. On 22 May 1981, the Old Bailey finds him guilty of thirteen murders and seven attempts, having "
        "rejected the diminished responsibility defence based on voices he attributed to God; twenty concurrent life "
        "terms are pronounced. In 2010, the High Court confirms the whole life character of the sentence. He dies in "
        "custody on 13 November 2020."),
    "sources": SOURCES, "victims": VICTIMS, "memorial": MEMORIAL, "timeline": TIMELINE, "locations": LOCATIONS,
    "evidence": EVIDENCE, "investigation": INVESTIGATION, "psychology": PSYCHOLOGY, "victimology": VICTIMOLOGY,
    "court": COURT, "experts": EXPERTS, "experts_agreement": EXPERTS_AGREEMENT,
    "experts_disagreement": EXPERTS_DISAGREEMENT, "experts_uncertain": EXPERTS_UNCERTAIN,
    "counterfactuals": COUNTERFACTUALS, "lessons": LESSONS, "unknowns": UNKNOWNS, "sections": SECTIONS,
    "episodes": EPISODES, "questions": QUESTIONS,
}
