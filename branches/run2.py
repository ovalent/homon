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

# import a class to get rapsberry pi values (CPU temp, CPU load, Mem)
from cpu_temperature import RPI_Data

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
# data upload interval (in seconds). Change as required.
DATA_UPLOAD_INTERVAL = 60

# The set of sensors. Choose which ones are required or use NullSensor if no physical sensor
# Multi sensor objects (such as BMP180 for temp and pressure) can be reused
#s_dummy = RT_DUMMY.RT_NullSensor()
s_light = RT_TSL2561.RT_TSL2561()
s_temperature = RT_MCP9808.RT_MCP9808()
s_pressure = RT_BMP180.RT_BMP180()
s_humidity = RT_HTU21D.RT_HTU21D()

# Raspberry Pi Data class (cpu temperature, CPU load, memory)
s_rpi = RPI_Data()


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
        
    # time send the sensor readings    
    lastSensorReadTime = time.time()
    
    print_verbose("-------------------------------------------------")    
    #print_verbose(datetime.datetime.now().isoformat()) 
    print_verbose(datetime.datetime.fromtimestamp(lastSensorReadTime).strftime('%Y-%m-%d %H:%M:%S'))   
    print_verbose("--------------------------") 
    # light sensor TSL2561
    if s_light.getDataValid():
        lightData = s_light.readLight()
        print_verbose("TSL2561 Light: %.2f lux" % lightData)
    # temperature sensor MCP9808
    if s_temperature.getDataValid():
        temperatureData = s_temperature.readTemperature()
        #display_lcd.temperature(temperatureData)
        print_verbose("MCP9808 Temperature: %.2f°C" % temperatureData)
    # humidity sensor HTU21D    
    if s_humidity.getDataValid():
        humidityData = s_humidity.readHumidity()
        humidityTemperatureData = s_humidity.readTemperature()
        #display_lcd.humidity(humidityData)
        print_verbose("HTU21D Humidity: %.2f%%RH" % humidityData)  
        print_verbose("HTU21D Temperature: %.2f°C" % humidityTemperatureData)    
    # pressure sensor BMP180
    if s_pressure.getDataValid():
        pressureData = s_pressure.readPressure()
        pressureTemperatureData = s_pressure.readTemperature()
        #display_lcd.pressure(pressureData)
        print_verbose("BMP180 Pressure: %.2fhPa" % pressureData)
        print_verbose("BMP180 Temperature: %.2f°C" % pressureTemperatureData)    
    # raspberry pi CPU temperature
    rpiTempetatureData = s_rpi.readTemperature()
    print_verbose("RPI Temperature: %.2f°C" % rpiTempetatureData)  
    
    # build string to display to LCD
    lcd_string = " " + datetime.datetime.now().strftime(' %a %d %b - %H:%M') + "\n"
    lcd_string = lcd_string + "Temperature: %.2f" % temperatureData + chr(223) + "C" + "\n" # chr(223) stand to replace degree "°" symbol
    lcd_string = lcd_string + "Humidity:   %.2f%%RH" % humidityData + "\n"
    lcd_string = lcd_string + "Pressure: %.2fhPa" % pressureData
    # display it on LCD  
    display_lcd.lcd.message(lcd_string)
    

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
    
    print_verbose("Initializing...")
    
    while True:        
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
    
    display_lcd = LCD_display()    
    try:        
        display_lcd.date()
        display_lcd.line_message(2, "   Initializing...")
        initSensors()
        mLoop()
    finally:
        display_lcd.initialisation()
        display_lcd.line_message(2, "      Stopped")
        time.sleep(3)
        display_lcd.lcd.backlightOff()
        
    


