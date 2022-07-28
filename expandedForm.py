# expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(num):
    # reverses the string of numbers
    res = []

    for i, digit in enumerate(str(num)[::-1]): # ::-1 reverses the string
        if int(digit) != 0:
            res.append(digit + ('0' * i)) # you can multiply strings
    
    return ' + '.join(res[::-1])

print(expanded_form(70304))
print(expanded_form(12))