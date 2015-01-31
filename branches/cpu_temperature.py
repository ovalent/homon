#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import subprocess
import psutil

class RPI_Data(object):  
  
    sensor_name = "CPU temperature"  
    sensor_unit = "°C"
    sensor_desc = "onboard Raspberry Pi B+"
  
    def readTemperature(self):
      #"Returns the temperature in degrees celcius"
      try:
	    s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
	    return float(s.split('=')[1][:-3])
      except:
	    return -255
	    
    def readCPU(self):
        # return CPU utilization in %
        psutil.cpu_percent(interval=0.1)
    
    def readMemory(self):
        # return (total - available) memory in %
        return psutil.virtual_memory().percent
  


