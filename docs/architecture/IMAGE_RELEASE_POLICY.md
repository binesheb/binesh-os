# Image and Release Policy

B.I.N.E.S.H. distinguishes development images from official releases.

## Development image

A development image may use upstream packages and is intended for:

- QEMU testing
- developer hardware
- architecture experiments
- CI validation

It must never be presented as a production release.

## Release candidate

A release candidate must have:

- pinned build inputs
- reproducible build documentation
- complete automated tests
- QEMU boot validation
- installer validation
- hardware acceptance for the target platform
- SBOM/provenance
- checksums
- signed metadata

## Production release

A production image additionally requires:

- signed artifacts
- secure update metadata
- rollback/recovery
- documented security support policy
- tested installer and recovery path
- release notes
- versioned compatibility matrix

Generated ISO files are release artifacts, not source files. The repository contains the inputs needed to reproduce them.
