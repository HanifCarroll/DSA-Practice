def reverse_message(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left, right = left + 1, right - 1
    
    left = right = 0
    while left <= len(arr) - 1:
        while right + 1 < len(arr) and arr[right + 1] != ' ':
            right += 1
        original_start, original_end = left, right

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
        
        left = right = original_end + 2
    return ''.join(arr)

message = list('This is a secret message')
# print(reverse_message(message))
def give_nums(x):
    ans = []
    for i in range(len(str(x))):
        ans.append(x % 10)
        x //= 10
    return list(reversed(ans))

print(give_nums(210))
# print(len(str(210)))
        