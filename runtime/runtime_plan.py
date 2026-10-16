"""Runtime selection without execution.

This module turns detected package metadata plus host capabilities into an
explicit execution plan. It never installs, launches or escalates privileges.
"""

from __future__ import annotations

from dataclasses import dataclass

from .package_detect import PackageInfo


@dataclass(frozen=True)
class RuntimePlan:
    action: str
    runtime: str
    reason: str


def plan_runtime(info: PackageInfo, capabilities: set[str]) -> RuntimePlan:
    if info.runtime == "native-linux":
        if info.architecture in {None, "unknown"}:
            return RuntimePlan("inspect", "native-linux", "architecture requires verification")
        if info.architecture in capabilities:
            return RuntimePlan("execute", "native-linux", "native architecture supported")
        return RuntimePlan("unsupported", "native-linux", "native architecture is unavailable")

    if info.runtime in capabilities:
        return RuntimePlan("execute", info.runtime, "runtime is available")

    if info.runtime == "windows-compatibility" and "windows-vm" in capabilities:
        return RuntimePlan("virtualize", "windows-vm", "Windows compatibility runtime is unavailable; VM is available")

    if info.runtime == "macos-package":
        return RuntimePlan("inspect", "macos-package", "macOS package requires a compatible macOS environment")

    if info.runtime == "windows-compatibility":
        return RuntimePlan("inspect", "windows-compatibility", "Windows runtime is unavailable")

    if info.runtime in {"archive", "linux-package"}:
        return RuntimePlan("install", info.runtime, "package requires an installer/package manager")

    return RuntimePlan("unsupported", info.runtime, "required runtime is unavailable")
