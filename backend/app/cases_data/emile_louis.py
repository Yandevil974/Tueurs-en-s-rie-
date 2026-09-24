"""
DOSSIER 03 — LES DISPARUES DE L'YONNE / ÉMILE LOUIS (France, Yonne, 1977-2013)

Sources publiques vérifiées le 2026-09-24. Les âges et dates divergent entre
sources : chaque écart est signalé et reste au niveau PROBABLE ou UNKNOWN (§43).
"""
from ..case_template import (block, counterfactual, default_sections, fact, item,
                             merge_sections, question, source, txt)

CASE_ID = "disparues-yonne-emile-louis"
V = "2026-09-24"

SOURCES = [
    source("rtl-7victimes", CASE_ID,
           "Affaire Émile Louis : qui sont les sept « disparues de l'Yonne » ?",
           "Émile Louis case: who were the seven 'missing women of the Yonne'?",
           "RTL", "Redaction", "https://www.rtl.fr/actu/justice-faits-divers/affaire-emile-louis-qui-sont-les-sept-disparues-de-l-yonne-victimes-du-tueur-en-serie-7900535305",
           "2025-09-07", "press", "CONFIRMED", V,
           "Noms, âges, placements institutionnels, témoignage du magistrat ayant présidé la cour d'assises.",
           "Names, ages, institutional placements, testimony of the magistrate who presided over the assize court."),
    source("monde-yonne", CASE_ID,
           "Les disparues de l'Yonne : Émile Louis, rattrapé 20 ans après",
           "The missing women of the Yonne: Émile Louis, caught 20 years later",
           "Le Monde", "Redaction", "https://www.lemonde.fr/ete-2007/article/2006-08-22/les-disparues-de-l-yonne-emile-louis-rattrape-20-ans-apres_805340_781732.html",
           "2006-08-22", "press", "CONFIRMED", V,
           "Chronologie judiciaire : non-lieu de 1984, arrêt de la Cour de cassation de 2002, condamnations de 2004 et appel de 2006.",
           "Judicial chronology: 1984 dismissal, 2002 Court of Cassation ruling, 2004 convictions and 2006 appeal."),
    source("lyonne-dates", CASE_ID,
           "Dix ans après sa mort, l'ombre d'Émile Louis subsiste",
           "Ten years after his death, Émile Louis's shadow remains",
           "L'Yonne républicaine", "Redaction", "https://www.lyonne.fr/auxerre-89000/actualites/dix-ans-apres-sa-mort-l-ombre-d-emile-louis-subsiste_14405786/",
           "2023-11-17", "press", "CONFIRMED", V,
           "« Émile Louis en dates » : naissances, dates de disparition, découverte du corps de Sylviane Lesage, rapport Jambert.",
           "'Émile Louis in dates': births, disappearance dates, discovery of Sylviane Lesage's body, Jambert report."),
    source("vINGTminutes-traces", CASE_ID,
           "Sur les traces des disparues de l'Yonne",
           "On the trail of the missing women of the Yonne",
           "20 Minutes", "Redaction", "https://www.20minutes.fr/france/38359-20041027-france-sur-les-traces-des-disparues-de-l-yonne",
           "2004-10-27", "press", "CONFIRMED", V,
           "Liens entre les victimes et Émile Louis ; absence de signalement des disparitions par les centres ; arrestation du 12 décembre 2000.",
           "Links between the victims and Émile Louis; failure of the centres to report the disappearances; arrest of 12 December 2000."),
    source("sudouest-parcours", CASE_ID,
           "Émile Louis : de 1974 à 2007, le long parcours meurtrier et judiciaire d'un tueur en série",
           "Émile Louis: from 1974 to 2007, the long murderous and judicial journey of a serial killer",
           "Sud Ouest", "Redaction", "https://www.sudouest.fr/faits-divers/emile-louis-de-1974-a-2007-le-long-parcours-meurtrier-et-judiciaire-d-un-tueur-en-serie-21524458.php",
           "2024-09-25", "press", "CONFIRMED", V,
           "Non-lieu de février 1984, aveux de décembre 2000, exhumation de deux corps, rétractation.",
           "February 1984 dismissal, December 2000 confessions, exhumation of two bodies, retraction."),
    source("rtl-getti", CASE_ID,
           "Émile Louis et les disparues de l'Yonne : « Il y a eu de très nombreux dysfonctionnements »",
           "Émile Louis and the missing women of the Yonne: 'There were very many dysfunctions'",
           "RTL", "Redaction (propos de Jean-Pierre Getti)", "https://www.rtl.fr/actu/justice-faits-divers/emile-louis-et-les-disparues-de-l-yonne-il-y-a-eu-de-tres-nombreux-dysfonctionnements-estime-l-ex-magistrat-jean-pierre-getti-7900535106",
           "2025-09-04", "interview", "CONFIRMED", V,
           "Témoignage de l'ex-magistrat qui a présidé le procès de 2004 : profils des victimes, dysfonctionnements.",
           "Testimony of the former magistrate who presided over the 2004 trial: victims' profiles, dysfunctions."),
]

# Seven victims, all young women placed in institutions managed by the DDASS and
# the APAJH in the Auxerre area (RTL, L'Yonne républicaine, 20 Minutes).
def _v(order, first, last, age, source, reliability, life_fr, life_en, note_fr, note_en, dis_fr, dis_en):
    """Build a victim file (§11). Missing documented data is displayed, never invented."""
    life = {
        "fr": {"headline": f"{first} {last}", "items": life_fr, "note": note_fr},
        "en": {"headline": f"{first} {last}", "items": life_en, "note": note_en},
    }
    return {
        "order": order, "first_name": first, "last_name": last, "age": age,
        "source": source, "reliability": reliability, "anonymised": False,
        "life": life,
        "disappearance": {"fr": {"items": dis_fr}, "en": {"items": dis_en}},
    }


NOTE_FR = ("Les sources publiques consultées divergent sur certains âges et sur plusieurs dates de disparition. "
           "Les écarts sont signalés dans chaque fiche ; l'application ne tranche pas sans source concordante.")
NOTE_EN = ("The public sources consulted diverge on certain ages and on several disappearance dates. The "
           "discrepancies are flagged in each file; the application does not settle them without concordant sources.")

VICTIMS = [
    _v(0, "Christine", "Marlot", "15", "lyonne-dates", "CONFIRMED",
       [{"label": "Âge", "text": "15 ans selon L'Yonne républicaine ; 16 ans selon d'autres articles."},
        {"label": "Naissance", "text": "26 mai 1961 à Avallon (Yonne), selon la presse locale."},
        {"label": "Contexte", "text": "Jeune femme placée, prise en charge dans le circuit des foyers et instituts de l'Yonne."}],
       [{"label": "Age", "text": "15 according to L'Yonne républicaine; 16 in other articles."},
        {"label": "Birth", "text": "26 May 1961 in Avallon (Yonne), according to the local press."},
        {"label": "Context", "text": "A young woman in state care, within the Yonne's homes and institutes circuit."}],
       NOTE_FR, NOTE_EN,
       [{"label": "Date", "text": "23 janvier 1977."},
        {"label": "Lieu", "text": "Région d'Auxerre (Yonne)."},
        {"label": "Corps", "text": "Jamais retrouvé."}],
       [{"label": "Date", "text": "23 January 1977."},
        {"label": "Place", "text": "Auxerre area (Yonne)."},
        {"label": "Body", "text": "Never recovered."}]),
    _v(1, "Jacqueline", "Weis", "18", "lyonne-dates", "CONFIRMED",
       [{"label": "Âge", "text": "18 ans."},
        {"label": "Contexte", "text": "Placée en nourrice chez la famille Louis ; elle quitte ce foyer pour un emploi à Avallon."},
        {"label": "Projet", "text": "Un emploi à Avallon, qu'elle devait rejoindre le jour de sa disparition."}],
       [{"label": "Age", "text": "18."},
        {"label": "Context", "text": "Fostered with the Louis family; she left that home for a job in Avallon."},
        {"label": "Plan", "text": "A job in Avallon, which she was to join on the day she disappeared."}],
       NOTE_FR, NOTE_EN,
       [{"label": "Date", "text": "4 avril 1977, à Auxerre."},
        {"label": "Circonstances", "text": "Émile Louis l'aurait conduite à la gare ce jour-là. Personne ne l'a jamais revue."},
        {"label": "Corps", "text": "Retrouvé en décembre 2000 sur les indications d'Émile Louis, près du Serein."}],
       [{"label": "Date", "text": "4 April 1977, in Auxerre."},
        {"label": "Circumstances", "text": "Émile Louis reportedly drove her to the station that day. Nobody ever saw her again."},
        {"label": "Body", "text": "Recovered in December 2000 on Émile Louis's indications, near the Serein river."}]),
    _v(2, "Chantal", "Gras", "18", "lyonne-dates", "CONFIRMED",
       [{"label": "Âge", "text": "18 ans."},
        {"label": "Contexte", "text": "Elle empruntait le car de ramassage conduit par Émile Louis ; la presse rapporte qu'elle s'asseyait à ses côtés."}],
       [{"label": "Age", "text": "18."},
        {"label": "Context", "text": "She used the collection bus driven by Émile Louis; the press reports she sat beside him."}],
       NOTE_FR, NOTE_EN,
       [{"label": "Date", "text": "21-22 avril 1977, à Villefargeau."},
        {"label": "Élément", "text": "Émile Louis aurait été aperçu dans sa voiture non loin de son domicile."},
        {"label": "Corps", "text": "Jamais retrouvé."}],
       [{"label": "Date", "text": "21-22 April 1977, in Villefargeau."},
        {"label": "Element", "text": "Émile Louis was reportedly seen in his car not far from her home."},
        {"label": "Body", "text": "Never recovered."}]),
    _v(3, "Madeleine", "Dejust", "21", "lyonne-dates", "CONFIRMED",
       [{"label": "Âge", "text": "21 ans selon L'Yonne républicaine ; 22 ans selon d'autres articles."},
        {"label": "Contexte", "text": "Travaillait dans un centre ; Émile Louis la conduisait en car vers son lieu de travail."}],
       [{"label": "Age", "text": "21 according to L'Yonne républicaine; 22 in other articles."},
        {"label": "Context", "text": "Worked in a centre; Émile Louis drove her by bus to her workplace."}],
       NOTE_FR, NOTE_EN,
       [{"label": "Date", "text": "27-28 juillet 1977, à Auxerre."},
        {"label": "Corps", "text": "Retrouvé en décembre 2000 sur les indications d'Émile Louis."}],
       [{"label": "Date", "text": "27-28 July 1977, in Auxerre."},
        {"label": "Body", "text": "Recovered in December 2000 on Émile Louis's indications."}]),
    _v(4, "Bernadette", "Lemoine", "19", "lyonne-dates", "CONFIRMED",
       [{"label": "Âge", "text": "19 ans selon RTL ; 20 ou 21 ans selon d'autres articles."},
        {"label": "Contexte", "text": "Sœur de Françoise Lemoine ; toutes deux placées."}],
       [{"label": "Age", "text": "19 according to RTL; 20 or 21 in other articles."},
        {"label": "Context", "text": "Sister of Françoise Lemoine; both in state care."}],
       NOTE_FR, NOTE_EN,
       [{"label": "Date", "text": "Premier trimestre 1978, à Auxerre."},
        {"label": "Corps", "text": "Jamais retrouvé."}],
       [{"label": "Date", "text": "First quarter of 1978, in Auxerre."},
        {"label": "Body", "text": "Never recovered."}]),
    _v(5, "Françoise", "Lemoine", "26", "lyonne-dates", "CONFIRMED",
       [{"label": "Âge", "text": "26 ans selon L'Yonne républicaine ; 19 ou 27 ans selon d'autres articles."},
        {"label": "Contexte", "text": "Émile Louis lui avait trouvé une chambre à Auxerre ; elle avait été embauchée comme serveuse dans un établissement fréquenté par l'entourage du suspect."}],
       [{"label": "Age", "text": "26 according to L'Yonne républicaine; 19 or 27 in other articles."},
        {"label": "Context", "text": "Émile Louis had found her a room in Auxerre; she had been hired as a waitress in an establishment frequented by the suspect's circle."}],
       NOTE_FR, NOTE_EN,
       [{"label": "Date", "text": "1977 ou 1978, à Auxerre."},
        {"label": "Élément", "text": "En 1978, son ancienne nourrice demande de ses nouvelles. Réponse rapportée : « Elle a disparu sans raison. »"},
        {"label": "Corps", "text": "Jamais retrouvé."}],
       [{"label": "Date", "text": "1977 or 1978, in Auxerre."},
        {"label": "Element", "text": "In 1978, her former foster carer asked after her. Reported answer: 'She disappeared for no reason.'"},
        {"label": "Body", "text": "Never recovered."}]),
    _v(6, "Martine", "Renault", "16", "lyonne-dates", "CONFIRMED",
       [{"label": "Âge", "text": "16 ans."},
        {"label": "Contexte", "text": "Dernière disparition de la série ; c'est à son sujet qu'Émile Louis est entendu en décembre 1979."}],
       [{"label": "Age", "text": "16."},
        {"label": "Context", "text": "Last disappearance of the series; it is about her that Émile Louis is heard in December 1979."}],
       NOTE_FR, NOTE_EN,
       [{"label": "Date", "text": "26 septembre 1979."},
        {"label": "Corps", "text": "Jamais retrouvé."}],
       [{"label": "Date", "text": "26 September 1979."},
        {"label": "Body", "text": "Never recovered."}]),
]


OTHER_VICTIM = {
    "title": txt("Sylviane Lesage, une victime hors série jugée", "Sylviane Lesage, a victim tried outside the series"),
    "body": txt(
        "Le 5 juillet 1981, le corps de Sylviane Lesage, 23 ans, maîtresse d'Émile Louis, est découvert dans un abri à "
        "bestiaux à Rouvray, près d'Auxerre. Émile Louis est inculpé de meurtre et écroué. Il bénéficie d'un non-lieu "
        "faute de preuves en février 1984. Elle ne figure pas parmi les sept « disparues » : son dossier a été jugé "
        "séparément.",
        "On 5 July 1981, the body of Sylviane Lesage, 23, Émile Louis's mistress, was discovered in a cattle shed in "
        "Rouvray, near Auxerre. Émile Louis was charged with murder and detained. He obtained a dismissal for lack of "
        "evidence in February 1984. She is not among the seven 'missing women': her file was tried separately.",
    ),
    "reliability": "CONFIRMED", "source": "sudouest-parcours",
}

MEMORIAL = {
    "title": txt("Sept jeunes femmes de l'Yonne", "Seven young women of the Yonne"),
    "biography": txt(
        "Christine Marlot, Jacqueline Weis, Chantal Gras, Madeleine Dejust, Bernadette Lemoine, Françoise Lemoine et "
        "Martine Renault étaient de jeunes femmes placées, prises en charge dans les foyers et instituts de l'Yonne. "
        "Cinq d'entre elles n'ont jamais été retrouvées. Leurs disparitions ont été qualifiées de fugues par les "
        "établissements concernés, qui ne les ont pas signalées comme telles à la justice.",
        "Christine Marlot, Jacqueline Weis, Chantal Gras, Madeleine Dejust, Bernadette Lemoine, Françoise Lemoine and "
        "Martine Renault were young women in state care, looked after in the homes and institutes of the Yonne. Five "
        "of them were never found. Their disappearances were recorded as running away by the institutions concerned, "
        "which did not report them as such to the justice system.",
    ),
    "testimony": txt(
        "Lors du procès de 2004, la fille aînée d'Émile Louis a déclaré devant la cour d'assises que son père "
        "« n'était pas un être humain ». Ce témoignage est rapporté par la presse ayant suivi l'audience.",
        "At the 2004 trial, Émile Louis's eldest daughter told the assize court that her father 'was not a human "
        "being'. This testimony is reported by the press that followed the hearing.",
    ),
    "memory": txt(
        "L'association qui a relancé l'affaire en 1996, et les deux personnes à l'initiative de sa médiatisation, ont "
        "porté pendant vingt ans un dossier que l'institution avait classé. Cinq des sept victimes n'ont pas de "
        "sépulture.",
        "The association that revived the case in 1996, and the two people behind its media exposure, carried for "
        "twenty years a file the institution had closed. Five of the seven victims have no grave.",
    ),
}

