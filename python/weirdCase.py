
def to_weird_case(words):
    count = 0
    result = ''
    for letter in words:
        if letter == ' ':
            result += letter
            count = 0
        else:
            if count % 2 == 0:
                result += letter.upper()
            else:
                result += letter.lower()
            count += 1
    return result

print(to_weird_case('String'))
print(to_weird_case('Weird string case'))