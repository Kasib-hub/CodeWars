# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"

def order(sentence):
    order = '123456789'
    strArr = sentence.split(' ')
    ans = [1] * len(strArr)
    for word in strArr:
        for char in word:
            if char in order:
                ans[int(char) - 1] = word
    return ' '.join(ans)
print(order("is2 Thi1s T4est 3a"))