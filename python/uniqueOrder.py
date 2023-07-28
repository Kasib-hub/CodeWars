# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']

from collections import Counter

def unique_in_order(iterable):
    prev = None
    ans = []
    for item in iterable:
        if item != prev:
            ans.append(item)
            prev = item
    return ans

print(unique_in_order('AAAABBBCCDAABBB'))