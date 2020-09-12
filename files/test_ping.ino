/*
 * Ping FFT is a program that runs fft on data collected from ping.
 * 
 * @author: Chanha Kim
 * @date:   06/30/2020
 * 
 */

// libraries
// #include <ArduinoQueue.h>

// this constant won't change. It's the pin number of the sensor's output:
const int pingPin = 7;
const int ledPin = 12;
const int buttPin = 2;

// some variables
bool on = false;
int button_state = 0;
long last_time = 0;
int previous = LOW;
const long threshold = 500;

// ArduinoQueue<int> data(100);

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(buttPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  button_state = digitalRead(buttPin);

  if (button_state == HIGH  && previous == LOW && millis() - last_time > threshold) {
    if (on == false) {
      on = true;
      digitalWrite(ledPin, HIGH);
    } else {
      on = false;
      digitalWrite(ledPin, LOW);
    }
    last_time = millis();
  }
  
  if (on == true) {
    // establish variables for duration of the ping, and the distance result
    // in inches and centimeters:
    long duration, cm;
  
    // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
    // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
    pinMode(pingPin, OUTPUT);
    digitalWrite(pingPin, LOW);
    delayMicroseconds(2);
    digitalWrite(pingPin, HIGH);
    delayMicroseconds(5);
    digitalWrite(pingPin, LOW);
  
    // The same pin is used to read the signal from the PING))): a HIGH pulse
    // whose duration is the time (in microseconds) from the sending of the ping
    // to the reception of its echo off of an object.
    pinMode(pingPin, INPUT);
    duration = pulseIn(pingPin, HIGH);

    Serial.println(duration);
    //Serial.write(duration);
  }
  previous = button_state;
  delay(100);
}
