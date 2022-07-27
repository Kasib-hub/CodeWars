# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]

def sort_array(source_array):
    arr = []
    for i, num in enumerate(source_array):
        if num % 2 != 0:
            arr.append(num)
            source_array[i] = 'a'
    # sorts in place so just do it before returning
    arr.sort()
    for j in range(len(source_array) -1, -1, -1):
        if source_array[j] == 'a':
            source_array[j] = arr.pop()
    return source_array
    
    # obj = {}
    # for i, num in enumerate(source_array):
    #     if num % 2 != 0:
    #         obj[num] = i
    # return obj

print(sort_array([5, 8, 6, 3, 4]))