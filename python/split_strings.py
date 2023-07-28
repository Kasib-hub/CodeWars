def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        # moving the slice as needed
        result.append(s[i:i+2])
    return result
    

print(solution('abc'))
print(solution('abcdef'))
print(solution('asdfadsf'))
print(solution('asdfads'))