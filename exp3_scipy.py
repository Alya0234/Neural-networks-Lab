import numpy as np
from scipy import linalg
from scipy import integrate

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

x = linalg.solve(A, b)
print("Solution of Ax = b:", x)

det = linalg.det(A)
print("Determinant:", det)

inv = linalg.inv(A)
print("Inverse:\n", inv)

f = lambda x: x**2
result, error = integrate.quad(f, 0, 2)

print("Integration result:", result)
print("Error:", error)