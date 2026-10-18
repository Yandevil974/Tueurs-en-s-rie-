# ARENA//X — les IA collaborent, tu récoltes la meilleure réponse

Un **seul fichier** (`index.html`) qui propose **deux façons d'obtenir une réponse** :

- **Collaboration** — plusieurs modèles écrivent en parallèle, un **synthétiseur** fusionne,
  corrige et rédige une réponse finale unique.
- **Solo** — **un seul modèle** répond directement, sans brouillons ni synthèse.

Les deux options existent **en gratuit et en premium**, se choisissent en un clic et sont
mémorisées. Streaming en direct, métriques, votes, crédits OpenRouter suivis à chaque manche,
sauvegarde JSON automatique — aucune dépendance, aucun serveur.

```
Ouvre index.html  →  choisis Collaboration ou Solo  →  pose ta question
   Collaboration :  N modèles écrivent  →  le synthétiseur fusionne  →  1 réponse
   Solo          :  1 modèle choisi écrit                          →  1 réponse
```

## Démarrer

1. Ouvre `index.html` (double-clic, `file://`, ou GitHub Pages).
2. Sans clé, tout fonctionne en **mode démonstration** : l'interface, le streaming simulé,
   les métriques, la synthèse, les votes et les sauvegardes sont testables.
3. Clique l'onglet **Réglages** (⚙) et colle **une seule clé pour commencer** :
   - **tu as déjà Groq** → colle la clé `gsk_…` de
     [console.groq.com/keys](https://console.groq.com/keys). Elle suffit pour le **gratuit**
     (collaboration et solo) : le catalogue se limite alors aux modèles Groq et le panneau
     se recalcule tout seul (2 modèles + synthèse, à cause des 8 000 tokens/minute du palier).
   - une clé [OpenRouter](https://openrouter.ai/keys) `sk-or-…` est **optionnelle** : elle
     débloque les modèles `:free` d'OpenRouter et tout le **premium** facturé.
   - une [clé de gestion](https://openrouter.ai/settings/management-keys) OpenRouter est
     optionnelle aussi : elle affiche le **solde restant** exact en premium.

```bash
# tester sur le téléphone, même Wi-Fi
python3 -m http.server 8000 --bind 0.0.0.0 --directory ai-arena
# puis ouvrir http://IP-DU-PC:8000/
```

## Deux catalogues × deux façons de répondre

**Catalogues** (bouton Gratuit / Premium de l'en-tête) :

| | 🍃 Gratuit | 💎 Premium |
|---|---|---|
| Modèles | les meilleurs `:free` d'OpenRouter + Groq | les meilleurs modèles payants |
| Coût | 0 $ | facturé par OpenRouter |
| Suivi | compteur « démo » / coût de la manche | **crédits restants affichés à chaque utilisation** |
| Recharge | — | [openrouter.ai/settings/credits](https://openrouter.ai/settings/credits) |

**Façons de répondre** (sélecteur `Collaboration | Solo`, présent dans l'accueil et dans la
barre de panneau) :

| | 🤝 Collaboration | 🎯 Solo |
|---|---|---|
| Appels par question | 3 brouillons (2 si Groq seul) + 1 synthèse | **1 seul appel** |
| Affichage | cartes de brouillons + carte « Réponse finale » | une seule carte « Réponse » |
| Choix | panneau de brouillons + synthétiseur | **un seul modèle** |
| Mémoire | un panneau par catalogue | un modèle solo par catalogue |

Le choix est **persistant** (il survit au rechargement) et se règle à deux endroits :
le sélecteur de l'accueil / de la barre de panneau pour basculer instantanément, ou le
bouton **Panneau** pour choisir précisément les modèles. En Solo, le premier modèle proposé
est présélectionné : l'app est utilisable immédiatement.

### Comment la collaboration fonctionne

1. **Consultation** — chaque modèle du panneau reçoit la question et rédige un brouillon
   indépendant, en streaming.
2. **Synthèse** — un modèle dédié reçoit la question **et tous les brouillons**. Sa consigne
   (modifiable) : vérifier les faits, corriger les erreurs, fusionner les apports, supprimer
   les redites, ne jamais mentionner les modèles, répondre dans la langue de la question.
3. Si la synthèse échoue, le brouillon le plus complet est affiché et signalé
   (« Meilleur brouillon »), avec un bouton pour relancer la synthèse. Si **tous** les
   brouillons échouent, une carte d'erreur explique quoi vérifier et propose de relancer
   la manche ou d'ouvrir les réglages : une manche ne reste jamais vide.

Chaque manche affiche les **deux étapes** (`1 Consultation` / `2 Synthèse`) avec leur état,
les brouillons repliables (Markdown rendu à l'ouverture), la réponse finale, les métriques
(latence, tok/s, tokens, coût) et les actions : 👍/👎, copier, relancer la synthèse.

## Crédits suivis à chaque utilisation

- **Avec une clé de gestion** : `GET /api/v1/credits` → solde du compte =
  `total_credits − total_usage`. C'est la valeur affichée dans la pastille et dans le dialogue,
  rafraîchie après chaque manche premium.
- **Sans clé de gestion** : `GET /api/v1/key` → usage et plafond de la clé ; la page explique
  la différence et propose de créer une clé de gestion.
- Couleurs de la pastille : vert (ok), ambre (< 5 $), rouge (< 1 $), gris (non configuré).
- Chaque manche premium enregistre aussi son coût et son **solde après coup** dans le fil.
- Lien de recharge dans l'en-tête, le dialogue Crédits et le dialogue Sauvegardes.

## Sauvegarde JSON automatique (Android)

Le bouton **↓** de l'en-tête ouvre le dialogue **Sauvegarde JSON** :

- **Automatique** — après chaque manche (intervalle 5 / 10 / 30 / 60 min), un fichier
  `arena-x-sauvegarde-AAAAMMJJ-HHMM.json` est écrit dans les téléchargements.
  Sur Chrome Android, autorise « Télécharger plusieurs fichiers » pour laisser tourner
  la sauvegarde.
- **Partager** — `navigator.share()` avec le fichier : Drive, Fichiers, Gmail, Telegram…
  (la voie la plus fiable pour sortir le JSON du téléphone).
- **Restaurer** — relit un fichier exporté (conversations, panneaux, réglages, votes).
- **Tout effacer** — supprime les `arenax.*` de `localStorage` après confirmation.

Le JSON contient `app`, `schema`, `version`, `exportedAt`, `settings`, `panels`, `synths`,
`turns` — **jamais les clés**. La conversation est aussi conservée en continu dans
`localStorage` (reprise après fermeture de l'onglet).

## Ce qui est inclus

- **Streaming SSE réel** (OpenRouter + Groq) via `fetch` + `ReadableStream`, bouton
  **Arrêter**, délai 150 s, relance ciblée de la synthèse.
- **Lecture robuste** : `delta.content` texte ou tableau, usage et `finish_reason`,
  repli non-streamé si le fournisseur renvoie du JSON, `stream_options.include_usage`.
- **Métriques** : TTFT, tok/s, tokens, coût (usage du fournisseur, sinon estimation et « ≈ »),
  et pour le premium le **solde restant** (clé de gestion) ou l'usage de la clé après la manche.
- **Markdown sûr** : HTML échappé d'abord, liens en liste blanche, tableaux, listes,
  citations, blocs de code avec bouton copier.
- **Mode démo intégral** : aucun appel réseau, textes simulés distincts par modèle.
- **Panneau à deux visages** : en Collaboration, recherche + onglets Brouillons/Synthèse +
  presets + 4 brouillons max ; en Solo, sélection unique en un clic. Sélection persistante
  par catalogue **et** par mode.
- **Clés** : `localStorage` ou `sessionStorage` (case « mémoriser »), affichage masqué,
  bouton « Tester » les trois connexions avec message d'erreur lisible.
- **Thèmes** sombre / clair / système, sans flash au chargement.
- **Mobile d'abord** : 0 px de débordement de 320 à 1440 px, barre de panneau collante,
  composeur fixe, dialogues plein écran.
- **Accessibilité** : `<dialog>` natif, focus visible, `aria-live`, lien d'évitement,
  navigation clavier (`Ctrl/⌘ + ↵`), `prefers-reduced-motion`, styles d'impression.

## Fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | l'application complète (HTML + CSS + JS inline) |
| `README.md` | ce document : usage, modes, crédits, sauvegarde |
| `GUIDE.md` | méthode technique : performances, streaming, sécurité, pièges |

## Limites connues

- Les appels partent **du navigateur** : les clés sont visibles dans l'onglet. Pour un site
  public, passe par un proxy serveur (voir `GUIDE.md`).
- OpenRouter met `/credits` en cache ~60 s : le solde peut accuser un léger retard.
- Les identifiants `:free` changent souvent : le catalogue est rafraîchi depuis
  `/api/v1/models` et une liste locale sert de secours hors ligne.
- Chrome Android peut bloquer les téléchargements répétés : autorise-les, ou utilise
  **Partager**.
