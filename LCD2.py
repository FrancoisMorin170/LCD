#ALIMENTER LE LCD EN 5V ! Pour etre lisible

from upm import pyupm_i2clcd as lcd
import mraa
import time
import sys
import string

myLCD = lcd.Jhd1313m1(0, 0x3E, 0x62)

while 1:
	
	myLCD.setColor(255, 0, 255)
	myLCD.clear()
	myLCD.setCursor(1, 2)
	myLCD.write('world')
	time.sleep(3)
