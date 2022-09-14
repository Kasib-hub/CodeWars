def sum_pairs(ints, s):
    if ints == []:
        return None

    map = {}
    for i, num in enumerate(ints):
        diff = s - num
        if diff in map:
            return [ints[map[diff]], ints[i]]
        map[num] = i
    # arr has the indices of nums that make the sum, return the sorted lowest 2nd sp

print(sum_pairs([11, 3, 7, 5], 10))
print(sum_pairs([4, 3, 2, 3, 4], 6))
print(sum_pairs([0, 0, -2, 3], 2))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
