#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
OUT="$ROOT/out/aarch64"
WORK="$ROOT/.build/aarch64"
SUITE="${BINESH_DEBIAN_SUITE:-bookworm}"
MIRROR="${BINESH_DEBIAN_MIRROR:-http://deb.debian.org/debian}"

mkdir -p "$OUT" "$WORK"
rm -rf "$WORK/rootfs"
mkdir -p "$WORK/rootfs"

command -v debootstrap >/dev/null || { echo "debootstrap is required" >&2; exit 1; }
command -v mksquashfs >/dev/null || { echo "squashfs-tools is required" >&2; exit 1; }
command -v grub-mkstandalone >/dev/null || { echo "grub EFI tools are required" >&2; exit 1; }

echo "[BINESH] Bootstrapping ARM64 userspace: $SUITE"
debootstrap --arch=arm64 --foreign "$SUITE" "$WORK/rootfs" "$MIRROR"

echo "[BINESH] ARM64 root filesystem created."
echo "[BINESH] This is the Raspberry Pi/ARM64 userspace foundation."
echo "[BINESH] Kernel, device-tree and Pi boot partition integration are next."
