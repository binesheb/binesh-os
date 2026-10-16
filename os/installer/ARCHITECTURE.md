# B.I.N.E.S.H. Installer Architecture

The installer is a separate application from the running OS.

```text
Boot media
   |
Installer environment
   |
Hardware discovery
   |
Storage discovery
   |
Installation plan
   |
Partition / filesystem
   |
Copy B.I.N.E.S.H. system
   |
Bootloader installation
   |
Machine identity
   |
Administrator setup
   |
First boot
```

## Safety requirements

- Never modify a disk without an explicit confirmation.
- Show the exact target disk and intended operation.
- Support a dry-run plan.
- Validate available space before writing.
- Verify copied files.
- Verify bootloader installation.
- Provide recovery diagnostics.
- Never embed passwords or private signing keys in the installer image.

## Initial implementation

The first installer target is x86_64 UEFI. The installer will initially install a tested B.I.N.E.S.H. system image to a virtual disk in CI before physical-disk support is declared stable.
