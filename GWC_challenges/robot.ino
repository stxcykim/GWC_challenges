#include <Servo.h>
Servo servoLeft;
Servo servoRight;
Serial.begin(9600);


void setup() {
  // put your setup code here, to run once:
  
servoLeft.attach(12);
servoRight.attach(13);
pinMode(13,OUTPUT);
pinMode(12,OUTPUT);
servoLeft.writeMicroseconds(1500);
servoRight.writeMicroseconds(1500);


}

void loop() {
  // put your main code here, to run repeatedly:

//// turn robot
//servoLeft.writeMicroseconds(10);
//servoRight.writeMicroseconds(20);
////
//delay(3000);

// robot goes straight
servoLeft.writeMicroseconds(1700);
servoRight.writeMicroseconds(1300);

delay(1000);

// robot goes straight
servoLeft.writeMicroseconds(1300);
servoRight.writeMicroseconds(1700);

delay(500);

// robot goes straight
servoLeft.writeMicroseconds(1700);
servoRight.writeMicroseconds(1300);

delay(500);

// robot goes straight
servoLeft.writeMicroseconds(1300);
servoRight.writeMicroseconds(1700);

delay(500);

servoLeft.writeMicroseconds(10);
servoRight.writeMicroseconds(20);
delay(3000);

Serial.print("Goodnight Moon");
delay(200);
Serial.println("");

////// turn robot
//servoLeft.writeMicroseconds(10);
//servoRight.writeMicroseconds(20);
//delay(3000);


// stop
//servoLeft.writeMicroseconds(1500);
//servoRight.writeMicroseconds(1500);
//
//delay(2000);
//
//// robot goes straight
//servoLeft.writeMicroseconds(1700);
//servoRight.writeMicroseconds(1300);
//
//delay(3000);
//
//// turn robot
//servoLeft.writeMicroseconds(10);
//servoRight.writeMicroseconds(20);
////
//delay(3000);


//servoLeft.writeMicroseconds(10);
//
// servoRight.writeMicroseconds(30);
//  digitalWrite(13,HIGH);
//delay(100);
//digitalWrite(13,LOW);
//delay(100);
//digitalWrite(12,HIGH);
//delay(100);
//digitalWrite(12,LOW);
//delay(100);
//
//delay(5000);
//
//servoLeft.writeMicroseconds(20);
//
// servoRight.writeMicroseconds(20);
digitalWrite(13,HIGH);
delay(100);
digitalWrite(13,LOW);
delay(100);
digitalWrite(12,HIGH);
delay(100);
digitalWrite(12,LOW);
delay(100);


}

