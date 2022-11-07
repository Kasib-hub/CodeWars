def snail(snail_map):
    res = []
    # pop off values as you iterate
    while snail_map:
        # top of list
        for lst in snail_map[0]:
            res.append(lst)
        
        snail_map.pop(0)
        if not snail_map:
            break
        # right side
        for arr in snail_map:
            res.append(arr[-1])
            arr.pop()
        # bottom side
        snail_map[-1].reverse()
        for item in snail_map[-1]:
            res.append(item)
            
        snail_map.pop()
        # left side
        for item in reversed(snail_map):
            res.append(item[0])
            item.pop(0)
        
    return res

print(snail([
    [1, 2, 3],
    [6, 5, 4],
    [9, 8, 7]
]))