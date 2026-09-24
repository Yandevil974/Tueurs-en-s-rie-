"""
DOSSIER 02 — GUY GEORGES, DIT « LE TUEUR DE L'EST PARISIEN » (France, Paris, 1991-2001)

Sources publiques vérifiées le 2026-09-24. Aucune donnée inventée.
"""
from ..case_template import block, counterfactual, fact, item, question, source, txt

CASE_ID = "guy-georges"
V = "2026-09-24"

SOURCES = [
    source("sudouest-parcours", CASE_ID,
           "Tueurs en série : Guy Georges, le « tueur de l'est parisien »",
           "Serial killers: Guy Georges, the 'killer of eastern Paris'",
           "Sud Ouest", "Redaction", "https://www.sudouest.fr/faits-divers/grandes-affaires/10-affaires-qui-ont-marque-la-france/guy-georges-le-parcours-du-tueur-de-l-est-parisien-3647213.php",
           "2024-09-26", "press", "CONFIRMED", V,
           "Rétrospective détaillée : faits antérieurs, condamnations, identification ADN, procès de 2001.",
           "Detailed retrospective: earlier facts, convictions, DNA identification, 2001 trial."),
    source("bfmtv-que-devient", CASE_ID,
           "Que devient Guy Georges, le « tueur de l'est parisien » ?",
           "What became of Guy Georges, the 'killer of eastern Paris'?",
           "BFMTV (RMC Crime)", "Redaction", "https://rmccrime.bfmtv.com/affaires-criminelles/france/que-devient-guy-georges-le-tueur-de-l-est-parisien_AN-202304290028.html",
           "2023-04-29", "press", "CONFIRMED", V,
           "Situation pénale après la période de sûreté de 22 ans.",
           "Penal situation after the 22-year minimum term."),
    source("francetv-au-bout-de-l-enquete", CASE_ID,
           "L'affaire Guy Georges — Au bout de l'enquête, la fin du crime parfait ?",
           "The Guy Georges case — Au bout de l'enquête",
           "France Télévisions", "Redaction", "https://www.france.tv/france-2/au-bout-de-l-enquete-la-fin-du-crime-parfait/6501398-l-affaire-guy-georges-1-2.html",
           "2024-09-28", "broadcast", "CONFIRMED", V,
           "Mention de la création du FNAEG à la suite de cette affaire.",
           "Mentions the creation of the FNAEG following this case."),
    source("parismatch-archives", CASE_ID,
           "Dans les archives de Match — Guy Georges, quand le serial killer rôdait dans Paris",
           "In the Match archives — Guy Georges, when the serial killer roamed Paris",
           "Paris Match", "Redaction", "https://www.parismatch.com/actu/societe/dans-les-archives-de-match-guy-georges-quand-le-serial-killer-rodait-dans-paris-140271",
           "2023-06-05", "press", "PROBABLE", V,
           "Archives de presse : dates et adresses précises, éléments d'enquête et « ratages » ; à recouper avec le dossier judiciaire.",
           "Press archives: precise dates and addresses, investigation elements and 'misses'; to be cross-checked with the judicial file."),
    source("bfmtv-fea", CASE_ID,
           "Faites entrer l'accusé : Guy Georges, le tueur de l'est parisien",
           "Faites entrer l'accusé: Guy Georges, the killer of eastern Paris",
           "RMC Story / BFMTV", "Redaction", "https://rmccrime.bfmtv.com/faites-entrer-l-accuse/faites-entrer-l-accuse-guy-georges-le-tueur-de-l-est-parisien_AN-202306110027.html",
           "2023-06-11", "broadcast", "PROBABLE", V,
           "Récit de l'identification par trace ADN commune et du procès.",
           "Account of the identification through a common DNA trace and of the trial."),
]

# Victims: names and ages as reported by the press; dates where several sources converge.
VICTIMS = [

    {"order": 0, "first_name": "Pascale", "last_name": "Escarfail", "age": "19", "source": "parismatch-archives",
     "reliability": "CONFIRMED",
     "life": {"fr": {"headline": "Pascale Escarfail", "items": [
         {"label": "Âge", "text": "19 ans selon la liste des victimes publiée par la presse ; certains articles indiquent 24 ans et des études de droit. L'écart est signalé, non tranché."},
         {"label": "Lieu de vie", "text": "Paris."}],
         "note": "Les sources publiques consultées divergent sur l'âge et la situation de Pascale Escarfail. Conformément à la charte, l'écart est affiché et la donnée reste au niveau PROBABLE."},
        "en": {"headline": "Pascale Escarfail", "items": [
         {"label": "Age", "text": "19 according to the victim list published by the press; some articles state 24 and law studies. The discrepancy is flagged, not resolved."},
         {"label": "Place of life", "text": "Paris."}],
         "note": "The public sources consulted diverge on the age and situation of Pascale Escarfail. Per the charter, the discrepancy is displayed and the data remains at PROBABLE level."}},
     "disappearance": {"fr": {"items": [
         {"label": "Date", "text": "Janvier 1991 (le 16 janvier 1991 selon Paris Match)."},
         {"label": "Circonstances", "text": "Tuée à son domicile parisien."}]},
        "en": {"items": [
         {"label": "Date", "text": "January 1991 (16 January 1991 according to Paris Match)."},
         {"label": "Circumstances", "text": "Killed at her Paris home."}]}}},


    {"order": 1, "first_name": "Catherine", "last_name": "Rocher", "age": "27", "source": "sudouest-parcours",
     "reliability": "CONFIRMED",
     "life": {"fr": {"headline": "Catherine Rocher", "items": [{"label": "Âge", "text": "27 ans."}, {"label": "Lieu de vie", "text": "Paris, secteur est."}]},
             "en": {"headline": "Catherine Rocher", "items": [{"label": "Age", "text": "27."}, {"label": "Place of life", "text": "Paris, eastern sector."}]}},
     "disappearance": {"fr": {"items": [{"label": "Circonstances", "text": "Viol et meurtre, à Paris, dans la série jugée en 2001."}]},
                       "en": {"items": [{"label": "Circumstances", "text": "Rape and murder, in Paris, in the series tried in 2001."}]}}},


    {"order": 2, "first_name": "Elsa", "last_name": "Benady", "age": "22", "source": "sudouest-parcours",
     "reliability": "CONFIRMED",
     "life": {"fr": {"headline": "Elsa Benady", "items": [{"label": "Âge", "text": "22 ans."}, {"label": "Lieu de vie", "text": "Paris."}]},
             "en": {"headline": "Elsa Benady", "items": [{"label": "Age", "text": "22."}, {"label": "Place of life", "text": "Paris."}]}},
     "disappearance": {"fr": {"items": [{"label": "Circonstances", "text": "Viol et meurtre, à Paris."}]},
                       "en": {"items": [{"label": "Circonstances", "text": "Rape and murder, in Paris."}]}}},


    {"order": 3, "first_name": "Agnès", "last_name": "Nijkamp", "age": "32", "source": "sudouest-parcours",
     "reliability": "CONFIRMED",
     "life": {"fr": {"headline": "Agnès Nijkamp", "items": [
         {"label": "Âge", "text": "32 ans (33 ans selon d'autres articles)."},
         {"label": "Profession", "text": "Architecte d'intérieur / décoratrice, de nationalité néerlandaise."},
         {"label": "Lieu de vie", "text": "Paris, près de la Bastille."}]},
        "en": {"headline": "Agnès Nijkamp", "items": [
         {"label": "Age", "text": "32 (33 in other articles)."},
         {"label": "Occupation", "text": "Interior architect / decorator, Dutch national."},
         {"label": "Place of life", "text": "Paris, near the Bastille."}]}},
     "disappearance": {"fr": {"items": [
         {"label": "Date", "text": "Décembre 1994 (le 10 décembre 1994 selon Paris Match)."},
         {"label": "Élément d'enquête", "text": "De l'ADN a été découvert à son domicile ; c'est l'un des maillons du rapprochement ultérieur entre les affaires."}]},
        "en": {"items": [
         {"label": "Date", "text": "December 1994 (10 December 1994 according to Paris Match)."},
         {"label": "Investigative element", "text": "DNA was discovered at her home; it is one of the links in the later connection between the cases."}]}}},


    {"order": 4, "first_name": "Hélène", "last_name": "Frinking", "age": "27", "source": "parismatch-archives",
     "reliability": "CONFIRMED",
     "life": {"fr": {"headline": "Hélène Frinking", "items": [
         {"label": "Âge", "text": "27 ans."},
         {"label": "Études", "text": "Étudiante ; son père est originaire des Pays-Bas."},
         {"label": "Lieu de vie", "text": "Paris, faubourg Saint-Martin (10e)."}]},
        "en": {"headline": "Hélène Frinking", "items": [
         {"label": "Age", "text": "27."},
         {"label": "Studies", "text": "Student; her father was from the Netherlands."},
         {"label": "Place of life", "text": "Paris, faubourg Saint-Martin (10th)."}]}},
     "disappearance": {"fr": {"items": [{"label": "Date", "text": "8 juillet 1995 (Paris Match)."}, {"label": "Circonstances", "text": "Viol et meurtre à son domicile."}]},
                       "en": {"items": [{"label": "Date", "text": "8 July 1995 (Paris Match)."}, {"label": "Circumstances", "text": "Rape and murder at her home."}]}}},


    {"order": 5, "first_name": "Magalie", "last_name": "Sirotti", "age": "19", "source": "sudouest-parcours",
     "reliability": "CONFIRMED",
     "life": {"fr": {"headline": "Magalie Sirotti", "items": [{"label": "Âge", "text": "19 ans."}, {"label": "Lieu de vie", "text": "Paris."}]},
             "en": {"headline": "Magalie Sirotti", "items": [{"label": "Age", "text": "19."}, {"label": "Place of life", "text": "Paris."}]}},
     "disappearance": {"fr": {"items": [{"label": "Circonstances", "text": "Viol et meurtre, à Paris."}]},
                       "en": {"items": [{"label": "Circonstances", "text": "Rape and murder, in Paris."}]}}},


    {"order": 6, "first_name": "Estelle", "last_name": "Magd", "age": "25", "source": "bfmtv-fea",
     "reliability": "CONFIRMED",
     "life": {"fr": {"headline": "Estelle Magd", "items": [{"label": "Âge", "text": "25 ans."}, {"label": "Lieu de vie", "text": "Paris, 11e arrondissement."}]},
             "en": {"headline": "Estelle Magd", "items": [{"label": "Age", "text": "25."}, {"label": "Place of life", "text": "Paris, 11th arrondissement."}]}},
     "disappearance": {"fr": {"items": [
         {"label": "Date", "text": "15-16 novembre 1997."},
         {"label": "Circonstances", "text": "Dernier meurtre de la série : au moment des faits, les enquêteurs avaient établi un lien entre les crimes et identifiaient une trace ADN commune."}]},
        "en": {"items": [
         {"label": "Date", "text": "15-16 November 1997."},
         {"label": "Circumstances", "text": "Last murder of the series: at the time, investigators had established a link between the crimes and identified a common DNA trace."}]}}},
]

