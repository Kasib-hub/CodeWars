def xo(s):
    l = s.lower()
    return l.count('x') == l.count('o')

print(xo('xo0'))
print(xo('xoxo'))
print(xo('xo0msreoOX'))


