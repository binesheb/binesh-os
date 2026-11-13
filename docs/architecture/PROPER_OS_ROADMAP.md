# Proper OS Roadmap

## Milestone 1 — Boot

Goal: B.I.N.E.S.H. boots as an independently built OS image in QEMU.

Deliverables:
- reproducible x86_64 build
- UEFI boot
- Linux kernel configuration
- initramfs
- root filesystem
- B.I.N.E.S.H. init/service layer
- serial console
- automated boot smoke test

## Milestone 2 — Installer

Goal: install B.I.N.E.S.H. to a virtual disk and reboot into the installed system.

## Milestone 3 — System

Goal: networking, users, storage, logging, device discovery and recovery.

## Milestone 4 — Desktop

Goal: usable graphical desktop and system settings.

## Milestone 5 — Application platform

Goal: package discovery, installation, sandboxing, containers and runtime management.

## Milestone 6 — ARM64/Raspberry Pi

Goal: boot and install B.I.N.E.S.H. on supported Raspberry Pi hardware.

## Milestone 7 — Embedded

Goal: align ESP32 runtime APIs with the common B.I.N.E.S.H. service/event model.

## Milestone 8 — Intelligence

Goal: integrate voice and the BNSH AI layer as local OS capabilities while preserving offline operation.

Every milestone requires documentation, tests and a reproducible artifact before it is considered complete.
