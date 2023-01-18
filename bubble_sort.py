def bubble_sort(a):

    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                sorted = False
    return a

print(bubble_sort([1, 3, 4, 2, 6, 7]))