SURVIVORS = [
    item("Pascale Nix, agressée en 1984, parvient à s'échapper. Guy Georges est alors condamné à dix ans de prison.",
         "Pascale Nix, attacked in 1984, managed to escape. Guy Georges was then sentenced to ten years in prison.",
         "CONFIRMED", "sudouest-parcours", "Survivante", "Survivor"),
    item("Élisabeth Ortega, 23 ans, est agressée mais parvient à s'enfuir ; une empreinte présentant un signe "
         "distinctif (un « pied égyptien ») est relevée.",
         "Élisabeth Ortega, 23, was attacked but managed to flee; a footprint with a distinctive feature (an "
         "'Egyptian foot') was recorded.",
         "CONFIRMED", "sudouest-parcours", "Survivante", "Survivor"),
    item("Mélanie Bacou échappe à l'agresseur, qui fuit en laissant tomber son portefeuille. Pour cette agression, "
         "Guy Georges est condamné à 30 mois de prison.",
         "Mélanie Bacou escaped the attacker, who fled dropping his wallet. For this attack, Guy Georges was "
         "sentenced to 30 months in prison.",
         "CONFIRMED", "sudouest-parcours", "Survivante", "Survivor"),
]

MEMORIAL = {
    "title": txt("Sept femmes, Paris 1991-1997", "Seven women, Paris 1991-1997"),
    "biography": txt(
        "Pascale Escarfail, Catherine Rocher, Elsa Benady, Agnès Nijkamp, Hélène Frinking, Magalie Sirotti et "
        "Estelle Magd ont été violées et tuées à Paris entre 1991 et 1997. Trois autres femmes ont survivi à des "
        "agressions : l'une en 1984, deux autres pendant la période de la série. Ce sont leurs échappées, leurs "
        "témoignages et les traces laissées dans leurs affaires qui ont fini par produire un rapprochement.",
        "Pascale Escarfail, Catherine Rocher, Elsa Benady, Agnès Nijkamp, Hélène Frinking, Magalie Sirotti and "
        "Estelle Magd were raped and killed in Paris between 1991 and 1997. Three other women survived attacks: one "
        "in 1984, two others during the series. It was their escapes, their testimony and the traces left in their "
        "cases that eventually produced a linkage.",
    ),
    "testimony": txt(
        "Au procès de 2001, les familles des victimes ont pesé sur le déroulement des audiences : les avocats de la "
        "défense ont poussé l'accusé à s'exprimer devant elles. Cette dynamique d'audience est documentée par la "
        "presse ayant suivi les trois semaines de procès.",
        "At the 2001 trial, the victims' families weighed on the conduct of the hearings: defence lawyers pushed the "
        "accused to speak before them. This hearing dynamic is documented by the press that followed the three weeks "
        "of trial.",
    ),
    "memory": txt(
        "Cette affaire a changé le droit français : l'identification par trace ADN a conduit à la création du FNAEG, "
        "le fichier national automatisé des empreintes génétiques. Derrière cet acquis technique, sept femmes ont "
        "perdu la vie et trois autres ont survécu.",
        "This case changed French law: identification by DNA trace led to the creation of the FNAEG, the national "
        "automated database of genetic fingerprints. Behind that technical gain, seven women lost their lives and "
        "three others survived.",
    ),
}

TIMELINE = [
    fact("Guy Georges est condamné à dix ans de prison après l'agression de Pascale Nix, qui parvient à s'échapper.",
         "Guy Georges is sentenced to ten years in prison after the attack on Pascale Nix, who manages to escape.",
         "CONFIRMED", "sudouest-parcours", "Premier fait jugé", "First offence tried", "1984"),
    fact("Condamné à cinq ans pour attentats à la pudeur sur des mineures placées à la DDASS.",
         "Sentenced to five years for indecent assaults on minors in state care.",
         "PROBABLE", "sudouest-parcours", "Autre condamnation", "Another conviction", "1983"),
    fact("Alors qu'il exécute sa peine à la centrale de Caen, il bénéficie d'une permission et prend le train pour "
        "Paris. Le 16 janvier 1991, Pascale Escarfail est violée et tuée dans son studio parisien.",
        "While serving his sentence at Caen prison, he is granted leave and takes the train to Paris. On 16 January "
        "1991, Pascale Escarfail is raped and killed in her Paris studio.",
        "CONFIRMED", "parismatch-archives", "Premier meurtre de la série", "First murder of the series", "1991-01-16"),
    fact("Catherine Rocher, Elsa Benady et Magalie Sirotti sont tuées à Paris dans les années suivantes.",
         "Catherine Rocher, Elsa Benady and Magalie Sirotti are killed in Paris in the following years.",
         "CONFIRMED", "sudouest-parcours", "Série", "Series", "1991-1997"),
    fact("Agnès Nijkamp, 32 ans, architecte d'intérieur néerlandaise, est retrouvée morte près de la Bastille. De "
        "l'ADN est découvert à son domicile.",
         "Agnès Nijkamp, 32, a Dutch interior architect, is found dead near the Bastille. DNA is discovered at her home.",
         "CONFIRMED", "sudouest-parcours", "Trace biologique", "Biological trace", "1994-12-10"),
    fact("Hélène Frinking, 27 ans, étudiante, est tuée dans le 10e arrondissement.",
         "Hélène Frinking, 27, a student, is killed in the 10th arrondissement.",
         "CONFIRMED", "parismatch-archives", "Cinquième meurtre", "Fifth murder", "1995-07-08"),
    fact("Estelle Magd, 25 ans, est tuée à son domicile du 11e arrondissement. C'est le dernier meurtre de la série.",
         "Estelle Magd, 25, is killed at her home in the 11th arrondissement. It is the last murder of the series.",
         "CONFIRMED", "bfmtv-fea", "Dernier meurtre", "Last murder", "1997-11-15"),
    fact("Le laboratoire du docteur Olivier Pascal identifie un profil génétique commun sur plusieurs scènes. Deux "
        "jours plus tard, Guy Georges est interpellé.",
         "Doctor Olivier Pascal's laboratory identifies a common genetic profile across several scenes. Two days "
        "later, Guy Georges is arrested.",
        "CONFIRMED", "sudouest-parcours", "Identification et arrestation", "Identification and arrest", "1998-01"),
    fact("Création du FNAEG, le fichier national automatisé des empreintes génétiques, dans le prolongement de cette "
        "affaire.",
         "Creation of the FNAEG, the national automated database of genetic fingerprints, in the wake of this case.",
         "CONFIRMED", "francetv-au-bout-de-l-enquete", "Conséquence législative", "Legislative consequence", "1998-06-17"),
    fact("Procès devant la cour d'assises de Paris, ouvert le 19 mars 2001. L'accusé nie les meurtres. Le 5 avril "
        "2001, il est condamné à la réclusion criminelle à perpétuité assortie d'une période de sûreté de 22 ans.",
         "Trial before the Paris assize court, opened on 19 March 2001. The accused denies the murders. On 5 April "
         "2001, he is sentenced to life imprisonment with a 22-year minimum term.",
         "CONFIRMED", "sudouest-parcours", "Procès et verdict", "Trial and verdict", "2001-04-05"),
    fact("À l'issue de la période de sûreté, il peut formuler des demandes à compter de mars 2020. Il reste incarcéré "
        "à la maison centrale d'Ensisheim (Haut-Rhin).",
         "At the end of the minimum term, he may file requests from March 2020. He remains imprisoned at Ensisheim "
         "central prison (Haut-Rhin).",
         "CONFIRMED", "bfmtv-que-devient", "Après", "Afterwards", "2023"),
]

