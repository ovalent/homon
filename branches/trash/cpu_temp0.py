import subprocess



def get_temperature():
    "Returns the temperature in degrees C"
    try:
        s = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"])
        return float(s.split('=')[1][:-3])
    except:
        return 0






print 'Temperature in C: ' +str(get_temperature())

