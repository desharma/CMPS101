# Question 3:
from problem_1_1 import InsertionSort, mergeSort

import numpy as np
import timeit

# Making arrays to hold times for each size 
bestTimeResultArrayMergeSort = np.zeros(10000)
worstTimeResultArrayMergeSort = np.zeros(10000)
bestTimeResultArrayInsertionSort = np.zeros(10000)
worstTimeResultArrayInsertionSort = np.zeros(10000)

for i in range(0,10000):
	bestCaseArray = np.arange(i)
	worstCaseArray = bestCaseArray[::-1].copy()
	t = timeit.Timer(lambda: mergeSort(bestCaseArray))
	t2 = timeit.Timer(lambda: mergeSort(worstCaseArray))
	bestCaseTime = (t.timeit(number=1))
	worstCaseTime = (t2.timeit(number=1))
	bestTimeResultArrayMergeSort[i] = bestCaseTime
	worstTimeResultArrayMergeSort[i] = worstCaseTime

for i in range(0,10000):
	bestCaseArray = np.arange(i)
	worstCaseArray = bestCaseArray[::-1].copy()
	t = timeit.Timer(lambda: InsertionSort(bestCaseArray))
	t2 = timeit.Timer(lambda: InsertionSort(worstCaseArray))
	bestCaseTime = (t.timeit(number=1))
	worstCaseTime = (t2.timeit(number=1))
	bestTimeResultArrayInsertionSort[i] = bestCaseTime
	worstTimeResultArrayInsertionSort[i] = worstCaseTime
