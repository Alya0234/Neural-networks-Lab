import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])

print("1D Array:", a)
print("2D Array:\n", b)

print("Shape:", b.shape)
print("Size:", b.size)
print("Data Type:", b.dtype)

print("Zeros:\n", np.zeros((2, 2)))
print("Ones:\n", np.ones((2, 2)))

print("Addition:", a + 2)
print("Multiplication:", a * 2)

c = np.array([5, 6, 7, 8])
print("Array Addition:", a + c)
print("Dot Product:", np.dot(a, c))