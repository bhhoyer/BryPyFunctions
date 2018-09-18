#!/usr/bin/python
#Author Bryan Hoyer K7UDR
#NW Digital Radio

import math

def mvolts_to_dbv(vin):
    ref = 500.0 #CODEC 3204 0dBV level
    dbv = 20 * math.log(vin/ref,10)
#    print dbv
    if dbv >= -6:
        lo = round(dbv*2)/2
        pcm = 0
    else:
        lo = -6
        pcm = round(dbv*2)/2 + 6
    return lo,pcm

print "Convert TX Level in mV RMS to LO and PCM Values in dB"
print "RMS = Vpeak/1.414, Vpeak-peak/2.828"
print

while True:
    vin = input('TX Level in mv RMS, CR to exit: ')
    rv = mvolts_to_dbv(vin)
    print "LO",rv[0]
    print "PCM",rv[1]
