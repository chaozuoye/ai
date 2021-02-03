import tensorflow as tf

t1 = tf.constant([[1, 2, 3], [4, 5, 6]])

t2 = tf.constant([[7, 8, 9], [10, 11, 12]])

t = tf.stack((t1, t2), axis=1)
print(t)
print(t.shape)