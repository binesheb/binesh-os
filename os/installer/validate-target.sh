#!/usr/bin/env bash
set -Eeuo pipefail

TARGET="${1:-}"
MIN_BYTES="${2:-2147483648}"

if [[ -z "$TARGET" ]]; then
  echo "ERROR: target disk is required" >&2
  exit 2
fi

if [[ "$TARGET" != /dev/* ]]; then
  echo "ERROR: target must be a block-device path" >&2
  exit 2
fi

if [[ ! -b "$TARGET" ]]; then
  echo "ERROR: target is not a block device: $TARGET" >&2
  exit 2
fi

SIZE="$(blockdev --getsize64 "$TARGET")"
if (( SIZE < MIN_BYTES )); then
  echo "ERROR: target is too small: $SIZE bytes; need at least $MIN_BYTES" >&2
  exit 3
fi

echo "Target: $TARGET"
echo "Size:   $SIZE bytes"
echo "Status: target passed basic installer validation"
