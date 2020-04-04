def move_zeros(nums):
    for i, num in enumerate(nums):
        if num == 0:
            nums.append(nums.pop(i))
    return nums

test = [0, 1, 0, 3, 17]
print(move_zeros(test))