# coding: utf-8

import os
import glob
import math
import random

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.python import keras
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import Model,Sequential
from tensorflow.python.keras.layers import Conv2D,Dense,Input,MaxPooling2D,UpSampling2D,Lambda
from tensorflow.python.keras.preprocessing.image import load_img,img_to_array,array_to_img,ImageDataGenerator

from tensorflow.python.keras.datasets import mnist