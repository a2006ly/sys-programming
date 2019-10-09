from tensorflow.python.keras.layers import Input,Lambda,Dense
from tensorflow.python.keras.models import Model

model_in = Input(shape=(20,))
x=Lambda(lambda x: x/255)(model_in)
x=Dense(64,activation='relu')(x)
model_out = Dense(10,activation='softmax')(x)

model = Model(inputs=model_in,outputs=model_out)

model.compile(
    loss='categorical_crossentropy',
    optimizer='SGD',
    metrics=['accuracy']
    )
