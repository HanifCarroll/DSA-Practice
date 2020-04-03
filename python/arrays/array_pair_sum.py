pair_sum([1,3,2,2],4) # 2.  1 +3 and 2+2

def pair_sum(arr, k):
    if len(arr) < 2:
        return # error

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        # The second time we go through 'target' will be 'num' from the first time.
        else:
            output.add( (min(num, target), max(num, target)) ) 
    return output