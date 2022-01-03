import time
import RPi.GPIO as GPIO
from pump import PumpWater
from moisture import MoistureDetect
from line import lineMessage
from model import WaterPredict
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.IN)         #Water read
GPIO.setup(3, GPIO.IN)

output,Moisture=MoistureDetect()

if output<0.9:
    water = WaterPredict().predict([[output]])
    print(water)
    lineMessage('hiyaku kite') 
    PumpWater(water[0])
else:
    lineMessage('no need ')

time.sleep(5)
