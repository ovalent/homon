#!/usr/bin/python
import time
from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()
lcd.clear()
lcd.backlightOn()
lcd.begin(16,4)
lcd.setCursor(0,0)
lcd.message(datetime.now().strftime('%b %d  %H:%M\n'))
lcd.setCursor(0,1)
lcd.message('hello')
