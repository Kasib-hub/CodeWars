def sum_dig_pow(a, b):
    ans = []
    for i in range(a, b +1):
        sum = 0
        count = 1
        for digit in str(i):
            sum += int(digit) ** count
            count += 1
            pass
        if i == sum:
            ans.append(i)
    return ans

print(sum_dig_pow(1, 10))
print(sum_dig_pow(1, 100))
print(sum_dig_pow(10, 89))
