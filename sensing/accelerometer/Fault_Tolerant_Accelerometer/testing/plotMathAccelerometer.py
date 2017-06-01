# Author: Tony DiCola
# Modified: Jose Carlos Mayoral
# License: Public Domain
import time

import utils

# Create an ADXL345 instance.
accel = utils.MathAccelerometer(5) # seconds
#accel.plot()
accel.changeDetection()
