#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

git diff --quiet && git diff --cached --quiet || {
  echo "Local changes detected; refusing to overwrite them." >&2
  exit 2
}

git fetch origin main
git merge --ff-only origin/main

echo "B.I.N.E.S.H. OS updated to $(git rev-parse --short HEAD)."
