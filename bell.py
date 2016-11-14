#!/usr/local/bin/python

from yardstick import *

b = RfCat(0)
init(b)

b.setMdmDRate(5649)
b.setFreq(433842000)
b.setAmpMode(0)



b.RFxmit("\x88\x8e\x8e\x88\x8e\x8e\x8e\x8e\x88\xee\x88\x88\x80\x00\x00"*4)


b.setModeIDLE()
