# B.I.N.E.S.H. Boot Flow

## x86_64

UEFI firmware -> B.I.N.E.S.H. boot entry -> bootloader -> Linux kernel + initramfs -> early hardware discovery -> root filesystem -> system/service manager -> B.I.N.E.S.H. services -> login/desktop/shell.

UEFI is the initial PC firmware interface. Recovery must provide a path to boot a known-good system image when the newest image fails.

## ARM64

The boot sequence is board-dependent. Board support stays isolated under ARM64 target configuration while the post-kernel B.I.N.E.S.H. system remains common wherever possible.

## ESP32

ESP32 continues to use its native embedded boot/firmware flow. It is not part of the Linux boot chain.
