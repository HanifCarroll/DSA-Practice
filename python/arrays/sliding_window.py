def find_sum(arr, target):
    results = []
    i = 0
    j = 1
    while i < len(arr):
        total = sum(arr[i:j+1])
        if total == target:
            results.append(arr[i:j+1])
            i += 1
            if j < len(arr):
                j += 1
        elif total > target:
            i += 1
        else:
            if j < len(arr):
                j += 1
            else:
                i += 1
            
    return results

array = [1, 4, 2, 3, 5, 3, 6, 2, 1, 5]
result = find_sum(array, 8)
for array in result:
    print(array)