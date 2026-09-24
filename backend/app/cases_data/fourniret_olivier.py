"""
DOSSIER 07 — MICHEL FOURNIRET ET MONIQUE OLIVIER (France / Belgique, 1987-2023)

Dossier centré sur la COMPPLICITÉ : c'est le seul angle dont les sources
publiques permettent de rendre compte de façon fiable, Monique Olivier étant
la seule personne jugée pour plusieurs de ces faits.
Sources publiques vérifiées le 2026-09-24.
"""
from ..case_template import (block, counterfactual, default_sections, fact, item,
                             merge_sections, question, source, txt)

CASE_ID = "fourniret-olivier"
V = "2026-09-24"

SOURCES = [
    source("radiofrance-olivier", CASE_ID,
           "Monique Olivier — biographie et suivi judiciaire",
           "Monique Olivier — biography and judicial coverage",
           "Radio France", "Redaction", "https://www.radiofrance.fr/personnes/monique-olivier?p=3",
           "2026", "press", "CONFIRMED", V,
           "Date de naissance, rencontre par correspondance en 1987, trois condamnations (2008, 2018, 2023).",
           "Date of birth, meeting by correspondence in 1987, three convictions (2008, 2018, 2023)."),
    source("franceinfo-2023", CASE_ID,
           "Procès de Monique Olivier : l'ex-femme de Michel Fourniret condamnée à la réclusion à perpétuité pour "
           "complicité dans trois meurtres, dont celui d'Estelle Mouzin",
           "Monique Olivier trial: Michel Fourniret's ex-wife sentenced to life for complicity in three murders, "
           "including Estelle Mouzin's",
           "franceinfo (Radio France)", "Redaction",
           "https://www.franceinfo.fr/societe/justice/michel-fourniret/proces-de-monique-olivier-l-ex-femme-de-michel-fourniret-condamnee-a-la-prison-a-perpetuite-pour-complicite-dans-trois-meurtres-dont-celui-d-estelle-mouzin_6254334.html",
           "2023-12-19", "press", "CONFIRMED", V,
           "Verdict, motivations de la cour, réquisitions, cumul des peines et calcul de la date de libération possible.",
           "Verdict, court reasoning, prosecution requests, accumulation of sentences and calculation of possible release date."),
    source("ici-olivier-2023", CASE_ID,
           "Monique Olivier : l'ex-femme du tueur en série condamnée à la perpétuité pour complicité dans trois crimes",
           "Monique Olivier: the serial killer's ex-wife sentenced to life for complicity in three crimes",
           "ICI (Radio France)", "Redaction", "https://www.ici.fr/infos/faits-divers-justice/monique-olivier-l-ex-femme-du-tueur-en-serie-condamnee-a-la-perpetuite-pour-complicite-dans-trois-crimes-7320709",
           "2023-12-19", "press", "CONFIRMED", V,
           "Déroulé de l'audience, noms et âges des trois victimes jugées, condamnations antérieures.",
           "Course of the hearing, names and ages of the three victims tried, previous convictions."),
    source("actu-proces-2023", CASE_ID,
           "Affaire Estelle Mouzin : le procès de Monique Olivier durera trois semaines",
           "Estelle Mouzin case: Monique Olivier's trial will last three weeks",
           "actu.fr", "Redaction", "https://actu.fr/ile-de-france/guermantes_77221/affaire-estelle-mouzin-lex-femme-de-michel-fourniret-monique-olivier-jugee-en-novembre-2023_56393070.html",
           "2023-07-17", "press", "CONFIRMED", V,
           "Extinction de l'action publique par la mort de l'auteur principal ; position de l'avocat de la famille Mouzin.",
           "Extinguishment of public prosecution by the death of the principal author; position of the Mouzin family lawyer."),
    source("franceinfo-cecile-vallin", CASE_ID,
           "Affaire Estelle Mouzin — suivi : garde à vue de Monique Olivier dans l'affaire Cécile Vallin",
           "Estelle Mouzin case — follow-up: Monique Olivier's police custody in the Cécile Vallin case",
           "franceinfo (Radio France)", "Redaction", "https://www.franceinfo.fr/faits-divers/affaire-estelle-mouzin/",
           "2025-09-03", "press", "CONFIRMED", V,
           "Poursuite des investigations : garde à vue levée après dix heures dans le dossier de la disparition de "
           "Cécile Vallin en 1997 en Savoie ; condamnation de l'État pour faute lourde dans l'affaire Estelle Mouzin.",
           "Continuing investigations: police custody lifted after ten hours in the file of Cécile Vallin's 1997 "
           "disappearance in Savoie; State condemned for gross negligence in the Estelle Mouzin case."),
]


def _v(order, first, last, age, source_key, life_fr, life_en, dis_fr, dis_en, reliability="CONFIRMED"):
    return {
        "order": order, "first_name": first, "last_name": last, "age": age,
        "source": source_key, "reliability": reliability, "anonymised": False,
        "life": {"fr": {"headline": f"{first} {last}", "items": life_fr},
                 "en": {"headline": f"{first} {last}", "items": life_en}},
        "disappearance": {"fr": {"items": dis_fr}, "en": {"items": dis_en}},
    }


VICTIMS = [
    _v(0, "Estelle", "Mouzin", "9", "ici-olivier-2023",
       [{"label": "Âge", "text": "9 ans."},
        {"label": "Lieu de vie", "text": "Guermantes (Seine-et-Marne) ; elle rentrait de l'école à pied."},
        {"label": "Dossier", "text": "Un dossier complet lui est consacré dans cette application : « L'affaire Estelle Mouzin »."}],
       [{"label": "Age", "text": "9."},
        {"label": "Place of life", "text": "Guermantes (Seine-et-Marne); she walked home from school."},
        {"label": "File", "text": "A complete file is devoted to her in this application: 'The Estelle Mouzin case'."}],
       [{"label": "Date", "text": "9 janvier 2003."},
        {"label": "Circonstances", "text": "Enlevée au retour de l'école. Séquestrée, violée et tuée selon les "
                                           "déclarations de Monique Olivier. Le corps n'a jamais été retrouvé."}],
       [{"label": "Date", "text": "9 January 2003."},
        {"label": "Circumstances", "text": "Abducted on the way home from school. Confined, raped and killed "
                                           "according to Monique Olivier's statements. The body was never recovered."}]),
    _v(1, "Joanna", "Parrish", "20", "ici-olivier-2023",
       [{"label": "Âge", "text": "20 ans selon franceinfo, 21 ans selon ICI : l'écart est signalé."},
        {"label": "Biographie", "text": "Non documentée dans les sources consultées."}],
       [{"label": "Age", "text": "20 according to franceinfo, 21 according to ICI: the discrepancy is flagged."},
        {"label": "Biography", "text": "Not documented in the sources consulted."}],
       [{"label": "Faits", "text": "Enlèvement, viol et meurtre ; le corps avait été retrouvé. Monique Olivier a été "
                                   "déclarée coupable de complicité le 19 décembre 2023."}],
       [{"label": "Facts", "text": "Abduction, rape and murder; the body had been recovered. Monique Olivier was found "
                                   "guilty of complicity on 19 December 2023."}],
       "DISPUTED"),
    _v(2, "Marie-Angèle", "Domèce", "19", "ici-olivier-2023",
       [{"label": "Âge", "text": "19 ans."},
        {"label": "Faits datés", "text": "1988 selon franceinfo."},
        {"label": "Biographie", "text": "Non documentée dans les sources consultées."}],
       [{"label": "Age", "text": "19."},
        {"label": "Dated facts", "text": "1988 according to franceinfo."},
        {"label": "Biography", "text": "Not documented in the sources consulted."}],
       [{"label": "Faits", "text": "Enlèvement et mort ; Monique Olivier a été déclarée coupable de complicité le "
                                   "19 décembre 2023."}],
       [{"label": "Facts", "text": "Abduction and death; Monique Olivier was found guilty of complicity on "
                                   "19 December 2023."}]),
]

