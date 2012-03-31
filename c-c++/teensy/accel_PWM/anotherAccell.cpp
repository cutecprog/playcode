/*
   Memsic2125
   
   Read the Memsic 2125 two-axis accelerometer.  Converts the
   pulses output by the 2125 into milli-g's (1/1000 of earth's
   gravity) and prints them over the serial connection to the
   computer.
   
   The circuit:
	* X output of accelerometer to digital pin 2
	* Y output of accelerometer to digital pin 3
	* +V of accelerometer to +5V
	* GND of accelerometer to ground
  
   http://www.arduino.cc/en/Tutorial/Memsic2125
   
   created 6 Nov 2008
   by David A. Mellis
   modified 30 Jun 2009
   by Tom Igoe
   
   This example code is in the public domain.

 */

// these constants won't change:
#include "WProgram.h"
void setup();
void loop();
const int xPin = 0;		// X output of the accelerometer
const int yPin = 1;		// Y output of the accelerometer
int ledPinRight_X =	5;
int ledPinLeft_X =  6;
int ledPinForward_Y =  7;
int ledPinBackward_Y =  8;
void setup() {
  // initialize serial communications:
  Serial.begin(9600);
  // initialize the pins connected to the accelerometer
  // as inputs:
  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
  
  pinMode(ledPinRight_X, OUTPUT); 
  pinMode(ledPinLeft_X, OUTPUT);
  pinMode(ledPinForward_Y, OUTPUT); 
  pinMode(ledPinBackward_Y, OUTPUT); 
}

void loop() {
  // variables to read the pulse widths:
  int pulseX, pulseY;
  // variables to contain the resulting accelerations
  int accelerationX, accelerationY;
  
  // read pulse from x- and y-axes:
  pulseX = pulseIn(xPin,HIGH);  
  pulseY = pulseIn(yPin,HIGH);
  
  // convert the pulse width into acceleration
  // accelerationX and accelerationY are in milli-g's: 
  // earth's gravity is 1000 milli-g's, or 1g.
  accelerationX = ((pulseX / 10) - 500) * 8;
  accelerationY = ((pulseY / 10) - 500) * 8;
  if (accelerationX >= 30){
    digitalWrite(ledPinRight_X, LOW);
    digitalWrite(ledPinLeft_X, HIGH);  
  }
  else if (accelerationX <= -50){
    digitalWrite(ledPinRight_X, HIGH);
    digitalWrite(ledPinLeft_X, LOW);
  }
  else{
   digitalWrite(ledPinRight_X, LOW);
    digitalWrite(ledPinLeft_X, LOW);
  }
  
  if (accelerationY >= 30){
    digitalWrite(ledPinForward_Y, LOW);
    digitalWrite(ledPinBackward_Y, HIGH);  
  }
  else if (accelerationY <= -50){
    digitalWrite(ledPinForward_Y, HIGH);
    digitalWrite(ledPinBackward_Y, LOW);
  }
  else{
   digitalWrite(ledPinForward_Y, LOW);
    digitalWrite(ledPinBackward_Y, LOW);
  }

  // print the acceleration
  Serial.print(accelerationX);
  // print a tab character:
  Serial.print("\t");
  Serial.print(accelerationY);
  Serial.println();

  delay(100);
}

// the main function is now built into core.a and linked into the final executable
