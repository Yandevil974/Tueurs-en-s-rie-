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
   **3 `produced`** (les 3 fichiers `.wav` de `content/media/`, tous d'Estelle Mouzin et Guy Georges),
   **11 `script_only`**, dont les 2 épisodes de Pickton. Restent donc **11 narrations à produire**.
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
