from pathlib import Path


def parse(text: str) -> str:
    t = text.lower()
    if "start announcement" in t or "start the announcement" in t:
        return "StartAnnouncement"
    if "stop announcement" in t or "stop the announcement" in t:
        return "StopAnnouncement"
    if "attendance status" in t or "how many staff" in t or "attendance" in t:
        return "AttendanceStatus"
    if "transport status" in t or "bus status" in t:
        return "TransportStatus"
    if "device status" in t or "system status" in t:
        return "DeviceStatus"
    return "Unknown"


def test_start_announcement():
    assert parse("Binesh, start announcement") == "StartAnnouncement"


def test_attendance_status():
    assert parse("What is the attendance status?") == "AttendanceStatus"


def test_unknown_command():
    assert parse("Play some music") == "Unknown"
