def max_after_flip(arr, flips):
    max_count = 0
    i = 0
    j = 1
    for index, num in enumerate(arr):
        

arr = [0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
result = max_after_flip(arr, 2)
print(result)