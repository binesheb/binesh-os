# B.I.N.E.S.H. OS Acceptance Criteria

An artifact may be called an **OS release** only when it satisfies the applicable criteria below.

## Boot

- [ ] Boots from a release USB/ISO in a clean VM.
- [ ] Boots using UEFI.
- [ ] Kernel and initial userspace load without manual host intervention.
- [ ] Boot failure provides recoverable diagnostics.

## Installation

- [ ] Installer can identify storage devices.
- [ ] Installer supports a safe guided installation path.
- [ ] First boot creates/configures an administrator.
- [ ] Installation can be verified after reboot.

## Core system

- [ ] Persistent filesystem.
- [ ] Network configuration.
- [ ] System clock/time synchronization.
- [ ] User and permission model.
- [ ] Service lifecycle management.
- [ ] Structured logs.
- [ ] Hardware discovery.
- [ ] Configuration persistence.

## Updates

- [ ] Release metadata is signed.
- [ ] Update packages/images are integrity checked.
- [ ] Failed updates can roll back.
- [ ] Version and channel are visible locally.
- [ ] Manual recovery/update path is documented.

## Applications

- [ ] Application metadata model exists.
- [ ] Installation/uninstallation records ownership.
- [ ] Applications run with explicit permissions.
- [ ] Unsupported packages explain why they cannot run.
- [ ] Application execution is auditable.

## Security

- [ ] Secrets are not stored in source control.
- [ ] Privileged operations require authorization.
- [ ] Release artifacts have provenance.
- [ ] Dangerous application capabilities are sandboxed or explicitly approved.

## Developer acceptance

- [ ] Clean build from documented instructions.
- [ ] Automated tests pass.
- [ ] VM smoke test passes.
- [ ] Source, build instructions and release metadata are in GitHub.
