from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.contrib.eager as tfe

tf.enable_eager_execution()

print("TensorFlow version: {}".format(tf.VERSION))
print("Eager execution: {}".format(tf.executing_eagerly()))



classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    hidden_units=[62500, 50000, 30000, 10000, 1000, 500, 100, 10],
    n_classes=2,
    model_dir='trainCNN/objectPrediction')

