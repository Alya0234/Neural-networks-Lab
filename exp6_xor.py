import numpy as np

# XOR input
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

# XOR output
y = np.array([[0],[1],[1],[0]])

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative
def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize weights
np.random.seed(1)
W1 = np.random.rand(2,2)
W2 = np.random.rand(2,1)

# Training
epochs = 10000
lr = 0.1

for _ in range(epochs):
    # Forward pass
    hidden = sigmoid(np.dot(X, W1))
    output = sigmoid(np.dot(hidden, W2))

    # Error
    error = y - output

    # Backprop
    d_output = error * sigmoid_derivative(output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden)

    # Update weights
    W2 += hidden.T.dot(d_output) * lr
    W1 += X.T.dot(d_hidden) * lr

print("Final Output:")
print(output.round())