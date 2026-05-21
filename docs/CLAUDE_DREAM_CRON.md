# Claude Code Dream Cron — Mac

Automatisation du dream quotidien Claude Code via macOS **launchd** (équivalent cron natif Mac).

## Schedule

- **Heure** : 01:30 local Mac (après le dream Morpheus de 00:30 UTC)
- **Si Mac endormi à 01:30** : la run est silencieusement skippée (launchd n'éveille pas la machine). Le dream du lendemain couvre les jours manqués en mode catch-up.

## Composants

1. **Script** : `scripts/dream.sh` (versionné dans ce repo)
2. **launchd plist** : `~/Library/LaunchAgents/com.shaka.second-brain.dream.plist` (hors repo, install local)
3. **Logs** : `.logs/dream.log`, `.logs/launchd.stdout.log`, `.logs/launchd.stderr.log` (ignorés par git)

## Installation

```bash
# 1. Le script est déjà dans le repo, vérifier qu'il est exécutable
chmod +x ~/Documents/second-brain/scripts/dream.sh

# 2. Copier/écrire le plist (voir contenu dans la dernière version commitée du repo)
# Exemple minimal :
cat > ~/Library/LaunchAgents/com.shaka.second-brain.dream.plist <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key><string>com.shaka.second-brain.dream</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Users/shakadaily/Documents/second-brain/scripts/dream.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict><key>Hour</key><integer>1</integer><key>Minute</key><integer>30</integer></dict>
    <key>RunAtLoad</key><false/>
    <key>WorkingDirectory</key><string>/Users/shakadaily/Documents/second-brain</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key><string>/Users/shakadaily/.nvm/versions/node/v24.14.0/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
        <key>HOME</key><string>/Users/shakadaily</string>
    </dict>
    <key>StandardOutPath</key><string>/Users/shakadaily/Documents/second-brain/.logs/launchd.stdout.log</string>
    <key>StandardErrorPath</key><string>/Users/shakadaily/Documents/second-brain/.logs/launchd.stderr.log</string>
    <key>ProcessType</key><string>Background</string>
</dict>
</plist>
EOF

# 3. Valider et charger
plutil -lint ~/Library/LaunchAgents/com.shaka.second-brain.dream.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.shaka.second-brain.dream.plist

# 4. Vérifier
launchctl print gui/$(id -u)/com.shaka.second-brain.dream | grep -E "(state|path|domain)"
```

## Commandes utiles

```bash
# Voir l'état
launchctl print gui/$(id -u)/com.shaka.second-brain.dream

# Déclencher une run manuelle (test)
launchctl kickstart -k gui/$(id -u)/com.shaka.second-brain.dream

# Suivre les logs en direct
tail -f ~/Documents/second-brain/.logs/dream.log

# Décharger temporairement
launchctl bootout gui/$(id -u)/com.shaka.second-brain.dream

# Recharger après modification du plist
launchctl bootout gui/$(id -u)/com.shaka.second-brain.dream
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.shaka.second-brain.dream.plist
```

## Sécurité

- Le script lance `claude -p` avec `--dangerously-skip-permissions` (obligatoire pour exécution non-interactive).
- Scope limité : `WorkingDirectory` = vault. Le prompt restreint explicitement les actions à `wiki/`.
- Le script ne touche jamais `.obsidian/*` et n'add que les fichiers wiki/ légitimes.

## Si quelque chose foire

Logs en première intention :

```bash
tail -100 ~/Documents/second-brain/.logs/dream.log
tail -50 ~/Documents/second-brain/.logs/launchd.stderr.log
```

Symptômes connus :

| Symptôme | Cause probable | Fix |
|---|---|---|
| `claude: command not found` | PATH manquant pour launchd | Vérifier `EnvironmentVariables.PATH` dans le plist |
| `git push` refusé | Credentials non-cachés | Configurer Git Credential Manager (déjà OK via Obsidian Git) |
| Conflit rebase | Morpheus a poussé entre-temps | Le script utilise `--autostash` ; en cas d'échec, manuel requis |
| Plist non chargé après reboot | LaunchAgents pas re-bootstrappé | macOS doit le faire automatiquement ; sinon `launchctl bootstrap` manuel |
