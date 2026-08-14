# B.I.N.E.S.H. OS core interfaces

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Mapping

@dataclass(frozen=True)
class Event:
    id: str
    type: str
    timestamp: datetime
    source: str
    payload: Mapping[str, Any]
    schema_version: int = 1

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "timestamp": self.timestamp.astimezone(timezone.utc).isoformat(),
            "source": self.source,
            "payload": dict(self.payload),
            "schema_version": self.schema_version,
        }

class Clock:
    def now(self) -> datetime:
        return datetime.now(timezone.utc)
