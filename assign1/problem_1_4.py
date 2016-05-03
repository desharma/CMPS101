# Question 4:
	
from problem_1_1 import InsertionSort, mergeSort

import numpy as np
import timeit
import matplotlib.pyplot as plt	

# Making arrays to hold times for each size 
bestTimeResultArrayMergeSort = np.zeros(3000)
worstTimeResultArrayMergeSort = np.zeros(3000)
bestTimeResultArrayInsertionSort = np.zeros(2000)
worstTimeResultArrayInsertionSort = np.zeros(2000)

# Best case and worst case for merge sort
for i in range(0,3000):
	bestCaseArray = np.arange(i)
	worstCaseArray = bestCaseArray[::-1].copy()
	t = timeit.Timer(lambda: mergeSort(bestCaseArray))
	t2 = timeit.Timer(lambda: mergeSort(worstCaseArray))
	bestCaseTime = (t.timeit(number=1))
	worstCaseTime = (t2.timeit(number=1))
	bestTimeResultArrayMergeSort[i] = bestCaseTime
	worstTimeResultArrayMergeSort[i] = worstCaseTime

# Best case and worst case for insertion sort
for i in range(0,2000):
	bestCaseArray = np.arange(i)
	worstCaseArray = bestCaseArray[::-1].copy()
	t = timeit.Timer(lambda: InsertionSort(bestCaseArray))
	t2 = timeit.Timer(lambda: InsertionSort(worstCaseArray))
	bestCaseTime = (t.timeit(number=1))
	worstCaseTime = (t2.timeit(number=1))
	bestTimeResultArrayInsertionSort[i] = bestCaseTime
	worstTimeResultArrayInsertionSort[i] = worstCaseTime
	
	
#Insertion sort run
plt.plot(bestTimeResultArrayInsertionSort)
plt.plot(worstTimeResultArrayInsertionSort)
plt.legend(['Best Case', 'Worst Case'])
plt.axis([0, 2000, 0, 2])
plt.show()

#Merge sort run
plt.plot(bestTimeResultArrayInsertionSort)
plt.plot(worstTimeResultArrayInsertionSort)
plt.legend(['Best Case', 'Worst Case'])
plt.axis([0, 2000, 0, 2])
plt.show()
