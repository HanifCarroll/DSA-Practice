from collections import defaultdict
def finder(arr1, arr2):
    d = defaultdict(int)
    for num in arr1:
        d[num] += 1
    for num in arr2:
        d[num] -= 1
    for num, count in d.items():
        if count:
            return num
    return None

arr1 = [4,2,1,6]
arr2 = [4,6,2]
print(finder(arr1, arr2))