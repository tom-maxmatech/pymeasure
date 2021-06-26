#from pymeasure.instruments.keithley import Keithley179A
from pymeasure.adapters import VISAAdapter

adapter = VISAAdapter('TCPIP0::192.168.123.104::1234::SOCKET')