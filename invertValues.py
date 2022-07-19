# using list comphrehension - look this up
def invert(lst):
    return [-x for x in lst]

arr = [1, -2, 3, -4, 5]
print(invert(arr))