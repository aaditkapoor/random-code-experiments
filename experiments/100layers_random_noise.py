# -*- coding: utf-8 -*-
"""Exp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VUyf1PzjrN7M_hYYj29rY4xp2vHMrmNT
"""

import numpy as np
from tensorflow import keras
import tensorflow as tf
import pandas as pd

def create_dataset(length=100,split=0.3):
  train_size = int(length - (length * split))
  test_size = length - train_size
  x = np.random.random([length,28])
  y = np.ones(shape=(length,))
  x_train, y_train, x_test, y_test = x[:train_size], y[:train_size], x[train_size:], y[train_size:]
  
  print("x_train: {}, x_test {}".format(x_train.shape, x_test.shape))
  return (x_train, y_train, x_test, y_test)


x_train, y_train, x_test, y_test = create_dataset()

model = keras.Sequential()
model.add(keras.layers.Input(shape=(28,)))
un = 10
for i in range(100):
  model.add(keras.layers.Dense(un, activation='relu'))
  un+=2

model.summary()

model.add(keras.layers.Dense(1, activation='sigmoid'))
model.compile(optimizer="adam", loss=keras.losses.binary_crossentropy, metrics=['acc'])

model.fit(x, y, epochs=10, validation_split=0.2)

model.evaluate(x_test, y_test)

p_t = np.random.random([1,28])
model.predict(p_t)

