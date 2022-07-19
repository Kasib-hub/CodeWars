
def invert(lst):
    for i, num in enumerate(lst):
        if num > 0:
            lst[i] = -num
        elif num < 0:
            lst[i] = abs(num)
    return lst

arr = [1, -2, 3, -4, 5]
print(invert(arr))