OTHER_VICTIMS = {
    "title": txt("Les autres victimes des condamnations antérieures", "The other victims of earlier convictions"),
    "body": txt(
        "En mai 2008, la cour d'assises des Ardennes a condamné Monique Olivier à la réclusion criminelle à "
        "perpétuité, assortie d'une période de sûreté de 28 ans, pour complicité dans le meurtre de sept jeunes "
        "femmes ou adolescentes commis entre 1987 et 2001, entre la France et la Belgique. En 2018, la cour d'assises "
        "des Yvelines l'a condamnée à 20 ans de réclusion pour complicité dans le meurtre de Farida Hammiche. Les "
        "identités et parcours de ces victimes ne figurent pas dans les sources consultées pour ce dossier : elles ne "
        "sont pas reconstituées ici.",
        "In May 2008, the Ardennes assize court sentenced Monique Olivier to life imprisonment with a 28-year minimum "
        "term for complicity in the murder of seven young women or teenagers committed between 1987 and 2001, between "
        "France and Belgium. In 2018, the Yvelines assize court sentenced her to 20 years for complicity in the murder "
        "of Farida Hammiche. The identities and lives of these victims do not appear in the sources consulted for "
        "this file: they are not reconstructed here.",
    ),
    "reliability": "CONFIRMED", "source": "radiofrance-olivier",
}

MEMORIAL = {
    "title": txt("Des victimes nommées, et d'autres qui ne le sont pas encore ici", "Named victims, and others not yet named here"),
    "biography": txt(
        "Trois victimes sont au centre du procès de 2023 : Estelle Mouzin, 9 ans, Joanna Parrish, 20 ou 21 ans, et "
        "Marie-Angèle Domèce, 19 ans. Sept autres jeunes femmes ou adolescentes ont été retenues dans la condamnation "
        "de 2008, et Farida Hammiche dans celle de 2018. Cette application ne publie pas d'identité non sourcée : les "
        "fiches seront complétées à mesure que des sources vérifiables seront réunies.",
        "Three victims are at the centre of the 2023 trial: Estelle Mouzin, 9, Joanna Parrish, 20 or 21, and "
        "Marie-Angèle Domèce, 19. Seven other young women or teenagers were retained in the 2008 conviction, and "
        "Farida Hammiche in the 2018 one. This application does not publish unsourced identities: the files will be "
        "completed as verifiable sources are gathered.",
    ),
    "testimony": txt(
        "« Je confirme ce que j'ai dit et je regrette tout ce que j'ai fait. » — derniers mots de Monique Olivier "
        "devant la cour d'assises des Hauts-de-Seine, le 19 décembre 2023.",
        "'I confirm what I said and I regret everything I did.' — Monique Olivier's last words before the "
        "Hauts-de-Seine assize court, on 19 December 2023.",
    ),
    "memory": txt(
        "La mort de l'auteur principal en 2021 a éteint l'action publique à son égard : il n'a été jugé pour aucun "
        "des faits concernant Estelle Mouzin. Les familles ont donc obtenu un procès, mais un procès de la complicité. "
        "C'est une situation rare, et elle dit quelque chose de ce que la justice peut et ne peut pas réparer.",
        "The death of the principal author in 2021 extinguished public prosecution with respect to him: he was tried "
        "for none of the facts concerning Estelle Mouzin. The families therefore obtained a trial, but a trial of "
        "complicity. This is a rare situation, and it says something about what justice can and cannot repair.",
    ),
}

TIMELINE = [
    fact("Monique Olivier, née le 31 octobre 1948, rencontre Michel Fourniret par correspondance alors qu'il est en "
         "prison.",
         "Monique Olivier, born on 31 October 1948, meets Michel Fourniret by correspondence while he is in prison.",
         "CONFIRMED", "radiofrance-olivier", "Rencontre", "Meeting", "1987"),
    fact("Période des faits retenus dans la condamnation de 2008 : sept jeunes femmes ou adolescentes tuées entre la "
         "France et la Belgique.",
         "Period of the offences retained in the 2008 conviction: seven young women or teenagers killed between "
         "France and Belgium.",
         "CONFIRMED", "radiofrance-olivier", "Période des faits", "Period of offences", "1987-2001"),
    fact("Marie-Angèle Domèce, 19 ans, est victime d'un enlèvement suivi de mort.",
         "Marie-Angèle Domèce, 19, is the victim of an abduction followed by death.",
         "CONFIRMED", "franceinfo-2023", "Première victime du procès de 2023", "First victim of the 2023 trial", "1988"),
    fact("Estelle Mouzin, 9 ans, disparaît à Guermantes le 9 janvier 2003. Le corps ne sera jamais retrouvé.",
         "Estelle Mouzin, 9, disappears in Guermantes on 9 January 2003. The body will never be recovered.",
         "CONFIRMED", "ici-olivier-2023", "Dernier fait retenu", "Last offence retained", "2003-01-09"),
    fact("La cour d'assises des Ardennes condamne Monique Olivier à la réclusion criminelle à perpétuité, assortie "
         "d'une période de sûreté de 28 ans, pour complicité dans sept meurtres.",
         "The Ardennes assize court sentences Monique Olivier to life imprisonment with a 28-year minimum term, for "
         "complicity in seven murders.",
         "CONFIRMED", "radiofrance-olivier", "Première condamnation", "First conviction", "2008-05"),
    fact("La cour d'assises des Yvelines la condamne à 20 ans de réclusion pour complicité dans le meurtre de Farida "
         "Hammiche, un assassinat qualifié de crapuleux.",
         "The Yvelines assize court sentences her to 20 years for complicity in the murder of Farida Hammiche, an "
         "assassination described as mercenary.",
         "CONFIRMED", "ici-olivier-2023", "Deuxième condamnation", "Second conviction", "2018"),
    fact("Monique Olivier accuse Michel Fourniret d'avoir enlevé, violé puis tué Estelle Mouzin. Elle précise que les "
         "faits se sont déroulés dans une maison de Ville-sur-Lumes appartenant à la sœur défunte de ce dernier. Elle "
         "est mise en examen pour complicité.",
         "Monique Olivier accuses Michel Fourniret of having abducted, raped then killed Estelle Mouzin. She "
         "specifies that the facts took place in a house in Ville-sur-Lumes belonging to his late sister. She is "
         "indicted for complicity.",
         "CONFIRMED", "franceinfo-2023", "Accusations", "Accusations", "2020-08"),
    fact("Michel Fourniret meurt en détention le 10 mai 2021, à 79 ans. En droit français, la mort éteint l'action "
         "publique.",
         "Michel Fourniret dies in custody on 10 May 2021, aged 79. Under French law, death extinguishes public "
         "prosecution.",
         "CONFIRMED", "actu-proces-2023", "Décès de l'auteur principal", "Death of the principal author", "2021-05-10"),
    fact("Procès de Monique Olivier devant la cour d'assises des Hauts-de-Seine, à Nanterre, du 28 novembre au "
         "19 décembre 2023. Verdict : réclusion criminelle à perpétuité avec 20 ans de sûreté, pour complicité dans "
         "l'enlèvement, la séquestration et la mort d'Estelle Mouzin, de Joanna Parrish et de Marie-Angèle Domèce.",
         "Trial of Monique Olivier before the Hauts-de-Seine assize court, in Nanterre, from 28 November to "
         "19 December 2023. Verdict: life imprisonment with a 20-year minimum term, for complicity in the abduction, "
         "confinement and death of Estelle Mouzin, Joanna Parrish and Marie-Angèle Domèce.",
         "CONFIRMED", "franceinfo-2023", "Troisième condamnation", "Third conviction", "2023-12-19"),
    fact("La peine se confond avec les condamnations antérieures. Selon le calcul du parquet, la condamnée ne sera "
         "pas libérable avant 2035. La défense indique ne pas faire appel.",
         "The sentence merges with earlier convictions. According to the prosecution's calculation, the convict will "
         "not be eligible for release before 2035. The defence states it will not appeal.",
         "CONFIRMED", "franceinfo-2023", "Cumul des peines", "Accumulation of sentences", "2023-12"),
    fact("Monique Olivier est placée en garde à vue dans le dossier de la disparition de Cécile Vallin en 1997 en "
         "Savoie ; la garde à vue est levée après dix heures.",
         "Monique Olivier is placed in police custody in the file of Cécile Vallin's 1997 disappearance in Savoie; "
         "the custody is lifted after ten hours.",
         "CONFIRMED", "franceinfo-cecile-vallin", "Suites judiciaires", "Further proceedings", "2025-09"),
]

