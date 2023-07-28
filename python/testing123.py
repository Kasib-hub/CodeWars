
def number(lines):
    return [f'{counter}: {line}' for counter, line in enumerate(lines, start=1)]

print(number(['a', 'b', 'c']))