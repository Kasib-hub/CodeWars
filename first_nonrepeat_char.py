def first_non_repeating_letter(string):
    if string == '':
        return ''
        
    lower_str = [x.lower() for x in string]

    for i, char in enumerate(string):
        if lower_str.count(lower_str[i]) == 1:
            return string[i]
        else:
            return ''
    

print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter('sTreSS'))