LOCATIONS = [
    {"kind": "region", "names": txt("Ardennes (France)", "Ardennes (France)"), "city": "", "region": "Grand Est",
     "country": "FR", "lat": 49.6, "lon": 4.6, "precision": "region", "date": "1987-2003",
     "note": txt("Secteur associé à plusieurs faits. Aucune adresse n'est publiée.",
                 "Area associated with several offences. No address is published."),
     "reliability": "CONFIRMED", "source": "radiofrance-olivier"},
    {"kind": "country", "names": txt("Belgique", "Belgium"), "city": "", "region": "", "country": "BE",
     "lat": 50.5, "lon": 4.5, "precision": "region", "date": "1987-2001",
     "note": txt("Des faits retenus dans la condamnation de 2008 ont été commis entre la France et la Belgique.",
                 "Offences retained in the 2008 conviction were committed between France and Belgium.",),
     "reliability": "CONFIRMED", "source": "radiofrance-olivier"},
    {"kind": "court", "names": txt("Cour d'assises des Hauts-de-Seine, Nanterre", "Hauts-de-Seine Assize Court, Nanterre"),
     "city": "Nanterre", "region": "Hauts-de-Seine", "country": "FR", "lat": 48.89, "lon": 2.20,
     "precision": "city", "date": "2023-12-19",
     "note": txt("Procès du 28 novembre au 19 décembre 2023.", "Trial from 28 November to 19 December 2023."),
     "reliability": "CONFIRMED", "source": "franceinfo-2023"},
]

