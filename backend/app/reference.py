"""Reference data: countries (§18-§19), glossary (§29), courses (§28)."""

COUNTRIES = [
    {"code": "FR", "names": {"fr": "France", "en": "France"}, "continent": "Europe", "flag": "🇫🇷"},
    {"code": "GB", "names": {"fr": "Royaume-Uni", "en": "United Kingdom"}, "continent": "Europe", "flag": "🇬🇧"},
    {"code": "US", "names": {"fr": "États-Unis", "en": "United States"}, "continent": "Amérique du Nord", "flag": "🇺🇸"},
    {"code": "DE", "names": {"fr": "Allemagne", "en": "Germany"}, "continent": "Europe", "flag": "🇩🇪"},
    {"code": "ES", "names": {"fr": "Espagne", "en": "Spain"}, "continent": "Europe", "flag": "🇪🇸"},
    {"code": "IT", "names": {"fr": "Italie", "en": "Italy"}, "continent": "Europe", "flag": "🇮🇹"},
    {"code": "BE", "names": {"fr": "Belgique", "en": "Belgium"}, "continent": "Europe", "flag": "🇧🇪"},
    {"code": "CA", "names": {"fr": "Canada", "en": "Canada"}, "continent": "Amérique du Nord", "flag": "🇨🇦"},
    {"code": "JP", "names": {"fr": "Japon", "en": "Japan"}, "continent": "Asie", "flag": "🇯🇵"},
    {"code": "BR", "names": {"fr": "Brésil", "en": "Brazil"}, "continent": "Amérique du Sud", "flag": "🇧🇷"},
    {"code": "AU", "names": {"fr": "Australie", "en": "Australia"}, "continent": "Océanie", "flag": "🇦🇺"},
    {"code": "ZA", "names": {"fr": "Afrique du Sud", "en": "South Africa"}, "continent": "Afrique", "flag": "🇿🇦"},
]

