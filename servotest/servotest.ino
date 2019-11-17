#include <Servo.h>
Servo myservo1;
Servo myservo2;
int pos = 0;

void setup() {
  myservo1.attach(9);
  myservo2.attach(8);
}

void loop() {
  for (pos = 0; pos <= 180; pos++){
    myservo1.write(pos);
    myservo2.write(pos);
    delay(50);
  }

  for (pos = 180; pos >= 0; pos--){
    myservo1.write(pos);
    myservo2.write(pos);
    delay(50);
  }

}
