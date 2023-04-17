import math
def solution(s, t):
#     distance = speed * time
#     speed * 2 for one unit of time
#     speed decreased by 1 afterwards and 1 unit of time can't sprint
#     get maximum possible distance
    distance = s * t
    
#     max sprints will always be half the time, round up for odd times
# for each max sprint, check if the distance is greater than 3 which is the minimum distance to sprint
    max_sprints = math.ceil(t / 2)
    for i in range(max_sprints):
        
        # checking if the distance is greater than 3 at each sprint
        if (s - 3 * i > 0):
            distance += s - 3 * i
    return distance
    pass

print(solution(2,4)) # 10