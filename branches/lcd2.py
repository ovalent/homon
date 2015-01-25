#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Example script to show usage of MCP230xx GPIO extender to drive character LCD.
from Adafruit_CharLCD import Adafruit_CharLCD
from Adafruit_MCP230xx import MCP230XX_GPIO

bus = 1         # Note you need to change the bus number to 0 if running on a revision 1 Raspberry Pi.
address = 0x20  # I2C address of the MCP230xx chip.
gpio_count = 8  # Number of GPIOs exposed by the MCP230xx chip, should be 8 or 16 depending on chip.

# LCD 20x4
num_columns = 20
num_lines = 4

# Create MCP230xx GPIO adapter.
mcp = MCP230XX_GPIO(bus, address, gpio_count)

# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=1, pin_e=2, pin_bl=7, pins_db=[3,4,5,6], GPIO=mcp)

lcd.clear()
lcd.begin(num_columns, num_lines)
lcd.backlightOn()
#lcd.message("  Adafruit 20x4\n  Standard LCD")
lcd.setCursor(0, 0)
lcd.message("  line 1")
lcd.setCursor(0, 1)
lcd.message("  line 2")
lcd.setCursor(0, 2)
lcd.message("  line 3")
lcd.setCursor(0, 3)
lcd.message("  line 4")

