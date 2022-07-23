def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

print(get_count('kasib'))
print(get_count('kaya abdullah'))
print(get_count('tykesha baker'))