# Question 5:

import numpy as np
import timeit
import matplotlib.pyplot as plt
from Question1 import InsertionSort, mergeSort

avgInsertionSortTimeArray = np.zeros(shape=(100,1000))
avgMergeSortTimeArray = np.zeros(shape=(100,1000))

# Run for 1000 permutations of 100 different sized random arrays for insertion sort
for i in range(0, 1000, 10):
	np.random.seed(seed = 50)
	insertionSortArray = np.random.randint(10000,size=i+1)
	for y in range (1000):
		np.random.shuffle(insertionSortArray)
		t = timeit.Timer(lambda: InsertionSort(insertionSortArray))
		avgInsertionSortTime = (t.timeit(number=1))
		avgInsertionSortTimeArray[i/10][y] = avgInsertionSortTime
	

# Run for 1000 permutations of 100 different sized random arrays for merge sort		
for i in range(0, 1000, 10):
	np.random.seed(seed = 50)
	mergeSortArray = np.random.randint(10000,size=i+1)
	for y in range (1000):
		np.random.shuffle(mergeSortArray)
		t = timeit.Timer(lambda: mergeSort(mergeSortArray))
		avgMergeSortTime = (t.timeit(number=1))
		avgMergeSortTimeArray[i/10][y] = avgMergeSortTime
		
# Average for insertion sorts
sum = 0		
avgInsertionArray = np.zeros(100)
avgInsertionArrayFinal = np.zeros(1000)
for i in range(100):
	sum = 0
	for y in range(1000):
		sum+=float(avgInsertionSortTimeArray[i][y])
	avgInsertionArray[i] = (sum/1000.0)
for x in range(100):
	avgInsertionArrayFinal[x*10] = avgInsertionArray[x]
	
## Average for merge sorts
sum = 0		
avgMergeArray = np.zeros(100)
avgMergeArrayFinal = np.zeros(1000)
for i in range(100):
	sum = 0
	for y in range(1000):
		sum+=float(avgMergeSortTimeArray[i][y])
	avgMergeArray[i] = (sum/1000.0)
for x in range(100):
	avgMergeArrayFinal[x*10] = avgMergeArray[x]
	
# Plot for average insert array
plt.plot(avgInsertionArrayFinal)
plt.legend(['Average Case'])
plt.show()

# Plot for average merge array, ran on second go
plt.plot(avgMergeArrayFinal)
plt.legend(['Average Case'])
plt.show()
	
		
	
