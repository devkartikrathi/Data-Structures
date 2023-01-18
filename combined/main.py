import numpy as np
import seaborn as sns
import random
import time
import matplotlib.pyplot as plt

class gen:

    def generator(s, e, i):
        l = list(np.random.randint(s, e, i))
        l.sort()
        return l

class analysis:

    def graph(x):
        tm = []
        itr = [10, 100, 1000, 10000, 25000, 50000, 75000, 100000]
        for i in itr:
            l = gen.generator(1, 100, i)
            if x == 'linear_search' :
                start = time.time()
                search.linear_search(l, random.randint(1, 100))
                end = time.time()
                tm.append(end-start)
            elif x == 'binary_search' :
                start = time.time()
                search.binary_search(l, random.randint(1, 100))
                end = time.time()
                tm.append(end-start)
            elif x == 'bubble_sort':
                start = time.time()
                sort.bubble_sort(l)
                end = time.time()
                tm.append(end-start)
            elif x == 'insertion_sort':
                start = time.time()
                sort.insertion_sort(l)
                end = time.time()
                tm.append(end-start)
        sns.lineplot(x = itr, y = tm)
        plt.show()

class search:

    def linear_search(a, x):
        d = 0
        found = False
        #print(a)
        for i in a:
            d+=1
            if d<len(a):
                if x == i:
                    print(f'{x} is present at {d} position')
                    found = True
            else:
                if found == False:
                    print(f'{x} not found.')
        return "Task completed..."

    def binary_search(a, x):

        def calc(a, x, low, high):
            while high>0:
                mid = (low+high)//2
                if x == a[mid]:
                    return mid, a
                elif mid==high:
                    return 'Not Found', a
                elif x>a[mid]:
                    low = mid+1
                    calc(a, x, low, high)
                else:
                    high = mid-1
                    calc(a, x, low, high)
            else:
                return 'Not Found', a

        low = 0
        high = len(a)
        return calc(a, x, low, high)

class sort:

    def bubble_sort(a):
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(a)-1):
                if a[i]>a[i+1]:
                    a[i], a[i+1] = a[i+1], a[i]
                    sorted = False
        return a

    def insertion_sort(a):
        for i in range(1, len(a)):
            key = a[i]
            j = i-1
            while j >=0 and key < a[j] :
                a[j+1] = a[j]
                j = j - 1
            a[j+1] = key
        return a

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
		sort.merge_sort(L)
		# Sorting the second half
		sort.merge_sort(R)
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
            sort.quick_sort(array, low, pi - 1)
            # Recursive call on the right of pivot
            sort.quick_sort(array, pi + 1, high)

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