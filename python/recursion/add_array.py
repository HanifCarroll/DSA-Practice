def add_array(arr):
    if len(arr) == 0:
        return 0
    
    return arr[0] + add_array(arr[1:])

arr = [1, 2, 8, 4, 5]

print(add_array(arr))

def count_list(arr):
    if len(arr) == 0:
        return 0
    return 1 + count_list(arr[1:])

print(count_list(arr))

def find_max(arr):
    if len(arr) == 0:
        return 0
    return max(arr[0], find_max(arr[1:]))
print(find_max(arr))