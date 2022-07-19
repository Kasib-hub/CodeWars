def rps(p1, p2):

    hands = {
        'rock':'scissors',
        'scissors':'paper',
        'paper':'rock'
    }

    # if the value at the key of p1 equals p2 then p1 won the match
    if hands[p1] == p2:
        return 'Player 1 won!'
    elif hands[p2] == p1:
        return 'Player 2 won!'
    else:
        return 'Draw!'

print(rps('rock', 'rock'))

