#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

require_clean_tree() {
  git diff --quiet && git diff --cached --quiet && git diff --quiet --ignore-submodules -- . ':!*.pyc' || {
    echo "Local changes detected; refusing to overwrite them." >&2
    exit 2
  }
}

current_branch="$(git branch --show-current)"
if [[ "$current_branch" != "main" ]]; then
  echo "Refusing to update from '$current_branch'. Switch to main first; automatic updates only track origin/main." >&2
  exit 2
fi

require_clean_tree

git fetch --prune origin main
git merge --ff-only origin/main

echo "B.I.N.E.S.H. OS updated to $(git rev-parse --short HEAD)."
