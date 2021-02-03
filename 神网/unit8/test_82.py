import tensorflow as tf

a = tf.range(6)

a1 = tf.reshape(a, [2, 3])

b = tf.constant([[7, 8, 9], [10, 11, 12]])

b1 = tf.gather(b, axis=1, indices=[1,2,0])

print(b1)

c = a1*b1

print(c.numpy())