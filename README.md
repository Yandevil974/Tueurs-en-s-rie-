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
- **Les victimes sont au centre** ; leur mémoire est traitée avec dignité.
  *Victims come first; their memory is treated with dignity.*
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
- 🕯 **Mémoire** — fiches sur les victimes lorsque les sources disponibles permettent de les documenter.
- 🌍 **Explorer** — carte interactive du monde : sélectionner un continent pour découvrir les dossiers associés, puis explorer les pays et régions.
- 📚 **Archives** — SOURCE / DATE / AUTEUR / TYPE / LIEN / FIABILITÉ.
- 🔎 **ET SI ?** — reconstruction hypothétique calculée à partir de dates documentées, avec mention obligatoire
  « CECI EST UNE RECONSTRUCTION HYPOTHÉTIQUE » et la phrase signature :
  *« Et maintenant, une question. Pas un jugement. Une réflexion. »*
- 🧠 **L'Analyste** — répond uniquement à partir de données documentées ; sinon :
  *« Cette information n'est pas suffisamment documentée. »*
- 🎓 **Formation** — criminologie, victimologie, psychologie criminelle, profilage géographique, biais cognitifs,
  sciences forensiques + glossaire (explication simple puis approfondissement).

---

## Architecture

```
yanisx/
├── backend/                 FastAPI + SQLAlchemy + SQLite (swappable → Postgres)
│   └── app/
│       ├── main.py          application, CORS, handlers, carte des routes
│       ├── db.py            engine / session / MEDIA_DIR
│       ├── models.py        dossiers, victimes, chronologie, enquête, sources, audio, formations…
│       ├── ethics.py        règles éditoriales et niveaux de fiabilité
│       ├── reference.py     pays, glossaire et formations
│       ├── case_template.py structure commune des dossiers
│       ├── seed.py          dossiers Python → SQLite (idempotent)
│       ├── routes/          cases, episodes, counterfactuals, explore, memory,
│       │                    reference, search, media
│       └── cases_data/      les 8 dossiers bilingues, faits sourcés
└── frontend/                Vite + React + TypeScript (web et mobile)
```

- **Usage personnel** : aucune connexion, création de compte ou synchronisation utilisateur. Les réglages,
  favoris, réflexions et progressions sont conservés localement dans le navigateur.
- **Accès au contenu** : tous les dossiers, chapitres, analyses, archives et épisodes sont consultables sans abonnement.
- **Audio** : diffusion avec support HTTP Range (recherche dans la piste et reprise) ; trois narrations françaises dans `content/media/`.
- **Frontend** : lecteur persistant, pauses pédagogiques, transcription synchronisée, carte du monde, recherche,
  mémoire, i18n FR/EN et réglages d'accessibilité.
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

```bash
# 2. Frontend
cd frontend
npm install
npm run dev                 # http://localhost:5173 ; /api est proxyé vers :8000
npm run build               # vérification de production
npm test                    # tests unitaires
```

Variables d'environnement / environment variables : `YANISX_DB`, `YANISX_MEDIA`, `YANISX_ORIGINS`.

## Application Android

L'APK de prévisualisation est publié dans la [release GitHub YANIS//X](https://github.com/Yandevil974/Tueurs-en-s-rie-/releases/tag/app-preview).
Il embarque les données du catalogue, la carte du monde et les fichiers audio disponibles pour fonctionner sans serveur sur Android.
Sur un téléphone, télécharge `yanisx-debug.apk`, autorise si nécessaire l'installation depuis le navigateur ou Fichiers, puis installe l'application. Il s'agit d'une build de test, pas d'une application du Play Store.

Le workflow `.github/workflows/build-apk.yml` reconstruit l'APK et met à jour la release `app-preview` à chaque mise à jour de la branche Android active.

---

## Sources

Toutes les sources sont publiques, datées et vérifiées le **2026-09-24** (presse : franceinfo, ICI / Radio France,
Le Monde, RTL, L'Obs, Les Jours, actu.fr, Marie Claire, Ouest-France ; archives collaboratives : Wikipédia FR/EN,
littérature scientifique). Elles sont exposées par l'API `/api/archives` et `/api/cases/{slug}/sources` avec leur
niveau de fiabilité. Aucune source n'est inventée ; une rumeur n'est jamais présentée comme un fait.

---

## Identité visuelle

Identité éditoriale : « YANIS//X — à travers mon regard », avec une palette sombre, du blanc cassé et un accent rouge.
Aucun gore, aucun crâne, aucune esthétique Halloween.

---

*Ce dépôt contient une application réelle et fonctionnelle — pas une maquette.*