TIMELINE = [
    fact("Sept jeunes femmes placées disparaissent dans la région d'Auxerre entre 1977 et 1979. Les établissements "
         "ne signalent pas ces disparitions, qualifiées de fugues.",
         "Seven young women in state care disappear in the Auxerre area between 1977 and 1979. The institutions do "
         "not report these disappearances, recorded as running away.",
         "CONFIRMED", "vINGTminutes-traces", "Disparitions", "Disappearances", "1977-1979"),
    fact("Émile Louis, chauffeur de car qui transporte ces jeunes femmes entre leur établissement et leur lieu de "
         "résidence, est entendu en décembre 1979 au sujet de la disparition de Martine Renault.",
         "Émile Louis, the bus driver who transported these young women between their institution and their place of "
         "residence, is heard in December 1979 about Martine Renault's disappearance.",
         "CONFIRMED", "sudouest-parcours", "Première audition", "First hearing", "1979-12"),
    fact("Le corps de Sylviane Lesage, 23 ans, est découvert dans un abri à bestiaux à Rouvray. Émile Louis est "
         "inculpé de meurtre et écroué.",
         "The body of Sylviane Lesage, 23, is discovered in a cattle shed in Rouvray. Émile Louis is charged with "
         "murder and detained.",
         "CONFIRMED", "lyonne-dates", "Affaire Lesage", "Lesage case", "1981-07-05"),
    fact("Émile Louis est condamné pour attentats à la pudeur sur des mineures placées à la DDASS : cinq ans, réduits "
         "à quatre en appel.",
         "Émile Louis is convicted of indecent assaults on minors in state care: five years, reduced to four on appeal.",
         "CONFIRMED", "sudouest-parcours", "Condamnation", "Conviction", "1983-01"),
    fact("Non-lieu dans l'affaire Lesage, faute de preuves. La même année, le gendarme Christian Jambert remet un "
         "rapport d'enquête préliminaire désignant Émile Louis comme principal suspect dans la disparition de six "
         "jeunes femmes. Le rapport reste sans suite.",
         "Dismissal in the Lesage case for lack of evidence. The same year, gendarme Christian Jambert submits a "
         "preliminary investigation report naming Émile Louis as the main suspect in the disappearance of six young "
         "women. The report is not followed up.",
         "CONFIRMED", "sudouest-parcours", "Le rapport sans suite", "The report left unacted", "1984-02"),
    fact("Christian Jambert est retrouvé mort. L'enquête conclut à un suicide ; des proches contestent cette version. "
         "Une information judiciaire contre X ouverte en 2004 se conclura par un non-lieu en 2011.",
         "Christian Jambert is found dead. The investigation concludes suicide; relatives dispute that version. A "
         "judicial investigation opened in 2004 ends in a dismissal in 2011.",
         "DISPUTED", "lyonne-dates", "Mort du gendarme", "Death of the gendarme", "1997"),
    fact("L'association de défense des handicapés de l'Yonne relance l'affaire et dépose une plainte auprès d'un juge "
         "d'instruction. Le parquet refuse de donner suite au motif que les faits sont prescrits. L'affaire est alors "
         "médiatisée.",
         "The Yonne disability defence association revives the case and files a complaint with an investigating "
         "judge. The prosecution refuses to proceed on the grounds that the facts are time-barred. The case is then "
         "publicised.",
         "CONFIRMED", "monde-yonne", "Relance associative", "Revival by an association", "1996"),
    fact("Émile Louis est interpellé et placé en garde à vue. Croyant les faits prescrits, il reconnaît avoir tué "
         "sept jeunes femmes. Il se rétracte en janvier 2001.",
         "Émile Louis is arrested and placed in police custody. Believing the facts time-barred, he admits having "
         "killed seven young women. He retracts in January 2001.",
         "CONFIRMED", "vINGTminutes-traces", "Aveux puis rétractation", "Confession then retraction", "2000-12-12"),
    fact("Sur ses indications, les corps de Madeleine Dejust et de Jacqueline Weis sont exhumés. Cinq corps ne seront "
         "jamais retrouvés.",
         "On his indications, the bodies of Madeleine Dejust and Jacqueline Weis are exhumed. Five bodies will never "
         "be recovered.",
         "CONFIRMED", "sudouest-parcours", "Exhumations", "Exhumations", "2000-12"),
    fact("La Cour de cassation estime que le dossier n'est pas prescrit : la séquestration, tant que le corps n'a pas "
         "été retrouvé, est un crime continu.",
         "The Court of Cassation holds that the file is not time-barred: confinement, as long as the body has not been "
         "found, is a continuing offence.",
         "CONFIRMED", "monde-yonne", "Arrêt décisif", "Decisive ruling", "2002-02-20"),
    fact("Émile Louis est condamné par la cour d'assises du Var pour viols et actes de barbarie sur sa seconde épouse "
         "et sa belle-fille. Les articles indiquent vingt ans de réclusion criminelle avec une période de sûreté des "
         "deux tiers ; un autre article évoque 24 ans d'emprisonnement. L'écart est signalé.",
         "Émile Louis is convicted by the Var assize court for rape and acts of barbarity against his second wife and "
         "stepdaughter. Articles state twenty years' imprisonment with a two-thirds minimum term; another article "
         "mentions 24 years. The discrepancy is flagged.",
         "DISPUTED", "monde-yonne", "Procès de Draguignan", "Draguignan trial", "2004-03"),
    fact("La cour d'assises de l'Yonne, à Auxerre, condamne Émile Louis à la réclusion criminelle à perpétuité, "
         "assortie d'une période de sûreté de 18 ans, pour l'assassinat des sept jeunes femmes.",
         "The Yonne assize court, in Auxerre, sentences Émile Louis to life imprisonment with an 18-year minimum term "
         "for the murder of the seven young women.",
         "CONFIRMED", "monde-yonne", "Verdict", "Verdict", "2004-11-25"),
    fact("Peine confirmée en appel. Le pourvoi est rejeté par la Cour de cassation en septembre 2007.",
         "Sentence confirmed on appeal. The appeal to the Court of Cassation is rejected in September 2007.",
         "CONFIRMED", "monde-yonne", "Appel et cassation", "Appeal and cassation", "2006-06-27"),
    fact("Émile Louis meurt en détention, à 79 ans.",
         "Émile Louis dies in custody, aged 79.",
         "CONFIRMED", "lyonne-dates", "Décès", "Death", "2013-10-20"),
]

LOCATIONS = [
    {"kind": "city", "names": txt("Auxerre et sa région (Yonne)", "Auxerre and its area (Yonne)"),
     "city": "Auxerre", "region": "Yonne / Bourgogne", "country": "FR", "lat": 47.798, "lon": 3.567,
     "precision": "region", "date": "1977-1979",
     "note": txt("Secteur des disparitions. Aucune adresse d'établissement ou de domicile n'est publiée.",
                 "Area of the disappearances. No institution or home address is published."),
     "reliability": "CONFIRMED", "source": "rtl-7victimes"},
    {"kind": "city", "names": txt("Rouvray", "Rouvray"), "city": "Rouvray", "region": "Yonne", "country": "FR",
     "lat": 47.45, "lon": 3.9, "precision": "city", "date": "1981-07-05",
     "note": txt("Découverte du corps de Sylviane Lesage ; lieu d'exhumation de deux des sept victimes en 2000.",
                 "Discovery of Sylviane Lesage's body; exhumation site of two of the seven victims in 2000."),
     "reliability": "CONFIRMED", "source": "lyonne-dates"},
    {"kind": "city", "names": txt("Villefargeau", "Villefargeau"), "city": "Villefargeau", "region": "Yonne",
     "country": "FR", "lat": 47.72, "lon": 3.45, "precision": "city", "date": "1977-04-21",
     "note": txt("Lieu de la disparition de Chantal Gras.", "Place of Chantal Gras's disappearance."),
     "reliability": "CONFIRMED", "source": "lyonne-dates"},
    {"kind": "court", "names": txt("Cour d'assises de l'Yonne, Auxerre", "Yonne Assize Court, Auxerre"),
     "city": "Auxerre", "region": "Yonne", "country": "FR", "lat": 47.798, "lon": 3.567, "precision": "city",
     "date": "2004-11-25", "note": txt("Procès du 2 au 25 novembre 2004.", "Trial from 2 to 25 November 2004."),
     "reliability": "CONFIRMED", "source": "monde-yonne"},
]

EVIDENCE = [
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "lyonne-dates",
     "title": txt("Le rapport du gendarme Jambert (1984)", "Gendarme Jambert's report (1984)"),
     "description": txt(
         "Un rapport d'enquête préliminaire explique pourquoi Émile Louis doit être considéré comme le suspect numéro "
         "un dans la disparition de six des sept jeunes femmes. Le rapport reste sans suite.",
         "A preliminary investigation report explains why Émile Louis should be considered the prime suspect in the "
         "disappearance of six of the seven young women. The report is not followed up.")},
    {"kind": "testimony", "weight": "documented", "reliability": "CONFIRMED", "source": "sudouest-parcours",
     "title": txt("Les aveux de décembre 2000, puis la rétractation", "The December 2000 confessions, then the retraction"),
     "description": txt(
         "Placé en garde à vue et croyant les faits prescrits, Émile Louis reconnaît sept meurtres, puis se rétracte "
         "en janvier 2001 en invoquant la pression des gendarmes. La rétractation n'a pas empêché la condamnation de "
         "2004.",
         "Placed in police custody and believing the facts time-barred, Émile Louis admitted seven murders, then "
         "retracted in January 2001, invoking pressure from the gendarmes. The retraction did not prevent the 2004 "
         "conviction.")},
    {"kind": "forensic", "weight": "decisive", "reliability": "CONFIRMED", "source": "sudouest-parcours",
     "title": txt("Deux corps exhumés", "Two exhumed bodies"),
     "description": txt(
         "Sur les indications de l'intéressé, les squelettes de Jacqueline Weis et de Madeleine Dejust sont retrouvés. "
         "Les cinq autres corps n'ont jamais été découverts.",
         "On the person's indications, the skeletons of Jacqueline Weis and Madeleine Dejust are found. The five "
         "other bodies were never discovered.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "rtl-7victimes",
     "title": txt("Le point commun institutionnel", "The institutional common factor"),
     "description": txt(
         "Le magistrat ayant présidé la cour d'assises décrit des victimes placées dans des établissements gérés par "
         "la DDASS et l'APAJH, et un même chauffeur de car entre le lieu de travail et le lieu de résidence.",
         "The magistrate who presided over the assize court describes victims placed in institutions managed by the "
         "DDASS and the APAJH, and the same bus driver between workplace and residence.")},
    {"kind": "documentary", "weight": "documented", "reliability": "CONFIRMED", "source": "monde-yonne",
     "title": txt("L'arrêt de la Cour de cassation du 20 février 2002", "The Court of Cassation ruling of 20 February 2002"),
     "description": txt(
         "La haute juridiction retient que la séquestration est un crime continu tant que le corps n'a pas été "
         "retrouvé, ce qui écarte la prescription invoquée par le parquet.",
         "The high court holds that confinement is a continuing offence as long as the body has not been found, which "
         "rules out the prescription invoked by the prosecution.")},
]

