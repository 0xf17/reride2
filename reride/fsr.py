"""
.. module:: reride/fsr
   : platform:
   : synopsis:

.. moduleauthor:: @anchitsh96, @grvashu

"""

import time
import Adafruit_ADS1x15
import Adafruit_GPIO.I2C as I2C

GAINVOL = 4.096
GAIN=16

adc = []
adc.append(Adafruit_ADS1x15.ADS1115(0x48, busnum=0))
adc.append(Adafruit_ADS1x15.ADS1115(0x49, busnum=1))

def map(x, min1, max1, min2, max2):
    steps = (x/(max1-min1))
    buf = steps*(max2-min2) + min2
    return buf

def read_fsr(delay=0.5):
    fsr = []*8
    for i in range(4):
        buf = adc[0].read_adc(i, gain=GAIN)
        fsr[i] = map(buf, -32768, 32767, 0, 2048)
    for i in range(4):
        buf = adc[1].read_adc(i, gain=GAIN)
        fsr[4+i] = map(buf, -32768, 32767, 0, 32768)
    time.sleep(delay)
    return fsr
