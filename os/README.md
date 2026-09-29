# B.I.N.E.S.H. OS Build System

This directory contains the bootable operating-system build layer.

## Targets

- `x86_64`: primary desktop/server development target
- `aarch64`: Raspberry Pi and ARM64 edge target
- `esp32`: embedded runtime, built separately from the Linux OS

## Current milestone

The x86_64 target now has a real development ISO builder:

```bash
sudo ./os/build/x86_64/build-image.sh
```

It bootstraps a Linux root filesystem, installs a kernel and live-boot initramfs, creates the B.I.N.E.S.H. system identity, builds a squashfs filesystem and produces an ISO suitable for the next QEMU validation stage.

Verify the artifact:

```bash
./os/build/verify-image.sh
```

## Build principles

Do not place generated disk images, credentials, signing keys or build caches in Git.

Development images may use upstream package repositories. Release builds must move to pinned inputs, provenance, checksums and signed metadata.

The installer is developed separately from the image builder and must be tested against virtual disks before physical-disk support is declared stable.
