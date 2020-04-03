def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_cached(n, cache=None):
    if n <= 1:
        return n
    if cache is None:
        cache = [None] * (n + 1)
    if cache[n]:
        return cache[n]
    cache[n] = fib_cached(n-1, cache) + fib_cached(n-2, cache)
    return cache[n]

def fib_iterative(n):
    a = 0
    b = 1
    for i in range(n):
        total = a + b
        a = b
        b = total
    return a

# print(fib_cached(998))
# print(fib_iterative(22998))