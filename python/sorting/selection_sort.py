def selection_sort(arr):
    result = []
    for i in range(len(arr)):
        smallest_index = get_smallest_element_index(arr)
        result.append(arr.pop(smallest_index))
    return result

def get_smallest_element_index(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


arr = [4, 8, 3, 1, 2]

print(selection_sort(arr))