EVIDENCE = [
    {"kind": "testimony", "weight": "decisive", "reliability": "CONFIRMED", "source": "franceinfo-2023",
     "title": txt("Les déclarations de la complice", "The accomplice's statements"),
     "description": txt(
         "Les accusations portées par Monique Olivier, puis ses précisions sur le lieu de séquestration et sur le "
         "transport du corps, constituent l'élément central du dossier Estelle Mouzin. Elles ont été recueillies en "
         "instruction puis confirmées à l'audience.",
         "The accusations made by Monique Olivier, then her precisions on the place of confinement and on the "
         "transport of the body, constitute the central element of the Estelle Mouzin file. They were collected during "
         "the investigation then confirmed at the hearing.")},
    {"kind": "dna", "weight": "decisive", "reliability": "CONFIRMED", "source": "franceinfo-2023",
     "title": txt("Trace d'ADN partiel sur un matelas", "Partial DNA trace on a mattress"),
     "description": txt(
         "Une trace d'ADN partiel d'Estelle Mouzin a été identifiée en août 2020 sur un matelas saisi en 2003 dans la "
         "maison de Ville-sur-Lumes. Ce scellé avait été conservé dix-sept ans.",
         "A partial DNA trace of Estelle Mouzin was identified in August 2020 on a mattress seized in 2003 in the "
         "Ville-sur-Lumes house. That exhibit had been kept for seventeen years.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "actu-proces-2023",
     "title": txt("L'extinction de l'action publique", "The extinguishment of public prosecution"),
     "description": txt(
         "La mort de Michel Fourniret le 10 mai 2021 a éteint l'action publique à son égard : seule la complice a pu "
         "être jugée. L'avocat de la famille Mouzin a publiquement regretté que l'auteur principal échappe à un "
         "procès pour ces faits.",
         "The death of Michel Fourniret on 10 May 2021 extinguished public prosecution with respect to him: only the "
         "accomplice could be tried. The Mouzin family lawyer publicly regretted that the principal author escaped a "
         "trial for these facts.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "franceinfo-2023",
     "title": txt("Motivations de la cour", "The court's reasoning"),
     "description": txt(
         "La cour a décrit une implication « totale » dans des faits d'une « extrême gravité » visant deux jeunes "
         "femmes et une enfant de 9 ans « séquestrée dans des circonstances inhumaines », et une personnalité "
         "« sans empathie » ni « affect pour des victimes déshumanisées ».",
         "The court described 'total' involvement in facts of 'extreme gravity' targeting two young women and a "
         "9-year-old child 'confined in inhuman circumstances', and a personality 'without empathy' or 'affect for "
         "dehumanised victims'.")},
]

INVESTIGATION = {
    "steps": [
        {"n": 1, "date": "1987", "title": txt("Une rencontre par correspondance", "A meeting by correspondence"),
         "body": txt("Monique Olivier rencontre Michel Fourniret alors qu'il est incarcéré. Cette relation est le "
                     "point de départ de tout le dossier de complicité.",
                     "Monique Olivier meets Michel Fourniret while he is imprisoned. That relationship is the "
                     "starting point of the whole complicity file."),
         "reliability": "CONFIRMED", "source": "radiofrance-olivier", "premium": False},
        {"n": 2, "date": "1987-2003", "title": txt("Une série entre deux pays", "A series across two countries"),
         "body": txt("Des faits sont commis entre la France et la Belgique. La justice française en jugera une partie "
                     "en 2008, une autre en 2018, une troisième en 2023.",
                     "Offences are committed between France and Belgium. French justice would try part of them in "
                     "2008, another part in 2018, a third in 2023."),
         "reliability": "CONFIRMED", "source": "radiofrance-olivier", "premium": False},
        {"n": 3, "date": "2003-01-09", "title": txt("Un dernier fait : Estelle Mouzin", "A last offence: Estelle Mouzin"),
         "body": txt("Estelle Mouzin, 9 ans, disparaît à Guermantes. Ce fait ne sera rattaché au couple que dix-sept "
                     "ans plus tard. Un dossier distinct lui est consacré dans cette application.",
                     "Estelle Mouzin, 9, disappears in Guermantes. This offence would be linked to the couple only "
                     "seventeen years later. A separate file is devoted to her in this application."),
         "reliability": "CONFIRMED", "source": "ici-olivier-2023", "premium": False},
        {"n": 4, "date": "2008-05", "title": txt("Une première condamnation pour complicité", "A first conviction for complicity"),
         "body": txt("La cour d'assises des Ardennes prononce la réclusion criminelle à perpétuité avec 28 ans de "
                     "sûreté, pour complicité dans le meurtre de sept jeunes femmes ou adolescentes.",
                     "The Ardennes assize court pronounces life imprisonment with a 28-year minimum term, for "
                     "complicity in the murder of seven young women or teenagers."),
         "reliability": "CONFIRMED", "source": "radiofrance-olivier", "premium": True},
        {"n": 5, "date": "2018", "title": txt("Une deuxième condamnation", "A second conviction"),
         "body": txt("La cour d'assises des Yvelines prononce 20 ans de réclusion pour complicité dans le meurtre de "
                     "Farida Hammiche.",
                     "The Yvelines assize court pronounces 20 years for complicity in the murder of Farida Hammiche."),
         "reliability": "CONFIRMED", "source": "ici-olivier-2023", "premium": True},
        {"n": 6, "date": "2020", "title": txt("Une parole qui déverrouille trois dossiers", "A statement that unlocks three files"),
         "body": txt("Ses accusations, puis ses précisions sur le lieu de séquestration et le transport du corps, "
                     "permettent de rattacher trois affaires : Estelle Mouzin, Joanna Parrish, Marie-Angèle Domèce.",
                     "Her accusations, then her precisions on the place of confinement and the transport of the body, "
                     "allow three cases to be linked: Estelle Mouzin, Joanna Parrish, Marie-Angèle Domèce."),
         "reliability": "CONFIRMED", "source": "franceinfo-2023", "premium": False},
        {"n": 7, "date": "2021-05-10", "title": txt("Un procès devient impossible pour l'auteur principal",
                                                     "A trial becomes impossible for the principal author"),
         "body": txt("Michel Fourniret meurt en détention. L'action publique est éteinte à son égard : il ne sera "
                     "jamais jugé pour les faits concernant Estelle Mouzin.",
                     "Michel Fourniret dies in custody. Public prosecution is extinguished with respect to him: he "
                     "will never be tried for the facts concerning Estelle Mouzin."),
         "reliability": "CONFIRMED", "source": "actu-proces-2023", "premium": True},
        {"n": 8, "date": "2023-12-19", "title": txt("Trois semaines d'audience, onze heures de délibéré",
                                                     "Three weeks of hearing, eleven hours of deliberation"),
         "body": txt("La cour d'assises des Hauts-de-Seine condamne Monique Olivier à la perpétuité avec 20 ans de "
                     "sûreté. Le parquet avait requis la peine maximale, soit 22 ans de sûreté.",
                     "The Hauts-de-Seine assize court sentences Monique Olivier to life with a 20-year minimum term. "
                     "The prosecution had requested the maximum penalty, i.e. a 22-year minimum term."),
         "reliability": "CONFIRMED", "source": "franceinfo-2023", "premium": False},
        {"n": 9, "date": "2025-09", "title": txt("D'autres dossiers encore ouverts", "Other files still open"),
         "body": txt("Elle est placée en garde à vue dans le dossier de la disparition de Cécile Vallin en 1997 en "
                     "Savoie ; la mesure est levée après dix heures.",
                     "She is placed in police custody in the file of Cécile Vallin's 1997 disappearance in Savoie; "
                     "the measure is lifted after ten hours."),
         "reliability": "CONFIRMED", "source": "franceinfo-cecile-vallin", "premium": True},
    ],
    "reality": txt(
        "Ce dossier s'est construit par vagues judiciaires successives : 2008, 2018, 2023. Chaque vague a porté sur "
        "un ensemble distinct de faits, et la dernière n'a pu juger que la complicité, l'auteur principal étant "
        "décédé. Des investigations se poursuivent sur d'autres disparitions.",
        "This file was built through successive judicial waves: 2008, 2018, 2023. Each wave concerned a distinct set "
        "of facts, and the last one could only try complicity, the principal author having died. Investigations "
        "continue on other disappearances."),
    "errors": [
        item("Dans le dossier Estelle Mouzin, la piste a été envisagée dès 2003 puis écartée : l'État a été condamné "
             "pour faute lourde le 3 septembre 2025.",
             "In the Estelle Mouzin file, the lead was considered as early as 2003 then set aside: the State was "
             "condemned for gross negligence on 3 September 2025.",
             "CONFIRMED", "franceinfo-cecile-vallin", "Voir le dossier dédié", "See the dedicated file"),
    ],
    "cold_case": {
        "what_we_know": [
            item("Trois condamnations pour complicité : 2008, 2018, 2023.",
                 "Three convictions for complicity: 2008, 2018, 2023.", "CONFIRMED", "radiofrance-olivier"),
            item("Neuf victimes au moins retenues au total dans ces condamnations (sept en 2008, une en 2018, trois "
                 "en 2023, dont Estelle Mouzin).",
                 "At least nine victims retained in total in these convictions (seven in 2008, one in 2018, three in "
                 "2023, including Estelle Mouzin).", "CONFIRMED", "franceinfo-2023"),
        ],
        "what_is_probable": [
            item("D'autres dossiers de disparition restent examinés, dont celui de Cécile Vallin (1997, Savoie).",
                 "Other disappearance files remain under examination, including that of Cécile Vallin (1997, Savoie).",
                 "PROBABLE", "franceinfo-cecile-vallin"),
        ],
        "what_is_disputed": [
            item("L'âge de Joanna Parrish : 20 ans selon franceinfo, 21 ans selon ICI.",
                 "Joanna Parrish's age: 20 according to franceinfo, 21 according to ICI.", "DISPUTED", "ici-olivier-2023"),
            item("La qualification de la complice : la cour a écarté la description d'une épouse « passive » ou "
                 "« soumise » retenue par certains experts-psychologues.",
                 "The characterisation of the accomplice: the court rejected the description of a 'passive' or "
                 "'submissive' wife retained by some expert psychologists.", "DISPUTED", "franceinfo-2023"),
        ],
        "what_is_unknown": [
            item("Les identités et parcours des victimes des condamnations de 2008 et 2018, dans les sources "
                 "consultées pour ce dossier.",
                 "The identities and lives of the victims of the 2008 and 2018 convictions, in the sources consulted "
                 "for this file.", "UNKNOWN", "radiofrance-olivier"),
            item("Le lieu où se trouve le corps d'Estelle Mouzin.", "The location of Estelle Mouzin's body.",
                 "UNKNOWN", "ici-olivier-2023"),
        ],
        "latest_progress": [
            item("Septembre 2025 : garde à vue de Monique Olivier dans le dossier Cécile Vallin, levée après dix heures.",
                 "September 2025: police custody of Monique Olivier in the Cécile Vallin file, lifted after ten hours.",
                 "CONFIRMED", "franceinfo-cecile-vallin"),
        ],
        "leads": [
            item("Des disparitions anciennes en Savoie et dans les Ardennes font l'objet de vérifications.",
                 "Old disappearances in Savoie and the Ardennes are subject to checks.", "PROBABLE", "franceinfo-cecile-vallin"),
        ],
        "limits": [
            item("L'auteur principal est décédé : plus aucune audience ne permettra d'obtenir son récit.",
                 "The principal author is dead: no hearing will ever obtain his account.", "CONFIRMED", "actu-proces-2023"),
        ],
    },
}

PSYCHOLOGY = {
    "disclaimer": txt("Aucun diagnostic n'est posé. La qualification de la personnalité de la condamnée relève ici de "
                      "la cour d'assises, pas de l'application.",
                      "No diagnosis is made. The characterisation of the convict's personality belongs here to the "
                      "assize court, not to the application."),
    "blocks": [
        block("expert", "Deux lectures opposées de la même personne", "Two opposed readings of the same person",
              "Certains experts-psychologues avaient décrit une épouse « passive » et « soumise ». Le parquet et la "
              "cour ont retenu au contraire une « complice active », fustigeant son « silence » et son "
              "« indifférence ». Ces deux lectures ont coexisté dans le même procès.",
              "Some expert psychologists had described a 'passive' and 'submissive' wife. The prosecution and the "
              "court retained instead an 'active accomplice', condemning her 'silence' and 'indifference'. These two "
              "readings coexisted in the same trial.",
              "CONFIRMED", "franceinfo-2023"),
        block("fact", "Une relation construite en détention", "A relationship built in custody",
              "La rencontre a eu lieu par correspondance alors que Michel Fourniret était incarcéré, en 1987. C'est "
              "un fait documenté, qui éclaire la structure de la relation sans l'expliquer.",
              "The meeting took place by correspondence while Michel Fourniret was imprisoned, in 1987. This is a "
              "documented fact, which illuminates the structure of the relationship without explaining it.",
              "CONFIRMED", "radiofrance-olivier"),
        block("behaviour", "Ce que la cour a retenu du comportement", "What the court retained of the behaviour",
              "La cour a relevé une implication « totale » dans les faits, une absence d'empathie et une "
              "« déshumanisation » des victimes. Elle a aussi reconnu une « tentative de questionnement » de la "
              "condamnée. Ces deux éléments figurent dans le même compte rendu d'audience.",
              "The court noted 'total' involvement in the facts, an absence of empathy and a 'dehumanisation' of the "
              "victims. It also recognised an 'attempt at questioning' by the convict. Both elements appear in the "
              "same hearing report.",
              "CONFIRMED", "ici-olivier-2023"),
        block("unknown", "Ce qui n'est pas établi", "What is not established",
              "Les raisons pour lesquelles elle n'a pas dénoncé les faits plus tôt ne sont pas établies par les "
              "sources consultées ; son avocat a lui-même évoqué cette question à l'audience.",
              "The reasons why she did not report the facts earlier are not established by the sources consulted; her "
              "own lawyer raised that question at the hearing.",
              "UNKNOWN", "actu-proces-2023"),
    ],
}

VICTIMOLOGY = {
    "ethics_note": txt("Aucune caractéristique des victimes n'explique moralement les crimes.",
                       "No characteristic of the victims morally explains the crimes."),
    "blocks": [
        block("context", "Des jeunes femmes et une enfant", "Young women and a child",
              "Les victimes retenues dans le procès de 2023 étaient deux jeunes femmes de 19 et 20 ou 21 ans, et une "
              "enfant de 9 ans. Celles de 2008 étaient sept jeunes femmes ou adolescentes.",
              "The victims retained in the 2023 trial were two young women of 19 and 20 or 21, and a 9-year-old "
              "child. Those of 2008 were seven young women or teenagers.",
              "CONFIRMED", "franceinfo-2023"),
        block("analysis", "Ce que la victimologie documente ici", "What victimology documents here",
              "La répartition des faits entre la France et la Belgique, et l'étalement sur seize ans, décrivent un "
              "périmètre géographique large et une série longue. Ces éléments servent à comprendre le fonctionnement "
              "du couple, pas à caractériser les victimes.",
              "The spread of the offences between France and Belgium, and their extension over sixteen years, "
              "describe a wide geographic perimeter and a long series. These elements serve to understand how the "
              "couple operated, not to characterise the victims.",
              "CONFIRMED", "radiofrance-olivier"),
    ],
}

COURT = {
    "jurisdiction": txt("France — cours d'assises des Ardennes (2008), des Yvelines (2018), des Hauts-de-Seine (2023)",
                        "France — Ardennes (2008), Yvelines (2018) and Hauts-de-Seine (2023) assize courts"),
    "verdict": txt("Coupable de complicité dans l'enlèvement, la séquestration et la mort d'Estelle Mouzin, de "
                   "Joanna Parrish et de Marie-Angèle Domèce (19 décembre 2023). Michel Fourniret, décédé en 2021, "
                   "n'a été jugé pour aucun de ces faits.",
                   "Guilty of complicity in the abduction, confinement and death of Estelle Mouzin, Joanna Parrish "
                   "and Marie-Angèle Domèce (19 December 2023). Michel Fourniret, who died in 2021, was tried for "
                   "none of these facts."),
    "sentence": {
        "label": txt("Réclusion criminelle à perpétuité, période de sûreté de 20 ans",
                     "Life imprisonment with a 20-year minimum term"),
        "pronounced": "2023-12-19",
        "requested": txt("Le parquet avait requis la peine maximale encourue, soit la perpétuité assortie de 22 ans "
                         "de sûreté.",
                         "The prosecution had requested the maximum incurred penalty, i.e. life with a 22-year "
                         "minimum term."),
        "cumul": txt("Trois condamnations : perpétuité avec 28 ans de sûreté (2008), 20 ans (2018), perpétuité avec "
                     "20 ans de sûreté (2023). Les peines se confondent ; selon le calcul du parquet, la condamnée ne "
                     "sera pas libérable avant 2035.",
                     "Three convictions: life with a 28-year minimum term (2008), 20 years (2018), life with a 20-year "
                     "minimum term (2023). The sentences merge; according to the prosecution's calculation, the "
                     "convict will not be eligible for release before 2035."),
        "reasoning": txt("La cour a qualifié la peine de « juste, adéquate et proportionnée à l'extrême gravité des "
                         "faits où son implication est totale ».",
                         "The court described the sentence as 'fair, adequate and proportionate to the extreme "
                         "gravity of facts in which her involvement is total'."),
        "appeal": txt("La défense a indiqué ne pas faire appel, pour ne pas « infliger un second procès aux parties "
                      "civiles ».",
                      "The defence stated it would not appeal, so as not to 'inflict a second trial on the civil "
                      "parties'."),
        "reliability": "CONFIRMED", "source": "franceinfo-2023",
    },
    "consequences": [
        item("La mort de l'auteur principal a privé les familles d'un procès le concernant : c'est une conséquence "
             "directe de l'extinction de l'action publique.",
             "The death of the principal author deprived the families of a trial concerning him: this is a direct "
             "consequence of the extinguishment of public prosecution.",
             "CONFIRMED", "actu-proces-2023"),
        item("Des investigations se poursuivent sur d'autres disparitions, dont celle de Cécile Vallin en 1997.",
             "Investigations continue on other disappearances, including that of Cécile Vallin in 1997.",
             "CONFIRMED", "franceinfo-cecile-vallin"),
        item("L'État a été condamné pour faute lourde le 3 septembre 2025 dans le volet Estelle Mouzin.",
             "The State was condemned for gross negligence on 3 September 2025 in the Estelle Mouzin part of the case.",
             "CONFIRMED", "franceinfo-cecile-vallin"),
    ],
}

EXPERTS = [
    {"label": txt("Lecture des experts-psychologues", "Expert psychologists' reading"), "field": "psychology",
     "position": txt("Une épouse décrite comme « passive » et « soumise ».", "A wife described as 'passive' and 'submissive'."),
     "reliability": "DISPUTED", "source": "franceinfo-2023"},
    {"label": txt("Lecture du parquet", "The prosecution's reading"), "field": "judicial",
     "position": txt("Une « complice active », dont le « silence » et l'« indifférence » ont été fustigés.",
                     "An 'active accomplice', whose 'silence' and 'indifference' were condemned."),
     "reliability": "CONFIRMED", "source": "franceinfo-2023"},
    {"label": txt("Lecture de la cour", "The court's reading"), "field": "judicial",
     "position": txt("Une implication « totale », une personnalité « sans empathie » ni « affect pour des victimes "
                     "déshumanisées », mais aussi une « tentative de questionnement » reconnue.",
                     "'Total' involvement, a personality 'without empathy' or 'affect for dehumanised victims', but "
                     "also a recognised 'attempt at questioning'."),
     "reliability": "CONFIRMED", "source": "franceinfo-2023"},
]
EXPERTS_AGREEMENT = txt("Toutes les lectures s'accordent sur la matérialité de la complicité, établie par la cour.",
                        "All readings agree on the materiality of the complicity, established by the court.")
EXPERTS_DISAGREEMENT = txt("Elles divergent sur la qualification de la personne : passive ou active.",
                           "They differ on the characterisation of the person: passive or active.")
EXPERTS_UNCERTAIN = txt("Ce qui reste incertain : les raisons de son silence pendant des années.",
                        "What remains uncertain: the reasons for her silence over the years.")

COUNTERFACTUALS = [
    counterfactual(
        "sentence",
        "Et si les peines prononcées avaient été exécutées sans confusion ?",
        "What if the sentences pronounced had been served without merger?",
        "Trois condamnations ont été prononcées : 2008 (perpétuité, 28 ans de sûreté), 2018 (20 ans), 2023 "
        "(perpétuité, 20 ans de sûreté). Les peines se confondent. Selon le calcul du parquet, la date de libération "
        "possible la plus proche est 2035.",
        "Three convictions were pronounced: 2008 (life, 28-year minimum term), 2018 (20 years), 2023 (life, 20-year "
        "minimum term). The sentences merge. According to the prosecution's calculation, the earliest possible "
        "release date is 2035.",
        {
            "unit": "years",
            "conviction_date": "2008-05-28",
            "sentence": {"type": "life_with_minimum_term", "minimum_term_years": 28, "label_fr": "Réclusion criminelle à perpétuité, sûreté de 28 ans", "label_en": "Life imprisonment with a 28-year minimum term"},
            "reference_event": {"label": txt("Première condamnation", "First conviction"), "date": "2008-05-28"},
            "hypothesis": {"label": txt("Fin théorique de la période de sûreté", "Theoretical end of the minimum term"), "date": "2036-05-28"},
            "scenario_event": {"label": txt("Deuxième condamnation (20 ans)", "Second conviction (20 years)"), "date": "2018-01-01"},
            "outcome_event": {"label": txt("Troisième condamnation, peines confondues", "Third conviction, merged sentences"), "date": "2023-12-19"},
            "actual_release": {"label": txt("Non libérable avant 2035 (calcul du parquet)", "Not eligible for release before 2035 (prosecution's calculation)"), "date": "2035-01-01"},
            "documented_offences_after": [],
            "jurisdiction_note": txt(
                "En droit français, la période de sûreté interdit toute mesure d'aménagement de peine pendant sa "
                "durée ; elle ne fixe pas une date de sortie. En cas de condamnations multiples, les peines peuvent "
                "se confondre. La date de 2035 est un calcul du parquet rapporté par la presse, pas une décision de "
                "libération : aucune libération n'est acquise à cette date, et son examen relèverait du juge de "
                "l'application des peines.",
                "In French law, the minimum term prohibits any sentence-adjustment measure during its duration; it "
                "does not set a release date. In cases of multiple convictions, sentences may merge. The 2035 date is "
                "a prosecution calculation reported by the press, not a release decision: no release is acquired at "
                "that date, and its examination would belong to the sentence-enforcement judge."),
        },
        [
            {"date": "2008-05-28", "kind": "reference", "label": txt("Condamnation 1 : perpétuité, sûreté 28 ans", "Conviction 1: life, 28-year minimum term")},
            {"date": "2018-01-01", "kind": "scenario", "label": txt("Condamnation 2 : 20 ans", "Conviction 2: 20 years")},
            {"date": "2023-12-19", "kind": "outcome", "label": txt("Condamnation 3 : perpétuité, sûreté 20 ans", "Conviction 3: life, 20-year minimum term")},
            {"date": "2035-01-01", "kind": "fact", "label": txt("Date de libération possible la plus proche (calcul du parquet)", "Earliest possible release date (prosecution's calculation)")},
            {"date": "2036-05-28", "kind": "hypothesis", "label": txt("Fin théorique de la sûreté de 2008", "Theoretical end of the 2008 minimum term")},
        ],
        True, "franceinfo-2023"),
    counterfactual(
        "denunciation",
        "Et si la complice avait parlé avant 2020 ?",
        "What if the accomplice had spoken before 2020?",
        "Les accusations de Monique Olivier concernant Estelle Mouzin sont intervenues en janvier 2020, dix-sept ans "
        "après la disparition. La condamnation de 2008 portait sur d'autres faits.",
        "Monique Olivier's accusations concerning Estelle Mouzin came in January 2020, seventeen years after the "
        "disappearance. The 2008 conviction concerned other facts.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Disparition d'Estelle Mouzin", "Disappearance of Estelle Mouzin"), "date": "2003-01-09"},
            "hypothesis": {"label": txt("Aucune déclaration sur ce fait", "No statement on this offence"), "date": "2019-12-31"},
            "scenario_event": {"label": txt("Premières accusations", "First accusations"), "date": "2020-01-01"},
            "outcome_event": {"label": txt("Condamnation pour complicité", "Conviction for complicity"), "date": "2023-12-19"},
            "documented_offences_after": [],
            "jurisdiction_note": txt(
                "Aucun fait nouveau n'est documenté après le 9 janvier 2003 dans les sources consultées : ce scénario "
                "ne permet donc pas de compter des victimes supplémentaires épargnées. Il mesure un délai "
                "d'information de la justice, et ses conséquences sur la recherche du corps.",
                "No new offence is documented after 9 January 2003 in the sources consulted: this scenario therefore "
                "does not allow additional spared victims to be counted. It measures a delay in informing justice, "
                "and its consequences for the search for the body."),
        },
        [
            {"date": "2003-01-09", "kind": "reference", "label": txt("Disparition", "Disappearance")},
            {"date": "2008-05-28", "kind": "fact", "label": txt("Condamnation pour d'autres faits", "Conviction for other facts")},
            {"date": "2020-01-01", "kind": "scenario", "label": txt("Premières accusations sur Estelle Mouzin", "First accusations on Estelle Mouzin")},
            {"date": "2020-08-21", "kind": "fact", "label": txt("ADN partiel identifié", "Partial DNA identified")},
            {"date": "2023-12-19", "kind": "outcome", "label": txt("Condamnation", "Conviction")},
        ],
        True, "franceinfo-2023"),
]

