
def score(dice):
    scores = {
        '1': 1000,
        '2': 200,
        '3': 300,
        '4': 400,
        '5': 500,
        '6': 600
    }
    dice_rolls = {}

    # populate dictionary with roll amounts
    for num in dice:
        dice_rolls[num] = 1 + dice_rolls.get(num, 0)
    
    # iterating through key,value pair in dictionary by using its items
    total = 0
    for key, value in dice_rolls.items():
        if value >= 3:
            total += scores[str(key)]
            if key == 1:
                total += 100 * (value - 3)
            if key == 5:
                total += 50 * (value - 3)
        elif key == 1:
            total += 100 * value
        elif key == 5:
            total += 50 * value
        print(f'the roll is {key}, for a count of {value}')

    return total

    

print(score([5, 1, 3, 4, 1])) #250
print(score([1, 1, 1, 3, 1])) #1100
print(score([2, 4, 4, 5, 4])) #450
print(score([2, 3, 4, 6, 2])) #0
print(score([4, 4, 4, 3, 3])) #400
print(score([2, 4, 4, 5, 4])) #450