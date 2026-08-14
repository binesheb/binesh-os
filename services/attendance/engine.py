"""Deterministic attendance domain service."""

from dataclasses import dataclass
from typing import Literal

PunchType = Literal["IN", "OUT"]

@dataclass(frozen=True)
class Punch:
    employee_id: str
    timestamp: str
    punch_type: PunchType
    source: str

@dataclass(frozen=True)
class AttendanceDecision:
    employee_id: str
    status: str
    reason: str


def process_punch(punch: Punch) -> AttendanceDecision:
    """Apply only explicit deterministic rules.

    Policy-specific rules should be injected/configured rather than hidden in
    platform code. This baseline records the event without guessing corrections.
    """
    if not punch.employee_id:
        return AttendanceDecision("", "REJECTED", "missing_employee_id")
    if punch.punch_type not in ("IN", "OUT"):
        return AttendanceDecision(punch.employee_id, "REJECTED", "invalid_punch_type")
    return AttendanceDecision(punch.employee_id, "ACCEPTED", "validated")
