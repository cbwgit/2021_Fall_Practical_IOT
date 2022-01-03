import time as time
import RPi.GPIO as GPIO

def PumpWater(water):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT) #water pump
    GPIO.output(37, 1)
    time.sleep(water/20)
    GPIO.output(37, 0)


