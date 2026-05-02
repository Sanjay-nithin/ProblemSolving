def partition(left, right):
    pivot = arr[right]
    i = left-1
    for j in range(left, right):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1

def quicksort(arr, left, right):
    if left < right:
        pi = partition(left, right)
        quicksort(arr, left, pi-1)
        quicksort(arr, pi+1, right)

arr = [10, 8, 9, 5, 1, 7]
quicksort(arr, 0, 5)
print(arr)