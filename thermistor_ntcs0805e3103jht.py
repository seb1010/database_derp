import numpy as np


class ThermMath:

    def __init__(self):
        self.nominal_val=10E3 # ohms
        self.nominal_temp_c = 25.0
        self.pullup = 10E3 # ohms
        self.beta = 3940
        self.adc_bits = 10


    def convert(self, adc_code: int):
        voltage_ratio = adc_code / (( 1 << self.adc_bits) - 1)
        r_therm = self.pullup * voltage_ratio / ( 1 - voltage_ratio)
        therm_temp_c = 1 / (np.log(r_therm / self.nominal_val) / self.beta
            + 1 / (self.nominal_temp_c + 273.15)) - 273.15
        return therm_temp_c        
