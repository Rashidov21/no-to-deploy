
# Quick Sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    elem = arr[len(arr)//2]
    
    right = list(filter(lambda x: x > elem, arr))
    center = [i for i in arr if i == elem]
    left = list(filter(lambda x: x < elem, arr))
    
    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([7,2,3,5,4,9,7,1]))