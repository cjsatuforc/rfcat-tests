#!/usr/local/bin/python

from yardstick import *

b = RfCat(0)
init(b)

b.setMdmDRate(3540)
b.setFreq(434000000)
b.setAmpMode(1)


for i in range(1,50):
	b.RFxmit("\x00\x00\x00")


b.setModeIDLE()

