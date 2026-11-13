from pathlib import Path

from runtime.package_detect import detect_package


def test_detects_windows_pe(tmp_path: Path):
    p = tmp_path / "setup.exe"
    p.write_bytes(b"MZ" + b"\0" * 62)
    info = detect_package(p)
    assert info.kind == "pe"
    assert info.runtime == "windows-compatibility"
    assert info.executable is True


def test_detects_native_elf_x86_64(tmp_path: Path):
    p = tmp_path / "app"
    header = bytearray(64)
    header[:4] = b"\x7fELF"
    header[18:20] = (0x3E).to_bytes(2, "little")
    p.write_bytes(header)
    info = detect_package(p)
    assert info.kind == "elf"
    assert info.architecture == "x86_64"
    assert info.runtime == "native-linux"


def test_detects_apk(tmp_path: Path):
    import zipfile

    p = tmp_path / "app.apk"
    with zipfile.ZipFile(p, "w") as archive:
        archive.writestr("AndroidManifest.xml", b"placeholder")
    info = detect_package(p)
    assert info.kind == "apk"
    assert info.runtime == "android"


def test_detects_dmg_by_extension(tmp_path: Path):
    p = tmp_path / "installer.dmg"
    p.write_bytes(b"not-executed")
    info = detect_package(p)
    assert info.kind == "dmg"
    assert info.runtime == "macos-package"
    assert info.executable is False
