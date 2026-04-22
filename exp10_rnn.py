import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Dummy sequential data
X = np.array([
    [[0],[0],[1]],
    [[1],[0],[1]],
    [[0],[1],[1]],
    [[1],[1],[1]]
])

y = np.array([0,1,1,0])

model = models.Sequential([
    layers.SimpleRNN(8, input_shape=(3,1), activation='tanh'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X, y, epochs=50, verbose=0)

loss, acc = model.evaluate(X, y, verbose=0)

print("RNN Accuracy:", acc)