arr = [23,1,54,2,2,7,47,4]
n = len(arr)

for i in range(1, n):
    j = i-1 
    key = arr[i]

    while j >= 0 and arr[j] >= key:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key

print(arr)