#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
OUT="$ROOT/out/os"
mkdir -p "$OUT"
echo "[BINESH] OS development build scaffold"
echo "[BINESH] Source: $ROOT"
echo "[BINESH] Output: $OUT"
echo "The bootable image pipeline is being implemented milestone-by-milestone."
echo "Do not use this scaffold as a production installer."