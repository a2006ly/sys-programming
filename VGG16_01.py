#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tensorflow.python.keras.applications.vgg16 import VGG16
model = VGG16()
model.summary()


# In[16]:


from tensorflow.python.keras.preprocessing.image import load_img
from tensorflow.python.keras.preprocessing.image import img_to_array
from tensorflow.python.keras.applications.vgg16  import preprocess_input
import numpy as np
#写真を読み込み　型Pillow
img_dog = load_img('img/dog.jpg',target_size=(224,224))
img_cat = load_img('img/cat.jpg',target_size=(224,224))
#写真を操作可能な数値に変更 ndarryに変更する
arr_dog = img_to_array(img_dog)
arr_cat = img_to_array(img_cat)
#VGG16の訓練データと一致する型に変更　preprocess_input
arr_dog = preprocess_input(arr_dog)
arr_cat = preprocess_input(arr_cat)
#画像をまとめて、２枚画像を含む配列の入力データに変換
arr_input = np.stack([arr_dog,arr_cat])
print(arr_input.shape)


# In[21]:


#予測処理
probs = model.predict(arr_input)
print(probs.shape)


# In[32]:


#予測結果をクラス名付けて、表示する
from tensorflow.python.keras.applications.vgg16 import decode_predictions
result = decode_predictions(probs,top=10)
result[0]


# In[29]:


#dog
result[0]
#cat
result[1]


# In[ ]:




