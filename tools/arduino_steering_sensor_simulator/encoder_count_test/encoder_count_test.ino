
#include <Encoder.h>

// define pins
#define sensorA 2
#define sensorB 3
#define ledA 12
#define ledB 11
#define An1 A1
#define An2 A2

Encoder myEnc(sensorB, sensorA);
//   avoid using pins with LEDs attached

void setup() {
  Serial.begin(9600);
  Serial.println("Basic Encoder Test:");
}

long oldPosition  = -999;
unsigned long previousMillis = millis();
bool position_printed = false;

void loop() {
    unsigned long currentMillis = millis();
    long newPosition = myEnc.read();
    if (newPosition != oldPosition ) {
        oldPosition = newPosition;
        previousMillis = currentMillis;
        position_printed = false;
    }
    else {
        if(currentMillis - previousMillis > 750 && !position_printed) {
            position_printed = true;
            Serial.println(newPosition);
        }
    }
        
}
