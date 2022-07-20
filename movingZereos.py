# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(lst):
    # cut out zeroes
    # append the zeroes
    res = [x for x in lst if x != 0]
    for i in range(lst.count(0)):
        res.append(0)
    return res

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))