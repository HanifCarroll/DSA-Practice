def compress_string(string):
    if len(string) <= 1:
        return string
    new_string = ''
    count = 0
    prev_letter = string[0]

    for letter in string:
        if letter != prev_letter:
            new_string += f'{count}{prev_letter}'
            count = 0
            prev_letter = letter
        count += 1
    new_string += f'{count}{string[-1]}'
    return new_string

print(compress_string(''))