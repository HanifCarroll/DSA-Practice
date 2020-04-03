def merge_lists(a, b):
    results = []
    while a and b:
        if not a:
            for item in b:
                results.append(item)
        elif not b:
            for item in a:
                results.append(item)
        elif a[0] < b[0]:
            results.append(a.pop(0))
        else:
            results.append(b.pop(0))
    return results
my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
