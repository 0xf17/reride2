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
SAMPLE = 20
INTERVAL = 0.005
GAINVOL = 4.096
adc = Adafruit_ADS1x15.ADS1115(0x48, busnum=0)
adc1 = Adafruit_ADS1x15.ADS1115(0x49, busnum=1)
CHANNELS_CONNECTED = 2
fsr = [0]*CHANNELS_CONNECTED
GAIN=16

CHANNELS_CONNECTED = 2
value= [0]*CHANNELS_CONNECTED

#for i in range(CHANNELS_CONNECTED):
value[0] = adc.read_adc(0, gain=GAIN)
value[1] = adc1.read_adc(0, gain=GAIN)

mean = (value[0]+value[1])/2
while True:
    values= []
    f1,f2 = [],[]
    for s in range(SAMPLE):
        #for i in range(CHANNELS_CONNECTED):
            buf = adc.read_adc(0, gain=GAIN) - mean
            mv = map(buf,-32768,32767,0,1023)
            buf1 = adc1.read_adc(0, gain=GAIN) - mean
            mv1 = map(buf1,-32768,32767,0,1023)

            #if i is 0:
            f1.append(mv)
            #else:
            f2.append(mv1)
            time.sleep(INTERVAL)
    values.append(f1)
    values.append(f2)

    for i in range(CHANNELS_CONNECTED):
        fsr[i] = round(average(values[i]),1)
    print(fsr)
    #client.send_data(fsr)
