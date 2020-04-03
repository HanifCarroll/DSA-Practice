def count_evens(arr):
    return count_evens2(arr, 0)

def count_evens2(arr, i):
    if i >= len(arr):
        return 0
    result = count_evens2(arr, i+1)
    if arr[i] % 2 == 0:
        result += 1
    return result

evens = [2, 3, 4, 5, 6]
print(count_evens(evens))