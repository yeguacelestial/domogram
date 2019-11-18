#include <DHT.h>

#define DHT_PIN A0
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);
void setup(){
    Serial.begin(115200);
    delay(500);
    Serial.println("DHT11 Humedad y Temperatura\n\n");
    delay(1000);
    dht.begin();
}

void loop(){

    Serial.print("Temperatura: ");
    Serial.print(dht.readTemperature());
    Serial.println("°C");
    Serial.print("Humedad: ");
    Serial.print(dht.readHumidity());
    Serial.print("%");
    Serial.println("\n");
    delay(2000);
}
