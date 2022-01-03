import pickle
import numpy as np

def WaterPredict():
  with open('./model.pkl','rb') as file:
      model = pickle.load(file)
  return model

