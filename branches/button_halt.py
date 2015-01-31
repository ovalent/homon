#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#Script that will stop the raspberry pi when a push button is pressed.
#push button has to be plugged to one free GPIO ground and an free GPIO channel.
#script has to be launched at startup from /etc/rc.local the with following command:
#"python /home/pi/scripts/halt.py &"

import RPi.GPIO as GPIO
import os
import time
from lcd_display import LCD_display

GPIO.setmode(GPIO.BOARD)
# GPIO21 set up as input on pin 40. It is pulled up to stop false signals 
GPIO_chanel = 40

#It is pulled up to stop false signals 
GPIO.setup(GPIO_chanel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    


    #wait for event (press switch)
    GPIO.wait_for_edge(GPIO_chanel, GPIO.FALLING)

    # stop run2.py process
    os.system("pkill -f run2.py")
    time.sleep(1)
    # display a message on the LCD screen  
    display_lcd = LCD_display()
    display_lcd.initialisation()
    display_lcd.lcd.message("System is shutting\ndown...\nDo not unplug until\ngreen light is off.")
    time.sleep(1)
    # finally halt the system
    os.system("sudo shutdown -h now")
except KeyboardInterrupt:  
  GPIO.cleanup(GPIO_chanel) # clean up GPIO on CTRL+C exit 
  
GPIO.cleanup(GPIO_chanel)   # clean up GPIO on normal exit  
