#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

CURRENT_BRANCH="$(git branch --show-current)"
if [[ "$CURRENT_BRANCH" != "main" ]]; then
  echo "[deploy] switching to main"
  if git show-ref --verify --quiet refs/heads/main; then
    git checkout main
  else
    git checkout -b main
  fi
fi

echo "[deploy] pulling latest main (if remote exists)"
if git remote get-url origin >/dev/null 2>&1; then
  git pull --ff-only origin main || true
else
  echo "[deploy] remote 'origin' is not configured"
fi

echo "[deploy] building app"
make build

echo "[deploy] running tests"
make test

echo "[deploy] pushing main"
if git remote get-url origin >/dev/null 2>&1; then
  git push origin main
else
  echo "[deploy] skip push: remote 'origin' is not configured"
  exit 2
fi

echo "[deploy] done"
