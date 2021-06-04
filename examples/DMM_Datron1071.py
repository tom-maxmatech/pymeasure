from pymeasure.instruments.datron import datron1071
from pymeasure.adapters import PrologixAdapter
import time

###################################################


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

###################################################

# Adapter Prologix USB GPIB Adapter
adapter = PrologixAdapter('/dev/ttyUSB0')
#Datron on GPIB Adresse 30
dmm = datron1071(adapter.gpib(30))

#Read 'Fake' IDN
print (dmm.id)

time.sleep(1)
#set DC Voltage
dmm.mode_dcv()
#set to sw Trigger
dmm.triggermode('SW')
#Range R6 = 1000 V
dmm.rangemode('R6')
#Trigger DMM 
dmm.trigger()
time.sleep(5)
#Read DMM
print (dmm.readval(trg=True))

#set DMM internel trigger moder
dmm.triggermode('int')
#set range R1 = 100 mV
dmm.rangemode('R1')

n=0
while n !=10:
    #read dmm val only
    print (dmm.readval(trg=False)[0])
    n = n+1

      

#exit()
dummy = input("enter start Cal.")
dmm.cal_enable() 
dummy = input("wait R")
dmm.mode_ohm()
dmm.rangemode("R4")
dummy = input("4W Short, Set 4W, Enter start ZERO Cal.")
print ('Wait for EMF stab.')
countdown(120)
dmm.cal_zero()
print ('Wait for Cal ZERO')
countdown(30)
dummy = input("4W 10k Enter start Cal.")
print ('Wait for EMF stab.')
countdown(120)
dmm.cal_gain()
print ('Wait for Cal.')
countdown(30)
dummy = input("dis")
dmm.cal_diable()

###############################
