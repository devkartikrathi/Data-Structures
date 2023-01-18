import numpy as np

def gen(s, e, i):
    l = list(np.random.randint(s, e, i))
    l.sort()
    return l

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

def binary_search(x, s, e, i):
    a = gen(s, e, i)
    low = 0
    high = len(a)
    return calc(a, x, low, high)

print(binary_search(5, 1, 100, 10))

def rec_binary_search(l, left, right, n):
    if left>right:
        return -1

    mid = (left+right)//2

    if n == l[mid]:
        return ('Found')
    elif n>l[mid]:
        return (rec_binary_search(l, mid+1, right, n))
    else:
        return (rec_binary_search(l, left, mid-1, n))

left = 0
right = 100

print(rec_binary_search(gen(1, 100, 10), left, right, 5))