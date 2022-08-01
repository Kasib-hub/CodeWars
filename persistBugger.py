import math


def persistence(n):
    count = 0
    while len(str(n)) != 1:
        list = []
        for num in str(n):
            list.append(int(num))
        n = math.prod(list)
        count += 1
    return count
    pass

print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))