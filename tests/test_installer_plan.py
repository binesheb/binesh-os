from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest

MODULE = Path(__file__).resolve().parents[1] / "os" / "installer" / "plan.py"
spec = spec_from_file_location("binesh_installer_plan", MODULE)
module = module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

Disk = module.Disk
make_plan = module.make_plan


def test_install_plan_is_explicit():
    plan = make_plan(Disk("/dev/vda", 20_000, False, "QEMU disk"), 10_000)
    assert plan.target == "/dev/vda"
    assert plan.erase_target is True
    assert plan.boot_mode == "uefi"
    assert plan.filesystem == "ext4"


def test_small_disk_is_rejected():
    with pytest.raises(ValueError, match="too small"):
        make_plan(Disk("/dev/vda", 100, False), 1000)
