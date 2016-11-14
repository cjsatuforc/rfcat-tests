
from rflib import *
import sys

def init(dev):
    dev.setMdmModulation(MOD_ASK_OOK)
    dev.setFreq(434e6)
    dev.setMdmSyncMode(0x00)
    dev.setMdmDRate(1000)
    dev.makePktFLEN(0)
    dev.setMdmNumPreamble(0)
    dev.setPktPQT(0)
    dev.setMaxPower()
    dev.setAmpMode(1)
