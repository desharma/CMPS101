# Question 1:

import numpy as np
import timeit
import matplotlib.pyplot as plt	
	
# Insertion Sort Implementation
def InsertionSort(A):
	for j in np.arange (2, len(A)): ##loop runs n-1 times
		
		key = A[j] ##insert A[j] into the sorted sequence A[1...j-1]
		i=j-1

		while i >= 0 and A[i] > key: ##loop can run up to j-1 times
			A[i+1] = A[i]
			A[i] = key
			i = i - 1
		A[i+1]=key
	return A
	
	
# Merge Sort Implementation	
def mergeSort(A):
		
	if A.size>1:
		middleIndex = A.size//2
		leftSide = A[:middleIndex].copy()
		rightSide = A[middleIndex:].copy()
		
		mergeSort(leftSide)
		mergeSort(rightSide)
		merge(leftSide, rightSide, A)
	
def merge(leftSide, rightSide, A):
	x=0
	y=0
	z=0
	size1 = leftSide.size + 1
	size2 = rightSide.size + 1
	leftSide.resize((size1), refcheck=False)
	rightSide.resize((size2), refcheck=False)
	leftSide[size1-1] = 99999999 #Arbitrarily large value in place of infinity
	rightSide[size2-1] = 99999999 #Arbitrarily large value in place of infinity
	while z < size1+size2-2:
		if leftSide[x] < rightSide[y]:
			A[z]=leftSide[x]
			x+=1
		else:
			A[z]=rightSide[y]
			y+=1
		z+=1
