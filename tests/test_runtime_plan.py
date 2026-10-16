from runtime.package_detect import PackageInfo
from runtime.runtime_plan import plan_runtime


def test_native_linux_uses_host_architecture():
    info = PackageInfo("app", "elf", "x86_64", "native-linux", True)
    plan = plan_runtime(info, {"x86_64"})
    assert plan.action == "execute"
    assert plan.runtime == "native-linux"


def test_windows_can_fall_back_to_vm():
    info = PackageInfo("app.exe", "pe", "unknown", "windows-compatibility", True)
    plan = plan_runtime(info, {"windows-vm"})
    assert plan.action == "virtualize"
    assert plan.runtime == "windows-vm"


def test_macos_package_is_not_claimed_as_linux_executable():
    info = PackageInfo("app.dmg", "dmg", None, "macos-package", False)
    plan = plan_runtime(info, {"native-linux"})
    assert plan.action == "inspect"


def test_archive_requires_installation_path():
    info = PackageInfo("app.tar", "tar", None, "archive", False)
    plan = plan_runtime(info, {"native-linux"})
    assert plan.action == "install"
