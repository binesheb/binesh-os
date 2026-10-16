# x86_64 target

The first proper OS target is x86_64 UEFI.

## Acceptance

1. Build from a clean Linux runner.
2. Produce a bootable ISO.
3. Boot through UEFI in QEMU.
4. Reach B.I.N.E.S.H. userspace.
5. Capture serial output for CI diagnostics.
6. Install the same artifact to a virtual disk.
7. Reboot the installed system.

The QEMU smoke-test contract is qemu-smoke.sh.

Until an actual image exists, the smoke script intentionally reports that the image milestone has not yet been reached instead of pretending to test a nonexistent artifact.
