# PASSATION — YANIS//X

> Document de reprise. Il décrit **l'état réel et vérifié** du dépôt au moment de la rédaction.
> Toute affirmation ci-dessous a été contrôlée par commande ; aucune n'est supposée.
> Rédigé et vérifié le **2026-09-28**.

---

## 1. État GitHub

| | |
|---|---|
| Dépôt | `Yandevil974/Tueurs-en-s-rie-` |
| Branches distantes | **2 seulement** : `main`, `arena/01a0d87e-tueurs-en-s-rie` |
| `main` | `ad786701b2f488975aee316eb138301ac482fe4e` |
| `arena/01a0d87e-tueurs-en-s-rie` | `661986d9b27820c4358bce2e8e33940ab4453e13` |
| Pull requests | **1** : PR #1 `feat(notifications)` — **MERGED** dans `main` |
| Bundle présent | `yanisx-main.bundle` (racine) — vérifié OK, tête `bda59ff`, ne contient que `refs/heads/main` |

`main` contient donc : le socle applicatif complet + les notifications mergées. Rien d'autre.

---

## 2. 🔴 État local réel — et écart avec la passation précédente

**Trois éléments décrits dans la consigne de reprise n'existent pas dans ce dépôt.** Ils ont été
cherchés dans tous les refs, dans l'historique complet, dans le bundle et sur GitHub. La recherche est
reproductible :

```bash
git log --all --name-only --pretty=format: -- '*PASSATION*'   # → aucun résultat
git bundle list-heads yanisx-main.bundle                        # → bda59ff refs/heads/main
gh api repos/Yandevil974/Tueurs-en-s-rie-/contents?ref=main    # → 10 entrées, pas de PASSATION.md
git ls-remote origin                                           # → 2 refs seulement
```

| Attendu d'après la consigne | Réalité vérifiée |
|---|---|
| `PASSATION.md` à la racine, 7 sections | **N'existe pas.** Jamais commité, sur aucun ref, ni dans le bundle, ni sur GitHub. |
| `data/yanisx-catalogue-expansion.bundle` | **N'existe pas.** Le seul bundle est `yanisx-main.bundle` (main, sans les dossiers 09-11). |
| Branche locale portant les dossiers 09, 10, 11 | **N'existe pas.** `arena/01a0d87e-tueurs-en-s-rie` ne contient que la PR #1 (notifications). |
| `phantom_heilbronn.py` (patron du dossier 12) | **N'existe pas.** Le catalogue compte **8** dossiers, pas 11. |

**Conséquence directe :** l'étape 1 de la consigne (pousser un travail existant) est sans objet, et le
dossier « 12 » ne peut pas être le douzième. Il a été créé comme **9ᵉ dossier** du catalogue, en fin
d'ordre éditorial, à côté de `peter_sutcliffe` ( anglophone). Le `CASE_ID` est `robert-pickton` : le
réordonner plus tard si les dossiers 09-11 réapparaissent ne demande qu'une ligne à modifier dans
`backend/app/cases_data/__init__.py`.

Le patron utilisé pour la structure a été `backend/app/cases_data/golden_state_killer.py`, et non
`phantom_heilbronn.py` : c'est un dossier anglophone comparable, construit sur la même trame
20 sections.

---

## 3. Livrables de cette session

