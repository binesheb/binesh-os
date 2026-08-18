# B.I.N.E.S.H. Voice Engine

The Voice Engine provides a platform-independent voice-command layer for B.I.N.E.S.H. OS.

## Design goals

- Keep speech recognition separate from business logic.
- Support offline operation where the selected platform permits it.
- Allow ESP32 devices to act as microphone/wake-word endpoints.
- Use Raspberry Pi as the preferred local STT/TTS processing node.
- Convert recognized speech into typed B.I.N.E.S.H. intents.
- Preserve auditability: voice commands become normal OS events.

## Pipeline

```text
Microphone -> VAD/Wake Word -> STT -> Intent Parser -> Event Bus -> B.I.N.E.S.H. Service
```

## Platform strategy

### ESP32

ESP32 should normally provide audio capture, wake-word detection, push-to-talk and lightweight endpoint functionality. Heavy speech recognition should be delegated to a Raspberry Pi or server unless the selected ESP32 model and model size make local inference practical.

### Raspberry Pi

Raspberry Pi is the preferred local voice-processing runtime. A provider adapter can connect the engine to an offline speech-to-text engine, wake-word engine and text-to-speech engine without changing the portable command model.

## Example commands

- `Binesh, start announcement`
- `Binesh, stop announcement`
- `Binesh, what is the attendance status?`
- `Binesh, what is the bus status?`
- `Binesh, give me the device status`

The current parser is intentionally conservative. Production deployments should add explicit wake-word handling, confidence thresholds, permissions and service-specific intent schemas before allowing privileged actions.
