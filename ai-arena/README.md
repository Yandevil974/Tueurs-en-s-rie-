# ARENA//X — arène de comparaison d'IA

Un **seul fichier** (`index.html`, ~147 Ko) qui envoie le même prompt à deux modèles d'IA
(ou jusqu'à huit), affiche les réponses **en direct**, mesure vitesse / tokens / coût, puis
te laisse voter ou noter. Aucune dépendance, aucun serveur, aucune clé dans le code.

## Démarrer

1. Ouvre `index.html` (double-clic, `file://`, ou GitHub Pages).
2. Sans clé, le **mode démo** simule les réponses : toute l'interface est testable.
3. Clique **Clés**, colle une clé [OpenRouter](https://openrouter.ai/keys) et/ou
   [Groq](https://console.groq.com/keys), puis **Tester les connexions**.

```bash
python3 -m http.server 8000 --bind 0.0.0.0 --directory ai-arena   # test sur téléphone
```

## Les 16 modèles

| 🍃 Gratuites | Fournisseur | 💎 Payantes | Fournisseur |
|---|---|---|---|
| Llama 3.1 8B | Groq | GPT-4o | OpenRouter |
| Mixtral 8x7B ⚠ | Groq | GPT-4o Mini | OpenRouter |
| Gemma 2 9B ⚠ | Groq | OpenAI o1-Mini | OpenRouter |
| Gemini Flash 1.5 | OpenRouter | Claude 3.5 Sonnet | OpenRouter |
| Pixtral 12B | OpenRouter | Gemini Pro 1.5 | OpenRouter |
| DeepSeek Chat | OpenRouter | Mistral Large 2 | OpenRouter |
| Qwen 2.5 Coder | OpenRouter | Llama 3.1 405B | OpenRouter |
| Llama 3.1 8B OS | OpenRouter | Llama 3.1 70B ⚠ | Groq |

⚠ = identifiant retiré par le fournisseur depuis 2025 ; la page l'explique au lieu
d'échouer silencieusement. Voir `GUIDE.md` §5 pour les remplaçants.

## Deux modes

- **⚔️ Duel A/B** — deux modèles, une réponse chacun, puis un vote (A / égalité / B /
  les deux mauvais).
- **🧩 Multi** — jusqu'à 8 modèles en parallèle sur le même prompt (8 gratuites, 8 payantes,
  ou 3 au hasard), chacun noté 👍 / 👎. Le classement fusionne duels et notes.

## Ce qui est inclus

- Streaming SSE réel (OpenRouter + Groq), bouton **Stop**, timeout 150 s, relance ciblée.
- TTFT, tok/s, tokens, coût estimé — et mention « ≈ » quand l'API ne fournit pas l'usage.
- Markdown sûr (tableaux, listes, citations, blocs de code avec copie), **HTML échappé**.
- Mode démo intégral sans aucune clé.
- Clés dans `localStorage` (ou `sessionStorage`), thème sombre/clair, mobile ≤ 390 px.
- Persistance conversation + votes, export Markdown, dialogue natif `<dialog>`.
- Accessibilité : navigation clavier, `aria-live`, focus visible, contrastes AA,
  `prefers-reduced-motion`, styles d'impression.

## Fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | l'application complète (HTML + CSS + JS) |
| `GUIDE.md` | méthode, performances, sécurité, corrections de `Yanis ia` |

> Usage personnel : les clés sont visibles dans le navigateur. Pour un site public,
> passe par un proxy serveur (voir `GUIDE.md` §6).
