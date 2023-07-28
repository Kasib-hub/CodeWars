
# def to_jaden_case(string):
#     arr = []
#     for word in string.split(' '):
#         arr.append(word.capitalize())
#     return ' '.join(arr)

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

print(to_jaden_case('Hello my name is kasib'))