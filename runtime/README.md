# B.I.N.E.S.H. Runtime

The runtime layer provides the universal application model.

It detects:

- CPU architecture
- operating environment
- package type
- required runtime
- dependencies
- declared permissions
- security/signature metadata

It then selects a supported execution path:

native -> container -> compatibility runtime -> emulator/VM

No package is executed merely because it has a recognized extension.
