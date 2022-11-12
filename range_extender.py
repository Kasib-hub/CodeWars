def solution(args):
    res = []
    temp = []
    for i in range(len(args) - 2):
        if args[i] + 1 == args[i+1]:
            temp.append(args[i])
        else:
            while len(temp) > 2:
                temp.pop(len(temp)//2)
            res.append(temp)
            temp = []
    return res

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])) # "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"