from collections import Counter

def anagrams(word, words):
    word_obj = Counter(word)
    res = []
    for item in words:
        temp_obj = Counter(item)
        if word_obj == temp_obj:
            res.append(item)
    return res


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
