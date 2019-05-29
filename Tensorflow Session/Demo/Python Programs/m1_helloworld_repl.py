import tensorflow as tf
hello = tf.constant('Hello, TensorFlow World!')
sess = tf.Session()
print(sess.run(hello))