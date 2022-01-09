import spidev 
from numpy import interp  # To scale values
import time
import os

# Open SPI bus
spi = spidev.SpiDev() 
spi.open(0,0) 


# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data


def MoistureDetect():
  output = analogInput(0) # Reading from CH0
  output = interp(output, [0, 1023], [0, 100])
  output = int(output)/100
  return output,analogInput(0)

