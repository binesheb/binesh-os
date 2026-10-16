# B.I.N.E.S.H. OS — ARM64 / Raspberry Pi

ARM64 is a first-class B.I.N.E.S.H. OS target.

## Initial hardware target

The first hardware acceptance target is Raspberry Pi-class ARM64 hardware.

The target image will eventually contain:

- ARM64 Linux kernel
- Raspberry Pi firmware/boot files where required
- device-tree support
- B.I.N.E.S.H. userspace
- network management
- diagnostics
- application/runtime manager
- OTA/update client

## Current milestone

The repository now contains the ARM64 userspace bootstrap:

```bash
sudo bash os/config/aarch64/build-image.sh
```

This currently validates the ARM64 Debian userspace bootstrap only. It is **not yet a bootable Raspberry Pi image**.

## Hardware acceptance gate

A Raspberry Pi image will not be called ready until it:

1. boots from supported media;
2. reaches B.I.N.E.S.H. userspace;
3. brings up networking;
4. exposes diagnostics;
5. survives reboot;
6. can update/recover;
7. passes the same application/runtime security rules as x86_64.

Physical SD/eMMC writing will not be automated until the image has passed virtual ARM64 validation where practical.
