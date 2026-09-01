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
previous_head="$(git rev-parse HEAD)"

git fetch --prune origin main
git merge --ff-only origin/main

if [[ "$(git rev-parse HEAD)" == "$previous_head" ]]; then
  echo "B.I.N.E.S.H. OS is already up to date at $(git rev-parse --short HEAD)."
  exit 0
fi

if ! tools/bootstrap.sh; then
  echo "Validation failed after update; rolling back to $(git rev-parse --short "$previous_head")." >&2
  git reset --hard "$previous_head"
  exit 1
fi

echo "B.I.N.E.S.H. OS updated and validated at $(git rev-parse --short HEAD)."
