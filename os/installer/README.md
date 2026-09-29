# Installer

The installer will eventually provide a graphical and command-line installation path.

Required capabilities:

1. Boot from USB/ISO.
2. Hardware and storage discovery.
3. Guided disk selection.
4. Partitioning and filesystem creation.
5. OS image installation.
6. Bootloader configuration.
7. User creation.
8. Network configuration.
9. First-boot handoff.
10. Recovery/repair mode.

The installer must have a dry-run/testing mode so CI can exercise its logic without modifying a real disk.
