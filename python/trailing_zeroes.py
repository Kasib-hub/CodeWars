
def zeros(n):
    if n < 2:
        return 0
    count = 0
    while (n >= 5):
        n //= 5   
        count += n 
    return count
    pass
    

print(zeros(0))
print(zeros(6))
print(zeros(30))
print(zeros(12))