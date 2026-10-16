# B.I.N.E.S.H. Installer — Virtual Disk Milestone

The installer is intentionally split into two layers:

1. **Planner** — pure logic that validates a requested installation.
2. **Executor** — privileged code that will modify a selected disk only after explicit confirmation.

## Virtual-disk acceptance flow

```text
B.I.N.E.S.H. ISO
      |
      v
QEMU installer environment
      |
      v
Discover /dev/vda
      |
      v
Generate install plan
      |
      v
Show destructive-operation summary
      |
      v
Explicit confirmation
      |
      v
Partition GPT
      |
      +--> EFI System Partition
      |
      +--> Linux root partition
      |
      v
Format filesystems
      |
      v
Install B.I.N.E.S.H. system
      |
      v
Install UEFI bootloader
      |
      v
Verify boot files
      |
      v
Reboot into installed OS
```

## Safety invariants

The executor must:

- refuse an empty target;
- refuse a target below the minimum size;
- display the exact block device and model;
- never select a physical disk implicitly;
- require explicit confirmation immediately before destructive operations;
- refuse to operate on a mounted system disk unless running inside the installer environment;
- verify filesystem creation;
- verify copied system files;
- verify EFI boot files;
- write an installation receipt;
- return a non-zero exit status on any failed step.

The first implementation is a **QEMU-only virtual-disk installer**. Physical-disk installation will remain disabled until the virtual-disk flow has passed automated tests.
