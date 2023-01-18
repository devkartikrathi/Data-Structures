def insertion_sort(l):

    for i in range(1, len(l)):
        x = l[i]
        j = i-1
        while j >=0 and x < l[j] :
            l[j+1] = l[j]
            j-=1
        l[j+1] = x
    return l

print(insertion_sort([10, 5, 7, 2]))

def rec_insertion_sort(l):
    pass

dean.soet@krmangalam.edu.in