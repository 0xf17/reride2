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
f = fsr.FSR()

f.calibrate()

while True:
    data=f.read_fsr(read=[0,4],mapped=False)
    print(data)
