/**
 * 200Hz is a simple Arduino program that reads
 * in signal through A0 at 200 Hz (i.e. 200 cycles
 * per second).
 * 
 * Author: Chanha Kim
 * Date: 08/12/2020
 */
 
void setup() {
  Serial.begin(115200);
}

void loop() {
  double val = analogRead(0);
  Serial.println(val);
  delay(5);
}
