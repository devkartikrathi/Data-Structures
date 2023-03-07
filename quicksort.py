def part(arr, left, right):
    piv = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= piv:
            i= i+1
            (arr[i], arr[j]) = (arr[j], arr[i])
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1
def quicksort(arr, left, right):
    if left<right:
        pi = part(arr, left, right)
        quicksort(arr, left, pi - 1)
        quicksort(arr, pi+1, right)
arr = [1, 3, 4, 2, 6, 7]
quicksort(arr, 0, len(arr)-1)
print(arr)