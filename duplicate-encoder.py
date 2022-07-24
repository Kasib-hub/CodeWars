



def duplicate_encode(word):
    str = ''
    for char in word.lower():
        if word.lower().count(char) > 1:
            str += ')'
        else:
            str += '('
    return str
    

print(duplicate_encode('Success'))
print(duplicate_encode('recede'))
