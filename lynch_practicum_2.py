# Your Name: Anna Lynch
#-------------------------------------------
# DO NOT MODIFY
# Exam code: lfqlij3ga
#-------------------------------------------    
# Put All Import statements in this section
import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------
# Problem 1
A = np.array([[-4.0, 3.0, 2.0], [3.0, 11.0, 0.0], [2.0, -1.0, 4.0]])
b = np.array([0.0, 8.0, -3.0])

x = np.linalg.solve(A, b)
r = np.dot(A, x) - b

print(r)

#-------------------------------------------
# Problem 2
data = np.loadtxt("prac2data.csv", delimiter=",")
x = np.array(data[:,0])
y = np.array(data[:,1])

A = np.polyfit(x, y, 3)

def yFunc(A, x):
    return A[3] + A[2] * x + A[1] * np.pow(x, 2) + A[0] * np.pow(x, 3)

for i in range(4):
    print("c" + str(i),  "=", A[3 - i])

plt.plot(x, yFunc(A, x))
plt.plot(x, y)
plt.show()

#-------------------------------------------
# Problem 3

def MyDeterminant(mat):
    return (mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0])

#-------------------------------------------

# Do they still make jobs for computational physics?