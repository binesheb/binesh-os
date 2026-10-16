"""Pure installer planning logic.

The planner only describes what would happen. A future privileged installer
will execute a reviewed plan after explicit user confirmation.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Disk:
    path: str
    size_bytes: int
    removable: bool
    model: str = ""


@dataclass(frozen=True)
class InstallPlan:
    target: str
    required_bytes: int
    erase_target: bool
    boot_mode: str
    filesystem: str


def make_plan(disk: Disk, required_bytes: int, boot_mode: str = "uefi") -> InstallPlan:
    if not disk.path:
        raise ValueError("target disk is required")
    if required_bytes <= 0:
        raise ValueError("required size must be positive")
    if disk.size_bytes < required_bytes:
        raise ValueError("target disk is too small")
    if boot_mode not in {"uefi"}:
        raise ValueError("unsupported boot mode")
    return InstallPlan(
        target=disk.path,
        required_bytes=required_bytes,
        erase_target=True,
        boot_mode=boot_mode,
        filesystem="ext4",
    )
