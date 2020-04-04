def is_palindrome(word):
    d = {}
    for letter in word:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    
    evens = odds = 0
    for letter, count in d.items():
        if count % 2 == 0:
            evens += 1
        else:
            odds += 1
    if len(word) % 2 == 0:
        return odds == 0
    else:
        return odds == 1

word = 'civil'
print(is_palindrome(word))