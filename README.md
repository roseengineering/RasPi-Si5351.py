RasPi-Si5351.py
================

Python library for setting the frequency of a Si5351 off the Raspberry Pi's I2C bus.

Library derived from code at https://github.com/adafruit/Adafruit_Si5351_Library

Make sure you have installed python3-smbus:

$ sudo apt-get install python3-smbus

Example code:

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

