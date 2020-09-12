//double x = 0.00;
//const double pi = 3.141592653589;

void setup() {
  Serial.begin(115200);
}

void loop() {
  double val = analogRead(0);
//  double val = sin(pi*x);
  Serial.println(val);
//  x += 0.005;
  delay(10);
}
