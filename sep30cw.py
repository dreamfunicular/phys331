import scipy.linalg as linalg
import numpy as np

arr = np.array([[4, 6, 2], [2, -2, -2], [6, 4, 1]])
P, L, U = linalg.lu(arr)

print(P)