# Every entry: simple explanation first, then deepening (§29).
GLOSSARY = [
    {
        "slug": "modus-operandi",
        "term": {"fr": "Modus operandi", "en": "Modus operandi"},
        "field": "criminology",
        "simple": {
            "fr": "La manière de faire : les gestes, outils et méthodes qu'une personne emploie pour commettre un fait.",
            "en": "The method of operating: the gestures, tools and techniques a person uses to commit an offence.",
        },
        "deep": {
            "fr": "Le modus operandi (MO) est fonctionnel : il permet de réussir le passage à l'acte, de contrôler la victime, de fuir. Il évolue donc avec l'expérience, les circonstances et les opportunités, et il peut être copié. En enquête, la stabilité d'un MO entre plusieurs scènes permet de rapprocher des affaires ; sa variation n'exclut pas pour autant un même auteur.",
            "en": "A modus operandi is functional: it enables the offence to succeed, the victim to be controlled, the escape to happen. It therefore evolves with experience, circumstance and opportunity, and it can be copied. In an investigation, a stable MO across scenes can link cases; variation does not rule out a single author.",
        },
        "case_refs": ["guy-georges", "btk-rader"],
    },
    {
        "slug": "signature-comportementale",
        "term": {"fr": "Signature comportementale", "en": "Behavioural signature"},
        "field": "behavioural_analysis",
        "simple": {
            "fr": "Un élément non nécessaire à la commission du fait, qui répond à un besoin psychologique de l'auteur.",
            "en": "An element not required to commit the offence, which answers a psychological need of the author.",
        },
        "deep": {
            "fr": "À la différence du MO, la signature n'a pas d'utilité pratique : elle est exprimée pour l'auteur. Elle est plus stable dans le temps, mais son interprétation reste une analyse d'expert et non un fait. Deux affaires peuvent partager un MO sans partager de signature, et l'inverse existe.",
            "en": "Unlike the MO, a signature has no practical utility: it is expressed for the author. It tends to be more stable over time, but reading it remains expert analysis rather than fact. Two cases can share an MO without sharing a signature, and the reverse also happens.",
        },
        "case_refs": ["btk-rader", "yorkshire-sutcliffe"],
    },
    {
        "slug": "victimologie",
        "term": {"fr": "Victimologie", "en": "Victimology"},
        "field": "victimology",
        "simple": {
            "fr": "L'étude des victimes : qui elles étaient, leur environnement, les circonstances documentées.",
            "en": "The study of victims: who they were, their environment, the documented circumstances.",
        },
        "deep": {
            "fr": "La victimologie descriptive recense des caractéristiques documentées (âge, lieu, habitudes, contexte, lien éventuel avec l'auteur) pour comprendre le choix des cibles et orienter l'enquête. Elle ne cherche jamais une justification du crime dans la victime : aucune caractéristique personnelle n'explique moralement un passage à l'acte, la responsabilité appartient à l'auteur.",
            "en": "Descriptive victimology records documented characteristics (age, place, routines, context, any link to the author) to understand target selection and guide an investigation. It never seeks a justification for the crime in the victim: no personal characteristic morally explains an offence — responsibility lies with the author.",
        },
        "case_refs": ["disparues-yonne-emile-louis", "estelle-mouzin"],
    },
    {
        "slug": "profilage",
        "term": {"fr": "Profilage", "en": "Criminal profiling"},
        "field": "behavioural_analysis",
        "simple": {
            "fr": "Une hypothèse de travail sur les caractéristiques probables d'un auteur non identifié, construite à partir des scènes.",
            "en": "A working hypothesis about the likely characteristics of an unidentified author, built from the scenes.",
        },
        "deep": {
            "fr": "Le profilage produit des hypothèses, pas des preuves. Sa fiabilité dépend de la qualité des données de scène et de la prudence de l'analyste. Il peut orienter utilement une enquête comme il peut la verrouiller sur une fausse piste lorsqu'il est traité comme une vérité. Aucun profil ne remplace une identification par trace ou par aveu vérifié.",
            "en": "Profiling produces hypotheses, not proof. Its reliability depends on the quality of scene data and the caution of the analyst. It can usefully steer an investigation, or lock it onto a false lead when treated as truth. No profile replaces identification by trace or by verified confession.",
        },
        "case_refs": ["golden-state-killer", "yorkshire-sutcliffe"],
    },
    {
        "slug": "cold-case",
        "term": {"fr": "Cold case", "en": "Cold case"},
        "field": "investigation",
        "simple": {
            "fr": "Une affaire non résolue, dont l'enquête active est interrompue mais qui reste juridiquement ouverte tant qu'elle n'est pas prescrite.",
            "en": "An unsolved case whose active investigation has stopped but which remains legally open until prescribed.",
        },
        "deep": {
            "fr": "Un cold case se définit moins par son ancienneté que par l'absence d'acte d'enquête en cours. Les réouvertures tiennent souvent à une technique nouvelle (ADN, généalogie génétique), à une révélation, à la découverte d'un lien entre dossiers, ou à la persistance des familles. En France, le pôle cold cases de Nanterre a été créé en 2021 pour centraliser ces dossiers.",
            "en": "A cold case is defined less by age than by the absence of ongoing investigative acts. Reopenings usually follow a new technique (DNA, genetic genealogy), a disclosure, a newly discovered link between files, or the persistence of families. In France, the Nanterre cold-case unit was created in 2021 to centralise such files.",
        },
        "case_refs": ["affaire-gregory", "estelle-mouzin"],
    },
    {
        "slug": "preuve-circonstancielle",
        "term": {"fr": "Preuve circonstancielle", "en": "Circumstantial evidence"},
        "field": "justice",
        "simple": {
            "fr": "Un élément qui ne démontre pas directement le fait, mais qui permet de le déduire par raisonnement.",
            "en": "An element that does not directly demonstrate the fact, but from which it can be inferred by reasoning.",
        },
        "deep": {
            "fr": "Un faisceau d'indices graves, précis et concordants peut fonder une conviction juridictionnelle. Sa force vient de la convergence, non d'un élément isolé. C'est aussi sa faiblesse : chaque maillon doit pouvoir être discuté contradictoirement, et une interprétation unique imposée trop tôt conduit à l'erreur judiciaire.",
            "en": "A bundle of serious, precise and consistent indications can found a judicial conviction. Its strength comes from convergence, not from a single element. That is also its weakness: every link must be open to adversarial challenge, and a single interpretation imposed too early leads to miscarriages of justice.",
        },
        "case_refs": ["affaire-gregory", "yorkshire-sutcliffe"],
    },
    {
        "slug": "biais-de-confirmation",
        "term": {"fr": "Biais de confirmation", "en": "Confirmation bias"},
        "field": "cognitive_bias",
        "simple": {
            "fr": "Chercher et retenir surtout les informations qui confirment ce que l'on croit déjà.",
            "en": "Seeking and keeping mostly the information that confirms what one already believes.",
        },
        "deep": {
            "fr": "Dans une enquête, ce biais se traduit par une piste privilégiée trop tôt : les éléments qui la confortent sont survalorisés, ceux qui la contredisent sont négligés ou réinterprétés. Il touche enquêteurs, experts, juges et médias. Les garde-fous documentés sont la pluralité d'hypothèses, la traçabilité des actes et le contradictoire.",
            "en": "In an investigation this bias appears as a lead favoured too early: supporting elements are overvalued, contradicting ones neglected or reinterpreted. It affects investigators, experts, judges and media alike. Documented safeguards are multiple hypotheses, traceability of acts, and adversarial testing.",
        },
        "case_refs": ["affaire-gregory", "disparues-yonne-emile-louis"],
    },
    {
        "slug": "genealogie-genetique",
        "term": {"fr": "Généalogie génétique", "en": "Genetic genealogy"},
        "field": "forensic_science",
        "simple": {
            "fr": "Utiliser l'ADN d'une scène et des bases de données généalogiques pour remonter une famille jusqu'à un individu.",
            "en": "Using crime-scene DNA and genealogy databases to trace a family tree back to an individual.",
        },
        "deep": {
            "fr": "La technique ne désigne pas un coupable : elle identifie des apparentés, puis construit un arbre généalogique que l'on croise avec l'âge, la géographie et d'autres données. Elle ne constitue qu'une piste, qui doit être confirmée par une comparaison ADN directe avec la personne visée. Son usage soulève des questions de consentement et de protection des données, variables selon les pays et encadrées en France.",
            "en": "The technique does not name a culprit: it identifies relatives, then builds a family tree crossed with age, geography and other data. It is only a lead, to be confirmed by direct DNA comparison with the person concerned. Its use raises consent and data-protection questions that vary by country and are regulated in France.",
        },
        "case_refs": ["golden-state-killer"],
    },
    {
        "slug": "fneg",
        "term": {"fr": "FNAEG", "en": "French national DNA database (FNAEG)"},
        "field": "forensic_science",
        "simple": {
            "fr": "Le fichier national automatisé des empreintes génétiques français.",
            "en": "The French automated national database of genetic fingerprints.",
        },
        "deep": {
            "fr": "Créé par la loi du 17 juin 1998, initialement pour les infractions sexuelles, le FNAEG a ensuite été étendu à d'autres catégories d'infractions. Il permet de rapprocher des traces biologiques non identifiées entre elles et avec des personnes déjà fichées. Son élargissement a fait l'objet de débats sur les libertés individuelles et la conservation des profils.",
            "en": "Created by the law of 17 June 1998, initially for sexual offences, the FNAEG was later extended to other categories of offences. It links unidentified biological traces to each other and to recorded persons. Its expansion has been debated in terms of individual liberties and profile retention.",
        },
        "case_refs": ["guy-georges"],
    },
    {
        "slug": "periode-de-surete",
        "term": {"fr": "Période de sûreté", "en": "Minimum term (France)"},
        "field": "justice",
        "simple": {
            "fr": "La période pendant laquelle aucune mesure d'aménagement de peine ne peut être accordée.",
            "en": "The period during which no sentence-adjustment measure may be granted.",
        },
        "deep": {
            "fr": "En droit français, une peine de réclusion à perpétuité peut être assortie d'une période de sûreté fixée par la cour d'assises ; elle peut aller jusqu'à trente ans, ou être « incompressible » dans les cas prévus par la loi. Elle ne signifie pas que la peine s'arrête à son terme : à l'issue, une demande reste possible et son examen relève du juge de l'application des peines.",
            "en": "In French law, a life sentence may carry a minimum term set by the assize court; it can reach thirty years, or be 'incompressible' in cases provided for by law. It does not mean the sentence ends at that point: afterwards a request remains possible and its examination belongs to the sentence-enforcement judge.",
        },
        "case_refs": ["guy-georges", "disparues-yonne-emile-louis", "fourniret-olivier"],
    },
    {
        "slug": "geographie-criminelle",
        "term": {"fr": "Géographie criminelle", "en": "Criminal geography"},
        "field": "geographic_profiling",
        "simple": {
            "fr": "L'étude de la répartition spatiale des faits pour comprendre les déplacements et les zones d'un auteur.",
            "en": "The study of the spatial distribution of offences to understand an author's movements and areas.",
        },
        "deep": {
            "fr": "Les travaux de géographie criminelle (notamment ceux de Kim Rossmo sur le geographic profiling) distinguent des zones de chasse, des zones tampons autour du domicile, et des points d'ancrage liés au travail ou à la famille. Ces modèles produisent des priorités de recherche probabilistes : ils ne localisent pas un domicile, ils ordonnent des hypothèses. Ils supposent une série de faits géolocalisés fiables.",
            "en": "Criminal geography research (notably Kim Rossmo's work on geographic profiling) distinguishes hunting areas, buffer zones around the home, and anchor points linked to work or family. These models produce probabilistic search priorities: they do not locate a home, they order hypotheses. They require a series of reliably geolocated events.",
        },
        "case_refs": ["golden-state-killer", "guy-georges"],
    },
    {
        "slug": "erreur-judiciaire",
        "term": {"fr": "Erreur judiciaire", "en": "Miscarriage of justice"},
        "field": "justice",
        "simple": {
            "fr": "Une condamnation, ou une accusation maintenue, qui ne correspond pas aux faits établis.",
            "en": "A conviction, or a maintained accusation, that does not correspond to the established facts.",
        },
        "deep": {
            "fr": "Les mécanismes documentés sont récurrents : identification erronée par témoin, aveux obtenus sous pression, expertise fragilisée, biais de confirmation, pression médiatique. L'erreur peut aussi être procédurale : des actes annulés pour irrégularité peuvent priver un dossier de ses éléments les plus solides, sans rien établir sur la culpabilité ou l'innocence.",
            "en": "Documented mechanisms recur: mistaken witness identification, confessions obtained under pressure, weakened expert evidence, confirmation bias, media pressure. The error may also be procedural: acts annulled for irregularity can strip a file of its strongest elements without establishing anything about guilt or innocence.",
        },
        "case_refs": ["affaire-gregory", "yorkshire-sutcliffe"],
    },
]

