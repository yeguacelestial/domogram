#include <DHT.h>
#include <Servo.h>

#define pinDHT A0
#define DHTtype DHT11

//OBJETOS SERVOMOTORES
Servo servoDerecha;
Servo servoIzquierda;

int pos = 0;

//OBJETO DHT
DHT dht(pinDHT, DHTtype);

//Pines SERVOMOTORES
const int pinServoDer = 8;
const int pinServoIzq = 9;

//Leds
const int led1 = 2;
const int led2 = 3;
const int led3 = 4;
const int led4 = 5;
const int led5 = 6;
const int led6 = 7;

String estado_led1;
String estado_led2;
String estado_led3;
String estado_led4;
String estado_led5;
String estado_led6;


//Sensor de distancia
const int EchoPin = 10;
const int TriggerPin = 11;
float distancia;
long tiempo;


//Valor recibido desde Python
unsigned int dato;

void setup(){
        Serial.begin(115200);
        pinMode(led1, OUTPUT);
        pinMode(led2, OUTPUT);
        pinMode(led3, OUTPUT);
        pinMode(led4, OUTPUT);
        pinMode(led5, OUTPUT);
        pinMode(led6, OUTPUT);
        pinMode(TriggerPin, OUTPUT);
        pinMode(EchoPin, INPUT);
        digitalWrite(TriggerPin, LOW);
        dht.begin();
        servoDerecha.attach(pinServoDer);
        servoIzquierda.attach(pinServoIzq);

        //POS INICIAL SERVOMOTORES
            //SERVO DERECHA 
            servoDerecha.write(0);
            //SERVO IZQUIERDA 
            servoIzquierda.write(180);
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
        
        //LED4
            if (dato == 'G'){
                digitalWrite(led4, 1);
                estado_led3 = "Luz 4: encendida.";
            }

            if (dato == 'H'){
                digitalWrite(led4, 0);
                estado_led3 = "Luz 4: apagada.";
            }
         
        //LED5
            if (dato == 'J'){
                digitalWrite(led5, 1);
                estado_led3 = "Luz 5: encendida.";
            }

            if (dato == 'K'){
                digitalWrite(led5, 0);
                estado_led3 = "Luz 5: apagada.";
            }

        //LED6
            if (dato == 'L'){
                digitalWrite(led6, 1);
                estado_led3 = "Luz 6: encendida.";
            }

            if (dato == 'Z'){
                digitalWrite(led6, 0);
                estado_led3 = "Luz 6: apagada.";
            }

        //TODOS LOS LEDS
            if (dato == 'U'){
                digitalWrite(led1, 1);
                digitalWrite(led2, 1);
                digitalWrite(led3, 1);
                digitalWrite(led4, 1);
                digitalWrite(led5, 1);
                digitalWrite(led6, 1);

                estado_led1 = "Luz 1: encendida.";
                estado_led2 = "Luz 2: encendida.";
                estado_led3 = "Luz 3: encendida.";
                estado_led4 = "Luz 4: encendida.";
                estado_led5 = "Luz 5: encendida.";
                estado_led6 = "Luz 6: encendida.";
            }

            if (dato == 'I'){
                digitalWrite(led1, 0);
                digitalWrite(led2, 0);
                digitalWrite(led3, 0);
                digitalWrite(led4, 0);
                digitalWrite(led5, 0);
                digitalWrite(led6, 0);
                
                estado_led1 = "Luz 1: apagada.";
                estado_led2 = "Luz 2: apagada.";
                estado_led3 = "Luz 3: apagada.";
                estado_led4 = "Luz 4: apagada.";
                estado_led5 = "Luz 5: apagada.";
                estado_led6 = "Luz 6: apagada.";
            }

        //TEMPERATURA Y HUMEDAD
            if (dato=='O'){
                Serial.println(dht.readTemperature() + String("°C"));
            }

            if (dato=='X'){
                Serial.println(dht.readHumidity() + String("%"));
            }

        //MOVIMIENTO
            if (dato=='V'){
                Serial.println(distancia);
            }

        //SERVOMOTORES
            //ABRIR LA CASA
            if (dato=='A'){
                for (pos = 0; pos <= 90; pos++){
                    servoIzquierda.write(180-pos);
                    servoDerecha.write(pos);
                    delay(50);
                }
            }

            //CERRAR LA CASA
            if(dato=='S'){
                for (pos = 0; pos <= 90; pos++){
                    servoIzquierda.write(90+pos);
                    servoDerecha.write(90-pos);
                    delay(50);
                }
            }

        //REPORTE GENERAL (POLIMORFISMO)
            if (dato=='P'){
                Serial.println(String ("Temperatura: ")
                +int(dht.readTemperature())
                +String("°C")
                +String("Humedad: ")
                +int(dht.readHumidity())
                +String("%, ")
                +String("Movimiento a la distancia de: ")
                +float(distancia)
                +String(", ")
                +String(estado_led1 + ", " + estado_led2 + ", " + estado_led3));
            }
    }

    //SENSOR DE DISTANCIA 
    digitalWrite(TriggerPin, 1);
    delay(10);
    digitalWrite(TriggerPin, 0);

    tiempo = pulseIn(EchoPin, HIGH);
    distancia = tiempo/59;
    
    delay (1000);
}
