arr = [1, 2, 3, 4, 5, 6]

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

print(sum_array(arr))