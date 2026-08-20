from datetime import datetime, timezone

from core.event import Event


def test_event_serialization():
    event = Event("1", "test", datetime(2026, 1, 1, tzinfo=timezone.utc), "test", {"ok": True})
    data = event.as_dict()
    assert data["id"] == "1"
    assert data["schema_version"] == 1
    assert data["payload"]["ok"] is True


def test_naive_timestamp_is_serialized_as_utc():
    event = Event("2", "test", datetime(2026, 1, 1, 12, 0, 0), "test", {})
    assert event.as_dict()["timestamp"] == "2026-01-01T12:00:00+00:00"
