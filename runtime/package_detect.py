"""Safe package and executable classification for B.I.N.E.S.H.

Detection never executes a file. It only inspects filenames and small magic
headers so the application manager can choose an appropriate runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import tarfile
import zipfile


@dataclass(frozen=True)
class PackageInfo:
    path: str
    kind: str
    architecture: str | None
    runtime: str
    executable: bool


def _elf_arch(machine: int) -> str | None:
    return {
        0x03: "x86",
        0x3E: "x86_64",
        0x28: "arm",
        0xB7: "aarch64",
        0x08: "mips",
    }.get(machine)


def detect_package(path: str | Path) -> PackageInfo:
    p = Path(path)
    suffix = p.suffix.lower()
    name = p.name.lower()

    if zipfile.is_zipfile(p):
        if suffix == ".apk":
            return PackageInfo(str(p), "apk", "unknown", "android", True)
        return PackageInfo(str(p), "zip", None, "archive", False)

    if tarfile.is_tarfile(p):
        return PackageInfo(str(p), "tar", None, "archive", False)

    with p.open("rb") as fh:
        magic = fh.read(64)

    if magic.startswith(b"\x7fELF"):
        arch = None
        if len(magic) >= 20:
            arch = _elf_arch(int.from_bytes(magic[18:20], "little"))
        return PackageInfo(str(p), "elf", arch, "native-linux", True)

    if magic[:2] == b"MZ":
        return PackageInfo(str(p), "pe", "unknown", "windows-compatibility", True)

    if magic.startswith(b"\xcf\xfa\xed\xfe") or magic.startswith(b"\xfe\xed\xfa\xcf"):
        return PackageInfo(str(p), "mach-o", "unknown", "macos-compatibility", True)

    if suffix == ".appimage":
        return PackageInfo(str(p), "appimage", None, "native-linux", True)

    if suffix in {".deb", ".rpm"}:
        return PackageInfo(str(p), suffix[1:], None, "linux-package", False)

    if suffix == ".dmg":
        return PackageInfo(str(p), "dmg", None, "macos-package", False)

    if suffix in {".msi"}:
        return PackageInfo(str(p), "msi", None, "windows-installer", False)

    if suffix in {".jar"}:
        return PackageInfo(str(p), "jar", None, "jvm", True)

    if suffix in {".wasm"}:
        return PackageInfo(str(p), "wasm", None, "wasm", True)

    if name.endswith(".tar.gz") or name.endswith(".tgz"):
        return PackageInfo(str(p), "tar.gz", None, "archive", False)

    raise ValueError(f"Unsupported or unknown package: {p}")
