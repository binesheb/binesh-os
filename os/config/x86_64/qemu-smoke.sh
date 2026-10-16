#!/usr/bin/env bash
set -euo pipefail

# Placeholder until the first bootable ISO exists.
# This is the explicit CI contract for the first bootable-image milestone.

if [[ -z "${BINESH_ISO:-}" ]]; then
  echo "[BINESH] QEMU smoke test: ISO not supplied; boot-image milestone not reached yet."
  exit 0
fi

command -v qemu-system-x86_64 >/dev/null || {
  echo "[BINESH] qemu-system-x86_64 is required."
  exit 1
}

timeout 45s qemu-system-x86_64   -machine q35   -m 2048   -cdrom "$BINESH_ISO"   -serial stdio   -display none
