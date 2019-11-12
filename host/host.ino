#include <DHT.h>

#define pinDHT 3
#define DHTtype DHT11

//OBJETO DHT
DHT dht(pinDHT, DHTtype);

//Leds
const int led1 = 11;
const int led2 = 2;
const int led3 = 13;
const int led_mov = 10;

String estado_led1;
String estado_led2;
String estado_led3;


//Sensor de distancia
const int EchoPin = 5;
const int TriggerPin = 6;
float distancia;
long tiempo;


//Valor recibido desde Python
byte dato;

void setup(){
        Serial.begin(115200);
        pinMode(led1, OUTPUT);
        pinMode(led2, OUTPUT);
        pinMode(led3, OUTPUT);
        pinMode(TriggerPin, OUTPUT);
        pinMode(EchoPin, INPUT);
}

void loop(){
    while (Serial.available()>0){

        //Lectura
        dato = Serial.read();

        //Leds

        //LED1
            if (dato == 'Q'){
                digitalWrite(led1, 1);
                estado_led1 = "Luz 1: encendida.";
            }

            if (dato == 'W'){
                digitalWrite(led1, 0);
                estado_led1 = "Luz 1: apagada.";
            }

        //LED2
            if (dato == 'E'){
                digitalWrite(led2, 1);
                estado_led2 = "Luz 2: encendida.";
            }

            if (dato == 'R'){
                digitalWrite(led2, 0);
                estado_led2 = "Luz 2: apagada.";
            }

        //LED3
            if (dato == 'T'){
                digitalWrite(led3, 1);
                estado_led3 = "Luz 3: encendida.";
            }

            if (dato == 'Y'){
                digitalWrite(led3, 0);
                estado_led3 = "Luz 3: apagada.";
            }

        //TODOS LOS LEDS
            if (dato == 'U'){
                digitalWrite(led1, 1);
                digitalWrite(led2, 1);
                digitalWrite(led3, 1);

                estado_led1 = "Luz 1: encendida.";
                estado_led2 = "Luz 2: encendida.";
                estado_led3 = "Luz 3: encendida.";
            }

            if (dato == 'I'){
                digitalWrite(led1, 0);
                digitalWrite(led2, 0);
                digitalWrite(led3, 0);
                
                estado_led1 = "Luz 1: apagada.";
                estado_led2 = "Luz 2: apagada.";
                estado_led3 = "Luz 3: apagada.";
            }

        //TEMPERATURA Y HUMEDAD
            if (dato=='O'){
                Serial.println(int(dht.readTemperature()) + String("°C"));
            }

            if (dato=='T'){
                Serial.println(int(dht.readHumidity()) + String("%"));
            }

        //MOVIMIENTO
            if (dato=='Y'){
                Serial.println(distancia);
            }

        //REPORTE GENERAL (POLIMORFISMO)
            if (dato=='P'){
                Serial.println(String ("Temperatura: "))
                +int(dht.readTemperature())
                +String("°C, ")
                +String("Humedad: ")
                +int(dht.readHumidity())
                +String("%, ")
                +String("Movimiento a la distancia de: ")
                +float(distancia)
                +String(", ")
                +String(estado_led1 + " " + estado_led2 + " " + estado_led3);
            }
    }

    //SENSOR DE DISTANCIA 
    digitalWrite(TriggerPin, 1);
    delay(10);
    digitalWrite(TriggerPin, 0);

    tiempo = (pulseIn(EchoPin, HIGH)/2);
    distancia = float(tiempo * 0.0343);

    if (distancia <= 10){
        digitalWrite (led_mov, 1);
        estado_led3 = "Luz de movimiento: ENCENDIDA.";
    }

    else {
        digitalWrite(led_mov, 0);
        estado_led3 = "Luz de movimiento: APAGADA.";
    }
    
    delay (1000);
}
