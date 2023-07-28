
def collatz(n):
    ans = []
    ans.append(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
            ans.append(n)
        else:
            n = n * 3 + 1
            ans.append(n)
    return '->'.join([str(x) for x in ans])
    pass

print(collatz(4))
print(collatz(3))