LESSONS = [
    item("La complicité est un objet juridique autonome : elle peut être jugée alors que l'auteur principal ne peut "
         "plus l'être.",
         "Complicity is an autonomous legal object: it can be tried when the principal author can no longer be.",
         "CONFIRMED", "actu-proces-2023", "Droit pénal", "Criminal law"),
    item("La mort d'un mis en cause éteint l'action publique : les familles obtiennent un procès, mais pas celui "
         "qu'elles attendaient.",
         "The death of an indicted person extinguishes public prosecution: families obtain a trial, but not the one "
         "they expected.",
         "CONFIRMED", "actu-proces-2023", "Limites de la justice", "Limits of justice"),
    item("Des condamnations successives peuvent porter sur des ensembles de faits distincts : la chronologie "
         "judiciaire n'est pas linéaire.",
         "Successive convictions can concern distinct sets of facts: the judicial chronology is not linear.",
         "CONFIRMED", "radiofrance-olivier", "Procédure", "Procedure"),
    item("Une expertise psychologique et une décision de justice peuvent aboutir à des qualifications opposées de la "
         "même personne.",
         "A psychological evaluation and a court decision can reach opposed characterisations of the same person.",
         "CONFIRMED", "franceinfo-2023", "Expertise et jugement", "Expertise and judgement"),
    item("Le cumul et la confusion des peines déterminent une date de libération possible qui n'est jamais une "
         "libération acquise.",
         "Accumulation and merger of sentences determine a possible release date that is never an acquired release.",
         "CONFIRMED", "franceinfo-2023", "Exécution des peines", "Sentence enforcement"),
]

