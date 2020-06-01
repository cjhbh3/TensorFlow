from __future__ import print_function
import tensorflow as tf


a = tf.constant(5)
b = tf.constant(2)
c = tf.constant(3)

add = tf.add(a, b)
sub = tf.subtract(a, b)
mul = tf.multiply(a, b)
div = tf.divide(a, b)

print("add = ", add.numpy())
print("sub = ", sub.numpy())
print("mul = ", mul.numpy())
print("div = ", div.numpy())