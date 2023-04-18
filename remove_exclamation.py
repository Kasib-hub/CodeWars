# https://www.codewars.com/kata/57fafb6d2b5314c839000195/train/python

def remove(s):
    res = []
    sentence = s.split(' ')
    for word in sentence:
        if word.count('!') != 1:
            res.append(word)
    return " ".join(res)