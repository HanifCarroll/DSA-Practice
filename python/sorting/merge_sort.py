def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    left_index = 0
    right_index = 0
    result = []
    while len(result) < len(left) + len(right):
        if ((left_index < len(left)) and (right_index == len(right)) or (left[left_index] < right[right_index])):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result
arr = [4, 2, 3, 6, 5, 1]
print(merge_sort(arr))