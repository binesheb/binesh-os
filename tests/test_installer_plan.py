import pytest

from os.installer.plan import Disk, make_plan


def test_install_plan_is_explicit():
    plan = make_plan(Disk("/dev/vda", 20_000, False, "QEMU disk"), 10_000)
    assert plan.target == "/dev/vda"
    assert plan.erase_target is True
    assert plan.boot_mode == "uefi"
    assert plan.filesystem == "ext4"


def test_small_disk_is_rejected():
    with pytest.raises(ValueError, match="too small"):
        make_plan(Disk("/dev/vda", 100, False), 1000)
