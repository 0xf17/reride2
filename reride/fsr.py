"""
.. module:: reride/fsr
   : platform:
   : synopsis:

.. moduleauthor:: @anchitsh96, @grvashu

"""

import time
import Adafruit_ADS1x15
import Adafruit_GPIO.I2C as I2C

def map(x, min1, max1, min2, max2):
    steps = (x/(max1-min1))
    buf = steps*(max2-min2) + min2
    return buf

class FSR:

    def __init__(self, adc1 = [0x48,0], adc2 = [0x49,1]):
        """ initialise the ADC and create FSR object

            interfaces the RPi to ADC

            Args:
                self : address of the FSR object (implicit)
                adc1 ([hex,int]): Address of ADC1 (Configuration register, Bus Number)
                adc2 ([hex,int]): Address of ADC2 (Configuration register, Bus Number)

            Returns:
                None

            Raises:
                None
        """
        self.adc = []
        self.adc.append(Adafruit_ADS1x15.ADS1115(adc1[0], busnum=adc1[1]))
        self.adc.append(Adafruit_ADS1x15.ADS1115(adc2[0], busnum=adc2[1]))

        self.gain = 16
        self.gain_vol = 4.096

        self.delay = 0.5

        self.zero = [0]*8

        # default adc minimum output of 16Bit
        self.raw_range = [-32768, 32767]
        self.mapped_range = [0, 1023]

    def set_gain(self, new_gain):
        """ change the default gain

            assign new gain to gain attribute

            Args:
                self : address of the FSR object (implicit)
                new_gain (int) : new gain value

            Returns:
                None

            Raises:
                None
        """
        self.gain = new_gain

    def set_mapped_range(self, new_range):
        """ change the default output range

            assign new output range to existing range

            Args:
                self : address of the FSR object (implicit)
                new_range ([int,int]) : new range

            Returns:
                None

            Raises:
                None
        """
        self.mapped_range = new_range

    def set_delay(self, new_delay):
        """ change the default delay

            assign new delay

            Args:
                self : address of the FSR object (implicit)
                new_delay (int) : new delay in microseconds

            Returns:
                None

            Raises:
                None
        """
        self.delay = new_delay

    def read_fsr(self, mapped=True, read=[0,1,2,3,4,5,6,7]):
        fsr = []
        for i in range(4):
            if i in read:
                buf = self.adc[0].read_adc(i, gain=self.gain)
                if mapped is True:
                    temp = map(buf, self.raw_range[0], self.raw_range[1], self.mapped_range[0], self.mapped_range[1])-self.zero[i]
                    fsr.append(int(temp))
                else:
                    fsr.append(buf)
        for i in range(4):
            if (4+i) in read:
                buf = self.adc[1].read_adc(i, gain=self.gain)
                if mapped is True:
                    temp = map(buf, self.raw_range[0], self.raw_range[1], self.mapped_range[0], self.mapped_range[1])-self.zero[4+i]
                    fsr.append(int(temp))
                else:
                    fsr.append(buf)
        time.sleep(self.delay)

        return fsr

    def calibrate(self, is_mapped=True):
        self.zero = self.read_fsr(mapped=is_mapped)

    def read_fsr_sampled(self, sampling_duration = 0.1, samples = 10, mapped=True, read=[0,1,2,3,4,5,6,7]):
        fsr_sampled = [0]*8

        for i in samples:
            fsr = self.read_fsr(self, mapped=mapped, read=read)
            fsr_sampled[i] = (fsr_sampled[i] + fsr[i])/2
            time.sleep(sampling_duration)

        return fsr_sampled