UNKNOWNS = [
    item("Les identités des victimes des condamnations de 2008 et 2018, dans les sources consultées ici.",
         "The identities of the victims of the 2008 and 2018 convictions, in the sources consulted here.",
         "UNKNOWN", "radiofrance-olivier"),
    item("Les raisons du silence de la condamnée pendant des années.", "The reasons for the convict's silence over the years.",
         "UNKNOWN", "actu-proces-2023"),
    item("Le lieu où se trouve le corps d'Estelle Mouzin.", "The location of Estelle Mouzin's body.",
         "UNKNOWN", "ici-olivier-2023"),
    item("Les suites du dossier Cécile Vallin.", "The follow-up to the Cécile Vallin file.",
         "UNKNOWN", "franceinfo-cecile-vallin"),
]

SECTIONS = merge_sections(default_sections(), [
    {"key": "introduction", "blocks": [block(
        "paragraph", "Un dossier de complicité", "A complicity file",
        "Ce dossier ne raconte pas un tueur : il documente une complicité jugée trois fois, en 2008, 2018 et 2023, et "
        "ce que la justice peut établir lorsque l'auteur principal meurt avant d'être jugé.",
        "This file does not tell the story of a killer: it documents a complicity tried three times, in 2008, 2018 "
        "and 2023, and what justice can establish when the principal author dies before being tried.",
        "CONFIRMED", "actu-proces-2023")]},
    {"key": "context", "blocks": [block(
        "paragraph", "France et Belgique, 1987-2003", "France and Belgium, 1987-2003",
        "Les faits retenus s'étendent sur seize ans et deux pays. Cette étendue explique la fragmentation judiciaire : "
        "plusieurs cours d'assises, plusieurs époques, plusieurs ensembles de victimes.",
        "The retained offences extend over sixteen years and two countries. That extent explains the judicial "
        "fragmentation: several assize courts, several periods, several sets of victims.",
        "CONFIRMED", "radiofrance-olivier")]},
    {"key": "offender", "blocks": [block(
        "paragraph", "Deux personnes, deux situations pénales", "Two persons, two penal situations",
        "Michel Fourniret, né en 1942, mort en détention le 10 mai 2021 à 79 ans, condamné en 2008 à la perpétuité "
        "pour sept meurtres et en 2018 à 20 ans. Monique Olivier, née le 31 octobre 1948, condamnée trois fois pour "
        "complicité, non libérable avant 2035 selon le calcul du parquet.",
        "Michel Fourniret, born in 1942, died in custody on 10 May 2021 aged 79, sentenced in 2008 to life for seven "
        "murders and in 2018 to 20 years. Monique Olivier, born on 31 October 1948, convicted three times for "
        "complicity, not eligible for release before 2035 according to the prosecution's calculation.",
        "CONFIRMED", "radiofrance-olivier")]},
    {"key": "behaviour", "blocks": [block(
        "behaviour", "La complicité comme comportement documenté", "Complicity as a documented behaviour",
        "Les actes retenus sont des actes de complicité : participation à des enlèvements, séquestration, transport "
        "du corps d'Estelle Mouzin selon ses propres déclarations. La cour a écarté la qualification d'épouse passive.",
        "The acts retained are acts of complicity: participation in abductions, confinement, transport of Estelle "
        "Mouzin's body according to her own statements. The court rejected the characterisation of a passive wife.",
        "CONFIRMED", "franceinfo-2023")]},
    {"key": "consequences", "blocks": [block(
        "paragraph", "Des dossiers encore ouverts", "Files still open",
        "La condamnation de 2023 n'a pas clos l'ensemble : des investigations se poursuivent, notamment sur la "
        "disparition de Cécile Vallin en 1997 en Savoie, et le volet civil de l'affaire Estelle Mouzin a abouti à une "
        "condamnation de l'État en 2025.",
        "The 2023 conviction did not close everything: investigations continue, notably on the disappearance of Cécile "
        "Vallin in 1997 in Savoie, and the civil part of the Estelle Mouzin case led to a State condemnation in 2025.",
        "CONFIRMED", "franceinfo-cecile-vallin")]},
])

