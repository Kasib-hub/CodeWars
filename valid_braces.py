
def valid_braces(string):
    braces = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    stack = []
    for char in string:
        if char in braces:
            stack.append(char)
        elif len(stack) > 0 and char == braces[stack[-1]]:
            stack.pop()
    
    return False if len(stack) > 0 else True

    pass

print(valid_braces("(){}[]"))
print(valid_braces("([{}])"))
print(valid_braces("(}"))
print(valid_braces("[(])"))
print(valid_braces("[({})](]"))