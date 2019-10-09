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
from IPython.display import display_png
from PIL import Image


def load_data():
    (x_train,_),(x_test,_) = mnist.load_data()
    x_train = x_train.reshape(-1,28,28,1)/255
    x_test = x_test.reshape(-1,28,28,1)/255
    return x_train,x_test

#マスキングノイズを加える
def make_masking_noise_data(x_data,percent=0.1):
    size = x_data.shape
    #二項式分部
    masking = np.random.binomial(n=1,p=percent,size=size)
    return x_data * masking


#ガウシアンノイズ関数
def make_gaussian_noise(x_data,scale=0.8):
    size = x_data.shape
    gaussian = np.random.normal(loc=0,scale=scale,size=size)
    gaussian = np.clip(gaussian,0,1)
    return x_data * gaussian


x_train,x_test =load_data()

x_train_masking = make_masking_noise_data(x_train)
x_test_masking = make_masking_noise_data(x_test)


x_train_gaussian = make_gaussian_noise(x_train)
x_test_gaussian = make_gaussian_noise(x_test)

display_png(array_to_img(x_train[0]))
display_png(array_to_img(x_train_masking[0]))
array_to_img(x_train_masking[0]).show()
display_png(array_to_img(x_train_gaussian[0]))
array_to_img(x_train_gaussian[0]).show()


#CAEモデル構築

autoencoder = Sequential()

#encoder畳み込み層
autoencoder.add(
    Conv2D(
        filters=16,
        kernel_size=(3,3),
        strides=(1,1),
        activation='relu',
        padding='same',
        input_shape=(28,28,1)
        )
    )

autoencoder.add(
    MaxPooling2D(
        pool_size=(2,2),
        #strides=1,
        padding='same'
        )
    )

autoencoder.add(
    Conv2D(
        filters=8,
        kernel_size=(3,3),
        strides=(1,1),
        activation='relu',
        padding='same',
        )
    )

autoencoder.add(
    MaxPooling2D(
        pool_size=(2,2),
        #strides=1,
        padding='same'
        )
    )

#Decoder畳み込み層
autoencoder.add(
    Conv2D(
        filters=8,
        kernel_size=(3,3),
        strides=(1,1),
        activation='relu',
        padding='same',
        input_shape=(28,28,1)
        )
    )

autoencoder.add(UpSampling2D((2,2)))

autoencoder.add(
    Conv2D(
        filters=16,
        kernel_size=(3,3),
        strides=(1,1),
        activation='relu',
        padding='same',
        )
    )

autoencoder.add(UpSampling2D((2,2)))

autoencoder.add(
    Conv2D(
        filters=1,
        kernel_size=(3,3),
        strides=(1,1),
        activation='sigmoid',
        padding='same',
        )
    )

autoencoder.compile(
    loss="binary_crossentropy",
    optimizer="adam",
    metrics=['accuracy']
    )

initial_weights = autoencoder.get_weights()
autoencoder.summary()


#gaussianノイズ画像入力

autoencoder.fit(
    x_train_gaussian,
    x_train,
    epochs=10,
    batch_size=20,
    shuffle=True
    )

gauss_preds = autoencoder.predict(x_test_gaussian)

for i in range(10):
    display_png(array_to_img(x_test[i]))
    display_png(array_to_img(x_test_gaussian[i]))
    display_png(array_to_img(gauss_preds[i]))
    print("-"*25)

autoencoder.set_weights(initial_weights)

autoencoder.fit(
    x_train_masking,
    x_train,
    batch_size=20,
    epochs=10,
    shuffle=True
    )

masking_preds = autoencoder.predict(x_test_masking)
for i in range(10):
    display_png(array_to_img(x_test[i]))
    display_png(array_to_img(x_test_masking[i]))
    display_png(array_to_img(masking_preds[i]))
    print("-"*25)