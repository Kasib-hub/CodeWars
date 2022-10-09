
def multiplication_table(size):
    dict = {}
    res = []
    for i in range(size):
        dict[i] = [i+1]
        for j in range(2, size+1):
            dict[i].append(j * (i+1))

    for prop in dict:
        res.append(dict[prop])
    
    return res

print(multiplication_table(3))
print(multiplication_table(4))