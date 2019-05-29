import tensorflow as tf

sess = tf.Session()

zeroD = tf.constant(5)
sess.run(tf.rank(zeroD))

oneD = tf.constant(["How", "are", "you?"])
sess.run(tf.rank(oneD))

twoD = tf.constant([[1.0, 2.3], [1.5, 2.9]])
sess.run(tf.rank(twoD))

threeD = tf.constant([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])
sess.run(tf.rank(threeD))

sess.close()