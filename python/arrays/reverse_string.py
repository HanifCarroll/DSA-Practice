def reverse_arr(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left, right = left + 1, right - 1
    return arr

arr = list('weirds')
print(reverse_arr(arr))