#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

'''
************************************************************
Sensor drivers from SyntroPython:
Check out https://github.com/richards-tech/SyntroPython for more details and installation instructions.
Note: in place of:
"sudo apt-get git build-essential qt4-default python-dev"
use this command:
"sudo apt-get install git build-essential qt4-dev-tools python-dev"
Thank you to www.richards-tech.com
************************************************************
'''

import sys
from optparse import OptionParser

# import LCD class
from lcd_display import LCD_display

# Now import what we need
import time
import datetime

# import the sensor drivers
sys.path.append('/home/pi/SyntroNet/SyntroPython/SensorDrivers')
import RT_TSL2561
import RT_BMP180
import RT_MCP9808
import RT_HTU21D
import RT_NullSensor

# the sensor update interval (in seconds). Change as required.
SENSOR_UPDATE_INTERVAL = 5

# The set of sensors. Choose which ones are required or use NullSensor if no physical sensor
# Multi sensor objects (such as BMP180 for temp and pressure) can be reused
#s_dummy = RT_DUMMY.RT_NullSensor()
s_light = RT_TSL2561.RT_TSL2561()
s_temperature = RT_MCP9808.RT_MCP9808()
s_pressure = RT_BMP180.RT_BMP180()
s_humidity = RT_HTU21D.RT_HTU21D()



'''
------------------------------------------------------------
    Sensor functions
'''

# global
# options
options = 0
args = 0
# to maintain last sensor read time
lastSensorReadTime = time.time()

def initSensors():
    s_light.enable()
    s_temperature.enable()
    s_pressure.enable()
    s_humidity.enable()

def readSensors():
    global lastSensorReadTime
    global options
    global args
    
    if ((time.time() - lastSensorReadTime) < SENSOR_UPDATE_INTERVAL):
        # call background loops
        s_light.background()
        s_temperature.background()
        s_pressure.background()
        s_humidity.background()
        return
        
    # time send send the sensor readings    
    lastSensorReadTime = time.time()
    
   
    print_verbose(datetime.datetime.now().isoformat())    
    if s_light.getDataValid():
        lightData = s_light.readLight()
        print_verbose("Light: %.2f lux" % lightData)
    if s_temperature.getDataValid():
        temperatureData = s_temperature.readTemperature()
        #display_lcd.temperature(temperatureData)
        print_verbose("Temperature: %.2f°C" % temperatureData)
    if s_humidity.getDataValid():
        humidityData = s_humidity.readHumidity()
        #display_lcd.humidity(humidityData)
        print_verbose("Humidity: %.2f%%RH" % humidityData)    
    if s_pressure.getDataValid():
        pressureData = s_pressure.readPressure()
        #display_lcd.pressure(pressureData)
        print_verbose("Pressure: %.2fhPa" % pressureData)        
    

'''
------------------------------------------------------------
    tools functions
'''
def print_verbose(msg):
    global options
    if options.verbose is True:
        print(msg)


'''
------------------------------------------------------------
    Main loop function
'''

def mLoop():
    ''' This is the main loop. '''

    while True:
        # update the date on lcd
        display_lcd.date()
        
        # see if anything from the sensors
        readSensors()
            
        # give other things a chance
        time.sleep(0.02)

'''
------------------------------------------------------------
    Main code
'''

if __name__ == '__main__':
   
    #get parameters
    parser = OptionParser()
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", 
                        help="display sensors values in terminal")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose", 
                        help="does not display anything in terminal [default]")
    parser.set_defaults(verbose=False)
    (options, args) = parser.parse_args()
        
    try:
        display_lcd = LCD_display()
        display_lcd.date()
        display_lcd.line_message(2, "   Initializing...")
        initSensors()
        mLoop()
    finally:
        display_lcd.initialisation()
        display_lcd.line_message(2, "      Stopped")
        time.sleep(3)
        display_lcd.lcd.backlightOff()
        
    


