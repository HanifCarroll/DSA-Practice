def min_coins(target, coins, computed=None):
    if computed is None:
        computed = {}
    minimum_coins = target
    
    if target in coins:
        computed[target] = 1
        return 1
    
    elif target in computed and computed[target] > 0:
        return computed[target]
    
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + min_coins(target - i, coins, computed)
            if num_coins < minimum_coins:
                minimum_coins = num_coins
                computed[target] = minimum_coins

    return minimum_coins

print(min_coins(15, [1, 5, 10, 20]))

