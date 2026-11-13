#!/usr/bin/env bash
set -Eeuo pipefail

OUT="${1:-out/installer/test-disk.img}"
SIZE_MB="${2:-4096}"

mkdir -p "$(dirname "$OUT")"

if ! [[ "$SIZE_MB" =~ ^[0-9]+$ ]] || (( SIZE_MB < 2048 )); then
  echo "Usage: $0 <image-path> <size-mb>=2048+" >&2
  exit 2
fi

if command -v qemu-img >/dev/null 2>&1; then
  qemu-img create -f raw "$OUT" "${SIZE_MB}M"
else
  dd if=/dev/zero of="$OUT" bs=1M count="$SIZE_MB" status=progress
fi

echo "[BINESH] Created virtual installer target: $OUT"
