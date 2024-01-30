arr = [5,7,4,3,8,2,9]
print(arr)

for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)