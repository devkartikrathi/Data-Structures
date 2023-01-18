def find_min(l, n):

    if n == 1:
        return l[0]
    else:
        return min(l[n-1], find_min(l, n-1))

a = [3, 4, 6 , 7, 9, 10, 5, 2, 8, -50]

print(find_min(a, len(a)))

min = a[0]
for i in range(1, len(a)):
    if a[i]<min:
        min = a[i]
print(min)