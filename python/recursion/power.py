def power_recursive(a, b):
    if b == 1:
        return a
    return a * power_recursive(a, b-1)

print(power_recursive(4, 4))