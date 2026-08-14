# Getting Started — ESP32

## Requirements

- ESP32-compatible board
- USB cable
- PlatformIO CLI or VS Code with PlatformIO

## Build

```bash
pio run -e esp32
```

## Flash

```bash
pio run -e esp32 -t upload
```

## Monitor

```bash
pio device monitor
```

Hardware-specific configuration belongs under `platforms/esp32/` and must not leak into portable services.
