#!/usr/bin/env python
# coding: utf-8

from tensorflow.python.keras.applications.vgg16 import VGG16,preprocess_input,decode_predictions
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense,Dropout,Flatten
from tensorflow.python.keras.optimizers import SGD
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
import math
import numpy as np



# 予測データロード
import glob
import os
import random
import pandas as pd

import matplotlib

import matplotlib.pyplot as plt
from tensorflow.python.keras.preprocessing.image import img_to_array, load_img


def imshow_with_title(ax, img, title):
        ax.imshow(img / 255.)
        ax.set_title(title)
        ax.axis('off')
        return ax

    
def get_train_sample_info(img_itr, n):
    class_labels = {idx: label for label, idx in img_itr.class_indices.items()}
    out_imgs, out_labels = np.array([]), np.array([])
    while len(out_imgs) < n:
        images, class_idx = next(img_itr)
        labels = [class_labels[idx]  for idx in  class_idx]
        out_imgs = np.concatenate([out_imgs, images]) if out_imgs else images
        out_labels = np.concatenate([out_labels, labels]) if out_labels  else  labels
    return out_imgs[:n], out_labels[:n]
    
    
def get_pred_sample_labels(probs, class_indices):
    class_labels = {idx: label for label, idx in class_indices.items()}
    tmp = '{}:{:.3f}  /  {}:{:.3f}'
    lbls = [tmp.format(class_labels[0], 1- p[0], class_labels[1], p[0])
                    for p in probs]
    return lbls


def show_img_samples(imgs, labels, ncols=4, save_fig=None):    
    n = len(imgs)
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(4 * ncols, 4 * nrows))
    for ax, img, label in zip(axes.ravel(), imgs, labels):
        ax = imshow_with_title(ax, img, label) 
    if save_fig:
        fig.savefig(save_fig)
        fig.show()

    
def show_train_samples_iter(img_itr, n=8):
    imgs, labels = get_train_sample_info(img_itr, n)
    show_img_samples(imgs, labels)

    
def show_train_samples(img_dir, classes, n=4, seed=0, save_fig=None):
    labels = []
    imgs = None
    for img_class in classes:
        labels += [img_class] * n 
        data_dir = os.path.join(img_dir, 'train/{}'.format(img_class))
        now_imgs, _ = load_random_imgs(data_dir, n, seed=seed)
        imgs = now_imgs if imgs is None else np.concatenate([imgs, now_imgs], axis=0)
    show_img_samples(imgs, labels, save_fig=save_fig)

    
def show_test_samples(imgs, probs, class_indices, true_labels):
    pred_labels = get_pred_sample_labels(probs, class_indices)
    labels = [p + '\n' + 'True:' + t for p, t in zip(pred_labels, true_labels)]
    show_img_samples(imgs, labels)

    
def ext_label_from_filepath(img_path):
    target_idx = 0
    return os.path.basename(img_path).split('_')[target_idx]
    
    
def get_rand_img_paths(data_dir, n, seed=0, with_labels=False):
    g = os.path.join(data_dir, '*.jpg')
    img_paths = glob.glob(g)
    random.seed(seed)
    random.shuffle(img_paths)
    target_paths = img_paths[:n]
    if with_labels:
        true_labels = [ext_label_from_filepath(x) for x in target_paths]
        return target_paths, true_labels
    else:
        return target_paths

    
def load_imgs(img_paths, target_size):
    list_imgs = [img_to_array(load_img(path, target_size=target_size))
                    for path in img_paths]
    return np.array(list_imgs)


def load_random_imgs(data_dir, n=8, seed=0, target_size=(224, 224)):
    target_paths, true_labels = get_rand_img_paths(data_dir, n, seed=seed, with_labels=True)
    imgs = load_imgs(target_paths, target_size)
    return imgs, true_labels


def adjust_ax(df, ax, ylabel):
    df.plot(ax=ax)
    ax.set_title(ylabel)
    ax.set_xlabel('epochs')
    ax.set_ylabel(ylabel)
    ax.legend()
    return ax




imgpath = 'C:/Users/user/Desktop/workspace/doc/sysp/img/Train_img'
testImgPath = 'C:/Users/user/Desktop/workspace/doc/sysp/img/unknow/tera.jpg'

#nclude_top: ネットワークの出力層側にある3つの全結合層
vgg16 = VGG16(include_top=False,input_shape=(224,224,3))
#vgg16.summary()

#自分のモデル作成
def build_Model(vgg16):
    #モデルを作成
    model = Sequential(vgg16.layers)
    #既存モデルを使用禁止
    for layer in model.layers[:15]:
        layer.trainable=False

    model.add(Flatten())
    model.add(Dense(256,activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1,activation='sigmoid'))
    
    return model

#モデル作成
model = build_Model(vgg16)

#モデルのコンパイル
model.compile(
    loss='binary_crossentropy',
    optimizer=SGD(lr=1e-4,momentum=0.9),
    metrics=['accuracy']
    )

model.summary()

#学習画像を取込
train_gen = ImageDataGenerator(
    rescale = 1/255,
    rotation_range=1,
    shear_range=0.5,
    zoom_range=1,
    width_shift_range=0.1,
    horizontal_flip=False,
    preprocessing_function=preprocess_input
    )

#itr作成
train_itr =train_gen.flow_from_directory(
    imgpath,
    target_size=(224,224),
    class_mode='binary',
    batch_size=16,
    seed=1
    )


#1エポックで何バッチ文学習

history = model.fit_generator(
    train_itr,
    steps_per_epoch=math.ceil(train_itr.samples/16),
    epochs=5
    )


#Image予測
#画像ロード
predit_img = load_img(testImgPath,target_size=(224,224))
predict_ndarr = img_to_array(predit_img)
#前処理
test_img = preprocess_input(predict_ndarr)
arr_input = np.stack([test_img])

#画像予測
probs = model.predict(arr_input)
#probs 

test_img_dir =  'C:/Users/user/Desktop/workspace/doc/sysp/img/unknow/'

x_text, true_labels = load_random_imgs(
    test_img_dir,
    seed=1
)

probs = model.predict(x_text)
probs

show_test_samples(
    x_text,
    probs,
    train_itr.class_indices,
    true_labels
)
