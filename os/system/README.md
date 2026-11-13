# System Layer

The system layer owns the integration that makes B.I.N.E.S.H. an operating system:

- init/service lifecycle
- users and permissions
- hostname and identity
- networking
- storage mounts
- hardware discovery
- logging
- power/reboot/shutdown
- update/recovery
- system diagnostics

Portable B.I.N.E.S.H. services must consume stable interfaces rather than directly controlling the host.
