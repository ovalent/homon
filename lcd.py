#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCD')
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_MCP230xx')
#sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_I2C')
from Adafruit_CharLCD import Adafruit_CharLCD
from Adafruit_MCP230xx import MCP230XX_GPIO

mcp = MCP230XX_GPIO(1, 0x20, 8)
lcd = Adafruit_CharLCD(pin_rs=1, pin_e=2, pins_db=[3,4,5,6], GPIO=mcp)

lcd.clear()

lcd.message("Adafruit 20x4\n Standard LCD")


