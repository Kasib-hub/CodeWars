def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    elif len(array1) != len(array2):
        return False
    array1 = [abs(x) for x in array1]
    array1.sort()
    array2.sort()
    for i, num in enumerate(array1):
        if num ** 2 != array2[i]:
            return False
    return True
    pass

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]))