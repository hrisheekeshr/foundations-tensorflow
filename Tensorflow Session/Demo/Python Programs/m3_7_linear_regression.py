import tensorflow as tf

#Model Parameters
W = tf.Variable([.3],dtype=tf.float32)
b = tf.Variable([-0.3],dtype=tf.float32)

#Model Input and Output

x = tf.placeholder(tf.float32)
linear_model = W * x + b 

y = tf.placeholder(tf.float32)

#loss 
loss = tf.reduce_sum(tf.square(linear_model - y))

#optimiser 

optimizer = tf.train.GradientDescentOptimizer(0.01)

train = optimizer.minimize(loss)

#training data
x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]


init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)

	for i in range(1000):
		sess.run(train, {x:x_train, y:y_train})

	curr_W, curr_b,curr_loss = sess.run([W,b,loss],{x:x_train,y:y_train})

	print("W : {} , b = {}, loss: {}".format(curr_W, curr_b,curr_loss))