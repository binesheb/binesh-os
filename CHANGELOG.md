# Changelog

All notable changes to B.I.N.E.S.H. OS are recorded here.

## Unreleased

### Added
- Cross-platform architecture for ESP32 and Raspberry Pi/Linux.
- GitHub-first contribution and source-of-truth model.
- Initial core/service/platform directory model.

### Fixed
- Normalize naive event timestamps as UTC before serialization to avoid host-local timezone drift.
- Refuse manual updates unless the checkout is on `main`, preventing an accidental merge of `origin/main` into a feature branch.
- Roll back a fast-forwarded source update when the dependency bootstrap or portable test suite fails, preserving the previously known-good checkout.
- Skip ESP32 compilation until firmware sources exist and run the portable test suite without requiring Python package discovery for the multi-runtime foundation layout.
- Remove the invalid pre-source ESP32 CI job so the foundation validation workflow only runs checks that are currently supported by the repository.

## 0.1.0

- Project initialization.
