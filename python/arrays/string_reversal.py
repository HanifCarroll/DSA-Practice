def reverse_string(string):
    if len(string) <= 1:
        return string
    res = []
    arr = string.strip().split(' ')
    idx = len(arr) - 1
    while idx >= 0:
        res.append(arr[idx])
        idx -= 1
    return ' '.join(res)

print(reverse_string('   This is a string'))
