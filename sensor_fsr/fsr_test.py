import sys
sys.path.append("..")

from reride import fsr

# read 10 values
for i in range(10):
    data = fsr.read_fsr(delay=0.3)
    print(data)
