import numpy as np

A = np.array([[1, 1, 1, 3],[1, 2, 2, 1],[2, 1, 1, 2],[3, 1, 1, 1]])
B = np.array([10.5, 10.5, 10.5, 10.5])
X = np.linalg.solve(A,B)

print(X)
