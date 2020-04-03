nums = [4, 9, 11, 23, 45, 56, 112, 153, 243, 435, 456, 657]

def binary_search(arr, value):
    return b_search(arr, value, 0, len(arr) - 1)

def b_search(arr, value, left, right):
    if left > right:
        return False
    middle = left + (right - left) // 2
    if value == arr[middle]:
        return middle
    elif value < arr[middle]:
        return b_search(arr, value, left, middle -1)
    elif value > arr[middle]:
        return b_search(arr, value, middle + 1, right)
print(binary_search(nums, 49))