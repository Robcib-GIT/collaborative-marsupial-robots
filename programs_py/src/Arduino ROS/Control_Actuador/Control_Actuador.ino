#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Empty.h>
#include <std_msgs/Float64.h>
#include <ros/time.h>

// Pines para lectura de potenciometro control posicion angulas
const int analogInPin = A0; // Analog input pin that the potentiometer is attached to
int sensorValue = 0; // value read from the pot
float angulo_inclinacion = 0; // value output to the PWM (analog out)

// Pines control actuador placa reles
const int Rele_1 = 9;
const int Rele_2 = 10;
bool COND_1 = true;
bool COND_2 = true;
bool COND_3 = true;

// declaracion de valores de ROS
ros::NodeHandle nh;

float angulo; 
float topico_angulo = 90;

// Callback del angulo de posicion recibido
void messageCb( const std_msgs::Float64& msg){
  topico_angulo = msg.data;
  COND_1 = true;
  COND_2 = true;
}

ros::Subscriber<std_msgs::Float64> s("/angle_platform", &messageCb);

void setup() {

  nh.initNode();
  nh.subscribe(s);
  

 // initialize serial communications at 9600 bps:
 pinMode(Rele_1, OUTPUT);
 pinMode(Rele_2, OUTPUT);
 //Serial.begin(9600); 
}

void loop() {
 // read the analog in value:
 sensorValue = analogRead(analogInPin); 
 // map it to the range of the analog out:
 angulo_inclinacion = map(sensorValue, 0, 1023, 0, 255); 

// Control On Off del actuador en funcion del angulo de inclinacion

if (angulo_inclinacion > topico_angulo && COND_2)
{
digitalWrite(Rele_1, LOW);
digitalWrite(Rele_2, HIGH);
  }

  
if (angulo_inclinacion < topico_angulo && COND_1)
{
digitalWrite(Rele_1, HIGH);
digitalWrite(Rele_2, LOW);
}
  

if (angulo_inclinacion >= topico_angulo-5 &&  angulo_inclinacion <= topico_angulo+5)
{
  COND_1 = false;
  COND_2 = false;
digitalWrite(Rele_1, HIGH);
digitalWrite(Rele_2, HIGH);
  }
/*
if (angulo_inclinacion>90 && angulo_inclinacion<180)
{
digitalWrite(Rele_1, HIGH);
digitalWrite(Rele_2, HIGH);
  }


if (angulo_inclinacion>180)
{
digitalWrite(Rele_1, HIGH);
digitalWrite(Rele_2, LOW);
  }

  if (angulo_inclinacion<=90)
{
digitalWrite(Rele_1, LOW);
digitalWrite(Rele_2, HIGH);
  }
  */


 //Serial.print("\t output = "); 
 //Serial.println(angulo_inclinacion);

 angulo +=1;

 nh.spinOnce();

 //delay(2); 
}
