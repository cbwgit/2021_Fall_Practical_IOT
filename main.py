
from importlib import import_module
from flask import Flask, render_template, Response ,request
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

moistureContent=0.8

def moisture(moistureContent):
    output,Moisture=MoistureDetect()
    if output<(moistureContent/100):
        water = WaterPredict().predict([[output]])
        print(water)
        lineMessage('hiyaku kite') 
        PumpWater(water[0])
    else:
        lineMessage('no need ')

# Flask constructor

app = Flask(__name__)



@app.route('/',methods=['POST','GET'])
def index():
    #Get moisture value
    if request.method == 'POST':
      moistureContent = request.form["moistureContent"]
      moisture(int(moistureContent))
      return moistureContent
    return render_template('index.html')


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', threaded=True)


