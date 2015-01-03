#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from cpu_temperature import Sensor_temperature_cpu
import time
import datetime

class Welcome(object):
    def __init__(self):
        print "Welcome to Homon!"        


if __name__ == '__main__':
  Welcome()
  
  s_temp_cpu = Sensor_temperature_cpu()
  while 1:  
    
    #get CPU sensor value
    var_cpu_temp = s_temp_cpu.get_sensor_value()
    print datetime.datetime.now().isoformat() + " - " + s_temp_cpu.sensor_name + ": " + str(var_cpu_temp) + " " + s_temp_cpu.sensor_unit

    time.sleep(2)

