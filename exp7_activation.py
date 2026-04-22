import numpy as np

def step(x):
    return 1 if x >= 0 else 0

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return max(0, x)

def tanh(x):
    return np.tanh(x)

x_values = [-2, -1, 0, 1, 2]

print("x\tStep\tSigmoid\tReLU\tTanh")

for x in x_values:
    print(x, "\t",
          step(x), "\t",
          round(sigmoid(x),3), "\t",
          relu(x), "\t",
          round(tanh(x),3))