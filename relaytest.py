import RPI.GPIO as GPIO
import time

# set up the GPIO
GPIO.setmode(GPIO.BCM) # use GPIO numbers instead of pin numbers

# set pin to output
RELAY_PIN = 17
GPIO.setup(RELAY_PIN, GPIO.OUT)

try:
    GPIO.output(RELAY_PIN, GPIO.HIGH) # turn on the power
except:
    exit('Couldn\'t turn on power supply')

time.sleep(3)
GPIO.output(RELAY_PIN, GPIO.LOW) # turn on the power