LOCATIONS = [
    {"kind": "city", "names": txt("Paris — est de la capitale", "Paris — east of the capital"),
     "city": "Paris", "region": "Île-de-France", "country": "FR", "lat": 48.86, "lon": 2.37,
     "precision": "city", "date": "1991-1997",
     "note": txt("Secteur des faits : 10e, 11e, 12e, 14e arrondissements selon les affaires. Aucune adresse de "
                "domicile privé n'est affichée.",
                "Area of the facts: 10th, 11th, 12th, 14th arrondissements depending on the case. No private home "
                "address is displayed."),
     "reliability": "CONFIRMED", "source": "parismatch-archives"},
    {"kind": "court", "names": txt("Cour d'assises de Paris", "Paris Assize Court"),
     "city": "Paris", "region": "Île-de-France", "country": "FR", "lat": 48.855, "lon": 2.345,
     "precision": "city", "date": "2001-04-05", "note": txt("Procès du 19 mars au 5 avril 2001.", "Trial from 19 March to 5 April 2001."),
     "reliability": "CONFIRMED", "source": "sudouest-parcours"},
    {"kind": "city", "names": txt("Maison centrale d'Ensisheim", "Ensisheim central prison"),
     "city": "Ensisheim", "region": "Haut-Rhin", "country": "FR", "lat": 47.87, "lon": 7.35,
     "precision": "city", "date": "2023", "note": txt("Lieu de détention indiqué par la presse en 2023.", "Place of detention reported by the press in 2023."),
     "reliability": "CONFIRMED", "source": "bfmtv-que-devient"},
]

EVIDENCE = [
    {"kind": "dna", "weight": "decisive", "reliability": "CONFIRMED", "source": "sudouest-parcours",
     "title": txt("Trace génétique commune", "Common genetic trace"),
     "description": txt(
         "Une même trace ADN est identifiée sur plusieurs scènes. Le laboratoire du docteur Olivier Pascal parvient à "
         "une identification, décrite par la presse comme obtenue presque par hasard, deux jours avant "
         "l'interpellation.",
         "The same DNA trace is identified on several scenes. Doctor Olivier Pascal's laboratory reaches an "
         "identification, described by the press as obtained almost by chance, two days before the arrest.")},
    {"kind": "trace", "weight": "documented", "reliability": "CONFIRMED", "source": "sudouest-parcours",
     "title": txt("Empreinte et signe distinctif", "Footprint and distinctive feature"),
     "description": txt(
         "Lors de l'agression d'Élisabeth Ortega, une empreinte marquée d'un signe distinctif est relevée : un « pied "
         "égyptien », lorsque le second orteil est plus long que le pouce.",
         "During the attack on Élisabeth Ortega, a footprint with a distinctive feature was recorded: an 'Egyptian "
         "foot', when the second toe is longer than the big toe.")},
    {"kind": "physical", "weight": "documented", "reliability": "CONFIRMED", "source": "sudouest-parcours",
     "title": txt("Un portefeuille perdu", "A lost wallet"),
     "description": txt(
         "Lors de l'agression de Mélanie Bacou, l'auteur prend la fuite et laisse tomber son portefeuille. Cet objet "
         "a conduit à une condamnation à 30 mois de prison.",
         "During the attack on Mélanie Bacou, the author fled and dropped his wallet. That item led to a 30-month "
         "prison sentence.")},
    {"kind": "physical", "weight": "documented", "reliability": "PROBABLE", "source": "sudouest-parcours",
     "title": txt("Un mode opératoire constant", "A constant method"),
     "description": txt(
         "Les victimes sont attachées et bâillonnées à l'aide de sparadrap ; les rapprochements entre affaires ont "
         "reposé sur la constance de ce mode opératoire, puis sur la trace biologique.",
         "Victims were tied and gagged with adhesive tape; the links between cases rested on the constancy of this "
         "method, then on the biological trace.")},
]

