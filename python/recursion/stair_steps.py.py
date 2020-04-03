def count_paths(steps):
    if steps < 0:
        return 0
    if steps <= 1:
        return 1
    paths = [None] * (steps + 1)
    paths[0] = 1
    paths[1] = 1
    paths[2] = 2
    for i in range(3, steps + 1):
        paths[i] = paths[i - 1] + paths[i - 2] + paths[i - 3]
    return paths[steps]

print(count_paths(100))

def count_paths2(steps):
    if steps < 0:
        return 0
    if steps <= 1:
        return 1
    paths = [1, 1, 2]
    for i in range(3, steps + 1):
        total = sum(paths)
        paths[0] = paths[1]
        paths[1] = paths[2]
        paths[2] = total
    return paths[2]
print(count_paths2(100))

def count_paths3(steps):


print(count_paths3(100))