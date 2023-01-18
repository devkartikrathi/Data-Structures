def selection_sort(l):

    for i in range(len(l)):
        key = i
        for j in range(i+1, len(l)):
            if l[key]>l[j]:
                key = j
        l[key], l[j] = l[j], l[key]

    return l

print(selection_sort([3, 2, 1, 5, 4]))