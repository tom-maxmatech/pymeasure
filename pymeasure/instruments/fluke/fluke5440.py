#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2021 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


from pymeasure.instruments import Instrument
from pymeasure.instruments.validators import strict_discrete_set, strict_range
from pymeasure.adapters import VISAAdapter

class fluke5440(Instrument):
    """
    Represent the Fluke 5440 
    Direct Voltage Calibrator

    Implemented: BASIC
    """
    #only the most simple functions are implemented


    terminator = Instrument.control(
        "GTRM", "STRM %d",
        """This set/read termination 0= END data, 1= CR END LF, 2= END LF
        3= CR LF, 4= LF
        """,
        validator=truncated_range,
        values=[0, 4],
        cast=int
    )    

    seperator = Instrument.control(
        "GSEP", "SSEP %d",
        """This set/read seperator 0= , 1= ;
        """,
        validator=truncated_range,
        values=[0, 1],
        cast=int
    )

    source = Instrument.control(
        "GOUT", "SOUT %g",
        """Calibrator Voltage / Current in V or A)
        """,
        validator=truncated_range,
        values=[-1100, 1100]
    )    
     
    readstatus = Instrument.measurement("GSTD",
    """ read Status Code
    """
    )

    readlongstatus = Instrument.measurement("GDNG",
    """ read long Term Status Code
    """
    )

    srq = Instrument.control(
        "GSRQ", "SSRQ %g",
        """SRQ Mask set read)
        """,
        validator=truncated_range,
        values=[0, 255]
    )

    srqpoll = Instrument.measurement("GSPB",
    """ SRQ Register poll
    """
    )

    #fake idn
    idn = "fluke5440"
      
    spec =""" 
[Volt]
-0.22,       0.22,        NA, NA,  0.0005,  500e-9,  10e-9 
0.2200001,   2.2,         NA, NA,  0.00045, 1e-6,    100e-9
-2.2,        -0.2200001,  NA, NA,  0.00045, 1e-6,    100e-9
2.200001,    10.999999,   NA, NA,  0.0002,  5e-6,    1e-6
-10.999999,  -2.200001,   NA, NA,  0.0002,  5e-6,    1e-6
11,          22,          NA, NA,  0.0002,  8e-6,    1e-6
-22,         -11,         NA, NA,  0.0002,  8e-6,    1e-6
2.00001,     275,         NA, NA,  0.00035, 100e-6,  10e-6
-275,        -22.00001,   NA, NA,  0.00035, 100e-6,  10e-6
275.001,     1100,        NA, NA,  0.00035, 400e-6,  100e-6
-1100,       -275.001,    NA, NA,  0.00035, 400e-6,  100e-6
    
    """
    

    
    def __init__(self, adapter, **kwargs):
        super(fluke5440, self).__init__(
            adapter, "fluke5440", **kwargs
        )

    def reset(self):
        self.write("RESET")

    def current(self):
        self.write("BSTC")

    def voltageB(self):
        self.write("BSTV")

    def normal(self):
        self.write("BSTO")    

    def oper(self):
        self.write("OPER")      

    def stby(self):
        self.write("STBY")   

    def sense_ext(self):
        self.write("ESNS") 

    def sense_int(self):
        self.write("ISNS")      

    def guard_ext(self):
        self.write("EGRD")                       

    def guard_int(self):
        self.write("IGRD")

    def div_on(self):
        self.write("DIVY")

    def div_off(self):
        self.write("DIVN")        

    def cal_int(self):
        self.write("CALI") 

    def set_reference(self):
        self.write("SREF")         

    def test(self):
        self.write("TSTA") 

    def testdigital(self):
        self.write("TSTD") 

    def test_hv(self):
        self.write("TSTH") 


