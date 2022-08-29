def wave(people):
    if people == '':
        return []
    res = []
    for i in range(len(people)):
        temp = list(people)
        if temp[i] != ' ':
            temp[i] = temp[i].upper()
            res.append(''.join(temp))
    return res
    pass

print(wave('hello'))
print(wave('codewars'))
print(wave(''))