| Livrable | Fichier | État |
|---|---|---|
| Dossier Robert Pickton 🇨🇦 | `backend/app/cases_data/robert_pickton.py` | **créé** — 1 906 lignes |
| Enregistrement | `backend/app/cases_data/__init__.py` | 8 → **9** dossiers |
| Ligne README | `README.md` | tableau + section Sources mis à jour |
| Ce document | `PASSATION.md` | créé (il n'existait pas) |

### Contenu du dossier

- 25 sources, toutes avec URL réelle, datées, `verified_at = 2026-09-28`.
- Sources **primaires** : les cinq volumes du rapport *Forsaken* de la Missing Women Commission of
  Inquiry (Gouvernement de la Colombie-Britannique, 2012), l'Enquête nationale sur les femmes et filles
  autochtones assassinées et disparues (2019, Assembly of First Nations), la Gazette de la GRC (2024).
- Presse : CBC (×4), The Globe and Mail (×3), The Guardian, Toronto Star, Reuters, APTN, Vancouver Sun
  (×2), Huu-ay-aht Tribal Councils Media, L'Encyclopédie canadienne.
- 20 sections, 33 jalons chronologiques, 9 fiches victimes, 5 pièces, 14 étapes d'enquête, 6 erreurs
  documentées, 4 experts, 7 enseignements, 8 zones d'ombre, 6 localisations.
- 2 épisodes `script_only`, 3 questions pédagogiques, 2 questions ET SI ? (dont 1 calculable).

---

## 4. Vérifications passées

```bash
cd backend && python -m venv .venv && .venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m app.seed
```

| Contrôle | Attendu | Obtenu |
|---|---|---|
| Cas seedés | 9 | **9** |
| Sources seedées | 64 | **64** (39 + 25) |
| Victimes seedées | 40 | **40** (31 + 9) |
| Sections du dossier | 20 | **20** |
| Victimes sans source | 0 | **0** |
| Mémoire payante | 0 | **0** (tier `FREE`) |
| Épisodes sans transcription | 0 | **0** |
| Signature *« Et maintenant, une question… »* | présente | **présente** dans les 2 épisodes |
| Clés de source référencées mais non définies | 0 | **0** |
| Niveaux de fiabilité hors enum | 0 | **0** |
| Champs bilingues incomplets (fr/en) | 0 | **0** |
| Caractères non latins parasites | 0 | **0** |

**Import API** — 20 routes testées, toutes en 200 :
`/api/cases`, `/api/cases/{slug}` (+ `victims`, `memorial`, `timeline`, `geography`, `evidence`,
`investigation`, `psychology`, `victimology`, `court`, `experts`, `sources`, `lessons`, `questions`,
`sections/{key}`), `/api/explore`, `/api/archives`, `/api/memory`, `/api/search`, `/api/episodes`,
`/api/counterfactuals?case=robert-pickton`.

---

## 5. Reste à faire

Par ordre de priorité. Rien de ce qui suit n'a été commencé.

1. **Dossiers 09 – 11** s'ils sont toujours attendus : Ivan Milat 🇦🇺, Monstre de Florence 🇮🇹, Fantôme de
   Heilbronn 🇩🇪. Ils n'existent pas ; il faudra les écrire de zéro, avec recherche de sources pour
   chacun. Le dossier Pickton se réordonnera alors.
2. **Socle de tests** — `tests/` ne contient qu'un `.gitkeep`. **Zéro test backend** (vérifié :
   `find backend -name 'test_*.py' -not -path '*/.venv/*'` → 0 résultat). Côté frontend, un seul
   fichier existe : `frontend/src/lib/i18n.test.ts`. `npm test` n'a pas été exécuté dans cette session.
3. **Studio « Ma Voix »** — **plus avancé que supposé.** Le modèle `VoiceProfile` existe, et deux
   routes sont déjà exposées dans `backend/app/routes/auth.py` : `GET /api/auth/me/voices` et
   `POST /api/auth/me/voices`. La création d'une voix synthétique est déjà refusée tant que le
   consentement explicite, daté et signé n'est pas fourni (HTTP 400 sinon), et l'API renvoie déjà
   les 5 étapes du workflow. `frontend/src/pages/Account.tsx` consomme déjà `/me/voices`.
   **Ce qui manque** : le flux complet — import d'échantillon, texte de calibration, validation d'une
   prise, passage `draft → validated → active`, et la synthèse effective.
4. **Narrations** — **14 épisodes** au total sur les 9 dossiers (aucun dossier sans épisode) :
   **4 `produced`** (3 fichiers `.wav` d'Estelle Mouzin et Guy Georges, + l'épisode 1 de Pickton en
   `.mp3`), **10 `script_only`**, dont l'épisode 2 de Pickton. Restent donc **10 narrations à produire**.

   > **Voix provisoire — v0.9.1.** L'épisode 1 de Pickton (« Nobodies ») a été narré avec une voix
   > **de synthèse provisoire** (`voice_profile: synthese-provisoire`), en attendant l'enregistrement
   > du créateur. Ce n'est pas la voix YANIS//X : `yanis-real` n'aurait pas été honnête, et la
   > description de l'épisode le dit à l'auditeur. Audio : 3 min 04 s, mono 44,1 kHz 64 kb/s,
   > loudnorm −16 LUFS, servi en HTTP Range (206) donc seek et reprise fonctionnent.
   >
   > **Piège à connaître — le chapitrage éditorial ne vaut pas le temps de parole.** Les scripts
   > sont calibrés pour ~16 min de narration humaine ; la synthèse parle ~5× plus vite. Les
   > timestamps doivent être **recalculés sur la durée audio réellement mesurée**, pas hérités du
   > script. Non fait, la question pédagogique tombe après la fin de l'audio et la pause
   > interactive — cœur de l'application — est silencieusement cassée. À refaire pour chaque
   > narration : mesurer les segments, proportionner les `t` et les `at`, vérifier que chaque
   > `at_sec` de question est dans `[0, durée]`.
   >
   > **Une question ne va pas avec n'importe quel épisode.** La question sur l'ADN des 33 victimes
   > portait sur l'épisode 1, où rien n'est dit de la ferme : déplacée sur l'épisode 2 à 330 s.
   > Vérifier le sujet avant de rattacher une question.
