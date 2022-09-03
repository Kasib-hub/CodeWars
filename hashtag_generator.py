def generate_hashtag(s):
    strArr = s.strip().split(' ')
    ans = '#'
    for item in strArr:
        if item != '':
            ans += item.capitalize()
    
    if ans == '#' or len(ans) > 140:
        return False
    else:
        return True
    

print(generate_hashtag("    Hello     World   "))
print(generate_hashtag("c i n"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag("    Hello     World   "))