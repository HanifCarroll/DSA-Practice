def merge_times(array):
    result = []
    for index, (start1, end1) in enumerate(array):
        if start1 == -1:
            continue
        start_time = start1
        end_time = end1
        for i in range(index+1, len(array)):
            start2, end2 = array[i]
            
            if (max(start_time, start2) <= min(end_time, end2)):
                start_time = min(start_time, start2)
                end_time = max(end_time, end2)
                array[i] = (-1, -1)
        result.append((start_time, end_time))
    result.sort(key=lambda tup: tup[0])
    return result

times = [(0,1), (3,5), (4,8), (10,12), (9,10)]
result = merge_times(times)
print(result)