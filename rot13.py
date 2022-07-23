def rot13(message):
    lower = message.lower()
    str = []
    for i, char in enumerate(lower):
        str.append(chr(ord(char) + 13))
        if str[i].upper() == str[i].lower():
            str[i] = chr(ord(char) - 13)
        elif char.upper() == message[i] and ord(message[i]) > 77 and ord(message[i]) < 91: 
           str[i] = str[i].upper()
    return ''.join(str)
    pass

print(rot13('test'))
print(rot13('Test'))
print(rot13('Kasib'))
print(rot13('Kaya'))