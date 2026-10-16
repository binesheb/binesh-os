# OS Build Pipeline

The build pipeline is separated from application development.

## Planned outputs

- binesh-os-x86_64.iso
- binesh-os-x86_64.qcow2
- binesh-os-aarch64.img
- installer/recovery media
- checksums
- signed release metadata

## Development order

1. Build a minimal root filesystem.
2. Build/pin the kernel.
3. Add bootloader/UEFI path.
4. Add B.I.N.E.S.H. init and system services.
5. Boot in QEMU.
6. Add installer.
7. Add desktop.
8. Add ARM64 image.
9. Add physical hardware acceptance tests.

Never call an image a release merely because it boots once. A release must pass docs/architecture/OS_ACCEPTANCE.md.