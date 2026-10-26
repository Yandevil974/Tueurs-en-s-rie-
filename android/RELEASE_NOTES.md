## ARENA//X pour Android — version 1.1

APK autonome : l'interface complète est embarquée dans l'application, aucun serveur, aucun compte à créer pour l'ouvrir.

**Installation**
1. Télécharge `ARENA-X.apk` ci-dessous.
2. Ouvre le fichier depuis les notifications (ou *Fichiers → Téléchargements*).
3. Android demande d'autoriser l'installation depuis cette source : accepte.
4. Lance **ARENA//X**, puis ⚙ → colle ta clé **Groq** (`gsk_…`) → Enregistrer.

**⚠️ Une seule fois : désinstalle l'ancienne version avant celle-ci.**
Les APK précédents étaient signés avec une clé de debug régénérée à chaque build :
Android refuse de les mettre à jour (signatures différentes). Cette version utilise une
clé **stable**, donc **toutes les mises à jour suivantes s'installeront par-dessus**,
sans désinstallation. Avant de désinstaller, pense à faire une sauvegarde
(⚙ → Sauvegarde GitHub) : la clé Groq, elle, devra être ressaisie.

**Nouveautés de la 1.1**
- Correction majeure : les modèles Groq de raisonnement (GPT-OSS, Qwen3.8) répondent
  enfin au lieu de « réfléchir » sans écrire (budget de tokens + relance automatique).
- Relance automatique en cas de limite de débit (429) au lieu d'un échec.
- Pendant la consultation, les brouillons restent visibles : « Réflexion… N tokens ».
- Signature stable : plus de désinstallation à chaque mise à jour.

**Contenu**
- 9 modèles gratuits (Groq, routeur `openrouter/free`, `:free`) et 9 premium
- **Collaboration** (brouillons + synthèse) ou **Solo** (un seul modèle)
- Réponse finale affichée en premier, brouillons repliés
- Sauvegarde JSON dans les *Téléchargements* du téléphone, et sauvegarde GitHub
- Fonctionne hors ligne pour l'interface ; les clés restent sur l'appareil
