# HW6 Problem 1 template file -- replace with your name here

#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ainput" and an nx1 column matrix "binput"
# inputs should be floating-point type
# it performs Gaussian elimination and outputs the eliminated new matrices A and b
# where "A" is nxn upper triangular, and "b" is an nx1 column matrix
def GaussElimin(Ainput,binput):
    n=len(binput)
    A = Ainput.copy() # make copies so as not to write over originals
    b = binput.copy()
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = A[j,i]/A[i,i] # multiplicative factor to zero point
            A[j,i] = 0.0 # we know this element goes to zero
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n] # do subtraction of two rows
            b[j] = b[j]-c*b[i] # do substraction of b's as well
    return (A,b)  # return modified A and b
    
#---Do not modify above this line--#

# Part B
A1 = np.array([[4.0, -2.0, 1.0], [-3.0, -1.0, 4.0], [1.0, -1.0, 3.0]])
b1 = np.array([15.0, 8.0, 13.0])
x1 = [2.0, -2.0, 3.0]

A2, b2 = GaussElimin(A1, b1)

print(A1)
print(x1)
print(b1)
print(np.matmul(A1, x1) - b1)

print("")

print(A2)
print(x1)
print(b2)
print(np.matmul(A2, x1) - b2)

# Part C
A2 = np.array([
    [0.000001, 2.0, 0.000001, 1.0],
    [2.0, 2.0, 3.0, 2.0],
    [4.0, -3.0, 0.000001, 1.0],
    [6.0, 1.0, -6.0, -5.0]
])
b2 = np.array([0.0, -2.0, -7.0, 6.0])
x2 = np.array([-0.5, 1.0, 1.0/3.0, -2.0])

A2a, b2a = GaussElimin(A2, b2)

print(np.matmul(A2a, x2) - b2a)