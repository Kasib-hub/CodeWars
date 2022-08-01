from collections import Counter

def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    dir = Counter(walk)
    
    if dir['n'] != dir['s'] or dir['e'] != dir['w']:
        return False

    return True 

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))