#pragma once

#include <cstdint>
#include <string>

namespace binesh::voice {

enum class VoiceState : uint8_t {
    Disabled,
    Idle,
    Listening,
    Processing,
    Speaking,
    Error
};

enum class Intent : uint8_t {
    Unknown,
    StartAnnouncement,
    StopAnnouncement,
    AttendanceStatus,
    TransportStatus,
    DeviceStatus
};

struct VoiceCommand {
    Intent intent{Intent::Unknown};
    std::string transcript;
    float confidence{0.0F};
};

class VoiceEngine {
public:
    void begin();
    void loop();
    VoiceState state() const;
    VoiceCommand parseCommand(const std::string& transcript) const;
    void handleCommand(const VoiceCommand& command);

private:
    VoiceState state_{VoiceState::Disabled};
};

} // namespace binesh::voice
