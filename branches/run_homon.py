#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from cpu_temperature import Cpu_temperature
from time import sleep

class Example(object):
    def run(self):
        print "Hello, world!"
        


if __name__ == '__main__':
  Example().run()
  while 1:  
    
    #get CPU sensor value
    var_cpu_temp = Cpu_temperature().get_sensor_value()
    print Cpu_temperature().sensor_name + ": " + str(var_cpu_temp) + " " + Cpu_temperature().sensor_unit

    sleep(2)

