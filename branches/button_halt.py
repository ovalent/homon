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

# GPIO21 set up as input on pin 40. It is pulled up to stop false signals 
GPIO_CHANEL = 40

# set the time (in seconds) the button has to be pressed before shutdown runs
WAIT_FOR = 5 

# set the mode with pin number (1 to 40)
GPIO.setmode(GPIO.BOARD)

# It is pulled up to stop false signals 
GPIO.setup(GPIO_CHANEL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    buttonReleased = True
    while buttonReleased:
        #wait for event (press switch)
        GPIO.wait_for_edge(GPIO_CHANEL, GPIO.FALLING)
        # button has been pressed
        buttonReleased = False
        # wait loop set with WAIT_FOR seconds         
        for i in range(WAIT_FOR * 10):
            time.sleep(0.1)
            if GPIO.input(GPIO_CHANEL):
                buttonReleased = True
                break

    # stop run2.py process
    os.system("pkill -f run2.py")
    time.sleep(1)
    
    # display a message on the LCD screen  
    display_lcd = LCD_display()
    display_lcd.initialisation()
    display_lcd.lcd.message("System is shutting\ndown...\nDo not unplug until\ngreen light is off.")
    time.sleep(1)
    
    # finally halt the system
    os.system("sudo shutdown -h now \"Halted by pressing button.\"")
    
except KeyboardInterrupt:  
  GPIO.cleanup(GPIO_CHANEL) # clean up GPIO on CTRL+C exit 
  
GPIO.cleanup(GPIO_CHANEL)   # clean up GPIO on normal exit  
