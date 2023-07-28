# case insensitive, only digits and letters
def duplicate_count(text):
    obj = {}
    for item in text.lower():
        if item not in obj:
            obj[item] = 1
        else:
            obj[item] += 1
    
    return len([x for x in obj if obj[x] > 1])

print(duplicate_count('abcde'))
print(duplicate_count('aabbccddeeee'))