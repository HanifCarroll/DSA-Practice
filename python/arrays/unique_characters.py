def unique_characters(string):
    d = {}
    for letter in string:
        if not letter in d:
            d[letter] = 1
        else:
            return False
    return True

def unique_characters2(string):
    return len(set(string)) == len(string)

print(unique_characters2('abc'))