#include <Arduino.h>

static const char* VERSION = "0.1.0-dev";

void setup() {
  Serial.begin(115200);
  delay(200);
  Serial.println();
  Serial.println("========================================");
  Serial.println(" B.I.N.E.S.H. OS");
  Serial.printf(" Version: %s\n", VERSION);
  Serial.println(" Platform: ESP32");
  Serial.println("========================================");
}

void loop() {
  // Keep the platform loop minimal. Services and hardware adapters are
  // initialized behind explicit interfaces as the runtime matures.
  delay(1000);
}
