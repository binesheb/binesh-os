# Installer

The installer will provide both graphical and command-line installation paths.

## Current architecture

The installer is separated into:

- **planner** — pure, testable installation decisions;
- **target validation** — verifies the selected block device;
- **executor** — privileged disk-writing implementation, still gated;
- **recovery** — repair and diagnostics.

## Virtual-disk testing

Create a disposable test disk:

```bash
bash tools/installer/create-test-disk.sh out/installer/test-disk.img 4096
```

The file is intended for QEMU-based testing and must never be confused with a physical disk.

## Required production capabilities

1. Boot from USB/ISO.
2. Hardware and storage discovery.
3. Guided disk selection.
4. Explicit destructive-operation confirmation.
5. Partitioning and filesystem creation.
6. OS image installation.
7. UEFI bootloader configuration.
8. User creation.
9. Network configuration.
10. First-boot handoff.
11. Recovery/repair mode.
12. Installation receipt and verification.

Physical-disk installation remains disabled until the virtual-disk flow passes automated validation.