INVESTIGATION = {
    "steps": [
        {"n": 1, "date": "1977-1979", "title": txt("Des fugues, pas des disparitions", "Runaways, not disappearances"),
         "body": txt("Sept jeunes femmes placées disparaissent entre 1977 et 1979. Aucun centre ne signale ces "
                     "disparitions : elles sont qualifiées de fugues. Aucune information judiciaire d'ensemble n'est "
                     "ouverte.",
                     "Seven young women in state care disappear between 1977 and 1979. No centre reports these "
                     "disappearances: they are recorded as running away. No overall judicial investigation is opened."),
         "reliability": "CONFIRMED", "source": "vINGTminutes-traces", "premium": False},
        {"n": 2, "date": "1979-12", "title": txt("Un chauffeur de car", "A bus driver"),
         "body": txt("Émile Louis conduit le car qui transporte ces jeunes femmes entre leur établissement et leur "
                     "lieu de résidence. Il est entendu en décembre 1979 au sujet de Martine Renault.",
                     "Émile Louis drives the bus transporting these young women between their institution and their "
                     "residence. He is heard in December 1979 about Martine Renault."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": False},
        {"n": 3, "date": "1981-07-05", "title": txt("Un corps dans une étable", "A body in a barn"),
         "body": txt("Le corps de Sylviane Lesage, 23 ans, est découvert à Rouvray. Émile Louis est inculpé de "
                     "meurtre et écroué.",
                     "The body of Sylviane Lesage, 23, is discovered in Rouvray. Émile Louis is charged with murder "
                     "and detained."),
         "reliability": "CONFIRMED", "source": "lyonne-dates", "premium": False},
        {"n": 4, "date": "1983-01", "title": txt("Une condamnation pour d'autres faits", "A conviction for other facts"),
         "body": txt("Il est condamné pour attentats à la pudeur sur des mineures de la DDASS : cinq ans, réduits à "
                     "quatre en appel.",
                     "He is convicted of indecent assaults on minors in state care: five years, reduced to four on appeal."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": False},
        {"n": 5, "date": "1984-02", "title": txt("Le rapport qui désigne, et qui dort", "The report that names, and sleeps"),
         "body": txt("Non-lieu dans l'affaire Lesage, faute de preuves. La même année, le gendarme Christian Jambert "
                     "remet un rapport désignant Émile Louis comme principal suspect dans la disparition de six jeunes "
                     "femmes. Le rapport reste sans suite.",
                     "Dismissal in the Lesage case for lack of evidence. The same year, gendarme Christian Jambert "
                     "submits a report naming Émile Louis as the main suspect in the disappearance of six young women. "
                     "The report is not followed up."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": True},
        {"n": 6, "date": "1996", "title": txt("Une association rouvre le dossier", "An association reopens the file"),
         "body": txt("L'association de défense des handicapés de l'Yonne dépose plainte. Le parquet refuse de donner "
                     "suite : les faits sont prescrits. L'affaire est alors portée devant les médias.",
                     "The Yonne disability defence association files a complaint. The prosecution refuses to proceed: "
                     "the facts are time-barred. The case is then taken to the media."),
         "reliability": "CONFIRMED", "source": "monde-yonne", "premium": False},
        {"n": 7, "date": "2000-12-12", "title": txt("Des aveux fondés sur une croyance", "Confessions based on a belief"),
         "body": txt("Émile Louis est interpellé. Croyant les faits prescrits, il reconnaît sept meurtres. Il se "
                     "rétracte en janvier 2001, invoquant la pression des gendarmes.",
                     "Émile Louis is arrested. Believing the facts time-barred, he admits seven murders. He retracts "
                     "in January 2001, invoking pressure from the gendarmes."),
         "reliability": "CONFIRMED", "source": "vINGTminutes-traces", "premium": True},
        {"n": 8, "date": "2000-12", "title": txt("Deux corps, cinq absences", "Two bodies, five absences"),
         "body": txt("Sur ses indications, les corps de Madeleine Dejust et de Jacqueline Weis sont exhumés. Les cinq "
                     "autres ne seront jamais retrouvés.",
                     "On his indications, the bodies of Madeleine Dejust and Jacqueline Weis are exhumed. The five "
                     "others will never be found."),
         "reliability": "CONFIRMED", "source": "sudouest-parcours", "premium": False},
        {"n": 9, "date": "2002-02-20", "title": txt("La prescription écartée", "Prescription ruled out"),
         "body": txt("La Cour de cassation retient que la séquestration est un crime continu tant que le corps n'est "
                     "pas retrouvé. Le dossier peut être jugé, vingt-cinq ans après les faits.",
                     "The Court of Cassation holds that confinement is a continuing offence as long as the body is not "
                     "found. The file can be tried, twenty-five years after the facts."),
         "reliability": "CONFIRMED", "source": "monde-yonne", "premium": True},
        {"n": 10, "date": "2004-11-25", "title": txt("Le verdict", "The verdict"),
         "body": txt("La cour d'assises de l'Yonne condamne Émile Louis à la réclusion criminelle à perpétuité avec "
                     "18 ans de sûreté. Peine confirmée en appel le 27 juin 2006, pourvoi rejeté en septembre 2007.",
                     "The Yonne assize court sentences Émile Louis to life imprisonment with an 18-year minimum term. "
                     "Sentence confirmed on appeal on 27 June 2006, appeal to the Court of Cassation rejected in "
                     "September 2007."),
         "reliability": "CONFIRMED", "source": "monde-yonne", "premium": False},
    ],
    "reality": txt(
        "Voici comment l'enquête s'est réellement déroulée : vingt ans d'oubli institutionnel, un rapport de "
        "gendarmerie resté sans suite en 1984, une relance associative en 1996, des aveux obtenus en 2000 parce que "
        "leur auteur croyait à la prescription, deux corps exhumés, et un arrêt de la Cour de cassation rendant le "
        "procès possible.",
        "This is how the investigation actually unfolded: twenty years of institutional oblivion, a gendarmerie report "
        "left unacted in 1984, a revival by an association in 1996, confessions obtained in 2000 because their author "
        "believed in prescription, two exhumed bodies, and a Court of Cassation ruling making the trial possible."),
    "errors": [
        item("Sept disparitions qualifiées de fugues par les établissements, non signalées à la justice.",
             "Seven disappearances recorded as running away by the institutions, not reported to the justice system.",
             "CONFIRMED", "vINGTminutes-traces", "Signalement", "Reporting"),
        item("Rapport de gendarmerie de 1984 désignant un suspect principal, resté sans suite.",
             "1984 gendarmerie report naming a prime suspect, left unacted.",
             "CONFIRMED", "sudouest-parcours", "Décision de classement", "Decision to close"),
        item("Parquet invoquant la prescription en 1996 pour refuser de donner suite à la plainte de l'association.",
             "Prosecution invoking prescription in 1996 to refuse following up the association's complaint.",
             "CONFIRMED", "monde-yonne", "Lecture juridique", "Legal reading"),
        item("L'ex-magistrat ayant présidé le procès de 2004 évoque de « très nombreux dysfonctionnements ».",
             "The former magistrate who presided over the 2004 trial speaks of 'very many dysfunctions'.",
             "CONFIRMED", "rtl-getti", "Témoignage", "Testimony"),
    ],
    "cold_case": {
        "what_we_know": [
            item("Sept victimes identifiées, toutes jeunes femmes placées dans des institutions de l'Yonne.",
                 "Seven identified victims, all young women placed in Yonne institutions.", "CONFIRMED", "rtl-7victimes"),
            item("Deux corps exhumés en 2000 ; cinq jamais retrouvés.",
                 "Two bodies exhumed in 2000; five never recovered.", "CONFIRMED", "sudouest-parcours"),
            item("Condamnation définitive après appel et rejet du pourvoi.",
                 "Final conviction after appeal and rejection of the cassation appeal.", "CONFIRMED", "monde-yonne"),
        ],
        "what_is_probable": [
            item("Les cinq corps non retrouvés se trouvent dans un secteur que le condamné connaissait, mais aucune "
                 "indication exploitable n'a été donnée.",
                 "The five unrecovered bodies are in an area known to the convicted man, but no usable indication was given.",
                 "PROBABLE", "sudouest-parcours"),
        ],
        "what_is_disputed": [
            item("Les circonstances de la mort du gendarme Christian Jambert en 1997 : l'enquête conclut à un suicide, "
                 "des proches contestent ; une information judiciaire ouverte en 2004 a conclu à un non-lieu en 2011.",
                 "The circumstances of gendarme Christian Jambert's death in 1997: the investigation concludes "
                 "suicide, relatives dispute it; a judicial investigation opened in 2004 ended in a dismissal in 2011.",
                 "DISPUTED", "lyonne-dates"),
            item("La peine prononcée à Draguignan en 2004 : vingt ans selon Le Monde, vingt-quatre ans d'emprisonnement "
                 "selon un autre article.",
                 "The sentence pronounced in Draguignan in 2004: twenty years according to Le Monde, twenty-four years "
                 "according to another article.", "DISPUTED", "monde-yonne"),
        ],
        "what_is_unknown": [
            item("Le lieu où se trouvent les cinq corps.", "The location of the five bodies.", "UNKNOWN", "sudouest-parcours"),
            item("Les dates exactes de plusieurs disparitions : les sources donnent des années différentes pour "
                 "Françoise Lemoine.",
                 "The exact dates of several disappearances: sources give different years for Françoise Lemoine.",
                 "UNKNOWN", "lyonne-dates"),
        ],
        "latest_progress": [
            item("Des fouilles du « cimetière » d'Émile Louis ont été réalisées plusieurs décennies après les faits, "
                 "à la recherche d'autres corps.",
                 "Searches of Émile Louis's 'cemetery' were carried out decades after the facts, looking for other bodies.",
                 "CONFIRMED", "sudouest-parcours"),
        ],
        "leads": [
            item("Les secteurs de Rouvray et des abords du Serein, où deux corps ont été retrouvés.",
                 "The areas of Rouvray and the banks of the Serein, where two bodies were found.",
                 "PROBABLE", "sudouest-parcours"),
        ],
        "limits": [
            item("Le condamné est mort en 2013 : plus aucune audition ne permettra d'obtenir des indications.",
                 "The convicted man died in 2013: no further hearing will yield indications.", "CONFIRMED", "lyonne-dates"),
        ],
    },
}

PSYCHOLOGY = {
    "disclaimer": txt("Aucun diagnostic psychiatrique n'est posé. Les éléments ci-dessous sont issus du dossier tel que "
                      "rapporté par les sources citées.",
                      "No psychiatric diagnosis is made. The elements below come from the file as reported by the cited sources."),
    "blocks": [
        block("fact", "Une position d'accès aux victimes", "A position of access to the victims",
              "Chauffeur de car pour des institutions médico-éducatives, conseiller municipal de Seignelay, Émile "
              "Louis occupait une position lui donnant un accès régulier et légitime aux jeunes femmes prises en "
              "charge. C'est un fait de dossier, établi par les sources et par le magistrat ayant présidé le procès.",
              "Bus driver for medico-educational institutions, municipal councillor of Seignelay, Émile Louis held a "
              "position giving him regular and legitimate access to the young women in care. This is a case fact, "
              "established by the sources and by the magistrate who presided over the trial.",
              "CONFIRMED", "rtl-7victimes"),
        block("behaviour", "Le contrôle par la position sociale", "Control through social position",
              "Les victimes étaient placées, dépendantes d'un circuit institutionnel, et leurs disparitions ont été "
              "qualifiées de fugues. Le comportement documenté consiste à agir dans un espace où la parole des "
              "victimes avait peu de poids institutionnel.",
              "The victims were in care, dependent on an institutional circuit, and their disappearances were recorded "
              "as running away. The documented behaviour consists of acting in a space where the victims' word carried "
              "little institutional weight.",
              "CONFIRMED", "vINGTminutes-traces"),
        block("behaviour", "Aveux, rétractation, silence", "Confession, retraction, silence",
              "Il avoue en croyant les faits prescrits, puis se rétracte en invoquant la pression des gendarmes, et "
              "nie en bloc devant la cour d'assises en 2004. Le président de la cour le décrit comme sachant éviter "
              "les pièges et bien y répondre.",
              "He confesses believing the facts time-barred, then retracts invoking pressure from the gendarmes, and "
              "denies everything before the assize court in 2004. The presiding judge describes him as knowing how to "
              "avoid traps and answer them well.",
              "CONFIRMED", "rtl-getti"),
        block("unknown", "Ce qui n'est pas documenté", "What is not documented",
              "Aucun élément du dossier consulté ne décrit de fantasmes, de rituels ou de mise en scène. Les sources "
              "ne documentent pas non plus d'expertise psychiatrique conclusive publiée.",
              "No element of the file consulted describes fantasies, rituals or staging. The sources also do not "
              "document any published conclusive psychiatric expertise.",
              "UNKNOWN", None),
    ],
}

VICTIMOLOGY = {
    "ethics_note": txt("Les caractéristiques ci-dessous décrivent un contexte institutionnel documenté. Elles "
                      "n'expliquent ni ne justifient moralement les crimes.",
                      "The characteristics below describe a documented institutional context. They neither explain "
                      "nor morally justify the crimes."),
    "blocks": [
        block("context", "Sept jeunes femmes placées", "Seven young women in state care",
              "Le magistrat ayant présidé la cour d'assises décrit des victimes placées dans des établissements gérés "
              "par la DDASS et l'APAJH, présentant une déficience mentale légère, et transportées par le même "
              "chauffeur entre leur lieu de travail et leur lieu de résidence.",
              "The magistrate who presided over the assize court describes victims placed in institutions managed by "
              "the DDASS and the APAJH, with mild mental disability, transported by the same driver between workplace "
              "and residence.",
              "CONFIRMED", "rtl-getti"),
        block("vulnerability", "Une vulnérabilité institutionnelle", "An institutional vulnerability",
              "La dépendance à un circuit de prise en charge, la faiblesse du poids de leur parole, et l'absence de "
              "signalement par les établissements constituent des facteurs de vulnérabilité documentés. Ils "
              "concernent le dispositif, pas les personnes.",
              "Dependency on a care circuit, the weak institutional weight of their word, and the absence of reporting "
              "by the institutions are documented vulnerability factors. They concern the system, not the persons.",
              "CONFIRMED", "vINGTminutes-traces"),
        block("analysis", "Le lien avec l'auteur", "The link with the author",
              "Jacqueline Weis avait été placée en nourrice chez la famille Louis ; Françoise Lemoine avait été sa "
              "maîtresse ; les autres venaient de centres où il travaillait comme chauffeur. Le lien n'est pas celui "
              "d'un inconnu : c'est un lien d'accès.",
              "Jacqueline Weis had been fostered with the Louis family; Françoise Lemoine had been his mistress; the "
              "others came from centres where he worked as a driver. The link is not that of a stranger: it is a link "
              "of access.",
              "CONFIRMED", "vINGTminutes-traces"),
    ],
}

COURT = {
    "jurisdiction": txt("France — cour d'assises de l'Yonne (Auxerre), cour d'assises d'appel, Cour de cassation",
                        "France — Yonne Assize Court (Auxerre), appeal assize court, Court of Cassation"),
    "verdict": txt("Coupable de l'assassinat des sept jeunes femmes disparues entre 1977 et 1979.",
                   "Guilty of the murder of the seven young women who disappeared between 1977 and 1979."),
    "sentence": {
        "label": txt("Réclusion criminelle à perpétuité, période de sûreté de 18 ans",
                     "Life imprisonment with an 18-year minimum term"),
        "pronounced": "2004-11-25",
        "requested": txt("Procès du 2 au 25 novembre 2004 devant la cour d'assises de l'Yonne.",
                         "Trial from 2 to 25 November 2004 before the Yonne assize court."),
        "cumul": txt("Une autre condamnation a été prononcée en 2004 devant la cour d'assises du Var pour viols et "
                     "actes de barbarie sur sa seconde épouse et sa belle-fille : vingt ans selon Le Monde, avec une "
                     "période de sûreté des deux tiers ; un autre article mentionne 24 ans. L'écart est signalé.",
                     "Another conviction was pronounced in 2004 before the Var assize court for rape and acts of "
                     "barbarity against his second wife and stepdaughter: twenty years according to Le Monde, with a "
                     "two-thirds minimum term; another article mentions 24 years. The discrepancy is flagged."),
        "reasoning": txt("L'accusé a nié les faits en bloc devant la cour. Le témoignage de sa fille aînée a été l'un "
                         "des moments marquants de l'audience.",
                         "The accused denied the facts entirely before the court. The testimony of his eldest daughter "
                         "was one of the striking moments of the hearing."),
        "appeal": txt("Peine confirmée en appel le 27 juin 2006 ; pourvoi rejeté par la Cour de cassation en "
                      "septembre 2007.",
                      "Sentence confirmed on appeal on 27 June 2006; appeal to the Court of Cassation rejected in "
                      "September 2007."),
        "reliability": "CONFIRMED", "source": "monde-yonne",
    },
    "consequences": [
        item("L'affaire est devenue une référence publique sur le traitement des disparitions de personnes placées et "
             "sur les dysfonctionnements institutionnels.",
             "The case became a public reference on the handling of disappearances of people in care and on "
             "institutional dysfunctions.",
             "CONFIRMED", "rtl-getti"),
        item("L'arrêt de la Cour de cassation du 20 février 2002 sur le crime continu de séquestration a une portée "
             "juridique générale.",
             "The Court of Cassation ruling of 20 February 2002 on confinement as a continuing offence has general "
             "legal scope.",
             "CONFIRMED", "monde-yonne"),
        item("La mort du gendarme Jambert reste un point de contestation publique, clos judiciairement par un "
             "non-lieu en 2011.",
             "Gendarme Jambert's death remains a point of public contestation, judicially closed by a dismissal in 2011.",
             "DISPUTED", "lyonne-dates"),
    ],
}

EXPERTS = [
    {"label": txt("Lecture du magistrat ayant présidé le procès", "Reading of the magistrate who presided over the trial"),
     "field": "judicial",
     "position": txt("Jean-Pierre Getti décrit des victimes au profil identique, placées dans des établissements gérés "
                     "par la DDASS et l'APAJH, et de « très nombreux dysfonctionnements ».",
                     "Jean-Pierre Getti describes victims with identical profiles, placed in institutions managed by "
                     "the DDASS and the APAJH, and 'very many dysfunctions'."),
     "reliability": "CONFIRMED", "source": "rtl-getti"},
    {"label": txt("Lecture de la presse d'investigation locale", "Reading of the local investigative press"),
     "field": "investigation",
     "position": txt("Le rapport du gendarme Jambert de 1984 désignait déjà un suspect principal ; son absence de "
                     "suite est présentée comme le point de bascule du dossier.",
                     "Gendarme Jambert's 1984 report already named a prime suspect; its lack of follow-up is "
                     "presented as the turning point of the file."),
     "reliability": "CONFIRMED", "source": "lyonne-dates"},
]
EXPERTS_AGREEMENT = txt("Les deux lectures s'accordent : l'information existait en 1984 et n'a pas été exploitée.",
                        "Both readings agree: the information existed in 1984 and was not exploited.")
EXPERTS_DISAGREEMENT = txt("Elles divergent sur la part respective des institutions de placement et de la chaîne pénale.",
                           "They diverge on the respective share of the placement institutions and of the criminal chain.")
EXPERTS_UNCERTAIN = txt("Ce qui reste incertain : l'effet précis qu'aurait eu une suite donnée au rapport de 1984.",
                        "What remains uncertain: the precise effect that following up the 1984 report would have had.")

COUNTERFACTUALS = [
    counterfactual(
        "report_not_followed",
        "Et si le rapport de 1984 avait eu une suite ?",
        "What if the 1984 report had been followed up?",
        "Le gendarme Christian Jambert a remis en 1984 un rapport d'enquête préliminaire désignant Émile Louis comme "
        "principal suspect dans la disparition de six des sept jeunes femmes. Ce rapport est resté sans suite. Le "
        "dossier n'a été jugé qu'en 2004.",
        "Gendarme Christian Jambert submitted in 1984 a preliminary investigation report naming Émile Louis as prime "
        "suspect in the disappearance of six of the seven young women. That report was not followed up. The file was "
        "tried only in 2004.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Rapport Jambert", "Jambert report"), "date": "1984-02-01"},
            "hypothesis": {"label": txt("Rapport sans suite", "Report not followed up"), "date": "1984-02-28"},
            "scenario_event": {"label": txt("Arrêt de la Cour de cassation écartant la prescription", "Court of Cassation ruling ruling out prescription"), "date": "2002-02-20"},
            "outcome_event": {"label": txt("Condamnation à perpétuité", "Life sentence"), "date": "2004-11-25"},
            "documented_offences_after": [
                {"date": "1983-01-01", "label": txt("Condamnation pour attentats à la pudeur sur mineures (5 ans, 4 en appel)", "Conviction for indecent assaults on minors (5 years, 4 on appeal)"), "reliability": "CONFIRMED"},
                {"date": "2004-03-26", "label": txt("Condamnation devant la cour d'assises du Var (viols, actes de barbarie)", "Conviction before the Var assize court (rape, acts of barbarity)"), "reliability": "CONFIRMED"},
            ],
            "jurisdiction_note": txt(
                "Point juridique essentiel : en 1996, le parquet a refusé de donner suite à la plainte de "
                "l'association au motif que les faits étaient prescrits. Ce n'est qu'en 2002 que la Cour de cassation "
                "a retenu le caractère continu de la séquestration. Un scenario d'instruction ouverte dès 1984 se "
                "serait donc heurté à la même question de prescription, dans l'état du droit alors applicable. "
                "L'application ne peut pas affirmer qu'une issue judiciaire aurait été différente.",
                "Essential legal point: in 1996, the prosecution refused to follow up the association's complaint on "
                "the grounds that the facts were time-barred. It was only in 2002 that the Court of Cassation held "
                "confinement to be a continuing offence. A scenario of an investigation opened as early as 1984 would "
                "therefore have met the same question of prescription, in the state of the law then applicable. The "
                "application cannot state that a judicial outcome would have been different."),
        },
        [
            {"date": "1979-09-26", "kind": "offence", "label": txt("Dernière disparition (Martine Renault)", "Last disappearance (Martine Renault)")},
            {"date": "1981-07-05", "kind": "fact", "label": txt("Corps de Sylviane Lesage découvert", "Sylviane Lesage's body discovered")},
            {"date": "1984-02-01", "kind": "reference", "label": txt("Rapport Jambert", "Jambert report")},
            {"date": "1984-02-28", "kind": "hypothesis", "label": txt("Rapport sans suite", "Report not followed up")},
            {"date": "1996-01-01", "kind": "fact", "label": txt("Relance par l'association", "Revival by the association")},
            {"date": "2000-12-12", "kind": "fact", "label": txt("Arrestation et aveux", "Arrest and confessions")},
            {"date": "2002-02-20", "kind": "scenario", "label": txt("Prescription écartée", "Prescription ruled out")},
            {"date": "2004-11-25", "kind": "outcome", "label": txt("Condamnation", "Conviction")},
        ],
        True, "sudouest-parcours"),
    counterfactual(
        "forensic_delay",
        "Et si deux corps exhumés en 2000 avaient pu parler en 1984 ?",
        "What if two bodies exhumed in 2000 could have spoken in 1984?",
        "Les squelettes de Jacqueline Weis et de Madeleine Dejust ont été retrouvés en décembre 2000 sur les "
        "indications d'Émile Louis. En 1984, date du rapport Jambert, aucune localisation n'était connue.",
        "The skeletons of Jacqueline Weis and Madeleine Dejust were found in December 2000 on Émile Louis's "
        "indications. In 1984, the date of the Jambert report, no location was known.",
        {
            "unit": "years",
            "reference_event": {"label": txt("Rapport Jambert, aucune localisation connue", "Jambert report, no known location"), "date": "1984-02-01"},
            "hypothesis": {"label": txt("Corps non localisés", "Bodies not located"), "date": "1984-02-01"},
            "scenario_event": {"label": txt("Exhumation de deux corps", "Exhumation of two bodies"), "date": "2000-12-18"},
            "jurisdiction_note": txt(
                "La découverte des corps a dépendu des indications fournies en garde à vue, et non d'une technique "
                "d'analyse. Dire qu'une science plus avancée en 1984 aurait permis de les localiser n'est pas "
                "documenté : la localisation reposait sur une parole, pas sur un scellé.",
                "The discovery of the bodies depended on indications given in police custody, not on an analysis "
                "technique. Saying that more advanced science in 1984 would have located them is not documented: "
                "location rested on speech, not on an exhibit."),
        },
        [
            {"date": "1984-02-01", "kind": "reference", "label": txt("Aucun corps localisé", "No body located")},
            {"date": "2000-12-18", "kind": "scenario", "label": txt("Deux corps exhumés", "Two bodies exhumed")},
        ],
        False, "sudouest-parcours"),
]

LESSONS = [
    item("Une disparition signalée comme une fugue cesse d'exister pour la justice : la qualification initiale "
         "détermine tout le reste.",
         "A disappearance recorded as running away ceases to exist for the justice system: the initial qualification "
         "determines everything else.",
         "CONFIRMED", "vINGTminutes-traces", "Qualification", "Qualification"),
    item("Un rapport d'enquête peut désigner un suspect et rester sans effet : la transmission entre gendarmerie et "
         "autorité judiciaire est un maillon critique.",
         "An investigation report can name a suspect and remain without effect: transmission between gendarmerie and "
         "judicial authority is a critical link.",
         "CONFIRMED", "sudouest-parcours", "Chaîne pénale", "Criminal chain"),
    item("Une interprétation juridique peut bloquer un dossier pendant des années, puis être renversée : la "
         "qualification de crime continu a rendu le procès possible en 2002.",
         "A legal interpretation can block a file for years, then be reversed: the qualification of continuing offence "
         "made the trial possible in 2002.",
         "CONFIRMED", "monde-yonne", "Droit", "Law"),
    item("Des aveux peuvent être produits par une croyance erronée sur la prescription : leur valeur doit être "
         "examinée à l'audience, ce qui a été fait en 2004 malgré la rétractation.",
         "Confessions can be produced by a mistaken belief about prescription: their value must be examined at the "
         "hearing, which was done in 2004 despite the retraction.",
         "CONFIRMED", "vINGTminutes-traces", "Aveux", "Confessions"),
    item("La persistance d'une association et la médiatisation ont suppléé l'inaction institutionnelle.",
         "The persistence of an association and media coverage made up for institutional inaction.",
         "CONFIRMED", "monde-yonne", "Société civile", "Civil society"),
    item("Les personnes placées et dépendantes sont les victimes les plus exposées à l'oubli : c'est un constat "
         "victimologique, pas une fatalité.",
         "People in care and dependent are the victims most exposed to oblivion: this is a victimological finding, not "
         "a fatality.",
         "CONFIRMED", "rtl-getti", "Vulnérabilité", "Vulnerability"),
]

UNKNOWNS = [
    item("La localisation des cinq corps jamais retrouvés.", "The location of the five bodies never recovered.",
         "UNKNOWN", "sudouest-parcours"),
    item("Les circonstances exactes de la mort du gendarme Christian Jambert en 1997.",
         "The exact circumstances of gendarme Christian Jambert's death in 1997.", "DISPUTED", "lyonne-dates"),
    item("La peine exacte prononcée à Draguignan en 2004 : les sources donnent 20 ou 24 ans.",
         "The exact sentence pronounced in Draguignan in 2004: sources give 20 or 24 years.", "DISPUTED", "monde-yonne"),
    item("Les âges exacts de plusieurs victimes au moment de leur disparition : les sources divergent de un à huit ans.",
         "The exact ages of several victims at the time of disappearance: sources differ by one to eight years.",
         "DISPUTED", "lyonne-dates"),
]

SECTIONS = merge_sections(default_sections(), [
    {"key": "introduction", "blocks": [block(
        "paragraph", "Sept disparitions, vingt ans d'oubli", "Seven disappearances, twenty years of oblivion",
        "Entre 1977 et 1979, sept jeunes femmes placées dans des institutions de l'Yonne disparaissent. Leurs "
        "disparitions sont qualifiées de fugues. Un rapport de gendarmerie désigne un suspect en 1984 et reste sans "
        "suite. Le procès n'aura lieu qu'en 2004.",
        "Between 1977 and 1979, seven young women placed in Yonne institutions disappear. Their disappearances are "
        "recorded as running away. A gendarmerie report names a suspect in 1984 and is not followed up. The trial "
        "takes place only in 2004.",
        "CONFIRMED", "vINGTminutes-traces")]},
    {"key": "context", "blocks": [block(
        "paragraph", "Un circuit de prise en charge", "A care circuit",
        "Les victimes sont des pupilles de la DDASS prises en charge dans des établissements gérés avec l'APAJH, dans "
        "un département où ces structures sont nombreuses. Le transport entre le lieu de travail et le lieu de "
        "résidence est assuré par un même chauffeur.",
        "The victims were wards of the DDASS looked after in institutions managed with the APAJH, in a department "
        "where such structures are numerous. Transport between workplace and residence was provided by the same driver.",
        "CONFIRMED", "rtl-getti")]},
    {"key": "offender", "blocks": [block(
        "paragraph", "Émile Louis (1934-2013)", "Émile Louis (1934-2013)",
        "Né le 26 janvier 1934 à Auxerre. Chauffeur de bus, conseiller municipal de Seignelay. Condamné en 2004 à la "
        "réclusion criminelle à perpétuité avec 18 ans de sûreté. Mort en détention le 20 octobre 2013, à 79 ans.",
        "Born 26 January 1934 in Auxerre. Bus driver, municipal councillor of Seignelay. Sentenced in 2004 to life "
        "imprisonment with an 18-year minimum term. Died in custody on 20 October 2013, aged 79.",
        "CONFIRMED", "lyonne-dates")]},
    {"key": "behaviour", "blocks": [block(
        "behaviour", "Agir là où la parole ne compte pas", "Acting where speech does not count",
        "Le comportement documenté est un comportement d'opportunité institutionnelle : les victimes dépendaient d'un "
        "circuit qui ne signalait pas leurs absences. Ce n'est pas une explication du passage à l'acte, c'est une "
        "description des conditions qui l'ont rendu invisible.",
        "The documented behaviour is one of institutional opportunity: the victims depended on a circuit that did not "
        "report their absences. This is not an explanation of the act, it is a description of the conditions that made "
        "it invisible.",
        "CONFIRMED", "vINGTminutes-traces")]},
    {"key": "arrest", "blocks": [block(
        "paragraph", "12 décembre 2000", "12 December 2000",
        "Émile Louis est interpellé, à Draguignan selon 20 Minutes. Croyant les faits prescrits, il reconnaît sept "
        "meurtres, puis se rétracte en janvier 2001.",
        "Émile Louis is arrested, in Draguignan according to 20 Minutes. Believing the facts time-barred, he admits "
        "seven murders, then retracts in January 2001.",
        "CONFIRMED", "vINGTminutes-traces")]},
    {"key": "consequences", "blocks": [block(
        "paragraph", "Une jurisprudence et un débat", "A case-law ruling and a debate",
        "L'arrêt du 20 février 2002 fait de la séquestration un crime continu tant que le corps n'est pas retrouvé. "
        "L'affaire a aussi ouvert un débat public durable sur la protection des personnes placées.",
        "The ruling of 20 February 2002 makes confinement a continuing offence as long as the body is not found. The "
        "case also opened a lasting public debate on the protection of people in care.",
        "CONFIRMED", "monde-yonne")]},
])

EPISODES = [
    {
        "number": 1,
        "title": txt("Le car de ramassage", "The collection bus"),
        "description": txt("Yonne, 1977-1979. Sept jeunes femmes placées disparaissent. Personne ne les cherche.",
                           "Yonne, 1977-1979. Seven young women in care disappear. Nobody looks for them."),
        "modes": ["documentary", "investigation", "victims", "chronology", "express", "psychology", "expert"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [
            {"at": 0, "title": txt("Ouverture", "Opening")},
            {"at": 60, "title": txt("Sept prénoms", "Seven first names")},
            {"at": 240, "title": txt("Des fugues", "Runaways")},
            {"at": 420, "title": txt("Le rapport de 1984", "The 1984 report")},
            {"at": 600, "title": txt("Et maintenant, une question", "And now, a question")},
        ],
        "transcript": {"segments": [
            {"id": "l1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X, à travers mon regard. Aujourd'hui, nous allons revenir sur une affaire "
                     "française qui n'a pas commencé par un crime. Elle a commencé par un mot : fugue.",
             "text_en": "You are on YANIS//X, through my eyes. Today we return to a French case that did not begin "
                        "with a crime. It began with a word: runaway."},
            {"id": "l2", "t": 60, "speaker": "yanis",
             "text": "Yonne, entre 1977 et 1979. Christine Marlot, quinze ans. Jacqueline Weis, dix-huit ans. "
                     "Chantal Gras, dix-huit ans. Madeleine Dejust, vingt et un ans. Bernadette Lemoine, dix-neuf "
                     "ans. Françoise Lemoine, vingt-six ans. Martine Renault, seize ans. Sept jeunes femmes, toutes "
                     "placées, toutes prises en charge dans des établissements du département.",
             "text_en": "Yonne, between 1977 and 1979. Christine Marlot, fifteen. Jacqueline Weis, eighteen. Chantal "
                        "Gras, eighteen. Madeleine Dejust, twenty-one. Bernadette Lemoine, nineteen. Françoise "
                        "Lemoine, twenty-six. Martine Renault, sixteen. Seven young women, all in state care, all "
                        "looked after in institutions of the department."},
            {"id": "l3", "t": 240, "speaker": "yanis",
             "text": "Aucun centre ne signale ces disparitions. Elles sont qualifiées de fugues. Un homme, pourtant, "
                     "est présent dans chacune de ces histoires : Émile Louis, le chauffeur de car qui transporte ces "
                     "jeunes femmes entre leur établissement et leur lieu de résidence. Jacqueline Weis avait été "
                     "placée en nourrice chez lui. Françoise Lemoine avait été sa maîtresse.",
             "text_en": "No centre reports these disappearances. They are recorded as running away. Yet one man is "
                        "present in each of these stories: Émile Louis, the bus driver who transported these young "
                        "women between their institution and their residence. Jacqueline Weis had been fostered with "
                        "him. Françoise Lemoine had been his mistress."},
            {"id": "l4", "t": 420, "speaker": "yanis",
             "text": "En février 1984, Émile Louis bénéficie d'un non-lieu dans l'affaire Sylviane Lesage, cette "
                     "jeune femme de vingt-trois ans retrouvée morte dans une étable de Rouvray en juillet 1981. La "
                     "même année, le gendarme Christian Jambert remet un rapport d'enquête préliminaire. Il explique "
                     "pourquoi Émile Louis doit être considéré comme le suspect numéro un dans la disparition de six "
                     "de ces sept jeunes femmes. Le rapport reste sans suite.",
             "text_en": "In February 1984, Émile Louis obtains a dismissal in the Sylviane Lesage case, the "
                        "twenty-three-year-old found dead in a barn in Rouvray in July 1981. The same year, gendarme "
                        "Christian Jambert submits a preliminary investigation report. He explains why Émile Louis "
                        "should be considered the prime suspect in the disappearance of six of these seven young "
                        "women. The report is not followed up."},
            {"id": "l5", "t": 600, "speaker": "yanis",
             "text": "Et maintenant, une question. Pas un jugement. Une réflexion.",
             "text_en": "And now, a question. Not a judgement. A reflection."},
            {"id": "l6", "t": 640, "speaker": "yanis",
             "text": "Il faudra attendre 1996 pour qu'une association dépose plainte — plainte refusée, faits "
                     "prescrits. Décembre 2000 pour des aveux, obtenus parce que leur auteur croyait à cette "
                     "prescription. Février 2002 pour que la Cour de cassation retienne que la séquestration est un "
                     "crime continu. Et le 25 novembre 2004 pour une condamnation à la réclusion criminelle à "
                     "perpétuité, avec dix-huit ans de sûreté. Cinq corps n'ont jamais été retrouvés.",
             "text_en": "It took until 1996 for an association to file a complaint — complaint refused, facts "
                        "time-barred. December 2000 for confessions, obtained because their author believed in that "
                        "prescription. February 2002 for the Court of Cassation to hold that confinement is a "
                        "continuing offence. And 25 November 2004 for a life sentence with an eighteen-year minimum "
                        "term. Five bodies were never recovered."},
            {"id": "l7", "t": 820, "speaker": "yanis",
             "text": "Écouter les histoires. Comprendre les affaires. Ne jamais oublier les victimes : Christine, "
                     "Jacqueline, Chantal, Madeleine, Bernadette, Françoise, Martine.",
             "text_en": "Listen to the stories. Understand the cases. Never forget the victims: Christine, Jacqueline, "
                        "Chantal, Madeleine, Bernadette, Françoise, Martine."},
        ]},
    },
    {
        "number": 2,
        "title": txt("Jambert", "Jambert"),
        "description": txt("Le gendarme qui avait écrit le rapport. Ce qu'il a vu, ce qu'il a transmis, et ce qui est arrivé après.",
                           "The gendarme who wrote the report. What he saw, what he passed on, and what happened after."),
        "modes": ["documentary", "investigation", "expert", "express"],
        "audio_status": "script_only", "voice_profile": "yanis-real",
        "chapters": [{"at": 0, "title": txt("Ouverture", "Opening")}, {"at": 120, "title": txt("1997", "1997")}],
        "transcript": {"segments": [
            {"id": "m1", "t": 0, "speaker": "yanis",
             "text": "Vous êtes sur YANIS//X. Cet épisode porte sur un homme qui n'est ni une victime ni un accusé : "
                     "Christian Jambert, gendarme, auteur en 1984 d'un rapport resté sans suite.",
             "text_en": "You are on YANIS//X. This episode is about a man who is neither a victim nor an accused: "
                        "Christian Jambert, gendarme, author in 1984 of a report left unacted."},
            {"id": "m2", "t": 120, "speaker": "yanis",
             "text": "En 1997, il est retrouvé mort. L'enquête conclut à un suicide. Des proches contestent cette "
                     "version. Une information judiciaire contre X est ouverte en 2004 ; elle se conclut par un "
                     "non-lieu en 2011. Cette application affiche ce point comme CONTESTÉ, et non comme établi.",
             "text_en": "In 1997, he is found dead. The investigation concludes suicide. Relatives dispute that "
                        "version. A judicial investigation against unknown persons is opened in 2004; it ends in a "
                        "dismissal in 2011. This application displays that point as DISPUTED, not as established."},
        ]},
    },
]

QUESTIONS = [
    question("1", 600, "investigation",
             "Sept disparitions sont qualifiées de fugues par les établissements. Quel est l'effet procédural immédiat de cette qualification ?",
             "Seven disappearances are recorded as running away by the institutions. What is the immediate procedural effect of that qualification?",
             [("a", "Aucun : une enquête reste possible", "None: an investigation remains possible"),
              ("b", "Aucune information judiciaire n'est ouverte, et les faits n'existent pas pour la justice", "No judicial investigation is opened, and the facts do not exist for the justice system"),
              ("c", "Les familles sont automatiquement informées", "Families are automatically informed"),
              ("d", "La prescription est interrompue", "Prescription is interrupted")],
             {"fr": {"whatInvestigatorsKnew": "En 1977-1979, aucun centre ne signale les disparitions ; elles sont qualifiées de fugues.",
                     "whatExpertsProposed": "Une fugue présumée d'une mineure ou d'une majeure placée n'ouvre pas, en soi, d'information judiciaire pour enlèvement. Le dossier n'existe pas tant qu'il n'est pas qualifié pénalement.",
                     "documented": "20 Minutes et RTL documentent l'absence de signalement et la qualification de fugue.",
                     "hypothetical": "Ce qu'une qualification différente aurait produit concrètement à l'époque.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir qu'un rapport de gendarmerie de 1984 désignerait un suspect principal.",
                     "answer_note": "La réponse attendue est B. Elle décrit un effet procédural, elle ne juge personne."},
              "en": {"whatInvestigatorsKnew": "In 1977-1979, no centre reported the disappearances; they were recorded as running away.",
                     "whatExpertsProposed": "A presumed runaway of a minor or an adult in care does not, in itself, open a judicial investigation for abduction. The file does not exist until it is criminally qualified.",
                     "documented": "20 Minutes and RTL document the absence of reporting and the runaway qualification.",
                     "hypothetical": "What a different qualification would concretely have produced at the time.",
                     "whatYouCouldNotKnow": "You could not know that a 1984 gendarmerie report would name a prime suspect.",
                     "answer_note": "The expected answer is B. It describes a procedural effect; it judges no one."}},
             "vINGTminutes-traces"),
    question("1", 760, "chronology",
             "Émile Louis avoue sept meurtres en décembre 2000. Pourquoi ces aveux sont-ils juridiquement fragiles ?",
             "Émile Louis confesses seven murders in December 2000. Why are these confessions legally fragile?",
             [("a", "Parce qu'ils ont été obtenus sans avocat", "Because they were obtained without a lawyer"),
              ("b", "Parce qu'ils reposent sur sa croyance que les faits étaient prescrits, et qu'il s'est rétracté", "Because they rest on his belief that the facts were time-barred, and he retracted"),
              ("c", "Parce qu'aucun corps n'a été retrouvé", "Because no body was recovered"),
              ("d", "Ils ne sont pas fragiles", "They are not fragile")],
             {"fr": {"whatInvestigatorsKnew": "Les aveux ont été recueillis en garde à vue, alors que l'intéressé croyait les faits prescrits ; il s'est rétracté en janvier 2001 en invoquant la pression des gendarmes.",
                     "whatExpertsProposed": "Un aveu rétracté conserve une valeur probatoire, mais elle est discutée à l'audience. Ici, deux corps ont été retrouvés sur ses indications, ce qui a conforté le dossier.",
                     "documented": "La rétractation, les deux exhumations et la condamnation de 2004 malgré la négation à l'audience sont documentées.",
                     "hypothetical": "Ce qu'aurait donné un procès fondé uniquement sur des aveux rétractés, sans exhumation.",
                     "whatYouCouldNotKnow": "Vous ne pouviez pas savoir que la Cour de cassation écarterait la prescription en 2002 au titre du crime continu de séquestration.",
                     "answer_note": "La réponse attendue est B. C est factuellement faux : deux corps ont été retrouvés."},
              "en": {"whatInvestigatorsKnew": "The confessions were collected in police custody, while the person believed the facts time-barred; he retracted in January 2001 invoking pressure from the gendarmes.",
                     "whatExpertsProposed": "A retracted confession retains evidential value, but it is argued at the hearing. Here, two bodies were found on his indications, which strengthened the file.",
                     "documented": "The retraction, the two exhumations and the 2004 conviction despite denial at the hearing are documented.",
                     "hypothetical": "What a trial based solely on retracted confessions, without exhumation, would have produced.",
                     "whatYouCouldNotKnow": "You could not know that the Court of Cassation would rule out prescription in 2002 on the basis of confinement as a continuing offence.",
                     "answer_note": "The expected answer is B. C is factually wrong: two bodies were recovered."}},
             "vINGTminutes-traces"),
]

CASE = {
    "id": CASE_ID,
    "title": txt("Les disparues de l'Yonne", "The missing women of the Yonne"),
    "subtitle": txt("Auxerre, 1977-1979. Sept jeunes femmes placées, un rapport de gendarmerie sans suite, vingt-cinq ans avant un procès.",
                    "Auxerre, 1977-1979. Seven young women in care, a gendarmerie report left unacted, twenty-five years before a trial."),
    "country": "FR", "region": "Bourgogne / Yonne", "city": "Auxerre",
    "year_start": 1977, "year_end": 2013, "period_label": txt("1977 – 2013", "1977 – 2013"),
    "status": "PARTIALLY_RESOLVED",
    "status_note": txt("Condamnation définitive prononcée en 2006 ; cinq corps n'ont jamais été retrouvés.",
                       "Final conviction pronounced in 2006; five bodies were never recovered."),
    "type": "serial", "tags": ["serial_killer", "institutional_failures", "cold_case", "france", "vulnerable_victims", "prescription"],
    "tier": "PREMIUM", "editorial": "yanis", "published_at": "2026-09-24", "sensitive": True,
    "triggers": txt("Meurtres de jeunes femmes en situation de handicap ; défaillances institutionnelles ; mort contestée d'un gendarme.",
                    "Murders of young women with disabilities; institutional failures; disputed death of a gendarme."),
    "lat": 47.798, "lon": 3.567, "cover": "cover-yonne",
    "stats": {"victims_documented": 7, "bodies_never_found": 5, "duration_years": 36},
    "summary": txt(
        "Entre 1977 et 1979, sept jeunes femmes placées dans des institutions de l'Yonne disparaissent. Leurs "
        "disparitions sont qualifiées de fugues par les établissements et ne sont pas signalées à la justice. En 1984, "
        "le gendarme Christian Jambert remet un rapport désignant Émile Louis, chauffeur de car de ces établissements, "
        "comme principal suspect : le rapport reste sans suite. En 1996, une association relance l'affaire ; le "
        "parquet oppose la prescription. En décembre 2000, Émile Louis est interpellé et avoue sept meurtres, croyant "
        "les faits prescrits ; deux corps sont exhumés sur ses indications, puis il se rétracte. Le 20 février 2002, "
        "la Cour de cassation écarte la prescription au titre du crime continu de séquestration. Le 25 novembre 2004, "
        "la cour d'assises de l'Yonne le condamne à la réclusion criminelle à perpétuité avec 18 ans de sûreté ; la "
        "peine est confirmée en appel en 2006 et le pourvoi rejeté en 2007. Il meurt en détention en 2013. Cinq corps "
        "n'ont jamais été retrouvés.",
        "Between 1977 and 1979, seven young women placed in Yonne institutions disappear. Their disappearances are "
        "recorded as running away by the institutions and are not reported to the justice system. In 1984, gendarme "
        "Christian Jambert submits a report naming Émile Louis, bus driver for those institutions, as prime suspect: "
        "the report is not followed up. In 1996, an association revives the case; the prosecution invokes "
        "prescription. In December 2000, Émile Louis is arrested and confesses seven murders, believing the facts "
        "time-barred; two bodies are exhumed on his indications, then he retracts. On 20 February 2002, the Court of "
        "Cassation rules out prescription on the basis of confinement as a continuing offence. On 25 November 2004, "
        "the Yonne assize court sentences him to life imprisonment with an 18-year minimum term; the sentence is "
        "confirmed on appeal in 2006 and the cassation appeal rejected in 2007. He dies in custody in 2013. Five "
        "bodies were never recovered."),
    "sources": SOURCES, "victims": VICTIMS, "memorial": MEMORIAL, "other_victim": OTHER_VICTIM,
    "timeline": TIMELINE, "locations": LOCATIONS, "evidence": EVIDENCE, "investigation": INVESTIGATION,
    "psychology": PSYCHOLOGY, "victimology": VICTIMOLOGY, "court": COURT, "experts": EXPERTS,
    "experts_agreement": EXPERTS_AGREEMENT, "experts_disagreement": EXPERTS_DISAGREEMENT,
    "experts_uncertain": EXPERTS_UNCERTAIN, "counterfactuals": COUNTERFACTUALS, "lessons": LESSONS,
    "unknowns": UNKNOWNS, "sections": SECTIONS, "episodes": EPISODES, "questions": QUESTIONS,
}
