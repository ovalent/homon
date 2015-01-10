#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import Adafruit_MCP9808.MCP9808 as MCP9808

class Sensor_temperature_ambiant(object):
    
    sensor_name = "Ambiant temperature"
    sensor_unit = "ºC"
    sensor_desc = "MCP9808"
    
    def __init__(self):
        self.sensor = MCP9808.MCP9808()        
        
    def start(self):
        return self.sensor.begin()
        
    def get_sensor_value(self):
        return self.sensor.readTempC()
