# Updating B.I.N.E.S.H. OS

B.I.N.E.S.H. OS is designed to support both deliberate operator-controlled upgrades and future managed updates across ESP32 and Raspberry Pi/Linux deployments.

## Manual repository update

For a development or source deployment, use the checked-in updater and dependency bootstrapper:

```bash
tools/update.sh
tools/bootstrap.sh
```

`tools/update.sh` fetches and fast-forwards from `origin/main` only and refuses to overwrite local changes. `tools/bootstrap.sh` installs the repository's declared Python dependencies and runs the portable test suite.

Do not use `git reset --hard` as an update mechanism. Resolve or commit local changes first so an upgrade never silently discards local work.

For ESP32 source deployments, rebuild and flash only after the repository update and tests succeed:

```bash
pio run -e esp32
pio run -e esp32 --target upload
```

## Automatic updates

Automatic updates must be platform-aware and use **GitHub `main` as the only automatic update source**:

- **ESP32:** OTA support should check the repository's accepted `main` update channel, verify integrity and compatibility, and retain a recovery/manual flash path.
- **Raspberry Pi/Linux:** managed deployments should fetch only `origin/main`, refuse local divergence, stage the update, install declared dependencies, run validation and a health check, and only then switch the active runtime.
- **Development checkouts:** do not self-update automatically. Use the manual fast-forward-only workflow above.

Unattended updates must never force-overwrite local source changes or configuration, pull from feature/development branches, or bypass validation. A failed update must leave a known-good runtime available for rollback where the platform supports it.

## Release policy

The project uses Semantic Versioning:

- **MAJOR** — incompatible service, platform, or interface changes.
- **MINOR** — backward-compatible capabilities such as a new service, driver, or runtime feature.
- **PATCH** — backward-compatible fixes, reliability improvements, and small operational changes.

Release tags use `vMAJOR.MINOR.PATCH`. Pushing a valid version tag triggers the repository release workflow and generates GitHub release notes.

## Rollback

For source deployments, return to a known release tag rather than an arbitrary commit:

```bash
git fetch origin --tags
git checkout v0.1.0
```

Production Raspberry Pi/Linux deployments should ultimately rollback by switching to the previously verified runtime artifact. ESP32 devices should retain a documented USB recovery path even after OTA support is added.

## Pre-release checklist

Before tagging a release:

1. Run the Python test suite.
2. Build the ESP32 environment.
3. Update `CHANGELOG.md` when the release contains user-visible changes.
4. Confirm that release notes describe upgrade or compatibility concerns.
5. Never include credentials, device databases, or signing secrets in the release artifacts.
