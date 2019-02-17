#include "dht.h"
#define dht_apin A5 // Analog pin humidity/temp sensor is plugged into
#define moistPin A0 // pin that moisture sensor is plugged into
 
dht DHT;

 
void setup(){
 
  Serial.begin(9600);
  delay(1000);//Wait before accessing Sensor
 
}//end "setup()"
 
void loop(){
  
  int sensorValue = analogRead(moistPin);
  DHT.read11(dht_apin);
  
  Serial.print("m");
  Serial.println(sensorValue);
  Serial.print("h");
  Serial.println(DHT.humidity);
  Serial.print("t");
  Serial.println(DHT.temperature); 
    
    delay(5000);//Wait 5 seconds before accessing sensor again.
 
  //Fastest should be once every two seconds.
 
}// end loop() 

