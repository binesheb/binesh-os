# Contributing to B.I.N.E.S.H. OS

Thank you for contributing. B.I.N.E.S.H. OS is intended to be built in public, with GitHub as the source of truth.

## Before changing code

- Search existing Issues and Discussions.
- For a new capability, open an issue or discussion first when the architectural impact is significant.
- Read `docs/architecture/` and `docs/development/`.
- Keep platform-specific code behind interfaces.

## Contribution types

### Ideas
Use GitHub Discussions for broad ideas, alternative designs, use cases and questions.

### Bugs
Open an Issue with reproduction steps, expected behavior, actual behavior, platform, version and relevant logs.

### Features
Describe the problem, proposed behavior, compatibility impact, security considerations and tests.

### Pull Requests
Fork or branch from `main`, make a focused change, add tests and update documentation. Keep commits understandable and avoid mixing unrelated changes.

## Branches

Recommended names:

```text
feature/<short-name>
fix/<short-name>
docs/<short-name>
refactor/<short-name>
platform/<target>/<short-name>
```

## Pull Request checklist

- [ ] The change has a clear purpose.
- [ ] Tests were added or updated.
- [ ] Documentation was updated when behavior changed.
- [ ] No secrets or credentials are included.
- [ ] Portable code does not directly depend on platform APIs.
- [ ] Offline behavior was considered where networking is involved.
- [ ] Audit/logging implications were considered for operational changes.
- [ ] CI passes.

## Architecture rules

Portable services belong in `services/` and should consume interfaces from `core/`. ESP32 implementation belongs under `platforms/esp32/` and hardware adapters under `drivers/`. Raspberry Pi/Linux implementation belongs under `platforms/raspberry-pi/`.

Do not copy business rules into multiple platform implementations.

## Review philosophy

Reviews should focus on correctness, safety, determinism, maintainability, security, observability and user impact. Suggestions are welcome even when the proposed implementation is different from the reviewer's preferred solution.

## Releases

Only maintainers merge release-ready changes into `main`. Releases are tagged and documented. Experimental work should remain in branches until it meets the acceptance criteria documented for the relevant milestone.
