
def digital_root(n):
    if n < 10:
        return n
    
    digit = 0
    for num in str(n):
        digit += int(num)
        
    return digital_root(digit)

print(digital_root(16))
print(digital_root(942))