EPISODES = [
    {
        "number": 1,
        "title": txt("La complice", "The accomplice"),
        "description": txt("Trois procès, trois époques, une même qualification : complicité. Ce que la justice peut "
                           "établir quand l'auteur principal est mort.",
                           "Three trials, three periods, one same qualification: complicity. What justice can "
                           "establish when the principal author is dead."),
        "modes": ["documentary", "investigation", "chronology", "express", "expert", "psychology", "victims"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 60, "title": txt("1987 : une correspondance", "1987: a correspondence")},
            {"at": 220, "title": txt("2008, 2018, 2023", "2008, 2018, 2023")},
            {"at": 420, "title": txt("Un procès sans l'auteur", "A trial without the author")},
            {"at": 580, "title": txt("Et maintenant, une question", "And now, a question")},
        ],
        "transcript": {"segments": [
            {"id": "f1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X, à travers mon regard. Cet épisode ne parle pas d'un tueur en série. Il "
                     "parle d'une qualification juridique : la complicité. Et d'une question : que reste-t-il à juger "
                     "quand l'auteur principal est mort ?",
             "text_en": "You are on YANIS//X, through my eyes. This episode is not about a serial killer. It is about "
                        "a legal qualification: complicity. And about a question: what is left to try when the "
                        "principal author is dead?"},
            {"id": "f2", "t": 60, "speaker": "yanis",
             "text": "1987. Monique Olivier, née le 31 octobre 1948, correspond avec un homme incarcéré : Michel "
                     "Fourniret. Cette correspondance devient une relation. Ce qui suit s'étend sur seize ans, entre "
                     "la France et la Belgique.",
             "text_en": "1987. Monique Olivier, born on 31 October 1948, corresponds with an imprisoned man: Michel "
                        "Fourniret. That correspondence becomes a relationship. What follows extends over sixteen "
                        "years, between France and Belgium."},
            {"id": "f3", "t": 220, "speaker": "yanis",
             "text": "Mai 2008 : la cour d'assises des Ardennes la condamne à la réclusion criminelle à perpétuité, "
                     "avec vingt-huit ans de sûreté, pour complicité dans le meurtre de sept jeunes femmes ou "
                     "adolescentes. 2018 : la cour d'assises des Yvelines prononce vingt ans de réclusion pour "
                     "complicité dans le meurtre de Farida Hammiche. Trois condamnations, trois ensembles de faits.",
             "text_en": "May 2008: the Ardennes assize court sentences her to life imprisonment with a twenty-eight "
                        "year minimum term, for complicity in the murder of seven young women or teenagers. 2018: the "
                        "Yvelines assize court pronounces twenty years for complicity in the murder of Farida "
                        "Hammiche. Three convictions, three sets of facts."},
            {"id": "f4", "t": 420, "speaker": "yanis",
             "text": "Puis vient le procès de Nanterre, du 28 novembre au 19 décembre 2023. Michel Fourniret est mort "
                     "le 10 mai 2021 : en droit français, la mort éteint l'action publique. Il ne sera jugé pour "
                     "aucun de ces faits. Dans le box, il n'y a qu'une personne. On y juge la complicité dans "
                     "l'enlèvement, la séquestration et la mort de trois victimes : Marie-Angèle Domèce, dix-neuf "
                     "ans ; Joanna Parrish, vingt ou vingt et un ans ; Estelle Mouzin, neuf ans.",
             "text_en": "Then comes the Nanterre trial, from 28 November to 19 December 2023. Michel Fourniret died on "
                        "10 May 2021: under French law, death extinguishes public prosecution. He will be tried for "
                        "none of these facts. In the dock, there is only one person. Complicity is tried in the "
                        "abduction, confinement and death of three victims: Marie-Angèle Domèce, nineteen; Joanna "
                        "Parrish, twenty or twenty-one; Estelle Mouzin, nine."},
            {"id": "f5", "t": 560, "speaker": "yanis",
             "text": "La cour retient une implication totale, une personnalité sans empathie, des victimes "
                     "déshumanisées. Elle écarte la description d'une épouse passive ou soumise qu'avaient retenue "
                     "certains experts-psychologues. Elle reconnaît aussi une tentative de questionnement. Verdict : "
                     "la perpétuité, avec vingt ans de sûreté. Le parquet avait requis vingt-deux. Les peines se "
                     "confondent avec les condamnations antérieures : selon le calcul du parquet, elle ne sera pas "
                     "libérable avant 2035.",
             "text_en": "The court finds total involvement, a personality without empathy, dehumanised victims. It "
                        "rejects the description of a passive or submissive wife retained by some expert "
                        "psychologists. It also recognises an attempt at questioning. Verdict: life, with a "
                        "twenty-year minimum term. The prosecution had requested twenty-two. The sentences merge with "
                        "earlier convictions: according to the prosecution's calculation, she will not be eligible for "
                        "release before 2035."},
            {"id": "f6", "t": 580, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "f7", "t": 620, "speaker": "yanis",
             "text": "Ses derniers mots devant la cour ont été : « Je confirme ce que j'ai dit et je regrette tout ce "
                     "que j'ai fait. » Son avocat a dit qu'il ne ferait pas appel, pour ne pas infliger un second "
                     "procès aux parties civiles. En septembre 2025, elle était encore entendue : dix heures de garde "
                     "à vue dans le dossier de la disparition de Cécile Vallin, en 1997, en Savoie.",
             "text_en": "Her last words before the court were: 'I confirm what I said and I regret everything I did.' "
                        "Her lawyer said he would not appeal, so as not to inflict a second trial on the civil "
                        "parties. In September 2025, she was still being heard: ten hours in police custody in the "
                        "file of Cécile Vallin's disappearance, in 1997, in Savoie."},
            {"id": "f8", "t": 780, "speaker": "yanis",
             "text": "Marie-Angèle Domèce avait dix-neuf ans. Joanna Parrish en avait vingt ou vingt et un. Estelle "
                     "Mouzin en avait neuf. Écouter les histoires. Comprendre les affaires. Ne jamais oublier les "
                     "victimes.",
             "text_en": "Marie-Angèle Domèce was nineteen. Joanna Parrish was twenty or twenty-one. Estelle Mouzin was "
                        "nine. Listen to the stories. Understand the cases. Never forget the victims."},
        ]},
    },
]

