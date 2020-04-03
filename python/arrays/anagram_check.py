import collections
def is_anagram(str1: str, str2: str) -> bool:
    s1 = str1.lower().replace(' ', '')
    s2 = str2.lower().replace(' ', '')

    if len(s1) != len(s2):
        return False

    counts = collections.defaultdict(int)

    for letter in s1:
        counts[letter] += 1
    for letter in s2:
        counts[letter] -= 1
    
    for value in counts.values():
        if value:
            return False
    return True


print(is_anagram('old west action', 'clint eastwood'))