#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import datetime
from Adafruit_CharLCD import Adafruit_CharLCD
from Adafruit_MCP230xx import MCP230XX_GPIO

class LCD_display(object):
    bus = 1         # Note you need to change the bus number to 0 if running on a revision 1 Raspberry Pi.
    address = 0x20  # I2C address of the MCP230xx chip.
    gpio_count = 8  # Number of GPIOs exposed by the MCP230xx chip, should be 8 or 16 depending on chip.

    # LCD 20x4
    num_columns = 20
    num_lines = 4
    
    def __init__(self):
        # Create MCP230xx GPIO adapter.
        mcp = MCP230XX_GPIO(self.bus, self.address, self.gpio_count)

        # Create LCD, passing in MCP GPIO adapter.
        self.lcd = Adafruit_CharLCD(pin_rs=1, pin_e=2, pin_bl=7, pins_db=[3,4,5,6], GPIO=mcp)

        self.lcd.clear()
        self.lcd.begin(self.num_columns, self.num_lines)
        self.lcd.backlightOn()
        self.lcd.setCursor(0, 0)
        self.lcd.message(datetime.datetime.now().strftime(' %a %d %b - %H:%M'))
        
    def line_message(self, row, text):
        # set the position (row from 0 to 3)
        self.lcd.setCursor(0, row)
        # display the message
        self.lcd.message(text)
    
    def temperature(self, text):
        #set the position
        self.lcd.setCursor(0, 1)
        #display the message and value
        self.lcd.message("Temperature: %.2f" % text)
        self.lcd.write4bits( 0xDF, True)
        self.lcd.message("C")
        
    def humidity(self, text):
        #set the position
        self.lcd.setCursor(0, 2)
        #display the message and value
        self.lcd.message("Humidity:   %.2f%%RH" % text)
        
    def pressure(self, text):
        #set the position
        self.lcd.setCursor(0, 3)
        #display the message and value
        self.lcd.message("Pressure: %.2fhPa" % text)
        
    def date(self):
        #set the position
        self.lcd.setCursor(0, 0)
        #display the message and value
        self.lcd.message(datetime.datetime.now().strftime(' %a %d %b - %H:%M'))