QUESTIONS = [
    question("1", 580, "investigation",
             "L'auteur principal meurt avant d'être jugé pour certains faits. Que peut encore faire la justice ?",
             "The principal author dies before being tried for certain facts. What can justice still do?",
             [("a", "Rien : le dossier s'éteint entièrement", "Nothing: the file is entirely extinguished"),
              ("b", "Juger la complicité, et poursuivre les investigations sur d'autres faits", "Try complicity, and continue investigations on other facts"),
              ("c", "Juger l'auteur à titre posthume", "Try the author posthumously"),
              ("d", "Transférer la responsabilité à la famille", "Transfer responsibility to the family")],
             {"fr": {"whatInvestigatorsKnew": "Michel Fourniret est mort le 10 mai 2021 ; l'action publique est éteinte à son égard. Monique Olivier a été jugée et condamnée pour complicité le 19 décembre 2023.",
                     "whatExpertsProposed": "En droit français, la mort éteint l'action publique contre la personne décédée, mais n'éteint pas les poursuites contre d'autres personnes mises en cause. La complicité est une infraction autonome.",
                     "documented": "Le procès de Nanterre s'est tenu sans l'auteur principal ; des investigations se poursuivent par ailleurs, notamment sur la disparition de Cécile Vallin.",
                     "hypothetical": "Ce qu'un procès de l'auteur principal aurait apporté aux familles.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir que la cour retiendrait une implication « totale » tout en reconnaissant une « tentative de questionnement ».",
                     "answer_note": "La réponse attendue est B. A est faux : le procès de la complice a eu lieu."},
              "en": {"whatInvestigatorsKnew": "Michel Fourniret died on 10 May 2021; public prosecution is extinguished with respect to him. Monique Olivier was tried and convicted for complicity on 19 December 2023.",
                     "whatExpertsProposed": "In French law, death extinguishes public prosecution against the deceased person, but does not extinguish proceedings against other indicted persons. Complicity is an autonomous offence.",
                     "documented": "The Nanterre trial was held without the principal author; investigations continue elsewhere, notably on Cécile Vallin's disappearance.",
                     "hypothetical": "What a trial of the principal author would have brought to the families.",
                     "whatYouCouldNotKnow": "You could not know that the court would find 'total' involvement while recognising an 'attempt at questioning'.",
                     "answer_note": "The expected answer is B. A is wrong: the accomplice's trial did take place."}},
             "actu-proces-2023"),
    question("1", 400, "psychology",
             "Des experts-psychologues décrivent une épouse « passive » et « soumise ». La cour retient une « complice active ». Que faut-il retenir de cet écart ?",
             "Expert psychologists describe a 'passive' and 'submissive' wife. The court finds an 'active accomplice'. What should be retained from that gap?",
             [("a", "Que les experts se sont trompés", "That the experts were wrong"),
              ("b", "Que deux lectures professionnelles peuvent diverger, et que la qualification juridique revient à la cour", "That two professional readings can diverge, and that the legal qualification belongs to the court"),
              ("c", "Que la cour a outrepassé son rôle", "That the court exceeded its role"),
              ("d", "Que l'écart n'a aucune portée", "That the gap has no significance")],
             {"fr": {"whatInvestigatorsKnew": "Les deux lectures figurent dans le même compte rendu d'audience : celle d'experts-psychologues et celle de la cour.",
                     "whatExpertsProposed": "Une expertise psychologique décrit une personnalité ; une cour qualifie juridiquement des faits. Ce sont deux opérations distinctes, qui peuvent aboutir à des conclusions différentes sans qu'aucune ne soit « fausse » au sens clinique.",
                     "documented": "Le parquet a fustigé le « silence » et l'« indifférence » de la condamnée, et la cour a retenu une implication totale.",
                     "hypothetical": "Ce qu'une autre composition de cour aurait retenu.",
                     "whatYouCouldNotKnow": "Le contenu intégral des expertises n'est pas accessible dans les sources consultées.",
                     "answer_note": "La réponse attendue est B. A et C sont des jugements que les sources ne permettent pas de porter."},
              "en": {"whatInvestigatorsKnew": "Both readings appear in the same hearing report: that of expert psychologists and that of the court.",
                     "whatExpertsProposed": "A psychological evaluation describes a personality; a court legally qualifies facts. These are two distinct operations, which can reach different conclusions without either being clinically 'wrong'.",
                     "documented": "The prosecution condemned the convict's 'silence' and 'indifference', and the court found total involvement.",
                     "hypothetical": "What a differently composed court would have found.",
                     "whatYouCouldNotKnow": "The full content of the evaluations is not accessible in the sources consulted.",
                     "answer_note": "The expected answer is B. A and C are judgements the sources do not allow."}},
             "franceinfo-2023"),
]

CASE = {
    "id": CASE_ID,
    "title": txt("Michel Fourniret et Monique Olivier : juger la complicité",
                 "Michel Fourniret and Monique Olivier: trying complicity"),
    "subtitle": txt("France et Belgique, 1987-2003. Trois procès, trois condamnations pour complicité, et un auteur "
                    "principal mort avant d'être jugé.",
                    "France and Belgium, 1987-2003. Three trials, three convictions for complicity, and a principal "
                    "author who died before being tried."),
    "country": "FR", "region": "Grand Est / Ardennes", "city": "Charleville-Mézières",
    "year_start": 1987, "year_end": 2025, "period_label": txt("1987 – 2025", "1987 – 2025"),
    "status": "PARTIALLY_RESOLVED",
    "status_note": txt("Trois condamnations pour complicité prononcées ; l'auteur principal est décédé sans avoir été "
                       "jugé pour les faits de 2023 ; des investigations se poursuivent sur d'autres disparitions.",
                       "Three convictions for complicity pronounced; the principal author died without being tried for "
                       "the 2023 facts; investigations continue on other disappearances."),
    "type": "serial",
    "tags": ["serial_killer", "complicity", "france", "belgium", "multiple_trials", "death_of_offender", "child_victim"],
    "tier": "PREMIUM", "editorial": "yanis", "published_at": "2026-09-24", "sensitive": True,
    "triggers": txt("Enlèvements, viols et meurtres, dont celui d'une enfant de 9 ans ; évocation sans description "
                    "graphique.",
                    "Abductions, rapes and murders, including that of a 9-year-old child; mentioned without graphic "
                    "description."),
    "lat": 49.6, "lon": 4.6, "cover": "cover-fourniret",
    "stats": {"victims_documented": 9, "trials": 3, "duration_years": 38},
    "summary": txt(
        "Entre 1987 et 2003, des enlèvements, viols et meurtres sont commis entre la France et la Belgique. Monique "
        "Olivier, qui avait rencontré Michel Fourniret par correspondance en 1987 alors qu'il était incarcéré, est "
        "condamnée trois fois pour complicité : en mai 2008 par la cour d'assises des Ardennes à la réclusion "
        "criminelle à perpétuité avec 28 ans de sûreté pour sept meurtres commis entre 1987 et 2001 ; en 2018 par la "
        "cour d'assises des Yvelines à 20 ans pour le meurtre de Farida Hammiche ; le 19 décembre 2023 par la cour "
        "d'assises des Hauts-de-Seine à la perpétuité avec 20 ans de sûreté, pour complicité dans l'enlèvement, la "
        "séquestration et la mort de Marie-Angèle Domèce (19 ans), Joanna Parrish (20 ou 21 ans) et Estelle Mouzin "
        "(9 ans). Michel Fourniret, mort en détention le 10 mai 2021, n'a été jugé pour aucun de ces derniers faits : "
        "la mort éteint l'action publique. Les peines se confondent ; selon le calcul du parquet, la condamnée ne "
        "sera pas libérable avant 2035. Des investigations se poursuivent sur d'autres disparitions.",
        "Between 1987 and 2003, abductions, rapes and murders are committed between France and Belgium. Monique "
        "Olivier, who had met Michel Fourniret by correspondence in 1987 while he was imprisoned, is convicted three "
        "times for complicity: in May 2008 by the Ardennes assize court to life imprisonment with a 28-year minimum "
        "term for seven murders committed between 1987 and 2001; in 2018 by the Yvelines assize court to 20 years for "
        "the murder of Farida Hammiche; on 19 December 2023 by the Hauts-de-Seine assize court to life with a 20-year "
        "minimum term, for complicity in the abduction, confinement and death of Marie-Angèle Domèce (19), Joanna "
        "Parrish (20 or 21) and Estelle Mouzin (9). Michel Fourniret, who died in custody on 10 May 2021, was tried "
        "for none of these last facts: death extinguishes public prosecution. The sentences merge; according to the "
        "prosecution's calculation, the convict will not be eligible for release before 2035. Investigations continue "
        "on other disappearances."),
    "sources": SOURCES, "victims": VICTIMS, "other_victims": OTHER_VICTIMS, "memorial": MEMORIAL,
    "timeline": TIMELINE, "locations": LOCATIONS, "evidence": EVIDENCE, "investigation": INVESTIGATION,
    "psychology": PSYCHOLOGY, "victimology": VICTIMOLOGY, "court": COURT, "experts": EXPERTS,
    "experts_agreement": EXPERTS_AGREEMENT, "experts_disagreement": EXPERTS_DISAGREEMENT,
    "experts_uncertain": EXPERTS_UNCERTAIN, "counterfactuals": COUNTERFACTUALS, "lessons": LESSONS,
    "unknowns": UNKNOWNS, "sections": SECTIONS, "episodes": EPISODES, "questions": QUESTIONS,
}
