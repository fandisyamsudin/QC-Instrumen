//www.nyebarilmu.com
//2020
//program kalibrasi timbangan digital dengan loadcell 5kg dan HX711
 
/*
 Tekan atau a / z untuk menyesuaikan calibration_factor hingga bacaan keluaran sesuai dengan berat yang diketahui
 Arduino pin 2 -> HX711 CLK
 Arduino pin 3 -> HX711 DOUT
*/
 
#include "HX711.h"
 
HX711 scale;
 
float calibration_factor = -400; //Nilai awal perkiraan
float units;
float ounces;
 
void setup() {
 Serial.begin(9600);
 Serial.println("HX711 Kalibrasi");
 Serial.println("Jangan ada benda apapun diatas load cell"); //ini penting
 
 Serial.println("Kemudian letakan benda"); //misalnya batu baterai yang sudah diketahui beratnya
 
Serial.println("Tekan + atau a untuk meningkatkan faktor kalibrasi");
 Serial.println("Tekan - atau z untuk mengurangi faktor kalibrasi");
scale.begin(3, 2);
 scale.set_scale();
 scale.tare();
 
 long zero_factor = scale.read_average(); 
 Serial.print("Zero factor: ");
 Serial.println(zero_factor);
}
 
void loop() {
 
 scale.set_scale(calibration_factor);
 
 Serial.print("Pembacaan : ");
 units = scale.get_units(), 10;
 if (units < 0)
 {
 units = 0.00;
 }
 ounces = units * 0.035274;
 Serial.print(units);
 Serial.print(" grams"); 
 Serial.print(" calibration_factor: ");
 Serial.print(calibration_factor);
 Serial.println();
 
 if(Serial.available())
 {
 char temp = Serial.read();
 if(temp == '+' || temp == 'a')
 calibration_factor += 1;
 else if(temp == '-' || temp == 'z')
 calibration_factor -= 1;
 }
}
