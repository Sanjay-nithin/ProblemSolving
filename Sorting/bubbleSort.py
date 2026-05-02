arr = [23,1,54,2,2,7,47,4]
n = len(arr)

for i in range(n):
    flag = True
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = False
    if flag:
        break
        
print(arr)
