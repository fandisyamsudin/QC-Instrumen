#include "HX711.h"
#include <LiquidCrystal_PCF8574.h>
 
LiquidCrystal_PCF8574 lcd(0x27);
 
HX711 scale;
 
float kalibrasi_faktor = -375;
float benda;
float berat;
 
void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2); 
  lcd.setBacklight(255);
  lcd.setCursor(0,0);
  lcd.print("Timbangan digital");
  lcd.setCursor(0,1);
  lcd.print("ala nyebarilmu.com");
  delay(2000);
  scale.set_scale(kalibrasi_faktor);
  scale.tare();
  Serial.println("Baca berat :");
  lcd.clear();
}
 
void loop()
{
  lcd.setCursor(0,0);
  lcd.print("Berat benda :");
  benda = scale.get_units(),10;
  if (benda < 0) //jika benda terbaca kurang dari nol maka tertampil 0.00 gr
  {
    benda = 0.00;
  }
  berat = benda * 0.035274;
  lcd.print(berat);
  lcd.print(" gram");
  delay(1000);
}
