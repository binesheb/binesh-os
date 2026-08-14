from datetime import datetime, timezone
from core.event import Event


def test_event_serialization():
    event = Event("1", "test", datetime(2026, 1, 1, tzinfo=timezone.utc), "test", {"ok": True})
    data = event.as_dict()
    assert data["id"] == "1"
    assert data["schema_version"] == 1
    assert data["payload"]["ok"] is True
