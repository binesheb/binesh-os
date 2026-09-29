# B.I.N.E.S.H. OS

**Binary Intelligent Network for Enhanced Strategic Handling**

> **B.I.N.E.S.H. OS is becoming a proper, installable operating system.**

B.I.N.E.S.H. is an open-source operating system and edge platform intended to boot on PCs and ARM64 systems, run applications and services, manage hardware, provide local automation and intelligence, and extend the same service model to embedded devices such as ESP32.

**GitHub is the source of truth.** The accepted architecture, source code, build definitions, tests, documentation, issues, pull requests and releases live in this repository.

## Project direction

The project started as an ESP32-oriented operating layer. That is no longer the primary definition.

B.I.N.E.S.H. OS is now organized as a complete OS stack:

```text
Platform firmware
      |
UEFI / board boot
      |
Bootloader
      |
Linux kernel
      |
Base system
      |
B.I.N.E.S.H. system layer
      |
B.I.N.E.S.H. application/runtime layer
      |
Desktop / CLI / API / Web / Voice
      |
Applications + automation + enterprise services
```

The initial desktop/server implementation will use the Linux kernel and established low-level components. B.I.N.E.S.H. owns the distribution integration, system behavior, user experience, application model, security policy, management layer and platform services. This lets us build a real OS without pretending that every foundational component needs to be reinvented.

## What B.I.N.E.S.H. should become

- Bootable from USB/ISO.
- Installable to a physical disk.
- Bootable in a virtual machine.
- Support x86_64 PCs.
- Support ARM64/Raspberry Pi.
- Provide a desktop and command-line environment.
- Provide a package and application manager.
- Run native Linux applications and supported portable runtimes.
- Provide containers and sandboxed applications.
- Add compatibility runtimes when technically and legally appropriate.
- Provide secure system and application updates with rollback.
- Provide device and hardware management.
- Provide local APIs and web administration.
- Provide voice as an OS service.
- Provide deterministic automation.
- Provide attendance, transport and operational services.
- Integrate local AI through the BNSH AI ecosystem.
- Extend the same service/event model to embedded B.I.N.E.S.H. runtimes.

## Platform targets

### x86_64

Primary development target for a general-purpose installable OS.

Acceptance target: boot a reproducible B.I.N.E.S.H. image under QEMU/UEFI, then install it to a virtual disk and reboot into the installed system.

### ARM64 / Raspberry Pi

First-class edge/server target.

Acceptance target: boot and install a supported ARM64 image on Raspberry Pi hardware while sharing the same portable B.I.N.E.S.H. service contracts.

### ESP32

ESP32 remains a supported **embedded runtime**, not a desktop Linux installation target. It provides deterministic hardware control, sensors, displays, RFID/biometrics, relays and field automation under the common B.I.N.E.S.H. event/service model.

## Application platform

B.I.N.E.S.H. will include a capability-aware Universal Application Manager.

Potential execution paths include:

```text
Native Linux
   |
Container / sandbox
   |
Language runtime
   |
Compatibility runtime
   |
Virtual machine / emulation
```

Supported formats are capability-dependent. Examples include native Linux packages, AppImage, OCI containers, Python/Node/JVM applications, WebAssembly and Android APKs when a suitable runtime is installed. Windows executables may use a compatibility runtime where supported. macOS packages such as DMG are not assumed to be executable on Linux; the manager must identify the package and report the available compatibility path rather than pretending compatibility exists.

## Core capabilities

### Operating system

- Boot and recovery
- Kernel integration
- Hardware discovery
- Drivers
- Storage
- Networking
- Users and permissions
- Services
- Logging
- Power management
- Diagnostics
- Secure updates

### Application platform

- Package metadata
- Package installation/removal
- Dependency resolution
- Runtime detection
- Sandboxing
- Containers
- Application permissions
- Application launchers
- Application audit records

### B.I.N.E.S.H. services

- Automation
- Attendance
- Transport
- Synchronization
- Diagnostics
- Voice
- Device management
- Enterprise API integration

## Repository layout

```text
binesh-os/
├── os/                  Bootable OS build and installer
│   ├── boot/
│   ├── config/
│   │   ├── x86_64/
│   │   └── aarch64/
│   ├── installer/
│   └── system/
├── core/                Portable B.I.N.E.S.H. primitives
├── services/            Operational services
├── runtime/             Universal application/runtime model
├── platforms/           ESP32 and Raspberry Pi implementations
├── drivers/             Hardware/protocol adapters
├── interfaces/          API, CLI, web and display interfaces
├── storage/             Persistent/offline storage
├── security/            Identity, signing and authorization
├── docs/                Architecture and operations
├── examples/            Examples and reference applications
├── tools/               Build, test and release tooling
├── tests/               Automated tests
└── .github/             CI, issue templates and contribution workflow
```

## Build philosophy

The OS must be reproducible.

Generated artifacts do not belong in Git. Build inputs, configuration, patches, scripts, manifests and version pins do.

The desktop/server build will produce bootable artifacts through a controlled pipeline. Embedded targets may use an embedded Linux image builder where appropriate. Buildroot is useful for focused embedded images, while Yocto/OpenEmbedded can provide a scalable multi-board build framework; these are implementation tools, not the identity of B.I.N.E.S.H.

## Development

```bash
git clone https://github.com/binesheb/binesh-os.git
cd binesh-os
python -m pytest
```

During the OS bootstrap phase, a Linux build host is the preferred environment for image generation. VM/CI builds will be used so that changes can be validated without physical hardware.

## GitHub-first development

```text
Idea
  |
Discussion / Issue
  |
Architecture decision
  |
Fork or branch
  |
Implementation
  |
Tests + documentation
  |
Pull Request
  |
CI
  |
Review
  |
main
  |
Release
  |
Installer / ISO / image
```

Anyone can propose features, hardware support, application runtimes, drivers, UI changes, documentation, tests or architecture changes through GitHub.

## Source-of-truth policy

The accepted `main` branch is authoritative.

- If a feature is not merged, it is not an official capability.
- If an architecture proposal is not accepted, it is not an architecture guarantee.
- Release artifacts must correspond to tagged source.
- Generated binaries are release outputs, not source.
- Secrets and signing keys never belong in the repository.

## Security

B.I.N.E.S.H. must be secure by default. Privileged operations require authorization. Applications must not automatically receive unrestricted host access. Release artifacts should be signed and update mechanisms must support integrity verification and recovery.

See [SECURITY.md](SECURITY.md).

## Roadmap

The detailed OS roadmap is in [docs/architecture/PROPER_OS_ROADMAP.md](docs/architecture/PROPER_OS_ROADMAP.md).

The immediate milestone is:

> **Boot a reproducible B.I.N.E.S.H. x86_64 development image in QEMU and reach B.I.N.E.S.H. userspace.**

Then we build the installer, system services, desktop, application platform and ARM64/Raspberry Pi image.

## License

Apache License 2.0. See [LICENSE](LICENSE).
