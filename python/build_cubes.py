
from tkinter import N


def find_nb(m):
    total = 0
    count = 0
    while total < m:
        count += 1
        total += count**3
        
    if total == m:
        return count
    return -1

print(find_nb(4183059834009))
print(find_nb(24723578342962))