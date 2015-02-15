#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from lcd_display import LCD_display

# GPIO21 set up as input on pin 38. It is pulled up to stop false signals 
# use for switch on-off LCD backlight
GPIO_CHANEL = 38
# set the mode with pin number (1 to 40), here 38
GPIO.setmode(GPIO.BOARD)
# It is pulled up to stop false signals 
GPIO.setup(GPIO_CHANEL, GPIO.IN, pull_up_down=GPIO.PUD_UP)


light_status = "on"
prev_input_state = 1

try:
    display_lcd = LCD_display(init=False)
    while True:
        # check if switch button 38 is pressed
        input_state = GPIO.input(GPIO_CHANEL)
        if ((not prev_input_state) and input_state):            
            print("* Button Pressed *")
            # button pressed: switch the LCD backlight on/off
            
            if light_status == "on":
                display_lcd.lcd.backlightOff()
                light_status = "off"
            else:
                display_lcd.lcd.backlightOn()
                light_status = "on"
            
        prev_input_state = input_state
        time.sleep(0.1)
        
except KeyboardInterrupt:  
  GPIO.cleanup(GPIO_CHANEL) # clean up GPIO on CTRL+C exit 
  
GPIO.cleanup(GPIO_CHANEL)   # clean up GPIO on normal exit  
