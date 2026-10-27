# Comment construire une arène d'IA performante en un seul fichier HTML

Ce guide accompagne `ai-arena/index.html` — un fichier autonome d'environ 190 Ko qui propose
**deux modes** : en collaboration, plusieurs modèles rédigent des brouillons en parallèle puis
un synthétiseur produit une réponse finale unique ; en solo, un seul modèle répond directement.
Streaming, métriques, crédits OpenRouter suivis à chaque manche, sauvegarde JSON automatique.
Il explique **les décisions techniques** et **ce qu'il faut éviter**.

---

## 1. Pourquoi un seul fichier ?

| Contrainte | Un seul fichier HTML | Projet React/Vite classique |
|---|---|---|
| Mise en route | double-clic, `file://` suffit | `npm install` + build |
| Requêtes avant le premier pixel | **0** | JS + CSS + fonts |
| Hébergement | GitHub Pages, un dossier, une clé USB | build + pipeline |
| Mobile (Acode, Termux) | le fichier s'ouvre directement | build impossible |
| Débogage | un seul endroit | source maps, bundler |

Pour une arène d'IA, **95 % du temps est passé à attendre les fournisseurs** : le poids du
frontend est donc négligeable devant la latence réseau. Un fichier unique supprime les
requêtes bloquantes et rend l'outil transportable. C'est le bon compromis ici — pas pour une
application à 50 écrans.

---

## 2. Les leviers de performance réellement utilisés

### 2.1 Zéro ressource externe bloquante

Aucun CDN, aucune police web, aucun `fetch` au chargement :

```html
<!-- à éviter : 3 requêtes bloquantes avant le premier rendu -->
<script src="https://tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter" rel="stylesheet">
```

À la place : **CSS inline dans `<style>`**, **SVG en sprite inline** pour les icônes,
**pile de polices système**.

```css
--sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
--mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
```

Une police système s'affiche **immédiatement** (0 octet, 0 FOUT) et reste lisible. Les
icônes sont des `<symbol>` réutilisés par `<use>` : quelques centaines d'octets au lieu
d'une police d'icônes de 50 Ko.

### 2.2 Le thème est décidé avant le premier pixel

Un script de 8 lignes dans `<head>` lit `localStorage` et pose `data-theme` **avant** le
rendu : aucun flash blanc au rechargement. Le reste du CSS bascule par variables :

```css
:root { --bg: #07080b; --text: #e9edf5; }
[data-theme="light"] { --bg: #f6f6f1; --text: #15181e; }
```

### 2.3 Le streaming est la performance perçue

Attendre la réponse complète de GPT-4o = 5 à 20 s d'écran figé. En streaming, le premier
token arrive en ~300 ms. On affiche donc **au fil de l'eau**, avec `fetch` + `ReadableStream` :

```js
const reader = res.body.getReader();
const decoder = new TextDecoder();
let buffer = "";

function pump() {
  return reader.read().then(({ done, value }) => {
    if (done) return;
    buffer += decoder.decode(value, { stream: true });
    let i;
    while ((i = buffer.indexOf("\n")) !== -1) {   // SSE = une ligne = un événement
      const line = buffer.slice(0, i).replace(/\r$/, "");
      buffer = buffer.slice(i + 1);
      if (line.startsWith("data:")) {
        const data = line.slice(5).trim();
        if (data === "[DONE]") return;
        const json = JSON.parse(data);
        const delta = json.choices?.[0]?.delta?.content;
        if (delta) onDelta(delta);                // texte brut, pas d'innerHTML
      }
    }
    return pump();
  });
}
```

Points importants :

- `TextDecoder(..., { stream: true })` : un caractère UTF-8 peut être coupé entre deux
  paquets réseau. Sans ça, « é » devient « Ã© ».
- Le parseur SSE **tolère** les lignes vides, les commentaires (`: OPENROUTER PROCESSING`)
  et les `data:` multi-lignes.
- `stream_options: { include_usage: true }` (OpenRouter) renvoie les **vrais** tokens.
  Chez Groq, les modèles classiques renvoient `usage` dans le dernier chunk.

