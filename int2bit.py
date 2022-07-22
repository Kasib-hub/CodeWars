
# int to bitstring. Count 1's in the string
def count_bits(n):
    # format gives string
    str = format(n, 'b')
    return str.count('1')

print(count_bits(8))
print(count_bits(16))