INVESTIGATION = {
    "steps": [
        {"n": 1, "date": "1991-01-16", "title": txt("Un premier corps", "A first body"),
         "body": txt("Pascale Escarfail est violée et tuée dans son studio parisien. Rien ne relie encore ce crime à "
                     "d'autres affaires.",
                     "Pascale Escarfail is raped and killed in her Paris studio. Nothing yet links this crime to "
                     "other cases."),
         "reliability": "CONFIRMED", "source": "parismatch-archives", "premium": False},
        {"n": 2, "date": "1991-1994", "title": txt("Des scènes qui se ressemblent", "Scenes that look alike"),
         "body": txt("D'autres femmes sont tuées dans l'est parisien. Le mode opératoire est constant : intrusion au "
                     "domicile, victime attachée et bâillonnée au sparadrap, viol, homicide à l'arme blanche.",
                     "Other women are killed in eastern Paris. The method is constant: intrusion into the home, victim "
                     "tied and gagged with adhesive tape, rape, homicide with a blade."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": False},
        {"n": 3, "date": "1994-12-10", "title": txt("Une trace biologique", "A biological trace"),
         "body": txt("De l'ADN est découvert au domicile d'Agnès Nijkamp. À cette date, le rapprochement avec les "
                     "autres affaires n'est pas établi.",
                     "DNA is discovered at Agnès Nijkamp's home. At that date, the link with the other cases is not "
                     "established."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": True},
        {"n": 4, "date": "1995", "title": txt("Des survivantes", "Survivors"),
         "body": txt("Deux agressions n'aboutissent pas : Élisabeth Ortega s'enfuit, une empreinte à signe distinctif "
                     "est relevée ; Mélanie Bacou échappe à l'agresseur, qui abandonne son portefeuille. Ce dernier "
                     "fait donne lieu à une condamnation à 30 mois.",
                     "Two attacks do not succeed: Élisabeth Ortega escapes and a footprint with a distinctive feature "
                     "is recorded; Mélanie Bacou escapes the attacker, who abandons his wallet. The latter leads to a "
                     "30-month sentence."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": False},
        {"n": 5, "date": "1995-1997", "title": txt("Le ratage documenté par la presse", "The miss documented by the press"),
         "body": txt("Paris Match relève qu'aucune comparaison similaire n'est effectuée entre les traces découvertes "
                     "chez Agnès Nijkamp (1994) et celles relevées lors de l'agression d'Élisabeth O. (1995). C'est un "
                     "cloisonnement entre dossiers, pas une absence de traces.",
                     "Paris Match notes that no similar comparison was made between the traces discovered at Agnès "
                     "Nijkamp's (1994) and those recorded during the attack on Élisabeth O. (1995). This is "
                     "compartmentalisation between files, not an absence of traces."),
         "reliability": "PROBABLE", "source": "parismatch-archives", "premium": True},
        {"n": 6, "date": "1997-11-15", "title": txt("Un dernier meurtre", "A last murder"),
         "body": txt("Estelle Magd, 25 ans, est tuée. À ce moment, les enquêteurs ont établi un lien entre les "
                     "crimes et identifient une trace ADN commune sur les lieux.",
                     "Estelle Magd, 25, is killed. At that point, investigators have established a link between the "
                     "crimes and identify a common DNA trace at the scenes."),
         "reliability": "CONFIRMED", "source": "bfmtv-fea", "premium": False},
        {"n": 7, "date": "1998-01", "title": txt("L'identification", "The identification"),
         "body": txt("Le laboratoire du docteur Olivier Pascal identifie un profil, décrit comme obtenu presque par "
                     "hasard. Deux jours plus tard, Guy Georges est arrêté.",
                     "Doctor Olivier Pascal's laboratory identifies a profile, described as obtained almost by chance. "
                     "Two days later, Guy Georges is arrested."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": True},
        {"n": 8, "date": "2001-04-05", "title": txt("Le verdict", "The verdict"),
         "body": txt("Après trois semaines d'audience ouvertes le 19 mars 2001, la cour d'assises de Paris condamne "
                     "Guy Georges à la réclusion criminelle à perpétuité, assortie d'une période de sûreté de 22 ans.",
                     "After three weeks of hearings opened on 19 March 2001, the Paris assize court sentences Guy "
                     "Georges to life imprisonment with a 22-year minimum term."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": False},
    ],
    "reality": txt(
        "L'affaire s'est résolue par la biologie, pas par le profil. Le rapprochement des scènes est intervenu tard, "
        "et la presse a documenté un défaut de comparaison entre deux jeux de traces. L'identification finale a "
        "produit une conséquence structurelle : la création du FNAEG.",
        "The case was solved by biology, not by profiling. The linkage of scenes came late, and the press documented "
        "a failure to compare two sets of traces. The final identification produced a structural consequence: the "
        "creation of the FNAEG."),
    "errors": [
        item("Des traces biologiques existaient sur plusieurs scènes avant le rapprochement ; la presse documente une "
             "absence de comparaison entre deux d'entre elles.",
             "Biological traces existed at several scenes before the linkage; the press documents an absence of "
             "comparison between two of them.",
             "PROBABLE", "parismatch-archives", "Cloisonnement", "Compartmentalisation"),
        item("Des permissions de sortie ont été accordées pendant l'exécution de peines antérieures ; l'une d'elles "
             "précède immédiatement le premier meurtre de la série.",
             "Leave was granted during the execution of earlier sentences; one of them immediately precedes the first "
             "murder of the series.",
             "CONFIRMED", "parismatch-archives", "Exécution des peines", "Sentence enforcement"),
    ],
    "cold_case": {
        "what_we_know": [
            item("Sept meurtres jugés en 2001, commis à Paris entre 1991 et 1997.",
                 "Seven murders tried in 2001, committed in Paris between 1991 and 1997.", "CONFIRMED", "sudouest-parcours"),
            item("Identification par trace ADN commune, arrestation en janvier 1998.",
                 "Identification through a common DNA trace, arrest in January 1998.", "CONFIRMED", "sudouest-parcours"),
        ],
        "what_is_probable": [
            item("Le rapprochement des scènes aurait pu intervenir plus tôt si les traces avaient été comparées "
                 "systématiquement.",
                 "The linkage of scenes might have occurred earlier had the traces been systematically compared.",
                 "PROBABLE", "parismatch-archives"),
        ],
        "what_is_disputed": [
            item("La qualification d'obtention « presque par hasard » de l'identification : c'est une formulation de "
                 "presse, pas une conclusion d'expertise.",
                 "The description of the identification as obtained 'almost by chance': this is press wording, not an "
                 "expert conclusion.", "DISPUTED", "sudouest-parcours"),
        ],
        "what_is_unknown": [
            item("L'âge et la situation exacte de Pascale Escarfail : les sources publiques divergent (19 ans ou 24 ans).",
                 "The exact age and situation of Pascale Escarfail: public sources diverge (19 or 24).",
                 "UNKNOWN", "parismatch-archives"),
        ],
        "latest_progress": [
            item("2023 : toujours incarcéré, éligible à formuler des demandes depuis mars 2020.",
                 "2023: still imprisoned, eligible to file requests since March 2020.", "CONFIRMED", "bfmtv-que-devient"),
        ],
        "leads": [], "limits": [],
    },
}

PSYCHOLOGY = {
    "disclaimer": txt("Aucun diagnostic n'est posé. Les éléments ci-dessous distinguent fait, hypothèse, analyse et inconnu.",
                      "No diagnosis is made. The elements below distinguish fact, hypothesis, analysis and unknown."),
    "blocks": [
        block("fact", "Un parcours institutionnel précoce", "An early institutional history",
              "Abandonné par ses parents, il a été recueilli par une famille en Anjou, puis est passé de foyer en "
              "foyer. Ces éléments biographiques sont rapportés par la presse à partir du dossier.",
              "Abandoned by his parents, he was taken in by a family in Anjou, then moved from one institution to "
              "another. These biographical elements are reported by the press from the file.",
              "PROBABLE", "angers-maville"),
        block("behaviour", "Un comportement de prédation et de répétition", "A behaviour of predation and repetition",
              "Le mode opératoire est stable sur plusieurs années : intrusion au domicile, contrainte par sparadrap, "
              "viol, homicide. La stabilité est un fait de dossier ; son interprétation relève de l'analyse.",
              "The method is stable over several years: intrusion into the home, restraint with adhesive tape, rape, "
              "homicide. The stability is a case fact; its interpretation belongs to analysis.",
              "CONFIRMED", "sudouest-parcours"),
        block("behaviour", "L'exploitation des interstices pénaux", "Exploiting the gaps in the penal system",
              "Une permission de sortie précède le premier meurtre de la série ; des condamnations pour agressions "
              "n'ont pas interrompu la série. Ce constat est documenté, il ne constitue pas une analyse psychologique.",
              "A period of leave precedes the first murder of the series; convictions for assaults did not interrupt "
              "the series. This finding is documented; it is not a psychological analysis.",
              "CONFIRMED", "parismatch-archives"),
        block("unknown", "Ce que l'audience n'a pas établi", "What the hearing did not establish",
              "Devant la cour d'assises, l'accusé a nié les meurtres. Les motivations internes ne sont donc pas "
              "documentées par un récit vérifiable.",
              "Before the assize court, the accused denied the murders. Internal motivations are therefore not "
              "documented by a verifiable account.",
              "UNKNOWN", "bfmtv-fea"),
    ],
}

VICTIMOLOGY = {
    "ethics_note": txt("Aucune caractéristique des victimes n'explique moralement les crimes.",
                       "No characteristic of the victims morally explains the crimes."),
    "blocks": [
        block("context", "Des femmes jeunes, vivant seules à Paris", "Young women living alone in Paris",
              "Les victimes étaient des femmes âgées de 19 à 32 ans, domiciliées à Paris, tuées dans leur logement ou "
              "à proximité. Deux d'entre elles étaient de nationalité ou d'origine néerlandaise.",
              "The victims were women aged 19 to 32, living in Paris, killed in or near their homes. Two of them were "
              "Dutch nationals or of Dutch origin.",
              "CONFIRMED", "sudouest-parcours"),
        block("analysis", "Ce que cela a produit en enquête", "What this produced in the investigation",
              "La récurrence d'un lieu (le domicile), d'une tranche d'âge et d'un secteur géographique a permis le "
              "rapprochement, puis la constitution d'une série. C'est un usage descriptif de la victimologie : il "
              "éclaire le comportement de l'auteur, il ne dit rien de la valeur des personnes.",
              "The recurrence of a place (the home), an age range and a geographic sector allowed the linkage, then "
              "the constitution of a series. This is a descriptive use of victimology: it illuminates the author's "
              "behaviour; it says nothing about the worth of the persons.",
              "CONFIRMED", "sudouest-parcours"),
        block("vulnerability", "Une vulnérabilité situationnelle", "A situational vulnerability",
              "Vivre seule dans un logement accessible depuis les parties communes constitue un facteur "
              "situationnel documenté dans ce type de série. Il ne fonde aucune responsabilité de la victime.",
              "Living alone in a dwelling accessible from common areas is a situational factor documented in this "
              "type of series. It establishes no responsibility of the victim.",
              "PROBABLE", "parismatch-archives"),
    ],
}

COURT = {
    "jurisdiction": txt("France — cour d'assises de Paris", "France — Paris Assize Court"),
    "verdict": txt("Coupable de sept viols suivis de meurtres commis entre 1991 et 1997.",
                   "Guilty of seven rapes followed by murders committed between 1991 and 1997."),
    "sentence": {
        "label": txt("Réclusion criminelle à perpétuité, période de sûreté de 22 ans",
                     "Life imprisonment with a 22-year minimum term"),
        "pronounced": "2001-04-05",
        "requested": txt("Le procès s'est tenu du 19 mars au 5 avril 2001.", "The trial was held from 19 March to 5 April 2001."),
        "cumul": txt("Condamnations antérieures : 10 ans en 1984 après l'agression de Pascale Nix ; 5 ans ramenés à 4 "
                     "en appel pour attentats à la pudeur sur mineures ; 30 mois pour l'agression de Mélanie Bacou.",
                     "Earlier convictions: 10 years in 1984 after the attack on Pascale Nix; 5 years reduced to 4 on "
                     "appeal for indecent assaults on minors; 30 months for the attack on Mélanie Bacou."),
        "reasoning": txt("L'accusé a nié les meurtres à l'audience ; la cour a retenu la culpabilité au terme de trois "
                         "semaines de débats.",
                         "The accused denied the murders at the hearing; the court found guilt after three weeks of "
                         "deliberations."),
        "appeal": txt("À l'issue de la période de sûreté, il peut formuler des demandes de remise en liberté depuis "
                      "mars 2020. Il déclarait au procès qu'il ne sortirait jamais de prison.",
                      "At the end of the minimum term, he may file release requests from March 2020. He stated at "
                      "trial that he would never leave prison."),
        "reliability": "CONFIRMED", "source": "sudouest-parcours",
    },
    "consequences": [
        item("Création du FNAEG, fichier national automatisé des empreintes génétiques, dans le prolongement de "
             "l'affaire.",
             "Creation of the FNAEG, the national automated database of genetic fingerprints, in the wake of the case.",
             "CONFIRMED", "francetv-au-bout-de-l-enquete"),
        item("L'affaire est devenue une référence publique sur le rapprochement de scènes par trace biologique.",
             "The case became a public reference on linking scenes through biological traces.",
             "CONFIRMED", "francetv-au-bout-de-l-enquete"),
    ],
}

EXPERTS = [
    {"label": txt("Lecture A — la science a résolu l'affaire", "Reading A — science solved the case"),
     "field": "forensic_science",
     "position": txt("Une trace ADN commune identifiée sur plusieurs scènes a permis l'identification et conduit à la "
                     "création du FNAEG.",
                     "A common DNA trace identified on several scenes enabled identification and led to the creation "
                     "of the FNAEG."),
     "reliability": "CONFIRMED", "source": "francetv-au-bout-de-l-enquete"},
    {"label": txt("Lecture B — le rapprochement est arrivé tard", "Reading B — the linkage came late"),
     "field": "investigation",
     "position": txt("La presse documente des « ratages » : absence de comparaison entre certaines traces dès 1994-1995, "
                     "alors que les éléments existaient.",
                     "The press documents 'misses': absence of comparison between certain traces as early as "
                     "1994-1995, although the elements existed."),
     "reliability": "PROBABLE", "source": "parismatch-archives"},
    {"label": txt("Lecture C — l'exécution des peines en question", "Reading C — sentence enforcement in question"),
     "field": "justice",
     "position": txt("Une permission de sortie accordée en janvier 1991 précède le premier meurtre de la série ; la "
                     "question de l'articulation entre exécution des peines et récidive est posée par les "
                     "rétrospectives de presse.",
                     "A period of leave granted in January 1991 precedes the first murder of the series; the question "
                     "of how sentence enforcement articulates with reoffending is raised by press retrospectives."),
     "reliability": "CONFIRMED", "source": "parismatch-archives"},
]
EXPERTS_AGREEMENT = txt("Les trois lectures s'accordent sur un point : les éléments matériels existaient avant l'identification de 1998.",
                        "All three readings agree on one point: the material elements existed before the 1998 identification.")
EXPERTS_DISAGREEMENT = txt("Elles divergent sur la cause du délai : technique, organisationnelle ou pénale.",
                           "They diverge on the cause of the delay: technical, organisational or penal.")
EXPERTS_UNCERTAIN = txt("Ce qui reste incertain : le nombre exact d'occasions manquées, qui n'est pas établi par une décision de justice.",
                        "What remains uncertain: the exact number of missed opportunities, which is not established by a court decision.")

COUNTERFACTUALS = [
    counterfactual(
        "evidence_linkage",
        "Et si les traces de 1994 et 1995 avaient été comparées ?",
        "What if the 1994 and 1995 traces had been compared?",
        "La presse documente qu'aucune comparaison n'a été effectuée entre les traces découvertes au domicile "
        "d'Agnès Nijkamp (décembre 1994) et celles relevées lors de l'agression d'Élisabeth O. (1995). Deux meurtres "
        "ont été commis après 1995 dans la série jugée en 2001.",
        "The press documents that no comparison was made between the traces discovered at Agnès Nijkamp's home "
        "(December 1994) and those recorded during the attack on Élisabeth O. (1995). Two murders were committed "
        "after 1995 in the series tried in 2001.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Trace au domicile d'A. Nijkamp", "Trace at A. Nijkamp's home"), "date": "1994-12-10"},
            "hypothesis": {"label": txt("Comparaison non effectuée", "Comparison not performed"), "date": "1995-12-31"},
            "scenario_event": {"label": txt("Trace ADN commune identifiée", "Common DNA trace identified"), "date": "1997-11-15"},
            "outcome_event": {"label": txt("Arrestation", "Arrest"), "date": "1998-01-26"},
            "documented_offences_after": [
                {"date": "1995-07-08", "label": txt("Hélène Frinking, 27 ans", "Hélène Frinking, 27")},
                {"date": "1996-01-01", "label": txt("Magalie Sirotti, 19 ans (année rapportée par la presse)", "Magalie Sirotti, 19 (year as reported by the press)"), "reliability": "PROBABLE"},
                {"date": "1997-11-15", "label": txt("Estelle Magd, 25 ans", "Estelle Magd, 25")},
            ],
            "jurisdiction_note": txt(
                "En 1994-1995, la France ne disposait pas encore du FNAEG, créé par la loi du 17 juin 1998. Une "
                "comparaison entre deux dossiers restait juridiquement possible mais dépendait de l'initiative des "
                "services. Le scénario étudié porte donc sur une pratique d'enquête, non sur une obligation légale.",
                "In 1994-1995, France did not yet have the FNAEG, created by the law of 17 June 1998. A comparison "
                "between two files remained legally possible but depended on the initiative of services. The scenario "
                "studied therefore concerns an investigative practice, not a legal obligation."),
        },
        [
            {"date": "1994-12-10", "kind": "reference", "label": txt("Trace à Bastille", "Trace near Bastille")},
            {"date": "1995-07-08", "kind": "offence", "label": txt("Meurtre d'Hélène Frinking", "Murder of Hélène Frinking")},
            {"date": "1996-01-01", "kind": "offence", "label": txt("Meurtre de Magalie Sirotti", "Murder of Magalie Sirotti")},
            {"date": "1997-11-15", "kind": "offence", "label": txt("Meurtre d'Estelle Magd", "Murder of Estelle Magd")},
            {"date": "1997-11-15", "kind": "scenario", "label": txt("Trace commune identifiée", "Common trace identified")},
            {"date": "1998-01-26", "kind": "outcome", "label": txt("Arrestation", "Arrest")},
        ],
        True, "parismatch-archives"),
    counterfactual(
        "sentence_enforcement",
        "Et si la permission de sortie de janvier 1991 n'avait pas été accordée ?",
        "What if the January 1991 leave had not been granted?",
        "Le premier meurtre de la série est commis le 16 janvier 1991, alors que l'auteur exécute une peine à la "
        "centrale de Caen et bénéficie d'une permission. Cinq autres victimes sont recensées après cette date.",
        "The first murder of the series was committed on 16 January 1991, while the author was serving a sentence at "
        "Caen prison and on leave. Five other victims are recorded after that date.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Permission de sortie", "Leave granted"), "date": "1991-01-01"},
            "hypothesis": {"label": txt("Premier meurtre de la série", "First murder of the series"), "date": "1991-01-16"},
            "scenario_event": {"label": txt("Arrestation", "Arrest"), "date": "1998-01-26"},
            "documented_offences_after": [
                {"date": "1991-01-16", "label": txt("Pascale Escarfail", "Pascale Escarfail")},
                {"date": "1992-01-07", "label": txt("Catherine Rocher, 27 ans (date rapportée par la presse)", "Catherine Rocher, 27 (date as reported by the press)"), "reliability": "PROBABLE"},
                {"date": "1993-01-07", "label": txt("Elsa Benady, 22 ans (date rapportée par la presse)", "Elsa Benady, 22 (date as reported by the press)"), "reliability": "PROBABLE"},
                {"date": "1994-12-10", "label": txt("Agnès Nijkamp, 32 ans", "Agnès Nijkamp, 32")},
                {"date": "1995-07-08", "label": txt("Hélène Frinking, 27 ans", "Hélène Frinking, 27")},
                {"date": "1996-01-01", "label": txt("Magalie Sirotti, 19 ans", "Magalie Sirotti, 19"), "reliability": "PROBABLE"},
                {"date": "1997-11-15", "label": txt("Estelle Magd, 25 ans", "Estelle Magd, 25")},
            ],
            "jurisdiction_note": txt(
                "Les permissions de sortie relèvent de l'administration pénitentiaire et du juge de l'application des "
                "peines, dans un cadre légal. La décision de 1991 a été prise dans ce cadre ; la question contrefactuelle "
                "ne porte pas sur sa légalité.",
                "Leave is granted by the prison administration and the sentence-enforcement judge, within a legal "
                "framework. The 1991 decision was taken within that framework; the counterfactual question does not "
                "concern its legality."),
        },
        [
            {"date": "1991-01-01", "kind": "reference", "label": txt("Permission", "Leave")},
            {"date": "1991-01-16", "kind": "offence", "label": txt("P. Escarfail", "P. Escarfail")},
            {"date": "1994-12-10", "kind": "offence", "label": txt("A. Nijkamp", "A. Nijkamp")},
            {"date": "1995-07-08", "kind": "offence", "label": txt("H. Frinking", "H. Frinking")},
            {"date": "1997-11-15", "kind": "offence", "label": txt("E. Magd", "E. Magd")},
            {"date": "1998-01-26", "kind": "outcome", "label": txt("Arrestation", "Arrest")},
        ],
        True, "parismatch-archives"),
]

LESSONS = [
    item("La comparaison systématique des traces entre dossiers est un facteur décisif : ici, le défaut de "
         "comparaison est documenté par la presse.",
         "Systematic comparison of traces between files is a decisive factor: here, the failure to compare is "
         "documented by the press.",
         "PROBABLE", "parismatch-archives", "Cloisonnement", "Compartmentalisation"),
    item("Les survivantes produisent des éléments d'enquête décisifs : une empreinte, un portefeuille abandonné, un "
         "signalement.",
         "Survivors produce decisive investigative elements: a footprint, an abandoned wallet, a description.",
         "CONFIRMED", "sudouest-parcours", "Témoignage", "Testimony"),
    item("Une avancée scientifique peut naître d'une affaire : le FNAEG a été créé en 1998 dans le prolongement de "
         "ce dossier.",
         "A scientific advance can arise from a case: the FNAEG was created in 1998 in the wake of this file.",
         "CONFIRMED", "francetv-au-bout-de-l-enquete", "Législation", "Legislation"),
    item("Une période de sûreté n'est pas une fin de peine : elle détermine le moment à partir duquel des demandes "
         "peuvent être formées.",
         "A minimum term is not the end of a sentence: it determines when requests may be filed.",
         "CONFIRMED", "bfmtv-que-devient", "Exécution des peines", "Sentence enforcement"),
    item("Lorsque les sources divergent sur une victime (âge, situation), l'écart doit être affiché plutôt que lissé.",
         "When sources diverge about a victim (age, situation), the discrepancy must be displayed rather than smoothed over.",
         "CONFIRMED", "parismatch-archives", "Rigueur", "Rigour"),
]

UNKNOWNS = [
    item("L'âge exact et la situation de Pascale Escarfail au moment des faits : les sources publiques divergent.",
         "The exact age and situation of Pascale Escarfail at the time: public sources diverge.", "UNKNOWN", "parismatch-archives"),
    item("Le nombre exact d'occasions de rapprochement manquées entre 1991 et 1997.",
         "The exact number of missed linkage opportunities between 1991 and 1997.", "UNKNOWN", "parismatch-archives"),
    item("Les motivations internes : l'accusé a nié les meurtres à l'audience.",
         "Internal motivations: the accused denied the murders at the hearing.", "UNKNOWN", "bfmtv-fea"),
]

SECTIONS = [
    {"key": "introduction", "title": txt("Introduction", "Introduction"), "tier": "FREE", "blocks": [
        block("paragraph", "Sept femmes, six ans, un secteur de Paris", "Seven women, six years, one sector of Paris",
              "Entre 1991 et 1997, sept femmes sont violées et tuées dans l'est parisien. L'affaire se résoudra par "
              "une trace biologique, et produira une modification durable du droit français.",
              "Between 1991 and 1997, seven women were raped and killed in eastern Paris. The case would be solved by "
              "a biological trace, and produce a lasting change in French law.",
              "CONFIRMED", "sudouest-parcours")]},
    {"key": "context", "title": txt("Contexte", "Context"), "tier": "FREE", "blocks": [
        block("paragraph", "Paris au début des années 1990", "Paris in the early 1990s",
              "Les faits s'inscrivent dans un Paris où la police scientifique se développe et où les fichiers "
              "génétiques n'existent pas encore : le FNAEG sera créé en 1998.",
              "The facts take place in a Paris where forensic science was developing and genetic databases did not "
              "yet exist: the FNAEG would be created in 1998.",
              "CONFIRMED", "francetv-au-bout-de-l-enquete")]},
    {"key": "offender", "title": txt("Auteur", "Author"), "tier": "PREMIUM", "blocks": [
        block("paragraph", "Guy Georges, né Guy Rampillon", "Guy Georges, born Guy Rampillon",
              "Né le 15 octobre 1962. Condamné une première fois en 1984 à dix ans de prison. Arrêté en janvier 1998, "
              "condamné le 5 avril 2001 à la réclusion criminelle à perpétuité assortie d'une période de sûreté de "
              "22 ans.",
              "Born on 15 October 1962. First sentenced in 1984 to ten years in prison. Arrested in January 1998, "
              "sentenced on 5 April 2001 to life imprisonment with a 22-year minimum term.",
              "CONFIRMED", "sudouest-parcours")]},
    {"key": "victims", "title": txt("Victimes", "Victims"), "tier": "FREE", "blocks": []},
    {"key": "timeline", "title": txt("Chronologie", "Chronology"), "tier": "FREE", "blocks": []},
    {"key": "investigation", "title": txt("Enquête", "Investigation"), "tier": "FREE", "blocks": []},
    {"key": "clues", "title": txt("Indices et preuves", "Clues and evidence"), "tier": "PREMIUM", "blocks": []},
    {"key": "behaviour", "title": txt("Analyse comportementale", "Behavioural analysis"), "tier": "PREMIUM", "blocks": [
        block("behaviour", "Un mode opératoire stable", "A stable method",
              "Intrusion au domicile, contrainte par sparadrap, viol, homicide à l'arme blanche. La stabilité permet "
              "le rapprochement ; elle n'explique pas le passage à l'acte.",
              "Intrusion into the home, restraint with adhesive tape, rape, homicide with a blade. Stability enables "
              "linkage; it does not explain the act.",
              "CONFIRMED", "sudouest-parcours")]},
    {"key": "psychology", "title": txt("Psychologie", "Psychology"), "tier": "PREMIUM", "blocks": []},
    {"key": "victimology", "title": txt("Victimologie", "Victimology"), "tier": "FREE", "blocks": []},
    {"key": "geography", "title": txt("Géographie", "Geography"), "tier": "FREE", "blocks": [
        block("paragraph", "L'est parisien", "Eastern Paris",
              "Les faits se concentrent dans les 10e, 11e, 12e et 14e arrondissements, avec une première victime en "
              "1991 rue Delambre. La carte affiche les secteurs, jamais les adresses privées.",
              "The facts concentrate in the 10th, 11th, 12th and 14th arrondissements, with a first victim in 1991 on "
              "rue Delambre. The map displays sectors, never private addresses.",
              "PROBABLE", "parismatch-archives")]},
    {"key": "arrest", "title": txt("Arrestation", "Arrest"), "tier": "FREE", "blocks": [
        block("paragraph", "Janvier 1998", "January 1998",
              "Deux jours après l'identification d'un profil génétique par le laboratoire du docteur Olivier Pascal, "
              "Guy Georges est interpellé. Il avoue deux autres crimes après son interpellation, selon Paris Match.",
              "Two days after the identification of a genetic profile by Doctor Olivier Pascal's laboratory, Guy "
              "Georges was arrested. He confessed to two other crimes after his arrest, according to Paris Match.",
              "CONFIRMED", "sudouest-parcours")]},
    {"key": "trial", "title": txt("Procès", "Trial"), "tier": "FREE", "blocks": []},
    {"key": "justice", "title": txt("Justice", "Justice"), "tier": "FREE", "blocks": []},
    {"key": "consequences", "title": txt("Conséquences", "Consequences"), "tier": "FREE", "blocks": [
        block("paragraph", "Le FNAEG", "The FNAEG",
              "La loi du 17 juin 1998 crée le fichier national automatisé des empreintes génétiques. C'est la "
              "conséquence structurelle la plus documentée de cette affaire.",
              "The law of 17 June 1998 created the national automated database of genetic fingerprints. It is the "
              "most documented structural consequence of this case.",
              "CONFIRMED", "francetv-au-bout-de-l-enquete")]},
    {"key": "archives", "title": txt("Archives", "Archives"), "tier": "PREMIUM", "blocks": []},
    {"key": "sources", "title": txt("Sources", "Sources"), "tier": "FREE", "blocks": []},
    {"key": "memorial", "title": txt("Mémoire", "Memory"), "tier": "FREE", "blocks": []},
    {"key": "unknowns", "title": txt("Zones d'ombre", "Unknown zones"), "tier": "FREE", "blocks": []},
    {"key": "lessons", "title": txt("Ce que l'affaire nous apprend", "What the case teaches us"), "tier": "FREE", "blocks": []},
]

EPISODES = [
    {
        "number": 1,
        "title": txt("L'est parisien", "Eastern Paris"),
        "description": txt("1991-1997 : sept femmes, un secteur, et des traces que personne ne compare.",
                           "1991-1997: seven women, one sector, and traces nobody compares."),
        "modes": ["documentary", "investigation", "chronology", "victims", "express", "psychology", "expert"],
        "audio_status": "produced", "audio": "episode-05-guy-georges.wav", "duration_sec": 116, "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 8, "title": txt("Janvier 1991", "January 1991")},
            {"at": 27, "title": txt("Des scènes qui se ressemblent", "Scenes that look alike")},
            {"at": 51, "title": txt("Les survivantes", "The survivors")},
            {"at": 70, "title": txt("Et maintenant, une question", "And now, a question")},
            {"at": 76, "title": txt("La trace commune", "The common trace")},
        ],
        "transcript": {"segments": [
            {"id": "g1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X, à travers mon regard. Aujourd'hui, nous allons revenir sur une affaire "
                     "qui a changé la police scientifique française. Sept femmes. Six ans. Un secteur de Paris.",
             "text_en": "You are on YANIS//X, through my eyes. Today we return to a case that changed French forensic "
                        "science. Seven women. Six years. One sector of Paris."},
            {"id": "g2", "t": 8, "speaker": "yanis",
             "text": "16 janvier 1991. Guy Georges est en permission de sortie. Il exécute une peine à la centrale de "
                     "Caen, il prend le train pour Paris. Ce soir-là, Pascale Escarfail est violée et tuée dans son "
                     "studio. Elle est la première victime d'une série qui n'a pas encore de nom.",
             "text_en": "16 January 1991. Guy Georges is on leave. He is serving a sentence at Caen prison; he takes "
                        "the train to Paris. That evening, Pascale Escarfail is raped and killed in her studio. She is "
                        "the first victim of a series that does not yet have a name."},
            {"id": "g3", "t": 27, "speaker": "yanis",
             "text": "Les scènes se ressemblent. On entre chez les victimes. On les attache, on les bâillonne avec du "
                     "sparadrap. On les viole, on les tue. Catherine Rocher, vingt-sept ans. Elsa Benady, vingt-deux "
                     "ans. Agnès Nijkamp, trente-deux ans, architecte d'intérieur néerlandaise, retrouvée près de la "
                     "Bastille. Hélène Frinking, vingt-sept ans, étudiante. Magalie Sirotti, dix-neuf ans. Estelle "
                     "Magd, vingt-cinq ans.",
             "text_en": "The scenes look alike. One enters the victims' homes. They are tied, gagged with adhesive "
                        "tape. Raped, killed. Catherine Rocher, twenty-seven. Elsa Benady, twenty-two. Agnès Nijkamp, "
                        "thirty-two, a Dutch interior architect, found near the Bastille. Hélène Frinking, "
                        "twenty-seven, a student. Magalie Sirotti, nineteen. Estelle Magd, twenty-five."},
            {"id": "g4", "t": 51, "speaker": "yanis",
             "text": "Et il y a celles qui ont survécu. Élisabeth Ortega, vingt-trois ans, s'enfuit. Une empreinte "
                     "est relevée, avec un signe distinctif : un pied égyptien, le second orteil plus long que le "
                     "pouce. Mélanie Bacou échappe à son agresseur, qui fuit en laissant tomber son portefeuille. Ces "
                     "deux femmes n'ont pas seulement survécu : elles ont produit des éléments.",
             "text_en": "And there are those who survived. Élisabeth Ortega, twenty-three, escapes. A footprint is "
                        "recorded, with a distinctive feature: an Egyptian foot, the second toe longer than the big "
                        "toe. Mélanie Bacou escapes her attacker, who flees dropping his wallet. These two women did "
                        "not only survive: they produced elements."},
            {"id": "g5", "t": 70, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "g6", "t": 76, "speaker": "yanis",
             "text": "En décembre 1994, de l'ADN est découvert au domicile d'Agnès Nijkamp. En 1995, des traces sont "
                     "relevées lors de l'agression d'Élisabeth Ortega. Paris Match relèvera plus tard qu'aucune "
                     "comparaison similaire n'a été effectuée entre ces deux jeux de traces. Il faudra attendre le "
                     "dernier meurtre, en novembre 1997, pour qu'une trace commune soit identifiée — et deux jours "
                     "de plus pour que Guy Georges soit arrêté.",
             "text_en": "In December 1994, DNA is discovered at Agnès Nijkamp's home. In 1995, traces are recorded "
                        "during the attack on Élisabeth Ortega. Paris Match would later note that no similar "
                        "comparison was made between those two sets of traces. It took until the last murder, in "
                        "November 1997, for a common trace to be identified — and two more days for Guy Georges to be "
                        "arrested."},
            {"id": "g7", "t": 97, "speaker": "yanis",
             "text": "Le 5 avril 2001, la cour d'assises de Paris condamne Guy Georges à la réclusion criminelle à "
                     "perpétuité, assortie d'une période de sûreté de vingt-deux ans. En 1998, la France avait créé "
                     "le FNAEG, le fichier national automatisé des empreintes génétiques. C'est la conséquence "
                     "structurelle de cette affaire.",
             "text_en": "On 5 April 2001, the Paris assize court sentenced Guy Georges to life imprisonment with a "
                        "twenty-two-year minimum term. In 1998, France had created the FNAEG, the national automated "
                        "database of genetic fingerprints. That is the structural consequence of this case."},
            {"id": "g8", "t": 116, "speaker": "yanis",
             "text": "Écouter les histoires. Comprendre les affaires. Ne jamais oublier les victimes : Pascale, "
                     "Catherine, Elsa, Agnès, Hélène, Magalie, Estelle.",
             "text_en": "Listen to the stories. Understand the cases. Never forget the victims: Pascale, Catherine, "
                        "Elsa, Agnès, Hélène, Magalie, Estelle."},
        ]},
    },
    {
        "number": 2,
        "title": txt("La trace", "The trace"),
        "description": txt("Comment une comparaison biologique a mis fin à six ans d'enquête — et ce qui n'a pas été comparé.",
                           "How a biological comparison ended six years of investigation — and what was not compared."),
        "modes": ["documentary", "investigation", "expert", "express"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [{"at": 0, "title": txt("Ouverture", "Opening")}, {"at": 12, "title": txt("Le laboratoire", "The laboratory")}],
        "transcript": {"segments": [
            {"id": "h1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X. Cet épisode porte sur un objet invisible : une trace. Et sur une "
                     "question de méthode : à quel moment compare-t-on ce que l'on a déjà ?",
             "text_en": "You are on YANIS//X. This episode is about an invisible object: a trace. And about a question "
                        "of method: at what point do we compare what we already have?"},
            {"id": "h2", "t": 12, "speaker": "yanis",
             "text": "Le laboratoire du docteur Olivier Pascal identifie un profil. La presse décrit cette "
                     "identification comme obtenue presque par hasard. Deux jours plus tard, l'homme est arrêté. Ce "
                     "que l'histoire retient, c'est l'efficacité de la science. Ce que le dossier montre, c'est que "
                     "les éléments existaient avant.",
             "text_en": "Doctor Olivier Pascal's laboratory identifies a profile. The press describes this "
                        "identification as obtained almost by chance. Two days later, the man is arrested. What "
                        "history retains is the efficiency of science. What the file shows is that the elements "
                        "existed before."},
        ]},
    },
]

QUESTIONS = [
    question("1", 70, "evidence",
             "Deux jeux de traces biologiques existent, l'un en 1994, l'autre en 1995. Aucune comparaison n'est faite. Que produit cette absence ?",
             "Two sets of biological traces exist, one in 1994, one in 1995. No comparison is made. What does that absence produce?",
             [("a", "Rien : les traces n'étaient pas comparables", "Nothing: the traces were not comparable"),
              ("b", "Une perte de temps d'enquête, sans effet juridique", "A loss of investigative time, without legal effect"),
              ("c", "Un délai pendant lequel la série se poursuit", "A delay during which the series continues"),
              ("d", "Impossible à déterminer", "Impossible to determine")],
             {"fr": {"whatInvestigatorsKnew": "Des traces biologiques avaient été découvertes au domicile d'Agnès Nijkamp en décembre 1994, et d'autres relevées lors de l'agression de 1995.",
                     "whatExpertsProposed": "La comparaison de traces issues de scènes différentes est la méthode standard de rapprochement en série. En l'absence de fichier national — le FNAEG sera créé en 1998 — elle dépendait de l'initiative des services.",
                     "documented": "Paris Match documente l'absence de comparaison entre ces deux jeux de traces.",
                     "hypothetical": "Le nombre précis d'occasions manquées n'est établi par aucune décision de justice.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir que l'identification de 1998 interviendrait deux jours après la mise en évidence d'une trace commune.",
                     "answer_note": "La réponse attendue est C. Elle décrit une conséquence temporelle documentée, sans porter de jugement sur les enquêteurs."},
              "en": {"whatInvestigatorsKnew": "Biological traces had been discovered at Agnès Nijkamp's home in December 1994, and others recorded during the 1995 attack.",
                     "whatExpertsProposed": "Comparing traces from different scenes is the standard method of serial linkage. In the absence of a national database — the FNAEG would be created in 1998 — it depended on the initiative of services.",
                     "documented": "Paris Match documents the absence of comparison between those two sets of traces.",
                     "hypothetical": "The precise number of missed opportunities is established by no court decision.",
                     "whatYouCouldNotKnow": "You could not know that the 1998 identification would come two days after a common trace was highlighted.",
                     "answer_note": "The expected answer is C. It describes a documented temporal consequence, without judging the investigators."}},
             "parismatch-archives"),
    question("1", 51, "victimology",
             "Trois femmes ont survécu à des agressions. Que produisent leurs témoignages dans ce dossier ?",
             "Three women survived attacks. What do their testimonies produce in this file?",
             [("a", "Uniquement un récit complémentaire", "Only a complementary account"),
              ("b", "Des éléments matériels : une empreinte, un objet abandonné", "Material elements: a footprint, an abandoned object"),
              ("c", "Une identification directe de l'auteur", "A direct identification of the author"),
              ("d", "Rien de juridiquement exploitable", "Nothing legally usable")],
             {"fr": {"whatInvestigatorsKnew": "Une empreinte à signe distinctif a été relevée après l'agression d'Élisabeth Ortega ; un portefeuille a été abandonné lors de l'agression de Mélanie Bacou, donnant lieu à une condamnation à 30 mois.",
                     "whatExpertsProposed": "Les agressions non mortelles produisent souvent les éléments les plus exploitables d'une série : description, traces, objets, horaires.",
                     "documented": "Ces éléments figurent dans les rétrospectives de presse de l'affaire.",
                     "hypothetical": "Aucune : il s'agit de faits de dossier.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir, en 1995, que ces éléments serviraient à une série jugée en 2001.",
                     "answer_note": "La réponse attendue est B. Le témoignage des survivantes est ici un vecteur de traces matérielles."},
              "en": {"whatInvestigatorsKnew": "A footprint with a distinctive feature was recorded after the attack on Élisabeth Ortega; a wallet was abandoned during the attack on Mélanie Bacou, leading to a 30-month sentence.",
                     "whatExpertsProposed": "Non-fatal attacks often produce the most usable elements of a series: description, traces, objects, timings.",
                     "documented": "These elements appear in press retrospectives of the case.",
                     "hypothetical": "None: these are case facts.",
                     "whatYouCouldNotKnow": "You could not know, in 1995, that these elements would serve a series tried in 2001.",
                     "answer_note": "The expected answer is B. Survivors' testimony is here a vehicle for material traces."}},
             "sudouest-parcours"),
    question("1", 105, "bias",
             "Après l'arrestation, la presse parle d'une identification obtenue « presque par hasard ». Quel risque de lecture cette formule fait-elle courir ?",
             "After the arrest, the press speaks of an identification obtained 'almost by chance'. What reading risk does that phrase create?",
             [("a", "Elle minimise un travail de laboratoire et un rapprochement de scènes", "It minimises laboratory work and a linkage of scenes"),
              ("b", "Elle exagère la fiabilité de l'ADN", "It exaggerates DNA reliability"),
              ("c", "Elle criminalise les victimes", "It criminalises the victims"),
              ("d", "Aucun : c'est une description factuelle", "None: it is a factual description")],
             {"fr": {"whatInvestigatorsKnew": "L'identification a résulté d'un travail de laboratoire et du rapprochement de traces issues de plusieurs scènes.",
                     "whatExpertsProposed": "Les formulations narratives (« par hasard », « miracle ») écrasent la chaîne technique réelle et peuvent nourrir une méfiance infondée envers la preuve scientifique.",
                     "documented": "La formule figure dans la rétrospective de Sud Ouest.",
                     "hypothetical": "La part exacte de hasard dans le processus n'est pas documentée.",
                     "whatYouCouldNotKnow": "Rien : la question porte sur la lecture d'une formulation de presse.",
                     "answer_note": "La réponse attendue est A."},
              "en": {"whatInvestigatorsKnew": "The identification resulted from laboratory work and the linkage of traces from several scenes.",
                     "whatExpertsProposed": "Narrative formulations ('by chance', 'miracle') flatten the real technical chain and can feed unwarranted distrust of scientific evidence.",
                     "documented": "The phrase appears in the Sud Ouest retrospective.",
                     "hypothetical": "The exact share of chance in the process is not documented.",
                     "whatYouCouldNotKnow": "Nothing: the question concerns reading a press formulation.",
                     "answer_note": "The expected answer is A."}},
             "sudouest-parcours"),
]

CASE = {
    "id": CASE_ID,
    "title": txt("Guy Georges, dit « le tueur de l'est parisien »", "Guy Georges, the 'killer of eastern Paris'"),
    "subtitle": txt("Paris, 1991-1997. Sept femmes tuées, trois survivantes, et une trace qui a changé le droit français.",
                    "Paris, 1991-1997. Seven women killed, three survivors, and a trace that changed French law."),
    "country": "FR", "region": "Île-de-France / Paris", "city": "Paris",
    "year_start": 1991, "year_end": 2001, "period_label": txt("1991 – 2001", "1991 – 2001"),
    "status": "RESOLVED", "type": "serial",
    "tags": ["serial_killer", "dna", "fneg", "france", "survivors", "forensic"],
    "tier": "PREMIUM", "editorial": "yanis", "published_at": "2026-09-24",
    "sensitive": True,
    "triggers": txt("Viols et meurtres ; description du mode opératoire sans détail graphique.",
                    "Rapes and murders; description of the method without graphic detail."),
    "lat": 48.86, "lon": 2.37, "cover": "cover-georges",
    "stats": {"victims_documented": 7, "survivors_documented": 3, "duration_years": 10},
    "summary": txt(
        "Entre janvier 1991 et novembre 1997, sept femmes sont violées et tuées dans l'est parisien, selon un mode "
        "opératoire constant. Trois autres femmes survivent à des agressions, dont deux pendant la série, et "
        "produisent des éléments d'enquête : une empreinte à signe distinctif, un portefeuille abandonné. Le "
        "rapprochement des scènes intervient tardivement ; la presse documente l'absence de comparaison entre deux "
        "jeux de traces en 1994 et 1995. En janvier 1998, un profil génétique commun est identifié par le laboratoire "
        "du docteur Olivier Pascal : Guy Georges est arrêté deux jours plus tard. Le 5 avril 2001, la cour d'assises "
        "de Paris le condamne à la réclusion criminelle à perpétuité, assortie d'une période de sûreté de 22 ans. "
        "Dans le prolongement de l'affaire, la loi du 17 juin 1998 crée le FNAEG.",
        "Between January 1991 and November 1997, seven women were raped and killed in eastern Paris, following a "
        "constant method. Three other women survived attacks, two of them during the series, and produced "
        "investigative elements: a footprint with a distinctive feature, an abandoned wallet. The linkage of scenes "
        "came late; the press documents the absence of comparison between two sets of traces in 1994 and 1995. In "
        "January 1998, a common genetic profile was identified by Doctor Olivier Pascal's laboratory: Guy Georges was "
        "arrested two days later. On 5 April 2001, the Paris assize court sentenced him to life imprisonment with a "
        "22-year minimum term. In the wake of the case, the law of 17 June 1998 created the FNAEG."),
    "sources": SOURCES, "victims": VICTIMS, "survivors": SURVIVORS, "memorial": MEMORIAL,
    "timeline": TIMELINE, "locations": LOCATIONS, "evidence": EVIDENCE, "investigation": INVESTIGATION,
    "psychology": PSYCHOLOGY, "victimology": VICTIMOLOGY, "court": COURT, "experts": EXPERTS,
    "experts_agreement": EXPERTS_AGREEMENT, "experts_disagreement": EXPERTS_DISAGREEMENT,
    "experts_uncertain": EXPERTS_UNCERTAIN, "counterfactuals": COUNTERFACTUALS, "lessons": LESSONS,
    "unknowns": UNKNOWNS, "sections": SECTIONS, "episodes": EPISODES, "questions": QUESTIONS,
}
