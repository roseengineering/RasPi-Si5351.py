# RasPi-Si5351.py

A python2 library for setting the frequency of a Si5351 off the Raspberry Pi's I2C bus.

## Introduction

This library is derived from Adafruit's si5351 library code at https://github.com/adafruit/Adafruit_Si5351_Library

The library requires python2 at the moment.  Since the Adafruit_I2C.py library depends on python-smbus and this code uses that library, make sure you have the python2 package python-smbus installed:

$ sudo apt-get install python-smbus

Example python2 code:

```
from Si5351 import Si5351

si = Si5351()

print "Set Output #0 to 13.703704 MHz"  

# vco = 25 MHz * (24 + 2 / 3) = 616.67 MHz
si.setupPLL(si.PLL_A, 24, 2, 3)

# out = 616.67 MHz / 45 = 13.703704 MHz 
si.setupMultisynth(0, si.PLL_A, 45)

# uncomment to divide 13.703704 by 64
# si.setupRdiv(0, si.R_DIV_64)

si.enableOutputs(True)
```

