def selection_sort(l):

    for i in range(len(l)):
        k = i
        for j in range(i, len(l)):
            if l[j] < l[k]:
                l[j], l[k] = l[k], l[j]
    return l

print(selection_sort([3, 2, 1, 5, 4]))