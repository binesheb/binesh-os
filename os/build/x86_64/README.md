# x86_64 image builder

This directory contains the first real B.I.N.E.S.H. OS image-generation path.

## Requirements

- Ubuntu/Debian build host
- root privileges
- debootstrap
- grub-mkrescue
- xorriso
- mksquashfs

Install host dependencies on Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y debootstrap grub-efi-amd64-bin grub-pc-bin xorriso squashfs-tools
```

## Build

The repository file is intentionally runnable through bash so GitHub's source-file API does not depend on preserving an executable-bit mode:

```bash
sudo bash ./os/build/x86_64/build-image.sh
```

Output:

```text
out/x86_64/binesh-os-x86_64-dev.iso
out/x86_64/binesh-os-x86_64-dev.iso.sha256
```

## QEMU

Install QEMU:

```bash
sudo apt-get install -y qemu-system-x86 ovmf
```

Then boot:

```bash
qemu-system-x86_64 -m 2048 -cdrom out/x86_64/binesh-os-x86_64-dev.iso -serial stdio
```

This is the first bootable development-image milestone, not the production installer. The next milestones are writable installation, UEFI validation, hardware discovery, networking, recovery and desktop integration.
