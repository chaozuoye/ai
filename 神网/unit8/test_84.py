import tensorflow as tf

a = tf.range(24)

b = tf.reshape(a,[4,6])

c = tf.gather_nd(b,[[0,0],[1,1],[2,2]])
print(b)
print(c.numpy())