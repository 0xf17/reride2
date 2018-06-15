"""
.. module:: test/fsr_test
   : platform:
   : synopsis: test and enlists all the functions of the reride/fsr library

.. moduleauthor:: @grvashu, @anchitsh96

"""

import sys
sys.path.append("..")

from reride import fsr

# read 10 values
for i in range(10):
    data = fsr.read_fsr(delay=0.3)
    print(data)