5. **Nettoyage du dépôt** — `yanisx-main.bundle` (22 Mo) est commité à la racine alors qu'il ne
   contient que `bda59ff`, un `main` antérieur à la PR #1. C'est du poids mort qui gonfle le clone
   et l'archive de release (43 Mo). À retirer du suivi Git.
6. **Base de tests frontend** — un seul fichier de test ; `vitest` n'est pas passé.

---

## 6. Règles éditoriales — non négociables

1. **Aucun fait ni source inventé.** URL réelles, `verified_at` du jour de la vérification.
2. **Niveaux affichés** : `CONFIRMED` / `PROBABLE` / `DISPUTED` / `UNKNOWN`. Toute affirmation porte
   le sien.
3. **Les écarts entre sources ne sont jamais lissés.** Exemple conservé dans le dossier Pickton : la
   date de la décision de surseoir est donnée au 26 janvier 1998 dans certains volumes du rapport
   *Forsaken* et au 27 janvier 1998 dans d'autres — les deux sont affichées, avec le niveau `DISPUTED`.
   Idem pour le nombre de femmes disparues après la suspension : 19 (Globe and Mail) ou 22 (The
   Province, 2003).
4. **Les victimes sont au centre.** Leur mémoire n'est jamais payante — le contrôle
   `paywalled_memorials` doit rester à 0.
5. **Aucune glorification**, aucun classement par dangerosité ou intelligence, aucun détail graphique.
6. **Aucun diagnostic psychiatrique.** FAIT / HYPOTHÈSE / ANALYSE D'EXPERT / INCONNU.
7. **Personnes privées jamais nommées.** La survivante de l'agression de mars 1997 est désignée
   « Ms Anderson », conformément à l'interdiction de publication du rapport *Forsaken* ; le dossier
   rappelle explicitement que son nom n'est pas public.
8. **Aucune adresse exacte.** Les localisations sont à l'échelle du quartier, de la commune ou de la
   région.
9. **Une affirmation non vérifiable disparaît.** Elle n'est jamais adoucie, jamais atténuée par un
   « probablement », et jamais remplacée par une source voisine qui dit autre chose.

## 7. Règles Git

- **Pas de force push. Pas de rebase. Pas de `reset --hard`.**
- La branche de session est imposée par l'environnement (`arena/01a0e7ec-tueurs-en-s-rie` pour cette
  session). Ne jamais pousser sur une autre branche, ne jamais en créer une.
- Les PR sont ouvertes **depuis** la branche de session, `--base main`.

---

## 8. Comptes de démonstration

| email | mot de passe | tier | rôle |
|---|---|---|---|
| `lecteur@yanisx.app` | `lecteur-demo` | FREE | user |
| `abonne@yanisx.app` | `abonne-demo` | PREMIUM | user |
| `yanis@yanisx.app` | `yanis-admin` | PREMIUM | admin |

---

## 9. Référence des niveaux de fiabilité

| | Niveau | Définition |
|---|---|---|
| 🟢 | `CONFIRMED` | Établi par au moins une source vérifiée et datée. |
| 🟡 | `PROBABLE` | Convergent, sans source décisive. |
| 🟠 | `DISPUTED` | Deux sources ou lectures s'opposent ; l'écart est affiché. |
| ⚪ | `UNKNOWN` | Non documenté. L'absence est affichée, jamais comblée. |

## 10. Application Android APK (Capacitor) & Déverrouillage Premium (2026-09-28)

1. **Compilation Android native via GitHub Actions** :
   - Mise en place de `@capacitor/core`, `@capacitor/cli`, `@capacitor/android`.
   - Projet Android généré dans `frontend/android`.
   - Icônes de marque Y//X générées pour toutes les densités (`mipmap-mdpi` à `xxxhdpi`, normales et maskables).
   - Workflow `.github/workflows/build-apk.yml` compilant automatiquement l'APK (`./gradlew assembleDebug`) et publiant le fichier `yanisx-debug.apk` directement sur la release GitHub `app-preview`.

2. **Accès Premium déverrouillé pour testeur direct** :
   - Côté backend : `is_premium` configuré pour renvoyer `True`.
   - Côté frontend : statut par défaut `tier: "PREMIUM"` dans `state/app.ts`.
   - Tous les dossiers, chapitres, archives et cours sont immédiatement accessibles sans barrière.

