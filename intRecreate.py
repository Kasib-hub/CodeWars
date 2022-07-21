import math

def divisors(num):
    arr = []
    for i in range(1, num + 1):
        if num % i == 0:
            arr.append(i*i)
    square_sum = sum(arr)
    if math.sqrt(square_sum) == round(math.sqrt(square_sum)):
        return [num, square_sum]

def list_squared(m, n):
    res = []
    for i in range(m, n + 1):
        if divisors(i):
            res.append(divisors(i))
    # your code
    return res
print(list_squared(250, 500))
print(list_squared(1, 250))
# return the number from which the divisors came from
# and the the sum of those divisors