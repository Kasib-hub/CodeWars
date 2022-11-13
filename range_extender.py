def solution(args):
    print(list(range(1,3)))
    res = []
    temp = []
    for i, num in enumerate(args):
        try:
            if args[i-1] == num - 1 and args[i+1] == num + 1 and num not in temp:
                if temp:
                    res.append(temp)
                    temp = []
                temp.append(num-1)
                temp.append(num)
                temp.append(num+1)
            elif args[i-1] != num - 1 and args[i+1] != num + 1 and num not in temp:
                if temp:
                    res.append(temp)
                    temp = []
                temp.append(num)
            
        except:
            print(f'{num} not in range')
    res.append(temp)
    return res
    pass
print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])) # "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"