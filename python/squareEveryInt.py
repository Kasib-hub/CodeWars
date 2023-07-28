num = 9119

# convert to str to split num. Convert back to int to square
# covert each square to str to concat. return the string as int
def square_digits(num):
    res = ''
    for digit in str(num):
        res += str(int(digit) * int(digit))
    return int(res)

print(square_digits(num))