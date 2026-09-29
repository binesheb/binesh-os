#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
OUT="$ROOT/out/x86_64"
WORK="$ROOT/out/work/x86_64"
SUITE="noble"
ARCH="amd64"
MIRROR="http://archive.ubuntu.com/ubuntu"

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "[BINESH] Missing required command: $1" >&2
    exit 1
  }
}

[[ $EUID -eq 0 ]] || { echo "[BINESH] Run as root (sudo)." >&2; exit 1; }
for c in debootstrap grub-mkrescue xorriso mksquashfs; do require_cmd "$c"; done

rm -rf "$WORK" "$OUT"
mkdir -p "$WORK/rootfs" "$WORK/iso/boot/grub" "$WORK/iso/live" "$OUT"

echo "[BINESH] Bootstrapping Ubuntu $SUITE $ARCH..."
debootstrap --arch="$ARCH" "$SUITE" "$WORK/rootfs" "$MIRROR"

mount --bind /dev "$WORK/rootfs/dev"
mount --bind /dev/pts "$WORK/rootfs/dev/pts"
mount -t proc proc "$WORK/rootfs/proc"
mount -t sysfs sys "$WORK/rootfs/sys"
mount -t tmpfs tmpfs "$WORK/rootfs/run"

cleanup() {
  set +e
  umount -lf "$WORK/rootfs/run"
  umount -lf "$WORK/rootfs/sys"
  umount -lf "$WORK/rootfs/proc"
  umount -lf "$WORK/rootfs/dev/pts"
  umount -lf "$WORK/rootfs/dev"
}
trap cleanup EXIT

cp /etc/resolv.conf "$WORK/rootfs/etc/resolv.conf"

cat > "$WORK/rootfs/etc/apt/sources.list" <<EOF
deb $MIRROR $SUITE main restricted universe multiverse
deb $MIRROR $SUITE-updates main restricted universe multiverse
deb $MIRROR $SUITE-security main restricted universe multiverse
EOF

cat > "$WORK/rootfs/etc/binesh-release" <<EOF
NAME="B.I.N.E.S.H. OS"
ID=binesh
VERSION="0.1.0-dev"
PLATFORM=x86_64
BASE="Ubuntu $SUITE"
EOF

cat > "$WORK/rootfs/etc/motd" <<'EOF'
B.I.N.E.S.H. OS
Binary Intelligent Network for Enhanced Strategic Handling

Development image
EOF

mkdir -p "$WORK/rootfs/usr/local/bin" "$WORK/rootfs/usr/local/sbin" "$WORK/rootfs/var/lib/binesh"

cat > "$WORK/rootfs/usr/local/bin/binesh-status" <<'EOF'
#!/bin/sh
set -eu
echo "B.I.N.E.S.H. OS"
cat /etc/binesh-release
echo "Kernel: $(uname -r)"
echo "Architecture: $(uname -m)"
EOF
chmod +x "$WORK/rootfs/usr/local/bin/binesh-status"

cat > "$WORK/rootfs/usr/local/sbin/binesh-firstboot" <<'EOF'
#!/bin/sh
set -eu
install -d -m 0755 /var/lib/binesh
printf 'initialized=%s
' "$(date -u +%FT%TZ)" > /var/lib/binesh/firstboot-complete
EOF
chmod +x "$WORK/rootfs/usr/local/sbin/binesh-firstboot"

cat > "$WORK/rootfs/etc/systemd/system/binesh-firstboot.service" <<'EOF'
[Unit]
Description=B.I.N.E.S.H. first boot initialization
After=local-fs.target
ConditionPathExists=!/var/lib/binesh/firstboot-complete

[Service]
Type=oneshot
ExecStart=/usr/local/sbin/binesh-firstboot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

echo "binesh-os" > "$WORK/rootfs/etc/hostname"

chroot "$WORK/rootfs" /bin/bash -eux <<'CHROOT'
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y --no-install-recommends   systemd systemd-sysv dbus sudo   linux-image-generic linux-firmware   live-boot   ca-certificates iproute2 iputils-ping bash coreutils util-linux kmod
systemctl enable binesh-firstboot.service
useradd --create-home --shell /bin/bash binesh || true
echo 'binesh:binesh' | chpasswd
usermod -aG sudo binesh
apt-get clean
rm -rf /var/lib/apt/lists/*
CHROOT

KERNEL="$(find "$WORK/rootfs/boot" -maxdepth 1 -type f -name 'vmlinuz-*' | sort -V | tail -1)"
INITRD="$(find "$WORK/rootfs/boot" -maxdepth 1 -type f -name 'initrd.img-*' | sort -V | tail -1)"
[[ -n "$KERNEL" && -n "$INITRD" ]] || { echo "[BINESH] Kernel/initramfs missing." >&2; exit 1; }

cp "$KERNEL" "$WORK/iso/boot/vmlinuz"
cp "$INITRD" "$WORK/iso/boot/initrd"
mksquashfs "$WORK/rootfs" "$WORK/iso/live/filesystem.squashfs" -comp xz -noappend

cat > "$WORK/iso/boot/grub/grub.cfg" <<'EOF'
set timeout=3
set default=0

menuentry "B.I.N.E.S.H. OS (development)" {
    linux /boot/vmlinuz boot=live quiet
    initrd /boot/initrd
}
EOF

grub-mkrescue -o "$OUT/binesh-os-x86_64-dev.iso" "$WORK/iso"
sha256sum "$OUT/binesh-os-x86_64-dev.iso" > "$OUT/binesh-os-x86_64-dev.iso.sha256"

echo "[BINESH] Image ready: $OUT/binesh-os-x86_64-dev.iso"
