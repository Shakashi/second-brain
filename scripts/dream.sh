#!/bin/bash
# Daily dream pass for Claude Code on Mac.
# Triggered by launchd at 01:30 local time (see ~/Library/LaunchAgents/com.shaka.second-brain.dream.plist).
# If Mac is asleep at 01:30, the run is silently skipped — next day's dream covers missed days (catch-up mode).

set -uo pipefail

VAULT="/Users/shakadaily/Documents/second-brain"
CLAUDE="/Users/shakadaily/.nvm/versions/node/v24.14.0/bin/claude"
TODAY="$(date +%Y-%m-%d)"
TS="$(date +%Y-%m-%dT%H:%M:%S%z)"
LOG_DIR="${VAULT}/.logs"
mkdir -p "$LOG_DIR"
RUN_LOG="${LOG_DIR}/dream.log"

echo "[${TS}] dream start" >> "$RUN_LOG"

cd "$VAULT" || { echo "[${TS}] FAIL cd to vault" >> "$RUN_LOG"; exit 1; }

# Pre-sync. Autostash protects against pending obsidian config diffs.
git pull --rebase --autostash >> "$RUN_LOG" 2>&1 || {
  echo "[${TS}] WARN git pull failed — continuing anyway" >> "$RUN_LOG"
}

PROMPT=$(cat <<EOF
Tu es Claude Code lancé automatiquement (launchd) pour faire le dream quotidien du vault second-brain.
Date du jour : ${TODAY}

Suis docs/AI_COLLABORATION_PROTOCOL.md à la lettre. Étapes :

1. Lis wiki/index.md et "tail -80 wiki/log.md" pour situer l'état.
2. "git log --since='48 hours ago' --oneline" pour voir les commits récents (Morpheus + Mac).
3. Utilise scripts/search_brain.py pour toute recherche ciblée — NE CHARGE PAS tout le vault.
4. Liste wiki/daily/ : si le dernier dream est antérieur à hier, traite le dream d'aujourd'hui en mode catch-up (couvre tous les jours manqués dans une seule entrée).
5. Si wiki/daily/${TODAY}.md n'existe pas : crée-le avec frontmatter conforme (type meta, tags [meta, synthesis]) et une section "## Claude Code additions".
   Si la page existe déjà avec une section Morpheus, ne touche QUE la section "## Claude Code additions" — sans dupliquer ce que Morpheus a écrit.
6. Le dream doit être bref et synthétique : pages créées/modifiées, décisions notables, questions ouvertes, prochaines actions naturelles. PAS de log dump.
7. Mets à jour wiki/index.md (section Daily Notes) si nouvelle entrée.
8. Ajoute une entrée dans wiki/log.md au format "## [${TODAY}] create | Daily dream — Claude Code additions" avec 2-4 bullets max.
9. python3 scripts/lint_brain.py — résoudre toute erreur avant commit.
10. git add UNIQUEMENT les fichiers wiki/ légitimement modifiés (jamais .obsidian/).
11. git commit -m "Daily ${TODAY}: Claude Code additions" avec ligne "Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>".
12. git pull --rebase puis git push origin main.

Contraintes strictes :
- Pas de nouvelle page entité/concept sans demande explicite — c'est un dream, pas un seed.
- Si rien de notable depuis hier, écris-le explicitement ("RAS, vault stable") et commit quand même.
- Termine en moins de 5 minutes.
- En cas d'erreur fatale, log dans .logs/dream.log et exit non-zéro.
EOF
)

# Run Claude Code one-shot, unattended.
# --dangerously-skip-permissions est requis pour le mode launchd non-interactif.
"$CLAUDE" -p "$PROMPT" \
  --dangerously-skip-permissions \
  --output-format text \
  >> "$RUN_LOG" 2>&1
EXIT_CODE=$?

TS_END="$(date +%Y-%m-%dT%H:%M:%S%z)"
echo "[${TS_END}] dream end (exit=${EXIT_CODE})" >> "$RUN_LOG"
exit $EXIT_CODE
