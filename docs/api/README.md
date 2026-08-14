# B.I.N.E.S.H. OS API

API versioning starts at `/api/v1`.

## Health

`GET /api/v1/health`

Returns service health and runtime metadata.

## Device

`GET /api/v1/device`

Returns platform, firmware version, uptime and capabilities.

## Configuration

`GET /api/v1/config`

Reads non-secret runtime configuration. Secrets must never be returned.

## Attendance

`POST /api/v1/attendance/punch`

Accepts a normalized punch event. The service validates, persists and processes it.

Example:

```json
{
  "employee_id": "EMP001",
  "timestamp": "2026-08-14T09:30:00+05:30",
  "source": "rfid",
  "device_id": "ATT-001"
}
```

## Transport

`GET /api/v1/transport/routes`

Returns locally known routes.

`POST /api/v1/transport/events`

Accepts vehicle/driver/route events.

## Sync

`GET /api/v1/sync/status`

Returns queue depth, last successful synchronization and current connectivity state.

## Errors

All errors use a consistent envelope:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid timestamp",
    "request_id": "..."
  }
}
```

Clients must not depend on human-readable error messages for program logic.
