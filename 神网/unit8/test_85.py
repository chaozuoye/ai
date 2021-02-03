import tensorflow as tf

import numpy as np

a = tf.constant([[1., 2., 3.],[4., 5., 6.]])

b = tf.random.shuffle(a)

c = tf.constant(np.arange(6), shape=(3,2) ,dtype=tf.float32)
print("b:\n"+str(b.numpy))
print("c:\n"+str(c.numpy))
d = tf.reduce_mean(b@c, axis=0)
print("c@b:\n"+str(d.numpy))
e = tf.argmin(d,axis=0)

print("d_value:",d.numpy())

print("e_value:",e.numpy())