"""
.. module:: sensor_fsr/v2
   : platform:
   : synopsis:

.. moduleauthor:: @anchitsh96

"""
import time
import Adafruit_ADS1x15
import Adafruit_GPIO.I2C as I2C
#from reride import client


def map(x, min1, max1, min2, max2):
    steps = (x/(max1-min1))
    buf = steps*(max2-min2) + min2
    return buf
def average(data):
    sum = 0
    for i in data:
        sum +=i
    return round(sum/len(data),4)
GAIN = 16
adc = Adafruit_ADS1x15.ADS1115(0x48, busnum=0)
print(adc)
#adc1 = Adafruit_ADS1x15.ADS1115(0x49, busnum=1)

#for i in range(CHANNELS_CONNECTED):
value[0] = adc.read_adc(0, gain=GAIN)

    #for s in range(SAMPLE):
        #for i in range(CHANNELS_CONNECTED):
buf = adc.read_adc(0, gain=GAIN) - value[0]
print (buf)
