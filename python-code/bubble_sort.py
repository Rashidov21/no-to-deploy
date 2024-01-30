arr = [5,7,4,3,8,2,9]
print(arr)
count = 0
for iter in range(len(arr) - 1):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count += 1
print(arr)
print(count)