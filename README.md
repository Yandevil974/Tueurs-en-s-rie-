# YANIS//X — à travers mon regard

Application documentaire interactive sur les affaires criminelles réelles : podcast, dossiers, criminologie,
psychologie, victimologie, enquête, archives et mémoire.

**Ce n'est ni une simple application de podcast, ni une base de données de tueurs en série, ni un produit
sensationnaliste.**

The interactive documentary application about real criminal cases: podcast, dossiers, criminology, psychology,
victimology, investigation, archives and memory. Not a simple podcast app, not a serial-killer database, not
sensationalism.

---

## Le parcours / The journey

`ÉCOUTER → DÉCOUVRIR → RÉFLÉCHIR → QUESTIONNER → ANALYSER → COMPRENDRE → ENQUÊTER → APPRENDRE → RENDRE HOMMAGE`

Le principe central : l'audio s'arrête à un moment stratégique, une question pédagogique à choix multiples
apparaît, puis une explication distingue **ce que les enquêteurs savaient**, **ce que les experts ont proposé**,
**ce qui est documenté** et **ce qui reste hypothétique** — avant la reprise automatique de la lecture.

The core principle: audio stops at a strategic moment, a multiple-choice pedagogical question appears, then an
explanation separates **what investigators knew**, **what experts proposed**, **what is documented** and **what
remains hypothetical** — before playback resumes automatically.

---

## Règles éditoriales absolues / Absolute editorial rules

- **Aucune donnée inventée.** Chaque fait porte un niveau de fiabilité et sa source datée.
  *No invented data. Every fact carries a reliability level and its dated source.*
- **Aucune glorification**, aucune romanticisation, aucun classement par dangerosité ou intelligence.
  *No glorification, no romanticisation, no ranking by dangerousness or intelligence.*
- **Les victimes sont au centre** et leur mémoire n'est **jamais payante**.
  *Victims come first and their memory is never paywalled.*
- **Aucun diagnostic psychiatrique** : FAIT / HYPOTHÈSE / ANALYSE D'EXPERT / INCONNU.
  *No psychiatric diagnosis: FACT / HYPOTHESIS / EXPERT ANALYSIS / UNKNOWN.*
- **Aucun bouton décoratif, aucun écran mort, aucune fiction présentée comme réelle.**
  *No decorative button, no dead screen, no fiction presented as real.*
- Aucune adresse privée exacte n'est publiée. *No exact private address is published.*

### Les quatre niveaux de fiabilité / The four reliability levels

| | Niveau / Level | Définition / Definition |
|---|---|---|
| 🟢 | **CONFIRMÉ / Confirmed** | Établi par au moins une source vérifiée et datée. |
| 🟡 | **PROBABLE / Probable** | Convergent, sans source décisive. |
| 🟠 | **CONTESTÉ / Disputed** | Deux sources ou lectures s'opposent ; l'écart est affiché. |
| ⚪ | **INCONNU / Unknown** | Non documenté. L'absence est affichée, jamais comblée. |

---

## Catalogue de lancement / Launch catalogue — 8 dossiers

| Dossier | Pays | Période | Statut |
|---|---|---|---|
| L'affaire Estelle Mouzin | 🇫🇷 | 2003 – 2025 | Partiellement résolue |
| Affaire Grégory Villemin | 🇫🇷 | 1984 – aujourd'hui | Non résolue |
| Guy Georges | 🇫🇷 | 1991 – 2001 | Résolue |
| Les disparues de l'Yonne (Émile Louis) | 🇫🇷 | 1977 – 2006 | Partiellement résolue |
| Michel Fourniret et Monique Olivier | 🇫🇷 🇧🇪 | 1987 – 2025 | Partiellement résolue |
| BTK — Dennis Rader | 🇺🇸 | 1974 – 2005 | Résolue |
| Golden State Killer — Joseph DeAngelo | 🇺🇸 | 1974 – 2020 | Résolue |
| Peter Sutcliffe (Yorkshire) | 🇬🇧 | 1975 – 2020 | Résolue |

Chaque dossier expose la structure canonique en **20 chapitres** : Introduction, Contexte, Auteur, Victime(s),
Chronologie, Enquête, Indices, Analyse comportementale, Psychologie, Victimologie, Géographie, Arrestation, Procès,
Justice, Conséquences, Archives, Sources, Mémoire, Zones d'ombre, Ce que l'affaire nous apprend.

---

## Modules / Modules

- 🎧 **Podcasts interactifs** — 7 modes : Documentaire, Enquête, Chronologie, Victimes, Express, Psychologie, Expert.
- 🔎 **Mode Enquête** — l'information apparaît dans l'ordre où les enquêteurs l'ont obtenue.
- 🧠 **Dans la tête** — analyse comportementale documentée, sans diagnostic.
- 🕯 **Mémoire** — fiches victimes complètes, toujours gratuites.
- 🌍 **Explorer** — MONDE → CONTINENT → PAYS → RÉGION → VILLE → AFFAIRE, carte et comparateur (sans classement).
- 📚 **Archives** — SOURCE / DATE / AUTEUR / TYPE / LIEN / FIABILITÉ.
- 🔎 **ET SI ?** — reconstruction hypothétique calculée à partir de dates documentées, avec mention obligatoire
  « CECI EST UNE RECONSTRUCTION HYPOTHÉTIQUE » et la phrase signature :
  *« Et maintenant, une question. Pas un jugement. Une réflexion. »*
