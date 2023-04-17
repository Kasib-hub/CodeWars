def solution(args):
    res = []
    temp = [args[0]]
    left, length = 0, 0
    for i in range(1, len(args)):
        print(temp)
        if args[i] != args[i-1] + 1:
            print(f"selected {args[i]}")
            if len(temp) > 1:
                res.append(temp)
                temp.clear()
        temp.append(args[i])
        # print(temp)
    print(res)
    pass
print(solution([-10,-9,-8,-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) # "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"