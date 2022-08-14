from collections import Counter

def dirReduc(arr):
    direct = [('NORTH', 'SOUTH'), ('SOUTH', 'NORTH'), ('EAST', 'WEST'), ('WEST', 'EAST')]
    obj = {key:value for (key, value) in direct}
    res = []
    
    for item in arr:
        if len(res) == 0:
            res.append(item)
        elif obj[item] == res[-1]:
            res.pop()
        else:
            res.append(item)
    return res
        
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
