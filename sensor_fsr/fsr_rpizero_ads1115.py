import time
import Adafruit_ADS1x15
from reride import client

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
CHANNELS_CONNECTED = 2
adc = Adafruit_ADS1x15.ADS1115()
CHANNELS_CONNECTED = 2
fsr = [0]*CHANNELS_CONNECTED
GAIN=16
value= [0]*CHANNELS_CONNECTED

for i in range(CHANNELS_CONNECTED):
value[i] = adc.read_adc(i, gain=GAIN)


mean = (value[0]+value[1])/2
while True:
    values= []
    f1,f2 = [],[]
    for s in range(SAMPLE):
        for i in range(CHANNELS_CONNECTED):
            buf = adc.read_adc(i, gain=GAIN) - mean
            mv = map(buf,0,32767,0,1023)

            if i is 0:
            f1.append(mv)
            else:
            f2.append(mv)
            time.sleep(INTERVAL)
    values.append(f1)
    values.append(f2)

    for i in range(CHANNELS_CONNECTED):
        fsr[i] = round(average(values[i]),1)
    print(fsr)
    client.send_data(fsr)
