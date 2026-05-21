# Workflow Mac — Second Brain

## 1. Cloner le vault

Sur ton Mac :

```bash
cd ~/Documents
git clone https://github.com/Shakashi/second-brain.git
```

Puis dans Obsidian :

1. Open folder as vault.
2. Choisir `~/Documents/second-brain`.
3. Dans Settings > Files and links, régler les attachments sur `raw/assets`.
4. Installer éventuellement les plugins communautaires : Dataview, Git, Marp Slides.

## 2. Ajouter un document depuis le Mac

Copie ton fichier dans :

```bash
~/Documents/second-brain/inbox/
```

Types supportés par le script :

- PDF : `.pdf`
- texte : `.txt`
- markdown : `.md`, `.markdown`

Puis commit/push :

```bash
cd ~/Documents/second-brain
git pull --rebase
cp ~/Downloads/mon-document.pdf inbox/
git add inbox/mon-document.pdf
git commit -m "Add source to inbox: mon document"
git push
```

Ensuite tu peux demander à Morpheus :

> Intègre les documents dans `second-brain/inbox/`.

Morpheus fera :

```bash
cd /home/shaka/second-brain
git pull --rebase
python3 scripts/ingest_inbox.py
# puis synthèse LLM dans wiki/
git add .
git commit -m "Ingest: ..."
git push
```

## 3. Travailler avec Claude Code sur Mac

Depuis ton Mac :

```bash
cd ~/Documents/second-brain
claude
```

Instruction à donner à Claude :

```text
Lis AGENTS.md puis docs/CLAUDE_CODE_GUIDE.md. Respecte strictement les règles du vault. Oriente-toi avec wiki/SCHEMA.md, wiki/index.md et wiki/log.md avant toute modification.
```

## 4. Synchronisation

Le repo GitHub est la source de synchronisation.

Avant de modifier :

```bash
git pull --rebase
```

Après modification :

```bash
git status --short
git add .
git commit -m "Update second brain"
git push
```

## 5. Routine simple recommandée

1. Tu ajoutes des PDFs/textes dans `inbox/` sur Mac.
2. Tu commit/push.
3. Tu demandes à Morpheus d'ingérer.
4. Tu pull sur Mac.
5. Tu lis le résultat dans Obsidian.

## 6. Sync automatique recommandée avec Obsidian Git

Pour éviter les erreurs du type `cannot pull with rebase: You have unstaged changes`, installe le plugin communautaire `Obsidian Git` sur le Mac.

Installation :

1. Obsidian > Settings > Community plugins.
2. Désactiver `Restricted mode` si nécessaire.
3. Browse > chercher `Obsidian Git`.
4. Install puis Enable.

Réglages conseillés, selon les noms visibles dans ta version du plugin :

- `Pull updates on startup` / `Pull on startup` / `Auto-pull on Obsidian startup` : enabled.
- `Vault backup interval` / `Auto backup interval` : 10 à 30 minutes. Dans ce plugin, "backup" signifie commit + sync Git, pas une sauvegarde séparée.
- `Commit message` : `vault backup: {{date}}` ou `vault backup: {{date}} {{time}}` si `{{time}}` est accepté.
- `Push on backup` / `Push after backup` : enabled si l'option est visible. Certaines versions l'intègrent directement dans l'opération de backup/sync.
- `Pull before push` / `Pull before backup` : enabled si l'option est visible.
- `Disable notifications` : optionnel.

Si tu ne vois pas exactement ces noms, le minimum viable est :

1. activer le pull au démarrage ;
2. définir un intervalle de backup automatique ;
3. vérifier qu'une commande `Commit-and-sync` ou `Backup` pousse bien sur GitHub.

Routine conseillée :

1. Ouvrir Obsidian.
2. Laisser Obsidian Git faire le pull au démarrage.
3. Travailler normalement.
4. Laisser l'auto backup commit/push régulièrement.
5. Avant de demander à Morpheus d'ingérer ou modifier le vault, vérifier que le plugin a bien poussé les derniers changements.

Attention : éviter d'éditer les mêmes pages au même moment qu'un agent. Le plus sûr est de déposer tes documents dans `inbox/`, laisser Obsidian Git pousser, puis demander à Morpheus d'ingérer.

Si Git reste bloqué à cause de fichiers locaux sans importance, vérifier d'abord :

```bash
git status --short
```

Si seuls des fichiers de workspace Obsidian apparaissent, ils peuvent être restaurés sans risque :

```bash
git restore .obsidian/workspace.json .obsidian/workspace-mobile.json 2>/dev/null || true
git pull --rebase
```
