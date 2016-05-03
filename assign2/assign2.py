# assign2.py
# Kyle Ebding - kebding@ucsc.edu
# Deepak Sharma - desharma@ucsc.edu

import numpy as np

# PROBLEM 1 -------------------------------------

def matmult(A, x):
    n = A.shape[0]
    xLength = x.shape[0] 
    if xLength != n:
        print("matrix and vector are incompatible")
        return 0
    x = np.reshape(x, (xLength, 1))
    b = np.empty((n), dtype=int)
    for i in range(n):
        b[i] = 0
        for j in range(n):
            b[i] += int( A[i, j] * x[j, 0] )
    return b

# test code to check if matmult works correctly
# A = np.array([ [1,2,3], [4,5,6], [7,8,9] ])
# x = np.array([2, 1, 3])
# b = matmult(A, x)
# print(b)

# PROBLEM 2 -------------------------------------

def hadmat(k):
    if (k == 0):
        return 0
    if (k == 1):
        return np.array([[1, 1], [1, -1]])
    else:
        smaller = hadmat(k-1)
        top = np.concatenate((smaller, smaller), axis = 1)
        bot = np.concatenate((smaller, -1*smaller), axis = 1)
        return np.concatenate((top, bot), axis = 0)

# test code for hadmat(4)
# h4 = hadmat(4)
# print("final =")
# for row in h4:
#    print(row)


# PROBLEM 4 -------------------------------------

def hadmatmult(H, x):
    k = H.shape[0]
    xLength = x.shape[0]
    if (xLength != k):
        print("invalid array / vector: cannot be multiplied")
        return 0
    
    if (k == 0):
        return 0

    x = np.reshape(x, (xLength, 1))
    x1 = x[0:(xLength/2)]
    x2 = x[(xLength/2):xLength]
    Hsmaller = H[0:k/2, 0:k/2]
    left = matmult(Hsmaller, x1)
    right = matmult(Hsmaller, x2)
    top = left + right
    bot = left - right
    result = np.concatenate((top, bot), axis=0)
    return result


# test code for hadmatmult(H3, [[1],[2],[3],[4]])
# vector = np.array([1,2,3,4])
# H = hadmat(3)
# foo = hadmatmult(H, vector)
# bar = matmult(H, vector)
# import numpy.testing as nt
# nt.assert_equal(foo, bar)


# PROBLEM 5 -------------------------------------

import timeit
import matplotlib.pyplot as plt

hmmTime = np.empty(12)
mmTime = np.empty(12)
for k in range(1, 13):
    H = hadmat(k)
    x = np.random.randint(-5, 50, [2**k])
   
    hmmTimer = timeit.Timer(lambda: hadmatmult(H, x))
    hmmTime[k-1] = hmmTimer.timeit(number=1)
    
    mmTimer = timeit.Timer(lambda: matmult(H, x))
    mmTime[k-1] = mmTimer.timeit(number=1)

xAxis = range(1, 13)
plt.figure()
plt.plot(xAxis, mmTime, 'r-', xAxis, hmmTime, 'g-')
plt.xlabel("n")
plt.ylabel("time")
plt.title("hadmatmult vs matmult")
plt.legend(["matmult", "hadmatmult"])
plt.show()
