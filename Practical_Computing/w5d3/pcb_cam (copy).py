# Note: Python 3
# Script by: H.J. Megens
# Last modified: 02-10-2017
# Where you can reach me: hendrik-jan.megens - at - wur.nl

import time
import RPi.GPIO as io
import datetime
import picamera

# Initiate Camera object
camera=picamera.PiCamera()
previoustime=0
ts=time.time()
io.setmode(io.BCM)

# Define GPIO pin numbers
greenled_pin = 17
redled_pin = 22

# Setup the LED pins
io.setup(redled_pin, io.OUT)         # activate input
io.setup(greenled_pin, io.OUT)

# Blink Green, then Red
io.output(greenled_pin,1)         # output pin to '1' --> enabled
time.sleep(1)                     # sleep time in seconds - change as you please
io.output(redled_pin,1)           # output pin to '1' --> enabled
time.sleep(0.1)                   # time in seconds - change as you please
io.output(greenled_pin,0)         # output pin to '0' --> disabled
time.sleep(0.2)

# Define filename for output based on current time
fn = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')

# Snap!
camera.capture(fn+'.jpg')        # take picture
time.sleep(0.2)                  # sleep time in seconds - leave this one as-is.

# Some signalling again... Blink blink
io.output(redled_pin,0)           # output pin to '0' --> disabled


time.sleep(0.1)                  # sleep time in seconds - change as you please
io.output(greenled_pin,1)        # output pin to '1' --> enabled
time.sleep(1)                    # sleep time in seconds - change as you please

# cleanup GPIO - otherwise not available for others.
io.cleanup()
