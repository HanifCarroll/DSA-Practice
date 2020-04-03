def largest_continuous_sum(arr):
    top_sum = 0
    top_nums = []
    end = len(arr)
    for i in range(end):
        for j in range(i + 1, end):
            total = sum(arr[i:j + 1])
            if total > top_sum:
                top_sum = total
                top_nums = [i, j]
    return (top_sum, top_nums)

my_list = [1, 2, -1, 3, 4, -1]
my_list2 = [1,2,-1,3,4,10,10,-10,-1]
my_list3 = [-1, 1]
print(largest_continuous_sum(my_list2))