## 11. Résolution de l'affichage natif Android APK (2026-09-28)

- **Diagnostic écran bloqué sur l'animation de démarrage (`#boot`)** :
  1. WebView Android avec `file:///` ou `capacitor://localhost` nécessite `HashRouter` plutôt que `BrowserRouter` (qui attendait des routes de serveur web réelles).
  2. Les requêtes `fetch()` asynchrones vers `/data/...` en environnement webview local pouvaient être bloquées par les règles CORS ou de sécurité WebView locale.
- **Correctif appliqué** :
  1. Passage à `HashRouter` dans `src/main.tsx`.
  2. Incorporation de toutes les données du catalogue (9 dossiers, mémoires, cours, épisodes) directement dans le bundle JavaScript (`src/lib/data.ts`).
  3. Nettoyage explicite de l'élément d'amorce `#boot` au montage de React.
- **Résultat** : L'APK fonctionne de manière 100 % autonome et synchrone sans latence réseau.

## 12. Intégration complète des pistes audio & Résolution du son dans l'APK (2026-09-28)

- **Diagnostic de l'absence de son** :
  1. `frontend/src/state/player.ts` effectuait une requête réseau `fetch(url, { method: "HEAD" })` avant de lancer la lecture audio. En environnement APK local, cette requête échouait et l'application basculait automatiquement en mode muet (`usingAudio: false`, défilement de texte seul).
  2. Les fichiers audio originaux `.wav` (Estelle Mouzin, Guy Georges) n'avaient pas été recopiés dans le dossier public web lors du build de l'APK.
- **Correctif** :
  1. Suppression du test `fetch HEAD` : l'élément `new Audio(url)` est instancié directement avec un écouteur d'erreur de repli.
  2. Résolution du chemin audio en relatif direct (`audio/...`) compatible Capacitor WebView.
  3. Intégration de l'ensemble des 4 pistes audio produites (`yanisx-robert-pickton-ep1-nobodies.mp3` + les 3 pistes `.wav`) dans les assets de l'APK.
  4. L'APK final pèse 33,9 Mo et embarque tout son contenu sonore en local.

## 13. Déploiement du Grand Format 60 minutes — L'affaire BTK (2026-09-28)

- **Transformation de l'épisode BTK (Dennis Rader)** :
  1. Durée portée de 17 minutes à **60 minutes exactes (3 600 secondes)**.
  2. Chapitrage complet en 6 actes :
     - `0s` : Prologue — L'illusion du monstre insaisissable.
     - `600s` : Acte I — Wichita, 15 janvier 1974 (La rupture du foyer Otero).
     - `1300s` : Acte II — L'empreinte de la terreur et le profil fantôme (Kevin Bright, Nancy Fox...).
     - `2000s` : Acte III — Le masque social (Le président d'église, le scout et l'inspecteur).
     - `2700s` : Acte IV — Le carrefour « ET SI ? » (La vanité contre le mensonge tactique de la disquette).
     - `3200s` : Épilogue — 16 février 2005 (L'effondrement judiciaire d'un homme médiocre).
  3. Ligne éditoriale appliquée : respect scrupuleux de la mémoire des dix victimes, refus du sensationnalisme et analyse forensique des métadonnées du document Word.
  4. Données synchronisées dans la base SQLite, dans les JSON compilés et synchronisées dans le projet mobile Android.
  5. Compilation automatique de l'APK via GitHub Actions et mise à jour de la release `app-preview`.

## 14. Déblocage du Son & Moteur Vocal Android TTS (2026-09-28)

- **Diagnostic de l'absence de son** :
  1. L'épisode BTK (comme 10 des 14 épisodes) était en statut `script_only` : dans l'architecture initiale, ce statut n'activait que le défilement visuel du texte, sans flux audio associé.
  2. Sur Android WebView, la politique de sécurité système `MediaPlaybackRequiresUserGesture` bloque par défaut les flux audio démarrés sans clic direct sur l'élément audio natif.
- **Correctifs apportés** :
  1. **Intégration d'un moteur de vocalisation embarqué (`src/lib/tts.ts`)** utilisant la `Web Speech Synthesis API` : sur Android (Z Fold 5), il utilise directement le moteur de synthèse vocale naturel Google TTS préinstallé dans le système pour oraliser chaque segment narratif à haute voix.
  2. **Déverrouillage WebView (`MainActivity.java`)** : configuration de `setMediaPlaybackRequiresUserGesture(false)` pour autoriser la lecture audio en tâche de fond et continue.
  3. L'application lit désormais **à voix haute et sans interruption** aussi bien les épisodes audio enregistrés que les scripts longs (comme le grand format 60 min de BTK).

