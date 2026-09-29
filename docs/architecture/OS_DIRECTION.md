# B.I.N.E.S.H. OS — Proper OS Direction

## Decision

B.I.N.E.S.H. OS is now defined as a **proper installable operating system platform**, not an ESP32 firmware project.

The first-class operating-system targets are:

1. x86_64 PCs and virtual machines
2. ARM64 systems, including Raspberry Pi
3. embedded B.I.N.E.S.H. runtime targets such as ESP32

The desktop/server OS will initially use the Linux kernel and mature boot/runtime components rather than attempting a production kernel rewrite. B.I.N.E.S.H. owns the distribution identity, system integration, userland services, package/runtime model, installer, management layer, APIs, UI, security policy, and application platform.

## OS stack

```
Firmware: UEFI / platform firmware
        |
Bootloader: B.I.N.E.S.H. boot integration
        |
Kernel: Linux
        |
Base system: libc + core utilities + init/service manager
        |
B.I.N.E.S.H. system layer
  - device manager
  - configuration
  - identity
  - logging
  - networking
  - storage
  - security
  - update engine
  - diagnostics
        |
B.I.N.E.S.H. application platform
  - package manager
  - runtime manager
  - sandboxing
  - containers
  - compatibility runtimes
  - voice
  - automation
        |
Interfaces
  - desktop
  - shell
  - REST/WebSocket API
  - web administration
  - voice
```

UEFI provides the standard PC firmware/OS-loader boundary used by modern systems. The repository will target UEFI-compatible boot media first. See the UEFI references in the documentation. 

## Why Linux first?

A proper OS must support real hardware, filesystems, networking, USB, graphics, audio, power management, security, drivers and virtualization. Reusing the Linux kernel gives B.I.N.E.S.H. a mature hardware foundation while allowing the project to innovate above it.

This is not the same as merely installing B.I.N.E.S.H. as an application on another distribution. The project will build reproducible B.I.N.E.S.H. OS images with its own system configuration and user experience.

## Build-system strategy

### Desktop/server

Use a reproducible Linux distribution build pipeline with pinned inputs. The build produces:

- bootable ISO for x86_64
- VM image for automated testing
- ARM64 image where applicable
- signed release artifacts

### Embedded/edge

Use an embedded image builder appropriate to the board class. Buildroot is useful for focused embedded Linux images, while Yocto/OpenEmbedded is a strong long-term option for scalable multi-board distribution engineering. These remain build dependencies rather than the public identity of B.I.N.E.S.H.

## Application model

B.I.N.E.S.H. will expose a universal application manager.

Supported formats are capability-dependent:

- native Linux packages
- AppImage
- containers/OCI
- Flatpak where enabled
- Python, Node.js and JVM applications
- WebAssembly
- Android APK through an Android runtime when available
- Windows PE/EXE through a compatibility runtime when available

A package is never assumed executable merely because its filename is recognized. The application manager checks architecture, runtime availability, signatures/policy, dependencies and sandbox requirements.

## Embedded distinction

ESP32 remains important, but it is a **B.I.N.E.S.H. Embedded Runtime**, not a desktop Linux installation target. The same service contracts and event model should be reused wherever resources permit.

## Non-negotiable properties

- Reproducible builds
- Signed releases
- Secure updates with rollback
- Offline operation for core services
- Hardware capability detection
- Persistent logs and audit records
- Least-privilege application execution
- Clear separation between portable logic and platform adapters
- GitHub as the source of truth

## Phases

### Phase 0 — Architecture reset
Define the OS contract, repository layout, build targets and acceptance tests.

### Phase 1 — Bootable development image
Produce a bootable x86_64 image that reaches a B.I.N.E.S.H. login/shell in a VM.

### Phase 2 — Real installer
USB installer, disk partitioning, recovery environment, first-boot configuration.

### Phase 3 — System services
Networking, storage, users, permissions, device management, logging and updates.

### Phase 4 — Desktop
Windowing/compositor integration, desktop shell, settings, file management and application launcher.

### Phase 5 — Application platform
Package manager, application metadata, sandboxing, containers and compatibility runtimes.

### Phase 6 — Raspberry Pi
ARM64 image, board support, GPIO/USB/camera/audio integration and edge deployment.

### Phase 7 — B.I.N.E.S.H. ecosystem
Voice, BNSH AI integration, automation, attendance, transport, enterprise APIs and fleet management.
