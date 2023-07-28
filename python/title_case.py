



def title_case(title, minor_words=''):
    if not minor_words:
        return ' '.join([x.capitalize() for x in title.split(' ')])


    minor_words = [x.lower() for x in minor_words.split(' ')]
    
    # converts title to capitalize except words in second argument
    
    res = []
    for i, word in enumerate(title.split(' ')):
        if i == 0 and word.lower() in minor_words:
            res.append(word.capitalize())
        
        elif word.lower() in minor_words:
            res.append(word.lower())
        
        else:
            res.append(word.capitalize())
    return ' '.join(res)
    
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))