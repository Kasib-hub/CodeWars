def valid_parentheses(string):
    left = string.count('(')
    right = string.count(')')
    if left != right:
        return False
        
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')' and len(stack) > 0:
            stack.pop()
        elif char == ')':
            return False
    if len(stack) > 0:
        return False
    return True
    
    

print(valid_parentheses('()')) #True
print(valid_parentheses(')(()))')) #false
print(valid_parentheses('(')) #false
print(valid_parentheses('(())((()())())')) #true
print(valid_parentheses('hi())(')) #false
print(valid_parentheses('hi(hi)()')) #True