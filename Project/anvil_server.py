import anvil.server
import numpy as np
import tensorflow as tf
import cv2
from testing_function import get_prediction

anvil.server.connect('BSR6ZYLIKFNKYCJS3WRA6GVO-436WM4R34T37WVBO') 

@anvil.server.callable
def predict_digit(image_path):
    return get_prediction(image_path)
