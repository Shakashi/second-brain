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

## 6. Alternative avec plugin Obsidian Git

Tu peux installer le plugin communautaire `Obsidian Git` pour automatiser pull/commit/push depuis Obsidian. Réglages conseillés :

- Auto pull on startup: enabled
- Auto backup interval: 10-30 minutes
- Commit message: `vault backup: {date}`

Attention : éviter d'éditer les mêmes pages au même moment qu'un agent.
