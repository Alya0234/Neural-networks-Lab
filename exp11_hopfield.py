import numpy as np


patterns = np.array([
    [1, -1, 1, -1],
    [-1, 1, -1, 1]
])


n = patterns.shape[1]
W = np.zeros((n, n))


for p in patterns:
    p = p.reshape(n, 1)
    W += p @ p.T

np.fill_diagonal(W, 0)

print("Weight Matrix:\n", W)


test = np.array([1, -1, -1, -1])

print("\nInitial Input:", test)


def update(x, W):
    for _ in range(5):
        x = np.sign(W @ x)
    return x

output = update(test, W)

print("Recovered Pattern:", output)
