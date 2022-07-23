def find_outlier(integers):
    parity = {
        'even': [],
        'odd': []
    }
    for num in integers:
        if num % 2 == 0:
            parity['even'].append(num)
        else:
            parity['odd'].append(num)

    for prop in parity:
        if len(parity[prop]) == 1:
            return parity[prop].pop()


print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))