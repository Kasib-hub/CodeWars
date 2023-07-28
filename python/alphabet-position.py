def alphabet_position(text):
    # str.isalpha() checks for letters
    return ' '.join([str(ord(x.lower()) - 96) for x in text if x.upper() != x.lower()])
    pass

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))