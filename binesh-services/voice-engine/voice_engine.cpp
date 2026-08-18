#include "voice_engine.h"

#include <algorithm>
#include <cctype>

namespace binesh::voice {

namespace {
std::string normalize(std::string value) {
    std::transform(value.begin(), value.end(), value.begin(), [](unsigned char c) {
        return static_cast<char>(std::tolower(c));
    });
    return value;
}

bool contains(const std::string& text, const char* phrase) {
    return text.find(phrase) != std::string::npos;
}
} // namespace

void VoiceEngine::begin() {
    // Audio/STT providers are platform adapters. The common engine remains portable.
    state_ = VoiceState::Idle;
}

void VoiceEngine::loop() {
    // Platform adapters feed recognized text into parseCommand().
}

VoiceState VoiceEngine::state() const {
    return state_;
}

VoiceCommand VoiceEngine::parseCommand(const std::string& transcript) const {
    const std::string text = normalize(transcript);
    VoiceCommand command;
    command.transcript = transcript;
    command.confidence = 1.0F;

    if (contains(text, "start announcement") ||
        contains(text, "start the announcement")) {
        command.intent = Intent::StartAnnouncement;
    } else if (contains(text, "stop announcement") ||
               contains(text, "stop the announcement")) {
        command.intent = Intent::StopAnnouncement;
    } else if (contains(text, "attendance status") ||
               contains(text, "how many staff") ||
               contains(text, "attendance")) {
        command.intent = Intent::AttendanceStatus;
    } else if (contains(text, "transport status") ||
               contains(text, "bus status")) {
        command.intent = Intent::TransportStatus;
    } else if (contains(text, "device status") ||
               contains(text, "system status")) {
        command.intent = Intent::DeviceStatus;
    }

    return command;
}

void VoiceEngine::handleCommand(const VoiceCommand& command) {
    // Intent dispatch is intentionally separated from STT so the same command
    // model can be used by ESP32, Raspberry Pi and server runtimes.
    if (command.intent == Intent::Unknown) {
        state_ = VoiceState::Error;
        return;
    }

    state_ = VoiceState::Processing;
    // Event-bus integration will dispatch the typed intent to the owning service.
    state_ = VoiceState::Idle;
}

} // namespace binesh::voice
