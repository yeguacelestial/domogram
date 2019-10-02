int led = 11;

unsigned int dato;

void setup(){
    Serial.begin(115200);
    pinMode(led, OUTPUT);
}

void loop(){
    digitalWrite(led, HIGH);
    Serial.println("El led está encendido.");
    delay(1000);
    digitalWrite(led, LOW);
    Serial.println("El led está apagado.");
    delay (1000);
}