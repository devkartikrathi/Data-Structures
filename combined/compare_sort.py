from main import gen 
import seaborn as sns
import matplotlib.pyplot as plt
import time
import pandas as pd

def bubble_sort(a):

    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                sorted = False

def insertion_sort(l):

    for i in range(1, len(l)):
        x = l[i]
        j = i-1
        while j >=0 and x < l[j] :
            l[j+1] = l[j]
            j-=1
        l[j+1] = x

def selection_sort(a):

    for step in range(len(a)):
        min_idx = step
        for i in range(step + 1, len(a)):
            if a[i] < a[min_idx]:
                min_idx = i
        (a[step], a[min_idx]) = (a[min_idx], a[step])

def merge_sort(arr):

	if len(arr) > 1:
		# Finding the mid of the array
		mid = len(arr)//2
		# Dividing the array elements
		L = arr[:mid]
		# into 2 halves
		R = arr[mid:]
		# Sorting the first half
		merge_sort(L)
		# Sorting the second half
		merge_sort(R)
		i = j = k = 0
		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def quick_sort(array, low, high):
        def partition(array, low, high):
            # Choose the rightmost element as pivot
            pivot = array[high]
            # Pointer for greater element
            i = low - 1
            # Traverse through all elements
            # compare each element with pivot
            for j in range(low, high):
                if array[j] <= pivot:
                    # If element smaller than pivot is found
                    # swap it with the greater element pointed by i
                    i = i + 1
                    # Swapping element at i with element at j
                    (array[i], array[j]) = (array[j], array[i])
            # Swap the pivot element with
            # e greater element specified by i
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            # Return the position from where partition is done
            return i + 1
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = partition(array, low, high)
            # Recursive call on the left of pivot
            quick_sort(array, low, pi - 1)
            # Recursive call on the right of pivot
            quick_sort(array, pi + 1, high)

def heap_sort(arr):
    def heapify(arr, N, i):
        largest = i # Initialize largest as root
        l = 2 * i + 1	 # left = 2*i + 1
        r = 2 * i + 2	 # right = 2*i + 2
        # See if left child of root exists and is
        # greater than root
        if l < N and arr[largest] < arr[l]:
            largest = l
        # See if right child of root exists and is
        # greater than root
        if r < N and arr[largest] < arr[r]:
            largest = r
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] # swap
            # Heapify the root.
            heapify(arr, N, largest)
    N = len(arr)
	# Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)
	# One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

tm_b, tm_i, tm_s, tm_m, tm_q, tm_h = [], [], [], [], [], []

itr = [10, 100, 1000, 2000]
for i in itr:
    l = gen.generator(1, 100, i)
    # start = time.time()
    # bubble_sort(l)
    # end = time.time()
    # tm_b.append(end-start)
    # start = time.time()
    # insertion_sort(l)
    # end = time.time()
    # tm_i.append(end-start)
    # start = time.time()
    # selection_sort(l)
    # end = time.time()
    # tm_s.append(end-start)
    start = time.time()
    merge_sort(l)
    end = time.time()
    tm_m.append(end-start)
    start = time.time()
    quick_sort(l, 0, len(l)-1)
    end = time.time()
    tm_q.append(end-start)
    start = time.time()
    heap_sort(l)
    end = time.time()
    tm_h.append(end-start)


data = {'itr' : [10, 100, 1000, 2000]
        # , 'i' : tm_i, 'b' : tm_b, 's' : tm_s
        , 'm' : tm_m, 'q' : tm_q, 'h' : tm_h}
df = pd.DataFrame(data)

# plt.plot(df['itr'], df['i'], color='green', label='Insertion Sort')
# plt.plot(df['itr'], df['b'], color='red', label='Bubble Sort')
# plt.plot(df['itr'], df['s'], color='blue', label='Selection Sort')
plt.plot(df['itr'], df['m'], color='pink', label='Merge Sort')
plt.plot(df['itr'], df['q'], color='orange', label='Quick Sort')
plt.plot(df['itr'], df['h'], color='cyan', label='Heap Sort')
plt.legend()
plt.show()