# §28 APPRENDRE — each concept illustrated by documented cases.
COURSES = [
    {
        "slug": "comprendre-une-enquete",
        "field": "investigation",
        "title": {"fr": "Comment se construit une enquête", "en": "How an investigation is built"},
        "intro": {
            "fr": "Une enquête n'est pas une suite de révélations : c'est un processus de collecte, d'hypothèses et de vérifications, avec ses lenteurs et ses erreurs.",
            "en": "An investigation is not a sequence of revelations: it is a process of collection, hypotheses and verification, with its slowness and its errors.",
        },
        "minutes": 12,
        "level": "beginner",
        "case_refs": ["guy-georges", "golden-state-killer"],
        "lessons": [
            {
                "title": {"fr": "Le point de départ : la scène", "en": "The starting point: the scene"},
                "body": {
                    "fr": "Tout commence par une scène figée et documentée : constatations, photographies, relevés, prélèvements. La qualité de cette première étape conditionne tout le reste. Une scène mal protégée perd définitivement des traces.",
                    "en": "Everything starts with a scene frozen and documented: observations, photographs, records, samples. The quality of this first step conditions everything else. A poorly protected scene permanently loses traces.",
                },
                "concept": "scene_documentation",
            },
            {
                "title": {"fr": "Rapprocher les affaires", "en": "Linking cases"},
                "body": {
                    "fr": "Une série se construit par comparaisons : traces biologiques, mode opératoire, zones géographiques, horaires. Le rapprochement n'est jamais automatique : il demande un travail de mise en relation entre services, parfois interrompu par des classements ou des cloisonnements.",
                    "en": "A series is built through comparisons: biological traces, method, geographic areas, timings. Linking is never automatic: it requires cross-service work, sometimes interrupted by case closures or compartmentalisation.",
                },
                "concept": "linkage",
            },
            {
                "title": {"fr": "La piste qui résiste", "en": "The lead that holds"},
                "body": {
                    "fr": "Une piste devient solide lorsqu'elle peut être testée : une trace comparée, un alibi vérifié, une téléphonie exploitée. Ce qui ne peut être ni confirmé ni infirmé reste une hypothèse, et doit être affiché comme telle.",
                    "en": "A lead becomes solid when it can be tested: a compared trace, a verified alibi, exploited phone data. What can be neither confirmed nor refuted remains a hypothesis, and must be displayed as such.",
                },
                "concept": "hypothesis_testing",
            },
            {
                "title": {"fr": "Ce qui fait échouer une enquête", "en": "What makes an investigation fail"},
                "body": {
                    "fr": "Les causes documentées : perte de traces, classement trop rapide, absence de synthèse, succession de magistrats sans transmission, moyens insuffisants, pression médiatique. Plusieurs décisions de justice françaises ont reconnu ces dysfonctionnements.",
                    "en": "Documented causes: lost traces, premature closure, absence of synthesis, succession of magistrates without handover, insufficient resources, media pressure. Several French court decisions have recognised such failures.",
                },
                "concept": "failure_modes",
            },
        ],
    },
    {
        "slug": "victimologie",
        "field": "victimology",
        "title": {"fr": "Victimologie : regarder les personnes", "en": "Victimology: looking at the persons"},
        "intro": {
            "fr": "La victimologie ne cherche pas pourquoi une victime a été choisie au sens moral : elle décrit, à partir de faits documentés, un environnement, un contexte, une vulnérabilité situationnelle.",
            "en": "Victimology does not ask why a victim was chosen in a moral sense: it describes, from documented facts, an environment, a context, a situational vulnerability.",
        },
        "minutes": 10,
        "level": "beginner",
        "case_refs": ["disparues-yonne-emile-louis", "estelle-mouzin"],
        "lessons": [
            {
                "title": {"fr": "Avant d'être une victime", "en": "Before being a victim"},
                "body": {
                    "fr": "Toute fiche commence par la personne : prénom, âge, études, travail, famille, projets. C'est une règle éditoriale et une exigence de rigueur : une biographie documentée vaut mieux qu'un rôle dans un récit.",
                    "en": "Every file begins with the person: first name, age, studies, work, family, projects. This is an editorial rule and a rigour requirement: a documented biography is worth more than a role in a narrative.",
                },
                "concept": "person_first",
            },
            {
                "title": {"fr": "Vulnérabilité situationnelle", "en": "Situational vulnerability"},
                "body": {
                    "fr": "Certaines situations exposent davantage : isolement, dépendance institutionnelle, trajet habituel, jeune âge, précarité. Décrire ces facteurs sert à comprendre un contexte et à prévenir, jamais à répartir une responsabilité.",
                    "en": "Some situations expose people more: isolation, institutional dependency, routine journeys, young age, precarity. Describing these factors helps understand a context and prevent harm, never to distribute responsibility.",
                },
                "concept": "situational_vulnerability",
            },
            {
                "title": {"fr": "Les victimes oubliées", "en": "Forgotten victims"},
                "body": {
                    "fr": "Des disparitions signalées comme des fugues, des victimes marginalisées, des dossiers jamais rapprochés : l'oubli institutionnel est un objet d'étude en soi. Il explique une partie des longues séries non détectées.",
                    "en": "Disappearances recorded as running away, marginalised victims, files never linked: institutional forgetting is a subject of study in itself. It explains part of long undetected series.",
                },
                "concept": "institutional_blindness",
            },
        ],
    },
    {
        "slug": "biais-cognitifs",
        "field": "cognitive_bias",
        "title": {"fr": "Biais cognitifs dans l'enquête", "en": "Cognitive biases in investigation"},
        "intro": {
            "fr": "Enquêter, c'est raisonner sous incertitude. Les biais ne sont pas une faiblesse morale : ce sont des mécanismes documentés qui déforment le raisonnement de tous.",
            "en": "To investigate is to reason under uncertainty. Biases are not a moral weakness: they are documented mechanisms that distort everyone's reasoning.",
        },
        "minutes": 9,
        "level": "intermediate",
        "case_refs": ["yorkshire-sutcliffe", "affaire-gregory"],
        "lessons": [
            {
                "title": {"fr": "L'ancrage", "en": "Anchoring"},
                "body": {
                    "fr": "La première information reçue pèse durablement sur l'interprétation des suivantes. Un suspect désigné très tôt devient difficile à abandonner, même lorsque les éléments contraires s'accumulent.",
                    "en": "The first piece of information received weighs durably on how later ones are read. A suspect named very early becomes hard to abandon, even as contrary elements accumulate.",
                },
                "concept": "anchoring",
            },
            {
                "title": {"fr": "Le biais de confirmation", "en": "Confirmation bias"},
                "body": {
                    "fr": "On sélectionne, inconsciemment, ce qui confirme l'hypothèse en cours. Le contre-mesure documentée consiste à formaliser plusieurs hypothèses concurrentes et à chercher activement ce qui les infirme.",
                    "en": "One unconsciously selects what confirms the current hypothesis. The documented counter-measure is to formalise several competing hypotheses and actively seek what would falsify them.",
                },
                "concept": "confirmation_bias",
            },
            {
                "title": {"fr": "La crédulité face au récit", "en": "Credulity towards narrative"},
                "body": {
                    "fr": "Un courrier, une cassette ou une revendication peuvent orienter une enquête entière. L'authenticité d'une communication doit être testée, et non présupposée : des affaires ont été déviées par des canulars.",
                    "en": "A letter, a tape or a claim can steer a whole investigation. The authenticity of a communication must be tested, not presumed: cases have been diverted by hoaxes.",
                },
                "concept": "narrative_capture",
            },
        ],
    },
    {
        "slug": "police-scientifique",
        "field": "forensic_science",
        "title": {"fr": "Police scientifique : ce que peut une trace", "en": "Forensic science: what a trace can do"},
        "intro": {
            "fr": "Une trace est un élément matériel transféré lors d'un contact. Elle ne parle pas d'elle-même : elle devient une preuve par une chaîne de recueil, d'analyse et d'interprétation.",
            "en": "A trace is material transferred during a contact. It does not speak for itself: it becomes evidence through a chain of collection, analysis and interpretation.",
        },
        "minutes": 11,
        "level": "intermediate",
        "case_refs": ["golden-state-killer", "btk-rader"],
        "lessons": [
            {
                "title": {"fr": "L'échange de Locard", "en": "Locard's exchange principle"},
                "body": {
                    "fr": "« Tout contact laisse une trace. » Le principe guide le recueil, mais il a une contrepartie : les traces se dégradent, se contaminent, se perdent. Le délai et les conditions de conservation sont décisifs.",
                    "en": "'Every contact leaves a trace.' The principle guides collection, but it has a counterpart: traces degrade, contaminate, are lost. Timing and storage conditions are decisive.",
                },
                "concept": "locard",
            },
            {
                "title": {"fr": "L'ADN et ses limites", "en": "DNA and its limits"},
                "body": {
                    "fr": "Un profil ADN permet une comparaison, pas une histoire. Un profil partiel, un mélange, une contamination réduisent sa force. La présence d'ADN n'établit ni le moment ni le mode de dépôt.",
                    "en": "A DNA profile allows a comparison, not a story. A partial profile, a mixture, a contamination reduce its strength. The presence of DNA establishes neither the moment nor the mode of deposition.",
                },
                "concept": "dna_limits",
            },
            {
                "title": {"fr": "Les métadonnées", "en": "Metadata"},
                "body": {
                    "fr": "Un document numérique conserve des informations techniques : auteur déclaré, application, horodatage. Elles orientent, puis doivent être recoupées : un nom d'utilisateur n'est pas une identification.",
                    "en": "A digital document retains technical information: declared author, application, timestamps. They orient, then must be cross-checked: a username is not an identification.",
                },
                "concept": "metadata",
            },
        ],
    },
    {
        "slug": "analyse-comportementale",
        "field": "behavioural_analysis",
        "title": {"fr": "Analyse comportementale : lire sans surinterpréter", "en": "Behavioural analysis: reading without over-interpreting"},
        "intro": {
            "fr": "Distinguer ce qu'un comportement montre de ce qu'il laisse supposer. C'est la compétence centrale du module DANS LA TÊTE.",
            "en": "Distinguishing what a behaviour shows from what it lets us suppose. This is the central skill of the IN THE MIND module.",
        },
        "minutes": 10,
        "level": "advanced",
        "case_refs": ["btk-rader", "fourniret-olivier"],
        "lessons": [
            {
                "title": {"fr": "Fait, hypothèse, analyse, inconnu", "en": "Fact, hypothesis, analysis, unknown"},
                "body": {
                    "fr": "Quatre étiquettes, systématiquement. Un fait est documenté ; une hypothèse est une proposition ; une analyse d'expert est une lecture professionnelle ; un inconnu reste un inconnu. Mélanger les quatre produit de la fiction.",
                    "en": "Four labels, systematically. A fact is documented; a hypothesis is a proposition; an expert analysis is a professional reading; an unknown stays unknown. Mixing the four produces fiction.",
                },
                "concept": "four_labels",
            },
            {
                "title": {"fr": "Planification et impulsivité", "en": "Planning and impulsivity"},
                "body": {
                    "fr": "Un comportement préparé (repérage, matériel, itinéraire de fuite) n'exclut pas une part d'improvisation, et inversement. La scène montre des gestes, pas une intention certaine.",
                    "en": "Prepared behaviour (reconnaissance, equipment, escape route) does not exclude improvisation, and vice versa. The scene shows gestures, not a certain intention.",
                },
                "concept": "organised_disorganised",
            },
            {
                "title": {"fr": "La mise en scène", "en": "Staging"},
                "body": {
                    "fr": "Modifier une scène pour orienter l'enquête est un comportement documenté. Sa détection repose sur des incohérences entre les traces et le récit proposé. Elle reste une interprétation, discutée au procès.",
                    "en": "Altering a scene to steer an investigation is a documented behaviour. Its detection relies on inconsistencies between traces and the proposed account. It remains an interpretation, argued at trial.",
                },
                "concept": "staging",
            },
        ],
    },
]
