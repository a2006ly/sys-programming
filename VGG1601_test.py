#!/usr/bin/env python
# coding: utf-8

from tensorflow.python.keras.applications.vgg16 import VGG16
from tensorflow.python.keras.applications.vgg16 import preprocess_input
from tensorflow.python.keras.applications.vgg16 import decode_predictions
from tensorflow.python.keras.preprocessing.image import load_img,img_to_array

import numpy as np

imgpath = 'C:/Users/user/Desktop/workspace/doc/sysp/img'
#���f���쐬
model = VGG16()
#model.summary()

#�摜���[�h pillow
cat_img = load_img('{}/cat.jpg'.format(imgpath),target_size=(224,224))
dog_img = load_img('{}/dog.jpg'.format(imgpath),target_size=(224,224))

#�摜�𐔒l�ύX
train_dog_nd = img_to_array(dog_img)
train_cat_nd = img_to_array(cat_img)

#�O����
train_dog_img = preprocess_input(train_dog_nd)
train_cat_img = preprocess_input(train_cat_nd)

#�摜��z��ɂ܂Ƃ�
train_img = np.stack([train_dog_img,train_cat_img])

probs = model.predict(train_img)

resutlt = decode_predictions(probs)
ind = np.argmax(resutlt[0])
print(ind)