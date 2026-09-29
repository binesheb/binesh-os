# B.I.N.E.S.H. OS Build System

This directory is the beginning of the bootable operating-system build layer.

## Targets

- `x86_64`: primary desktop/server development target
- `aarch64`: Raspberry Pi and ARM64 edge target
- `esp32`: embedded runtime, built separately from the Linux OS

The initial objective is a deterministic development image that boots in a virtual machine before hardware installation is attempted.

## Rule

Do not place generated disk images, credentials, signing keys or build caches in Git. CI and release pipelines generate artifacts from pinned source inputs.
