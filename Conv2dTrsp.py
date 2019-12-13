from tensorflow.python.keras.layers import Conv2DTranspose, Input
from tensorflow.python.keras.models import Model

import numpy as np

def conv_transpose():
    input = Input((2,2,3))
    layer = Conv2DTranspose(2, kernel_size=3, use_bias=False)
    x = layer(input)
    model = Model(input, x)

    weights = layer.get_weights()
    print(weights[0].shape)#(3,3,2,3)

    weights = np.arange(1, 55).reshape(3,3,2,3).astype(np.float32)
    layer.set_weights([weights])

    print("weights")
    print(weights[:,:,0,0])
    print(weights[:,:,0,1])
    print(weights[:,:,0,2])
    print(weights[:,:,1,0])
    print(weights[:,:,1,1])
    print(weights[:,:,1,2])
    X = np.arange(1,13).reshape(1,2,2,3) * 0.1
    print("input")
    print(X[0,:,:,0])
    print(X[0,:,:,1])
    print(X[0,:,:,2])
    result = model.predict(X)
    print("output")
    print(result[0,:,:,0])
    print(result[0,:,:,1])

if __name__ == "__main__":
    conv_transpose()
