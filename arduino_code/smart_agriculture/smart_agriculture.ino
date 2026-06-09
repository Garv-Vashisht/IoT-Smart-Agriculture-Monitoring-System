#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

int soilPin = 34;
int ldrPin = 35;
int relayPin = 25;

void setup() {

  Serial.begin(115200);

  dht.begin();

  pinMode(relayPin, OUTPUT);

  digitalWrite(relayPin, HIGH);
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  int soilMoisture = analogRead(soilPin);
  int lightIntensity = analogRead(ldrPin);

  Serial.println("===== SENSOR DATA =====");

  Serial.print("Temperature: ");
  Serial.println(temperature);

  Serial.print("Humidity: ");
  Serial.println(humidity);

  Serial.print("Soil Moisture: ");
  Serial.println(soilMoisture);

  Serial.print("Light Intensity: ");
  Serial.println(lightIntensity);

  if (soilMoisture < 1500) {

    digitalWrite(relayPin, LOW);

    Serial.println("Pump Status: ON");

  } else {

    digitalWrite(relayPin, HIGH);

    Serial.println("Pump Status: OFF");
  }

  Serial.println("========================");

  delay(5000);
}