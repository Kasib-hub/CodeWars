# getting the time it takes to clear arr with n tills available

def queue_time(customers, n):
    if n == 1:
        return sum(customers)

    if n >= len(customers):
        return max(customers)

    till = [0] * n
    # sort the queue arr until you can populate the tills
    for person in customers:
        till.sort()
        till[0] += person
    return max(till)

print(queue_time([5,3,4], 1))
print(queue_time([10,2,3,3], 2))