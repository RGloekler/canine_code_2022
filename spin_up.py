import odrive, time, random
from odrive.enums import *

# get gpio module for relay/power control
import RPI.GPIO as GPIO

# set up the GPIO
GPIO.setmode(GPIO.BCM) # use GPIO numbers instead of pin numbers

# set pin to output
RELAY_PIN = 17
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    GPIO.output(RELAY_PIN, GPIO.HIGH) # turn on the power
except:
    exit('Couldn\'t turn on power supply')

# get an odrive
odrv0 = odrive.find_any()
print(odrv0.vbus_voltage)

# get the axis
axis0 = getattr(odrv0, "axis0")

while True:
    # set control modes
    odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
    odrv0.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL

    # ramp up the speed
    for step in range(0, 6):
        odrv0.axis0.controller.input_vel = step
        time.sleep(1)

    # ramp back down
    for step in range(6, 0, -1):
        odrv0.axis0.controller.input_vel = step
        time.sleep(1)

    odrv0.axis0.controller.input_vel = 0
    time.sleep(5)
try:
    GPIO.output(RELAY_PIN, GPIO.LOW) # turn on the power
except:
    exit('Couldn\'t turn off power supply')
