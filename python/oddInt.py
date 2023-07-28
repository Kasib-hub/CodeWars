def find_it(seq):
    for num in seq:
        # count gives number of instances within the list
        if seq.count(num) % 2 != 0:
            return num

print(find_it('aabbbcc'))