### 2.4 Les mises à jour DOM sont limitées à une par image

```js
function onDelta(text) {
  raw += text;
  if (!frame) frame = requestAnimationFrame(flush);  // max 60 rendus/s
}
```

Sans ce garde-fou, un modèle rapide (Groq : 300–800 tok/s) déclenche des centaines de
réécritures par seconde et fait chauffer le téléphone.

Le Markdown n'est **analysé qu'à la fin** du stream (pendant le stream on affiche du texte
brut) : c'est le meilleur rapport simplicité / coût.

### 2.5 Défilement : un seul calcul par frame

```js
window.addEventListener("scroll", () => {
  if (scrollRaf) return;                       // déjà planifié
  state.stick = innerHeight + scrollY >= scrollHeight - 210;
}, { passive: true });
```

`passive: true` évite de bloquer le défilement. Et si l'utilisateur remonte lire une
réponse, **on arrête de le tirer vers le bas** : un bouton « Dernière réponse » apparaît.

### 2.6 Sauvegarde différée

`localStorage.setItem` est synchrone et peut coûter plusieurs millisecondes. On écrit :

- pendant le stream : au maximum toutes les 600 ms (`saveChatSoon`),
- à la fin de chaque réponse,
- dans `pagehide` / `beforeunload` pour ne rien perdre.

Et si le quota est dépassé, on **dégrade proprement** : on garde les 4 derniers échanges et
on prévient l'utilisateur, au lieu de planter.

### 2.7 Mesures honnêtes

Trois nombres utiles, mesurés avec `performance.now()` :

| Mesure | Calcul | Pourquoi |
|---|---|---|
| **TTFT** | premier delta − départ | réactivité perçue |
| **tok/s** | tokens ÷ (fin − premier delta) | débit réel pendant la génération |
| **coût** | tokens × tarif ÷ 1 000 000 | ordre de grandeur |

Les tokens sont ceux de l'API quand elle les fournit ; sinon on estime (≈ 4 caractères par
token) et on l'indique par « ≈ ». Les tarifs sont dans une table en haut du fichier :
**ils changent**, et un prix affiché faux est pire que pas de prix.

---

## 3. Sécurité : trois règles non négociables

### 3.1 Ne jamais interpréter le HTML du modèle

Une réponse peut contenir `<img src=x onerror=...>`. Ici **tout le texte est échappé**
avant d'être transformé en Markdown, et le HTML brut s'affiche comme du texte :

```js
const ESCAPES = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };
const escHtml = (v) => String(v).replace(/[&<>"']/g, (c) => ESCAPES[c]);
```

Seul le Markdown *produit par notre propre parseur* finit dans `innerHTML`, avec des liens
forcés en `rel="noopener noreferrer nofollow"`.

### 3.2 Les clés API ne vont que chez le fournisseur

- saisies dans l'interface, jamais dans le code ni dans le dépôt ;
- stockées dans `localStorage` (ou `sessionStorage` si « mémoriser » est décoché) ;
- envoyées **directement** à `openrouter.ai` / `api.groq.com`, sans serveur intermédiaire.

C'est acceptable pour un usage personnel sur un appareil de confiance. Pour un site public,
il faut un proxy serveur (voir §6) : sinon n'importe qui peut lire les clés dans le
navigateur.

### 3.3 `.gitignore`

```
.env
.env.*
!.env.example
*.pem
*.key
```

Une clé poussée sur GitHub est compromise **immédiatement** (les robots scannent). Il faut
la révoquer, pas seulement supprimer le commit.

---

## 4. Ce qui n'allait pas dans `Yanis ia`, et les corrections

Le fichier `Yanis ia` déposé à la racine du dépôt partait d'une bonne idée (les 8 gratuites
ou les 8 payantes « collaborent », boutons 👍 / 👎). Dans son état, il ne pouvait pas
s'exécuter. Voici les défauts concrets, tous corrigés dans `ai-arena/index.html` :

