import numpy as np
import pandas as pd
import os
import sys
import pathlib
import pickle
import csv
import time
import tensorflow as tf
import tensorflow.keras
from datetime import datetime
from sklearn.base import TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from skopt import gp_minimize, plots, space
from skopt.utils import use_named_args
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers.experimental import preprocessing


# Models from:
# https://arxiv.org/pdf/1409.1556.pdf
def create_vvg16():
    base_vgg = tf.keras.applications.VGG16(input_shape=(450, 450, 3), include_top=False, weights="imagenet")
    x = base_vgg.output
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(4096, activation="elu")(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    x = tf.keras.layers.Dense(4096, activation="elu")(x)
    x = tf.keras.layers.Dropout(0.5)(x)

    output_layer = tf.keras.layers.Dense(1, activation="softmax")(x)
    vgg_model = tf.keras.Model(inputs=base_vgg.input, outputs=output_layer)

    return vgg_model

def create_vgg19():
    base_vgg = tf.keras.applications.VGG19(input_shape=(450, 450, 3), include_top=False, weights="imagenet")
    x = base_vgg.output
    x = tf.keras.layers.Flatten()(x)
    x = tf.keras.layers.Dense(4096, activation="elu")(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    x = tf.keras.layers.Dense(4096, activation="elu")(x)
    x = tf.keras.layers.Dropout(0.5)(x)

    output_layer = tf.keras.layers.Dense(1, activation="softmax")(x)
    vgg_model = tf.keras.Model(inputs=base_vgg.input, outputs=output_layer)

    return vgg_model