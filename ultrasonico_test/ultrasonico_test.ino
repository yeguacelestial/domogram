const int EchoPin = 2;
const int TriggerPin = 3;
float distancia;
long tiempo;


void setup(){
    Serial.begin(115200);
    pinMode(TriggerPin, OUTPUT);
    pinMode(EchoPin, INPUT);
    digitalWrite(TriggerPin, LOW);
    Serial.println("SENSOR DE MOVIMIENTO");
}

void loop(){

    long t;
    long d;
    
    digitalWrite(TriggerPin, HIGH);
    delay(10);
    digitalWrite(TriggerPin, LOW);

    t = pulseIn(EchoPin, HIGH); //Ancho de pulso
    d = t/59;

    Serial.print("Distancia: ");
    Serial.print(d);
    Serial.print("cm.\n");
    delay(500);
}
