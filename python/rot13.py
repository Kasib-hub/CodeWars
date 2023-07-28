import enum


def rot13(message):
    res = []
    lower_str = [x.lower() for x in message]
    for i, char in enumerate(message):
        if char.isalpha():
            shift_char = chr(ord(lower_str[i]) + 13)

            if not shift_char.isalpha():
                shift_char = chr(ord(lower_str[i]) + 13 - 26)
            res.append(shift_char)

            if char == char.upper():
                res[i] = res[i].upper()
        else:
            res.append(char)
            
    return ''.join(res)


print(rot13('test'))
print(rot13('Test'))
print(rot13('Kasib'))
print(rot13('Kaya'))