def merge(left, right):
    l = r = 0
    m, n = len(left), len(right)    
    res = []
    while l < m and r < n:
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res.extend(left[l:])
    res.extend(right[r:])

    return res

def mergeSort(arr, low, high):
    if low == high:
        return [arr[low]]
    
    mid = low + (high-low)//2
    left = mergeSort(arr, low , mid)
    right = mergeSort(arr, mid+1, high)

    return merge(left, right)
    

arr = [10, 8, 9, 5, 1, 7]
print(mergeSort(arr, 0, 5))