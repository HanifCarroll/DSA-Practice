def quick_sort_reference(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort(arr):
    pass

    
arr = [4, 2, 1, 7, 5, 3]
print(quick_sort(arr))