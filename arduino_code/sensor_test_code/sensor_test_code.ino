void setup() {

  Serial.begin(115200);
}

void loop() {

  int value = analogRead(34);

  Serial.print("Sensor Value: ");

  Serial.println(value);

  delay(1000);
}