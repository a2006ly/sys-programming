#!/usr/bin/env python
# coding: utf-8

# In[27]:


from tensorflow.python.keras.applications.vgg16 import VGG16
#出力層を含めない
vgg16 = VGG16(include_top = False,input_shape=(224,224,3))
vgg16.summary()



#モデルの定義
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense,Dropout,Flatten

def build_transfer_model(vgg16):
    #既存のモデルを使って、新しいモデルを作成
    model = Sequential(vgg16.layers)
    #取り出した重みの層を学習しないように設定
    for layer in model.layers[:15]:
        layer.trainable = False
    
    #追加する出力部分の層を構築
    model.add(Flatten())
    model.add(Dense(256,activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1,activation='sigmoid'))
    
    return model

model = build_transfer_model(vgg16)


# In[30]:


#mモデルのコンパイル
from tensorflow.python.keras.optimizers import SGD
model.compile(
    loss='binary_crossentropy',
    optimizer=SGD(lr=1e-4,momentum=0.9),
    metrics=['accuracy']
)
model.summary()


# In[31]:


#学習用の画像をミニバッチで読み込むためのジェネレータを利用
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.applications.vgg16 import preprocess_input

idg_train = ImageDataGenerator(
    rescale=1/255,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    preprocessing_function=preprocess_input
)


# In[32]:


#学習画像ロードするためのいてれーたを生成 注意　画像フォルダの配下にclassフォールダ作成しないと、ダメ！！！！
#訓練用データ
img_itr_train = idg_train.flow_from_directory(
    'img/train/',
    target_size=(224,224),
    batch_size=16,
    class_mode='binary'
)

#検証用
img_itr_validation = idg_train.flow_from_directory(
    'img/validation/',
    target_size=(224,224),
    batch_size=16,
    class_mode='binary'
)


# In[33]:


import os
from datetime import datetime

model_dir = os.path.join(
    "models",
    datetime.now().strftime('%y%m%d_%H%M')
)

os.makedirs(model_dir,exist_ok=True)

dir_weights = os.path.join(model_dir,'weights')
os.makedirs(dir_weights,exist_ok=True)


# In[34]:


import json
import pickle

#作成ネットワーク保存
model_json = os.path.join(model_dir,'model.json')
with open(model_json,'w') as f:
    json.dump(model.to_json(),f)

#学習時の正解ラベルの保存
model_classes = os.path.join(model_dir,'classes.pkl')
with open(model_classes,'wb') as f:
    pickle.dump(img_itr_train.class_indices,f)


# In[35]:


import math

#何バッチ文学習すれば1エポックを計算
batch_size = 16
steps_per_epoch = math.ceil(
    img_itr_train.samples/batch_size
)

validation_steps = math.ceil(
    img_itr_validation.samples/batch_size
)


# In[36]:


from tensorflow.python.keras.callbacks import ModelCheckpoint,CSVLogger

cp_filepath = os.path.join(dir_weights,'ep_{epoch:02d}_ls_{loss:.1f}.h5')
cp = ModelCheckpoint(
    cp_filepath,
    monitor='loss',
    verbose=0,
    save_beast_only=False,
    save_weights_only=True,
    model='auto',
    #重みを５エポックで保存　
    period=5
)

csv_filepath = os.path.join(model_dir,'loss.csv')
csv = CSVLogger(csv_filepath,append=True)


# In[37]:


#モデル学習
history = model.fit_generator(
    img_itr_train,
    steps_per_epoch=steps_per_epoch,
    epochs=30,
    validation_data=img_itr_validation,
    validation_steps=validation_steps,
    callbacks = [cp,csv]
)


# In[2]:


# 予測データロード
import glob
import os
import random
import math
import numpy as np
import pandas as pd

import matplotlib
# matplotlib.use('Agg')

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
    # fig.show()

    
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

test_img_dir = 'img/unknow'

x_text, true_labels = load_random_imgs(
    test_img_dir,
    seed=1
)

probs = model.predict(x_text)
probs

show_test_samples(
    x_text,
    probs,
    img_itr_train.class_indices,
    true_labels
)


# In[ ]:




