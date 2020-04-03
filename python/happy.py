def get_digits(x):
    digits = []
    for i in range(len(str(x))):
        digits.append(x % 10)
        x //= 10
    return digits

def is_happy(x):
    digits = get_digits(x)
    seen = set()
    while True:
        total = 0
        for num in digits:
            total += num ** 2
        if total == 1:
            return True
        if total in seen:
            return False
        seen.add(total)
        digits = get_digits(total)
        total = 0

print(is_happy(15))
    