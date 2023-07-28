
import math

def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True
    
    root_floor = math.isqrt(num)
    if math.sqrt(num) == root_floor:
        return False
    
    for i in range(2, root_floor + 1):
        if num % i == 0:
            return False
    return True
    


print(is_prime(73))
print(is_prime(75))
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(-1))
print(is_prime(64))
