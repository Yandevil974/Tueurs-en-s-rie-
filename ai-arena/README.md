# ARENA//X — les IA collaborent, tu récoltes la meilleure réponse

Un **seul fichier** (`index.html`, ~190 Ko) qui fait travailler plusieurs modèles d'IA sur la
même question, puis confie leurs brouillons à un **synthétiseur** qui fusionne, corrige et
rédige une réponse finale unique. Streaming en direct, métriques, votes, crédits OpenRouter
suivis à chaque manche, sauvegarde JSON automatique — aucune dépendance, aucun serveur.

```
Ouvre index.html  →  pose ta question  →  N modèles écrivent en parallèle
                                      →  le synthétiseur corrige et fusionne
                                      →  une seule réponse, sourcée par plusieurs IA
```

## Démarrer

1. Ouvre `index.html` (double-clic, `file://`, ou GitHub Pages).
2. Sans clé, tout fonctionne en **mode démonstration** : l'interface, le streaming simulé,
   les métriques, la synthèse, les votes et les sauvegardes sont testables.
3. Clique l'onglet **Réglages** (⚙), colle une clé [OpenRouter](https://openrouter.ai/keys)
   (mode gratuit **et** premium) et, si tu veux, une clé
   [Groq](https://console.groq.com/keys) et une
   [clé de gestion](https://openrouter.ai/settings/management-keys) pour le solde exact.

```bash
# tester sur le téléphone, même Wi-Fi
python3 -m http.server 8000 --bind 0.0.0.0 --directory ai-arena
# puis ouvrir http://IP-DU-PC:8000/
```

## Les deux modes

| | 🍃 Gratuit | 💎 Premium |
|---|---|---|
| Modèles | les meilleurs `:free` d'OpenRouter + Groq | les meilleurs modèles payants |
| Coût | 0 $ | facturé par OpenRouter |
| Suivi | compteur « démo » / coût de la manche | **crédits restants affichés à chaque utilisation** |
| Recharge | — | [openrouter.ai/settings/credits](https://openrouter.ai/settings/credits) |

Le fonctionnement est identique dans les deux modes : **3 brouillons en parallèle** (jusqu'à 4),
puis **1 synthèse**. Seul le panneau de modèles change.

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
- **Panneau de collaboration** : recherche, onglets Brouillons/Synthèse, presets,
  4 brouillons max, sélection persistante par mode.
- **Clés** : `localStorage` ou `sessionStorage` (case « mémoriser »), affichage masqué,
  bouton « Tester » les trois connexions avec message d'erreur lisible.
- **Thèmes** sombre / clair / système, sans flash au chargement.
- **Mobile d'abord** : 0 px de débordement à 390 px, barre de panneau collante,
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
