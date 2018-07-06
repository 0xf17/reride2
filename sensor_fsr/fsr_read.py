"""
.. module:: sensor_fsr/fsr_read
   : platform:
   : synopsis: test and enlists all the functions of the reride/fsr library

.. moduleauthor:: @anchitsh96

"""

import sys
sys.path.append("..")

from reride import fsr

# Default initialisation

f = fsr.FSR(adc1=[0x48,0])
f.set_delay(0.8)
#f.calibrate()

while True:
    data=f.read_fsr(read=[0,1,2,3],mapped=False,cancel_noise=True)
    print(data)