- 🧠 **L'Analyste** — répond uniquement à partir de données documentées ; sinon :
  *« Cette information n'est pas suffisamment documentée. »*
- 🎓 **Formation** — criminologie, victimologie, psychologie criminelle, profilage géographique, biais cognitifs,
  sciences forensiques + glossaire (explication simple puis approfondissement).
- 🎙 **Ma Voix** — studio de voix du créateur ; synthèse vocale uniquement avec consentement explicite, daté et signé.

---

## Architecture

```
yanisx/
├── backend/                 FastAPI + SQLAlchemy 2.0 + SQLite (swappable → Postgres)
│   └── app/
│       ├── main.py          application, CORS, handlers, carte des routes
│       ├── db.py            engine / session / MEDIA_DIR
│       ├── models.py        21 tables (cases, victims, memorials, timeline, evidence,
│       │                    investigation, psychology, victimology, courts, experts,
│       │                    counterfactuals, episodes, questions, media, sources,
│   │                    countries, courses, glossary, users, voice_profiles,
│       │                    revisions, user_progress)
│       ├── ethics.py        constantes éditoriales, niveaux, badges, interdictions
│       ├── reference.py     pays, glossaire, formations
│       ├── case_template.py helpers txt/fact/block/item/source/question/counterfactual
│       ├── seed.py          Python dossiers → SQLite (idempotent) + moteur ET SI ?
│       ├── auth.py          JWT, tiers FREE/PREMIUM, rôles
│       ├── routes/          auth, cases, episodes, counterfactuals, explore,
│       │                    memory, reference, search, progress, media, admin
│       └── cases_data/      les 8 dossiers bilingues, faits sourcés
└── frontend/                Vite + React 19 + TypeScript + zustand (application mobile/web)
```

- **Authentification** : JWT (PBKDF2-SHA256), tiers `FREE` / `PREMIUM`, rôles `user` / `editor` / `admin`.
- **Audio** : diffusion avec support HTTP Range (seek + reprise) ; trois narrations françaises produites dans `content/media/`.
- **Progression** : reprise audio, sections lues, réponses, favoris, réflexions, badges sobres.
- **Frontend** : navigation mobile, lecteur persistant, pauses pédagogiques, transcription synchronisée, carte, recherche, mémoire, i18n FR/EN et studio « Ma voix ».
- **Administration** : reseed, historique des révisions, audit de santé du catalogue
  (victimes non sourcées, mémoire payante, épisodes sans transcription).
- **Bilingue** FR + EN dès le lancement ; architecture prête pour DE / ES / IT / PT.

---

## Démarrage / Getting started

```bash
# 1. Backend
cd backend
pip install -r requirements.txt
python -m app.seed                       # construit la base depuis les dossiers Python
uvicorn app.main:app --host 0.0.0.0 --port 8000
# docs interactives : http://localhost:8000/api/docs
```

Comptes de démonstration / demo accounts:

| email | mot de passe | tier | rôle |
|---|---|---|---|
| `lecteur@yanisx.app` | `lecteur-demo` | FREE | user |
| `abonne@yanisx.app` | `abonne-demo` | PREMIUM | user |
| `yanis@yanisx.app` | `yanis-admin` | PREMIUM | admin |

> En production : changer `YANISX_SECRET`, servir en HTTPS, brancher un vrai fournisseur de paiement
> (le tier ne doit jamais venir du client), activer les sauvegardes de `data/`.

```bash
# 2. Frontend
cd frontend
npm install
npm run dev                 # http://localhost:5173 ; /api est proxyé vers :8000
npm run build               # vérification de production
npm test                    # tests unitaires
```

Variables d'environnement / environment variables : `YANISX_DB`, `YANISX_MEDIA`, `YANISX_SECRET`,
`YANISX_TOKEN_HOURS`, `YANISX_ORIGINS`.

---

## Sources

Toutes les sources sont publiques, datées et vérifiées le **2026-09-24** (presse : franceinfo, ICI / Radio France,
Le Monde, RTL, L'Obs, Les Jours, actu.fr, Marie Claire, Ouest-France ; archives collaboratives : Wikipédia FR/EN,
littérature scientifique). Elles sont exposées par l'API `/api/archives` et `/api/cases/{slug}/sources` avec leur
niveau de fiabilité. Aucune source n'est inventée ; une rumeur n'est jamais présentée comme un fait.

---

## Identité visuelle

« ARCHIVES CRIMINELLES PREMIUM » : noir, anthracite, gris, blanc cassé, rouge sombre en accent.
Aucun gore, aucun crâne, aucune esthétique Halloween.

---

*Ce dépôt contient une application réelle et fonctionnelle — pas une maquette.*
