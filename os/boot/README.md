# Boot

B.I.N.E.S.H. OS uses a standard firmware-to-bootloader-to-kernel chain.

Initial PC path:

UEFI -> bootloader -> Linux kernel -> initramfs -> B.I.N.E.S.H. userspace

The boot implementation must support recovery and version selection. Release boot artifacts must be reproducible and integrity checked.
