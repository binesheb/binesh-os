# B.I.N.E.S.H. Runtime

The runtime layer provides the universal application model.

## Detection

runtime/package_detect.py classifies packages and executable formats without executing them.

Examples:

| Input | Classification | Runtime |
|---|---|---|
| ELF | native executable | native Linux |
| APK | Android package | Android runtime |
| EXE/PE | Windows executable | Windows compatibility runtime |
| DMG | macOS disk image | macOS package handling |
| DEB/RPM | Linux package | Linux package manager |
| AppImage | Linux application | native Linux |
| JAR | JVM application | JVM |
| WASM | WebAssembly module | WASM runtime |
| TAR/ZIP | archive | archive installer |

Detection is deliberately separate from execution.

## Security rule

A recognized extension does not make an application trusted or executable. Before installation/execution, the application manager must evaluate:

1. architecture compatibility
2. runtime availability
3. package integrity
4. signature/provenance
5. declared permissions
6. sandbox policy
7. dependencies

The manager must report unsupported packages clearly rather than attempting unsafe execution.
