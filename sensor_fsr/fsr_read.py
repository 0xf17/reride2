"""
.. module:: test/fsr_test
   : platform:
   : synopsis: test and enlists all the functions of the reride/fsr library

.. moduleauthor:: @grvashu, @anchitsh96

"""

import sys
sys.path.append("..")

from reride import fsr

# # select bus/interface
#
# # read 10 values
# for i in range(10):
#     data = fsr.read_fsr(delay=0.3)
#     print(data)

# Default initialisation
f = fsr.FSR()

f.calibrate()
# Custom initialisation
#f = fsr.FSR(adc1 = [0x49,1], adc2 = [0x48,0])

#f.set_gain(16)
#f.set_mapped_range([0,1023])
#f.set_delay(0.1)
while True:
    #data=f.read_fsr_sampled(sampling_duration=0.2, samples=5)
    data=f.read_fsr(read=[0,4],mapped=False)
    print(data)
