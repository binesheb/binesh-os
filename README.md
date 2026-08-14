# B.I.N.E.S.H. OS

**Binary Intelligent Network for Enhanced Strategic Handling**

A modular, open-source edge operating platform designed to run the same operational services across ESP32, Raspberry Pi/Linux, and future runtimes.

> **GitHub is the source of truth.** The repository is the product specification, implementation, documentation, discussion space, change history, and release record.

## Why B.I.N.E.S.H. OS?

B.I.N.E.S.H. OS is being built as a reusable platform for real-world automation and operational systems: deterministic control, attendance, transport, device management, synchronization, diagnostics, local APIs, dashboards, OTA updates, and hardware integrations.

It is deliberately not limited to one microcontroller. The architecture separates portable domain logic from platform and hardware adapters.

## Platform targets

- **ESP32 / ESP32-S3** — real-time I/O, sensors, relays, RFID, biometrics, displays and field controllers.
- **Raspberry Pi / Linux** — gateways, local servers, databases, dashboards, protocol bridges and heavier workloads.
- **Future runtimes** — designed behind stable interfaces so additional platforms can be added without rewriting services.

## Architecture

```text
                         B.I.N.E.S.H. OS
                                |
          +---------------------+---------------------+
          |                     |                     |
       CORE API             SERVICES              SHELL/API
          |                     |                     |
   config / events       attendance             CLI / Web / REST
   logging / security    transport              OLED / admin
   scheduler             automation
   storage               synchronization
   diagnostics           diagnostics
          |                     |
          +---------- PLATFORM ABSTRACTION ----------+
                         |             |
                      ESP32        Raspberry Pi
                         |             |
                     hardware       Linux/USB/GPIO
                         |             |
                         +------+------+
                                |
                         MQTT / HTTP / WS
                                |
                         External systems
```

## Repository principles

1. **GitHub is authoritative.** If it is not documented or merged here, it is not an official platform capability.
2. **Portable logic first.** Business rules must not depend directly on ESP-IDF, Arduino, Python GPIO libraries, or other platform-specific APIs.
3. **Deterministic by design.** Given the same inputs, configuration and state, a service should produce the same result.
4. **Offline first.** Network loss must degrade gracefully rather than silently losing operational events.
5. **Auditable changes.** Important state transitions and corrections must be traceable.
6. **Secure by default.** Credentials, signing keys and device secrets never belong in Git.
7. **Community through GitHub.** Ideas belong in Discussions/Issues, implementation belongs in Pull Requests, and releases belong in Git tags/releases.
8. **Documentation is part of the product.** New behavior requires documentation and tests.

## Repository layout

```text
binesh-os/
├── core/                 Portable OS primitives
├── services/             Attendance, transport, sync, diagnostics, automation
├── platforms/            ESP32 and Raspberry Pi/Linux runtimes
├── drivers/              Hardware and protocol adapters
├── interfaces/           API, CLI, web and display interfaces
├── storage/              Persistent/offline storage abstractions
├── security/             Authentication, signing and security primitives
├── docs/                 Architecture, modules, API and operations
├── examples/             Minimal deployable examples
├── tools/                Developer and release tooling
├── tests/                Portable and platform tests
├── .github/              CI, issue templates and contribution automation
└── LICENSE
```

## Getting started

### ESP32

Install PlatformIO, select the required board environment, then build and flash the ESP32 runtime. See [`docs/getting-started/esp32.md`](docs/getting-started/esp32.md).

### Raspberry Pi

Use the Linux runtime directly or deploy the containerized runtime. See [`docs/getting-started/raspberry-pi.md`](docs/getting-started/raspberry-pi.md).

### Development

```bash
git clone https://github.com/binesheb/binesh-os.git
cd binesh-os
```

Run the portable test suite before making changes:

```bash
python -m pytest
```

## Development model

The project uses a GitHub-first workflow:

```text
Idea
  ↓
GitHub Discussion / Issue
  ↓
Architecture decision
  ↓
Branch / Fork
  ↓
Implementation + tests + docs
  ↓
Pull Request
  ↓
Review + CI
  ↓
Merge to main
  ↓
Release / tag
```

Anyone should be able to:

- open an Issue for a bug or concrete engineering task;
- start a Discussion for an idea or architecture proposal;
- fork the repository;
- create a feature branch;
- submit a Pull Request;
- improve documentation;
- contribute examples, drivers or tests;
- review proposed changes;
- suggest alternative implementations.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Source-of-truth policy

The repository's `main` branch represents the current accepted implementation. `docs/architecture/` represents the accepted architecture. Pull Requests are the controlled path for code changes. GitHub Issues and Discussions are the public engineering backlog and proposal space.

Local generated files, binaries, credentials, device databases and deployment secrets are **never** considered source-of-truth artifacts.

## Security

Do not commit API keys, passwords, certificates with private keys, device credentials, production databases, or OTA signing secrets. Report security vulnerabilities privately according to [`SECURITY.md`](SECURITY.md).

## Status

**Phase: Foundation / v0.1 architecture**

The interfaces are intentionally being established before hardware-specific implementations are locked in. This allows ESP32 and Raspberry Pi to share the same service contracts.

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