| Problème | Conséquence | Correction |
|---|---|---|
| `fetch("https://groq.com")` | 405 / HTML au lieu du JSON | `https://api.groq.com/openai/v1/chat/completions` |
| `fetch("https://openrouter.ai")` | idem | `https://openrouter.ai/api/v1/chat/completions` |
| `"Authorization": Bearer${key}` | `ReferenceError`, en-tête invalide | `"Bearer " + key` |
| Template strings non fermées (`res-${...}`, `` Bearer${key}` ``) | **toute la page** ne parse pas | chaînes concaténées, `node --check` en pré-commit |
| Du texte Markdown collé à la fin du `<script>` | SyntaxError | fichier valide, séparé en sections commentées |
| `div.innerHTML = &lt;input …&gt;` | le HTML est échappé, aucun contrôle ne s'affiche | `document.createElement("input")` |
| `<script src="https://tailwindcss.com">` | ce n'est pas un CDN Tailwind (mauvais MIME + bloquant) | CSS maison, 0 requête |
| Classes `hidden` de Tailwind | aucun style sans Tailwind | `[hidden] { display: none !important }` et CSS propre |
| `id` contenant `/` (`res-meta-llama/...`) | `getElementById` ne le retrouve pas | identifiants indexés (`data-ti` / `data-ri`) |
| Aucun `AbortController` | impossible d'arrêter, pas de délai max | `AbortController` + bouton Stop + timeout 150 s |
| Aucune gestion d'erreur | écran figé « Calcul… » | messages par code HTTP (401, 402, 429, 5xx…) + détails dépliables |
| Clés en clair mais non persistées | à ressaisir à chaque rechargement | stockage local avec case « mémoriser » |
| Modèles retirés (Mixtral, Gemma 2, Llama 3.1 70B…) | erreurs 400/404 garanties | identifiants actuels + message explicite pour les modèles historiques |

---

## 5. Les identifiants de modèles vieillissent vite

Ta liste date de 2024. Depuis, les fournisseurs ont retiré plusieurs modèles :

| Modèle de ta liste | Statut | Remplaçant |
|---|---|---|
| Mixtral 8x7B (Groq) | retiré le 20/03/2025 | `openai/gpt-oss-120b` |
| Gemma 2 9B (Groq) | retiré | `openai/gpt-oss-20b` |
| Llama 3.1 70B `llama-3.1-70b-versatile` (Groq) | retiré le 24/01/2025 | `openai/gpt-oss-120b` |
| `llama-3.1-8b-instant` (Groq) | annoncé retiré en 2026 | `openai/gpt-oss-20b` |
| Gemini Flash 1.5 `:free`, Pixtral 12B `:free`, DeepSeek Chat `:free`, Llama 3.3 70B `:free` | plus « gratuits » sur OpenRouter (paliers supprimés) | `openrouter/free`, `nvidia/nemotron-3-super-120b-a12b:free` |

Le roster gratuit embarqué contient le routeur `openrouter/free`, les quatre modèles Groq
(`openai/gpt-oss-120b`, `openai/gpt-oss-20b`, `qwen/qwen3.8-27b`,
`openai/gpt-oss-safeguard-20b`) et les meilleurs `:free` d'OpenRouter
(`openai/gpt-oss-120b:free`, `google/gemma-4-31b-it:free`,
`google/gemma-4-26b-a4b-it:free`, `nvidia/nemotron-3-super-120b-a12b:free`).
`mergeCatalog()` réinjecte le routeur et les Groq s'ils manquent au catalogue distant. Quand l'API répond « modèle inexistant », la carte
affiche un message clair au lieu d'un écran muet. Pour remettre à jour la liste : `GET https://openrouter.ai/api/v1/models`
et `GET https://api.groq.com/openai/v1/models` (avec ta clé).

---

## 5 bis. Deux modes de réponse : collaboration et solo

Le même fichier sert deux stratégies, sans dupliquer le moteur :

```
state.style = "collab"                 state.style = "solo"
  panels[mode]  → N brouillons           soloModels[mode] → 1 modèle
  synths[mode]  → 1 synthétiseur         runSolo()        → 1 appel direct
  runRound() → runDraft() × N + runSynth()
```

- **Choix persisté** : `style`, `soloFree`, `soloPaid` sont stockés avec les autres réglages
  (`arenax.settings.v3`). Un modèle solo **par catalogue** : changer Gratuit/Premium ne
  perd pas la sélection de l'autre côté.
- **Source unique de vérité** : `currentKeys()` renvoie toujours `{ drafts, synth, solo, mode }`.
  Les deux moteurs (`runRound`, `runSolo`) et les deux rendus (`buildTurn`) lisent cette
  structure, donc le reste du code (crédits, historique, sauvegarde JSON) est partagé.
- **Une manche solo = un seul appel**, donc un seul contrôleur d'annulation
  (`turn.id + ":solo"`), une seule carte dans le fil, et une seule ligne de métriques
  (« réponse N tok · coût réponse »). L'état de l'étape unique est dérivé de `turn.synth`.
- **Le panneau s'adapte** : en Solo, la liste devient une sélection unique (radio) et les
  onglets Brouillons/Synthèse ainsi que les presets disparaissent — pas de bouton inutile.
- **Catalogue piloté par les clés** : `pools()` masque un fournisseur dont la clé est absente
  (sauf si aucune clé n'existe, pour garder la démo utilisable). Le panneau gratuit par
  défaut privilégie **2 modèles Groq + le routeur `openrouter/free` en synthèse** (un Groq
  prend le relais sans clé OpenRouter). Avec une clé Groq seule, on reste à 2 brouillons +
  1 synthèse (palier 8 000 tokens/minute) et `ensurePanels()` revalide brouillons, synthèse
  **et** modèle solo après chaque changement de clé.
- **Premium sans crédits = repli réel, pas démo** : `hasPaidAccess()` exige une clé
  OpenRouter et, si le solde est connu, un solde > 0. Sinon `pools().paid` renvoie le roster
  gratuit, la manche porte `degraded: true` et l'interface affiche « premium non activé ».
  Dès que `refreshCredits()` voit un solde positif, `ensurePanels()` remplace le roster et
  les modèles payants reviennent — sans rechargement.
- **Limitation de débit Groq** : un sémaphore maison garde au maximum **2 requêtes Groq
  simultanées** ; les suivantes attendent leur tour (et sont annulées proprement par
  « Arrêter »), ce qui évite les 429 sur le palier gratuit.

---

## 5 ter. Sauvegarde GitHub en direct (API Contents)

L'app écrit dans un dépôt sans serveur : trois appels suffisent.

```
GET  /repos/{repo}/contents/{path}?ref={branch}   → { content (base64), sha }
PUT  /repos/{repo}/contents/{path}                → { message, content (base64), branch, sha? }
```

- **Le `sha` est obligatoire pour une mise à jour**, absent pour une création : on relit donc
  systématiquement le fichier avant d'écrire (`ghGetFile()` → `ghPutFile()`). Un 404 est
  traité comme « fichier absent », pas comme une erreur.
- **Encodage** : l'API exige du base64 sur de l'UTF-8. `TextEncoder` → `btoa` par tranches de
  32 Ko (sinon `String.fromCharCode.apply` explose sur les grosses sauvegardes), et
  `atob` → `TextDecoder` pour la lecture. Les accents français survivent.
- **Jeton** : *fine-grained*, portée limitée à un dépôt, permission `Contents: write`.
  Il vit dans une clé de stockage **séparée** (`arenax.github.v3`) et n'entre jamais dans
  `backupPayload()` : une sauvegarde partagée ne fuit pas le jeton.
- **Erreurs traduites** : 401 jeton invalide, 403 droit manquant, 404 dépôt/branche introuvable,
  409 conflit — au lieu d'un « HTTP 4xx » opaque.
- **Sauvegarde auto** : `maybeAutoBackup()` télécharge le fichier local **et** pousse sur GitHub
  si la configuration est complète, donc les deux copies restent alignées.

---

## 5 quater. Historique : plusieurs conversations, un tiroir à gauche

L'application garde désormais **plusieurs conversations**, listées dans un tiroir qui
s'ouvre par le bouton hamburger en haut à gauche (ou `Ctrl` + `Maj` + `H`).

```
arenax.chats.v3 = {
  v: 3,
  current: "cmvq…",                    // conversation ouverte
  list: [{ id, title, ts, updated, mode, style, turns: [ … ] }, …]
}
```

- **Migration silencieuse** : au premier démarrage de cette version, l'ancienne clé unique
  `arenax.chat.v3` est convertie en une conversation, puis supprimée. Rien à faire à la main.
- **Titre = premier prompt** (54 caractères max, tronqué proprement) : pas de titre inventé
  par un modèle, donc pas d'appel payant rien que pour nommer un fil.
- **Date honnête** : `turnsSig()` (nombre d'échanges + identifiant et taille de la dernière
  réponse) décide si `updated` bouge. Un simple rendu de l'interface ne fait pas remonter
  une conversation dans la liste.
- **Volumes** : 24 conversations, 8 échanges pour les conversations fermées, 32 pour celle
  qui est ouverte. Si le quota du navigateur est atteint, l'écriture réessaie en divisant
  le nombre de conversations puis le nombre d'échanges, et prévient une seule fois.
  Aucune écriture n'est tentée quand la mémoire est vide : un état transitoire ne peut pas
  effacer un historique relu partiellement.
- **Ce qui est sauvegardé** : conversation ouverte (identifiant + mode + style), puis
  réouverture directe au rechargement. Supprimer demande confirmation et est définitif ;
  il n'y a pas encore de renommage.
- **Sauvegarde JSON** : `backupPayload()` ajoute `chats` (toutes les conversations) à côté
  de `turns` (la conversation ouverte, conservé pour la compatibilité). Une restauration
  qui contient `chats` remplace l'historique, sinon l'ancien format reste accepté.
- **Pourquoi `localStorage` et pas IndexedDB** : l'écriture est synchrone, donc un
  `pagehide` sur Android peut sauver la dernière réponse ; pas de transaction à gérer,
  pas de dépendance, et le fichier reste unique.

Le tiroir est du HTML simple (`aside#drawer` + `div#drawerScrim`), animé par
`transform: translateX()`, refermé par le voile, `Échap` ou la croix. Sur mobile, la barre
du haut ne garde que le hamburger (le bouton « + » y est masqué) pour ne pas la surcharger.

---

## 5 quinquies. Pièces jointes : photos et fichiers texte

Le bouton trombone du champ d'écriture (ou un collage `Ctrl+V`, ou un glisser-déposer)
ajoute jusqu'à **3 photos** et **2 fichiers texte** par question.

- **Photos** : redimensionnées à 1 400 px sur le côté long en JPEG 82 %, l'aperçu envoyé
  au modèle fait donc quelques centaines de Ko au plus. Une photo de téléphone de 4 000 px
  coûte cher en tokens d'entrée pour aucun gain de lecture.
- **Fichiers texte** : `.txt .md .csv .json .log` et code (`.js .py .html .css .sql…`),
  1 Mo maximum, **24 000 caractères** conservés — le reste est coupé et l'interface le dit.
- **Vision réelle, pas supposée** : OpenRouter publie `architecture.input_modalities`.
  Si l'image n'y figure pas, le modèle ne reçoit pas la photo. Le panneau est donc
  **restreint aux modèles qui lisent les images** le temps du tour, classés par
  `BEST_VISION_FREE` / `BEST_VISION_PAID` (Gemma 4 31B et Nemotron Nano Omni en gratuit,
  Gemini 3.1 Pro / GPT‑5.6 Sol / Opus 5.5 en premium). En solo, un modèle non vision est
  remplacé par le meilleur modèle vision du panneau. Si aucun modèle n'est vision, l'envoi
  est **bloqué** avec un message qui dit *quelle clé manque* : côté Groq, Llama 4 (le seul
  modèle image du fournisseur) a été retiré du palier gratuit le 17 juillet 2026, donc
  « gratuit avec Groq seul » ne peut pas lire une photo. Avec une **clé OpenRouter
  gratuite** (sans carte), Gemma 4 31B la lit pour 0 $ — c'est le chemin recommandé.
- **Format du message** : contenu multimodal standard OpenAI, donc accepté par Groq comme
  par OpenRouter : `[{type:"text"}, {type:"image_url", image_url:{url:"data:image/jpeg;base64,…"}}]`.
  Les fichiers texte, eux, sont insérés dans le prompt sous `--- FICHIER JOINT : nom ---`.
- **Historique** : seule la **vignette 240 px** est conservée en `localStorage`, jamais
  l'image pleine définition (24 conversations feraient exploser le quota). Le texte des
  fichiers joints n'est pas rejoué non plus : la bulle garde le nom et le nombre de
  caractères. La photo reste donc visible dans le fil après rechargement, mais l'original
  n'est pas rejouable vers les modèles.
- **Limite assumée** : l'application lit les images, elle n'en produit pas. Les modèles du
  panneau (Opus 5.5, GPT‑5.6, Gemini 3.1 Pro, DeepSeek) renvoient **du texte
  uniquement**. Une retouche photo demande un modèle image (`gemini-3.1-flash-image`,
  `gpt-image`…) et une vidéo un modèle vidéo (Veo 3.1, Sora) : ce sont d'autres appels,
  facturés à l'image (≈ 0,04 à 0,15 $) ou à la seconde (≈ 0,05 à 0,40 $). Hors périmètre
  de ce panneau pour l'instant.

---

## 6. Passer en production (site public)

Un fichier statique ne peut pas cacher une clé. Le schéma minimal :

```
Navigateur ──► ton serveur (/api/chat) ──► OpenRouter / Groq
                 │ clé en variable d'environnement
                 │ limitation de débit par IP
                 └ quotas + journal d'usage
```

- **Le serveur relaie le flux tel quel** (`res.body` → `ReadableStream`), sinon tu perds le
  streaming et donc tout l'intérêt.
- Vercel / Cloudflare Workers : une fonction edge de ~30 lignes suffit.
- Ajoute `Access-Control-Allow-Origin` **uniquement** sur ton domaine.
- Prévois un quota : 8 modèles × 10 requêtes = 80 appels par clic ; sans limite, ta facture
  suit le premier visiteur curieux.

Pour un usage **personnel**, le fichier unique reste le plus rapide à déployer : GitHub
Pages, ou même ouverture locale.

---

## 7. Héberger et tester

```bash
# ouverture directe (tout fonctionne, y compris le stockage local)
xdg-open ai-arena/index.html

# ou service local, utile pour tester sur téléphone
python3 -m http.server 8000 --bind 0.0.0.0 --directory ai-arena
```

Sur GitHub : *Settings → Pages → Deploy from a branch*, dossier `/` puis l'URL
`…/ai-arena/`. Sur mobile, Acode ouvre le fichier et le rend avec le moteur du téléphone.

**Checklist de test** avant de partager :

1. sans clé : réponses en démo, vote, classement, export ;
2. avec clé OpenRouter puis Groq : streaming réel, métriques, erreurs 401/429 ;
3. coupure réseau en pleine réponse → message et bouton « Réessayer » ;
4. rechargement → conversation, thème, réglages, notes conservés ;
5. mobile 390 px : rien ne déborde, le clavier ne masque pas le champ ;
6. mode multi : 8 modèles maximum, notes 👍/👎 fusionnées dans le classement.

---

## 8. Limites assumées

- **Appels directs = clé visible** par quiconque a accès à l'appareil.
- **CORS** : certains fournisseurs bloquent les appels navigateur ; ici OpenRouter et Groq
  l'autorisent, mais un modèle peut échouer pour cette raison (message dédié).
- **Tarifs et identifiants** sont des données vivantes : table à maintenir.
- **Tokens estimés** quand l'API ne les renvoie pas ; c'est indiqué par « ≈ ».
- **Pas de multi-tour par modèle en multi** : chaque modèle reçoit son propre historique
  (sinon les réponses des autres pollueraient le sien).
