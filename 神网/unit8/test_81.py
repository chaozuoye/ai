import numpy as np
import tensorflow as tf


a = tf.constant([[2, 5, 1], [3, 4, 6]])

b = tf.argmax(a,0)

print(b.numpy())