import time
import Adafruit_ADS1x15

def map(x, min1, max1, min2, max2):
    steps = (x/(max1-min1))
    buf = steps*(max2-min2) + min2
    return buf

adc = Adafruit_ADS1x15.ADS1115()

#def calibrate(
GAIN=16

CHANNELS_CONNECTED = 2
values= [0]*CHANNELS_CONNECTED

for i in range(CHANNELS_CONNECTED):
    values[i] = adc.read_adc(i, gain=GAIN)

mean = (values[0]+values[1])/2


while True:
    for i in range(CHANNELS_CONNECTED):
        buf = adc.read_adc(i, gain=GAIN) - mean+3
        values[i] = map(buf,0,32767,0,1023)
    for i in range(CHANNELS_CONNECTED):
        print(int(values[i]),end=' ')
    print('')
    time.sleep(0.5)

