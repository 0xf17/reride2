"""
.. module:: sensor_fsr/fsr_rpizero_ads1115
   : platform:
   : synopsis:

.. moduleauthor:: @anchitsh96

"""

import time
import Adafruit_ADS1x15
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

SAMPLE = 10
INTERVAL = 0.005
GAINVOL = 4.096
CHANNELS_CONNECTED = 2
adc = Adafruit_ADS1x15.ADS1115(0x48,busnum=0)
CHANNELS_CONNECTED = 4
fsr = [0]*CHANNELS_CONNECTED
GAIN=16
value= [0]*CHANNELS_CONNECTED

for i in range(CHANNELS_CONNECTED):
    value[i] = adc.read_adc(i, gain=GAIN)
mean = (value[0]+value[1]+value[2]+value[3])/4
while True:
    values= []
    f1,f2,f3,f4 = [],[],[],[]
    for s in range(SAMPLE):
        for i in range(CHANNELS_CONNECTED):
            buf = adc.read_adc(i, gain=GAIN) - mean
            mv = round(map(buf,-32768,32767,0,8192),0)

            if i is 0:
                f1.append(mv)
            elif i is 1:
                f2.append(mv)
            elif i is 2:
                f3.append(mv)
            else:
                f4.append(mv)
            time.sleep(INTERVAL)
    values.append(f1)
    values.append(f2)
    values.append(f3)
    values.append(f4)

    for i in range(CHANNELS_CONNECTED):
        fsr[i] = round(average(values[i]),0)
    print(fsr)
    #client.send_data(fsr)
