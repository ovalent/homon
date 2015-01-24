#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys

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

light = RT_TSL2561.RT_TSL2561()
temperature = RT_MCP9808.RT_MCP9808()
pressure = RT_BMP180.RT_BMP180()
humidity = RT_HTU21D.RT_HTU21D()

# Now import what we need

#import SyntroPython
#import SyntroPythonPy
import time
import datetime


    
'''
------------------------------------------------------------
    Sensor functions
'''

# global to maintain last sensor read time
lastSensorReadTime = time.time() 

def initSensors():
    light.enable()
    temperature.enable()
    pressure.enable()
    humidity.enable()

def readSensors():
    global lastSensorReadTime
    
    if ((time.time() - lastSensorReadTime) < SENSOR_UPDATE_INTERVAL):
        # call background loops
        light.background()
        temperature.background()
        pressure.background()
        humidity.background()
        return
        
    # time send send the sensor readings    
    lastSensorReadTime = time.time()
    
   
    print(datetime.datetime.now().isoformat())
    
    if light.getDataValid():
        lightData = light.readLight()
        print("Light: %.2f lux" % lightData)
    if temperature.getDataValid():
        temperatureData = temperature.readTemperature()
        print("Temperature: %.2fC" % temperatureData)
    if pressure.getDataValid():
        pressureData = pressure.readPressure()
        print("Pressure: %.2fhPa" % pressureData)        
    if humidity.getDataValid():
        humidityData = humidity.readHumidity()
        print("Humidity: %.2f%%RH" % humidityData)    




'''
------------------------------------------------------------
    pi camera functions and main loop
'''

def mLoop():
    ''' This is the main loop. '''

    while True:
        # see if anything from the sensors
        readSensors()
            
        # give other things a chance
        time.sleep(0.02)

'''
------------------------------------------------------------
    Main code
'''

initSensors()
mLoop()


