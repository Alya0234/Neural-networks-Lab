import numpy as np

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])

weights = np.zeros(2)
bias = 0
lr = 0.1
epochs = 10

for _ in range(epochs):
    for i in range(len(X)):
        linear = np.dot(X[i], weights) + bias
        y_pred = 1 if linear >= 0 else 0

        error = y[i] - y_pred

        weights += lr * error * X[i]
        bias += lr * error

print("Weights:", weights)
print("Bias:", bias)

print("Predictions:")
for i in range(len(X)):
    linear = np.dot(X[i], weights) + bias
    y_pred = 1 if linear >= 0 else 0
    print(X[i], "->", y_pred)