import tensorflow as tf
import matplotlib.pyplot as plt



(a1,a2),(b1,b2) = tf.keras.datasets.boston_housing.load_data()


plt.hist(a2,bins=20)
plt.show()

plt.plot(a1[:,5],a2,'o')
plt.show()

f=tf.random_normal(()13,1)