

def get_winner(ballots):
    votes = {}
    for item in ballots:
        votes[item] = votes.get(item, 0) + 1
    
    res = dict(sorted(votes.items(), key=lambda item: item[1], reverse=True))
    first = []
    other_sum = 0
    for i, key in enumerate(res):
        if i == 0:
            first.append(key)
            first.append(res[key])
        if i > 0:
            # checking if value at largest key equals next value else total the rest
            if first[1] == res[key]:
                return None
            else:
                other_sum += res[key]
    if first[1] > len(ballots)/2:
        return first[0]
    return None

            
            
    
        
  #your code