from services.attendance.engine import Punch, process_punch


def test_valid_punch_is_accepted():
    result = process_punch(Punch("EMP001", "2026-08-14T09:30:00+05:30", "IN", "rfid"))
    assert result.status == "ACCEPTED"


def test_missing_employee_is_rejected():
    result = process_punch(Punch("", "2026-08-14T09:30:00+05:30", "IN", "rfid"))
    assert result.status == "REJECTED"
