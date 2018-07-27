"""
.. module:: reride/fsr
   : platform:
   : synopsis:

.. moduleauthor:: @anchitsh96, @grvashu

"""

import time
import Adafruit_ADS1x15
import Adafruit_GPIO.I2C as I2C

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
        self.raw_range = [0, 32767]
        self.mapped_range = [0, 1024]

    def map(self, x, min1, max1, min2, max2):
        if min1 >= self.raw_range[0] and max1 <= self.raw_range[1]:
            buf = min2 + (max2 - min2) * ((x-min1)/(max1-min1))
        else:
            buf = 0
        return buf

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

    def read_fsr(self, mapped=True, read=[0,1,2,3,4,5,6,7], cancel_noise=True):
        fsr = []
        zero = []
        if mapped == True:
            out_range = self.mapped_range
        else:
            out_range = self.raw_range

        #print(out_range)

        # update noise based on out range
        if cancel_noise == True:
            for i in range(8):
                zero.append(self.map(self.zero[i],self.raw_range[0],self.raw_range[1], out_range[0],out_range[1]))

        else:
            for i in range(8):
                zero.append(0)

        for i in range(4):
            if i in read:
                buf = 0
                try:
                    buf = self.adc[0].read_adc(i, gain=self.gain)
                except OSError as err:
                    print('Read Error: '+str(err))
                temp = self.map(buf, self.raw_range[0], self.raw_range[1], out_range[0], out_range[1]) - zero[i]
                # if temp>out_range[1] or temp<out_range[0]:
                #     print('error')
                fsr.append(int(temp))
        for i in range(4):
            if (4+i) in read:
                buf = 0
                try:
                    buf = self.adc[1].read_adc(i, gain=self.gain)
                except OSError as err:
                    print('Read Error: '+str(err))
                temp = self.map(buf, self.raw_range[0], self.raw_range[1], out_range[0], out_range[1]) - zero[4+i]
                # if temp>out_range[1] or temp<out_range[0]:
                #     print('error')
                fsr.append(int(temp))
        time.sleep(self.delay)

        return fsr

    def calibrate(self):
        time.sleep(1)   # wait for sometime before calibrating
        self.zero = self.read_fsr(mapped=False, read=[0,1,2,3], cancel_noise=False)

    def read_fsr_sampled(self, sampling_duration = 0.005, samples = 20, mapped=True, read=[0,1,2,3,4,5,6,7]):
        fsr_sampled = [0]*8

        for i in range(samples):
            fsr = self.read_fsr(self, mapped=mapped, read=read)
            fsr_sampled[i] = (fsr_sampled[i] + fsr[i])/2
            time.sleep(sampling_duration)

        return fsr_sampled