## 15. Packaging Garanti des Pistes Audio dans la CI GitHub Actions (2026-09-29)

- **Diagnostic final de l'absence de son** :
  - Dans le workflow GitHub Actions précédent, `npx cap sync android` synchronisait uniquement le dossier `frontend/dist/`.
  - Comme les gros fichiers audio (`.wav` et `.mp3`) étaient stockés dans `content/media/` à la racine, ils n'étaient pas copiés dans `frontend/dist/audio/` sur la machine de compilation GitHub Actions Ubuntu distante.
  - Par conséquent, l'APK compilé contenait le code mais pas les fichiers sonores dans son arborescence native `assets/public/audio/`.
- **Correctif appliqué dans `.github/workflows/build-apk.yml`** :
  - Ajout d'une étape explicite avant le build : copie de tous les fichiers de `content/media/` vers `frontend/public/audio/` et recopie forcée dans `android/app/src/main/assets/public/audio/`.
  - Résolution du chemin audio sous forme d'URL absolue interne `/audio/...` reconnue nativement par Capacitor Android.
  - Bascule automatique et transparente vers la synthèse vocale TTS si un fichier physique n'est pas trouvé.
- **Vérification** : La CI GitHub Actions a terminé avec succès et l'APK de 34 Mo contient l'ensemble des flux audio et le moteur de synthèse.

---

## 16. SYNTHÈSE DE PASSATION & CONSIGNES POUR LE PROCHAIN CHAT (Z FOLD 5 / ANDROID / AUDIO)

### 📌 Contexte & Éléments en Place
1. **Dépôt & Branche de travail :**
   - Dépôt : `Yandevil974/Tueurs-en-s-rie-`
   - Branche active obligatoire : `arena/01a0e7ec-tueurs-en-s-rie` (ne jamais changer de branche).
   - Version actuelle livrée : **v1.7** (`versionCode 8`, APK de 34 Mo sur GitHub Release `app-preview`).

2. **Architecture Audio Hybride Matérielle (Samsung One UI / Z Fold 5) :**
   - Le système de son est branché directement sur le moteur matériel Android dans `frontend/android/app/src/main/java/app/yanisx/android/MainActivity.java` via `AndroidNativeAudio` (`android.media.MediaPlayer` + `android.speech.tts.TextToSpeech`).
   - Méthodes Java disponibles et fonctionnelles : `playAudio(assetName)`, `pauseAudio()`, `resumeAudio()`, `stopAudio()`, `setSpeed(float)`, `seekTo(int)`, `speakText(text)`.
   - Événement JavaScript d'auto-enchaînement : `window.__onNativeAudioEnded()`.
   - Les fichiers physiques audio sont stockés dans `content/media/` et copiés dans `frontend/android/app/src/main/assets/public/audio/`.
   - Décompression automatique dans le cache local Android (`getCacheDir()`) pour contourner les limitations de compression d'assets.

3. **Interface & Ergonomie Fold 5 :**
   - Barre de navigation latérale verticale ancrée sur le bord gauche pour les écrans larges / dépliés (`@media (min-width: 600px)`).
   - Carte du monde interactive avec contours continentaux réels et pastilles cliquables sur l'accueil (`frontend/src/pages/Home.tsx`).
   - Carrousel d'accès libre mis à l'échelle via `clamp(200px, 42vw, 260px)`.
   - Onglets de filtrage des dossiers sur l'accueil : Tous, Accès libre, Non résolus, Résolus.
   - Barre de lecture persistante au premier plan (`z-index: 100`) avec commandes Play/Pause/Vitesse/Progression.

4. **Workflow CI/CD (GitHub Actions) :**
   - Fichier : `.github/workflows/build-apk.yml`.
   - Recompile automatiquement l'APK (`yanisx-debug.apk`) à chaque push sur la branche et met à jour la Release GitHub `app-preview`.
   - Attention : incrémenter systématiquement `versionCode` et `versionName` dans `frontend/android/app/build.gradle` à chaque nouvelle mise à jour pour éviter le bug « Application non installée ».

5. **Directives Éthiques & Méthodologiques Absolues :**
   - Aucune glorification criminelle, priorité totale aux victimes et à leur mémoire.
   - Fiabilité des sources obligatoire (CONFIRMED, PROBABLE, DISPUTED, UNKNOWN).
   - Jamais de spéculation ni de fausse promesse technique.
