#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
ISO="$ROOT/out/x86_64/binesh-os-x86_64-dev.iso"
SHA="$ISO.sha256"

[[ -f "$ISO" ]] || { echo "[BINESH] ISO not found: $ISO" >&2; exit 1; }
[[ -f "$SHA" ]] || { echo "[BINESH] checksum not found: $SHA" >&2; exit 1; }

sha256sum -c "$SHA"

if command -v xorriso >/dev/null 2>&1; then
  xorriso -indev "$ISO" -toc >/dev/null
fi

echo "[BINESH] Image verification passed."
echo "[BINESH] This validates artifact integrity only; it does not replace a QEMU boot test."
