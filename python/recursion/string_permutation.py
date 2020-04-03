def permutate(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        # For every letter in string
        for i, letter in enumerate(s):

            # For every permutation
            for perm in permutate(s[:i] + s[i + 1:]):
                print('Perm is', perm)

                # Add to output
                out += [letter + perm]
    return out

def permutate2(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i, letter in enumerate(s):
            for string in permutate2(s[:i] + s[i+1:]):
                out += [letter + string]

    return out
print(permutate2('abc'))