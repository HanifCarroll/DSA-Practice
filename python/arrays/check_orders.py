def is_in_order(a, b, c):
    p1 = p2 = 0
    for order in c:
        if p1 < len(a) and order == a[p1]:
            p1 += 1
        elif p2 < len(b) and order == b[p2]:
            p2 += 1
        else:
            return False
    return True

a = [1, 3, 5]
b = [2, 4, 6]
good = [1, 2, 3, 5, 4, 6]
bad = [1, 2, 4, 6, 5, 3]

print(is_in_order(a, b, bad))