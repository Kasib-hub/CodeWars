def tower_builder(n_floors):
    star_var = 1
    stars = []
    spaces = []
    res = []
    space_length = n_floors - 1
    j = 0
    for i in range(1, n_floors + 1):
        stars.append('*' * star_var)
        spaces.append(' ' * space_length)
        star_var += 2
        space_length -= 1
        res.append(f'{spaces[j]}{stars[j]}{spaces[j]}')
        j += 1
    
    return res
    # for prop in pyramid:
    #     space = '*'.ljust(3).rjust(3)
    #     res.append('*' * pyramid[prop])
    # return res

print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(5))
print(tower_builder(7))