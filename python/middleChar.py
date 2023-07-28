

def get_middle(s):
    if len(s) % 2 == 0:
        return s[round(len(s) / 2 - 1)] + s[round(len(s) / 2)]
    else:
        return s[round((len(s) - 1) / 2)]

print(get_middle('test'))
print(get_middle('testing'))
