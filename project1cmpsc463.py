
#my improved version

def binarySearch(arr, key, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low

def adaptiveInsertionSort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        loc = binarySearch(arr, key, 0, j)

        while j >= loc:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partitionRandom(array, low, high):

  pivotindex = random.randint(low, high)

  pivotVal = array[pivotindex]

  i = low - 1

  (array[pivotindex], array[high]) = (array[high], array[pivotindex])

  for j in range(low, high):
    if array[j] < pivotVal:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  
  return i

def hybrid_quick_sort_adaptive(arr, low, high, insertion_threshold = 10):
    if low < high:
        if high - low + 1 <= insertion_threshold:
            adaptiveInsertionSort(arr, low, high)
        else:
            pi = partitionRandom(arr, low, high)
            hybrid_quick_sort_adaptive(arr, low, pi)
            hybrid_quick_sort_adaptive(arr, pi + 2, high)


#GeeksForGeeks version
# https://www.geeksforgeeks.org/advanced-quick-sort-hybrid-algorithm/

# Python implementation of the above approach

# Function to perform the insertion sort
def insertion_sort(arr, low, n):
	for i in range(low + 1, n + 1):
		val = arr[i]
		j = i
		while j>low and arr[j-1]>val:
			arr[j]= arr[j-1]
			j-= 1
		arr[j]= val

# The following two functions are used 
# to perform quicksort on the array. 

# Partition function for quicksort
def partition(arr, low, high):
	pivot = arr[high]
	i = j = low
	for i in range(low, high):
		if arr[i]<pivot:
			arr[i], arr[j]= arr[j], arr[i]
			j+= 1
	arr[j], arr[high]= arr[high], arr[j]
	return j

# Function to call the partition function 
# and perform quick sort on the array
def quick_sort(arr, low, high):
	if low<high:
		pivot = partition(arr, low, high)
		quick_sort(arr, low, pivot-1)
		quick_sort(arr, pivot + 1, high)
		return arr

# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, low, high):
	while low<high:

		# If the size of the array is less 
		# than threshold apply insertion sort 
		# and stop recursion
		if high-low + 1<10:
			insertion_sort(arr, low, high)
			break

		else:
			pivot = partition(arr, low, high)

			# Optimised quicksort which works on 
			# the smaller arrays first

			# If the left side of the pivot 
			# is less than right, sort left part
			# and move to the right part of the array
			if pivot-low<high-pivot:
				hybrid_quick_sort(arr, low, pivot-1)
				low = pivot + 1
			else:
				# If the right side of pivot is less 
				# than left, sort right side and 
				# move to the left side
				hybrid_quick_sort(arr, pivot + 1, high)
				high = pivot-1



import time
import random


bestCase = list(range(1, 101))
worstCase = list(range(100, 0, -1))

#averageCase = [random.randint(1, 1000) for _ in range(100)]



start_timeADIS = time.time()

hybrid_quick_sort_adaptive(bestCase, 0, len(bestCase) - 1)


end_timeADIS = time.time()
print("Best Case hybrid quick adaptive sort execution time: ",end_timeADIS-start_timeADIS)

start_timeADIS = time.time()
hybrid_quick_sort_adaptive(worstCase, 0, len(worstCase) - 1)
end_timeADIS = time.time()
print("Worst Case hybrid quick adaptive sort execution time: ",end_timeADIS-start_timeADIS)

bestCase = list(range(1, 101))
worstCase = list(range(100, 0, -1))


start_timeIS = time.time()

hybrid_quick_sort(bestCase, 0, len(bestCase) - 1)


end_timeIS = time.time()
print("Best Case hybrid quick sort execution time: ",end_timeIS-start_timeIS)

start_timeIS = time.time()
hybrid_quick_sort(worstCase, 0, len(worstCase) - 1)
end_timeIS = time.time()
print("Worst case hybrid quick sort execution time: ",end_timeIS-start_timeIS)


print(end_timeADIS-start_timeADIS < end_timeIS-start_timeIS)


'''
BENCHMARKING RESULTS

-----------------------TEST 1-----------------------

Best Case hybrid quick adaptive sort execution time:  0.001001119613647461
Worst Case hybrid quick adaptive sort execution time:  0.001001119613647461

Best Case hybrid quick sort execution time:  0.002996683120727539
Worst case hybrid quick sort execution time:  0.0029985904693603516


-----------------------TEST 2-----------------------


Best Case hybrid quick adaptive sort execution time:  0.0009965896606445312
Worst Case hybrid quick adaptive sort execution time:  0.0

Best Case hybrid quick sort execution time:  0.0029990673065185547
Worst case hybrid quick sort execution time:  0.003001689910888672


-----------------------TEST 3-----------------------


Best Case hybrid quick adaptive sort execution time:  0.001001119613647461
Worst Case hybrid quick adaptive sort execution time:  0.0009989738464355469

Best Case hybrid quick sort execution time:  0.003000497817993164
Worst case hybrid quick sort execution time:  0.0029993057250976562


-----------------------TEST 4-----------------------


Best Case hybrid quick adaptive sort execution time:  0.0
Worst Case hybrid quick adaptive sort execution time:  0.0010023117065429688

Best Case hybrid quick sort execution time:  0.0029981136322021484
Worst case hybrid quick sort execution time:  0.0029976367950439453


'''
'''

the algorithm I went with is hybrid quicksort
this algorithm combines both quicksort and insertion sort. Insertion sort is better when the array is small, so the algorithm uses insertion sort when the array is small enough. Otherwise, it uses quicksort.
How I improved this algorithm is firstly 
I improved the insertion sort by making adding makeing use a binary search within the sorted portion of the array to find the correct position to determin where to insert each element
this reduces the number of comparisons compared to a standard insertion sort. I also improved the quicksort by making it a randomized quicksort. This is done by choosing a random element as pivot. 


All together my algorthim consistantly performs better than the traditional hybrid quicksort. I call it Hybrid Adaptive Quick Sort as it uses a little bit of both.


The binary search function performs a binary search within the sorted portion of the array to find the correct position for the current element.

The adaptive insertion sort function iterates through the array and uses binary search to determine where to insert each element. This reduces the number of comparisons compared to a standard insertion sort.

The binary search function returns the index where the key should be inserted to maintain the sorted order.

The elements are shifted to make space for the key, and the key is inserted at the correct position.





'''