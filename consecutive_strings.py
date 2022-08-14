


def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''

    arr = []
    for i in range(len(strarr)):
        temp = []
        j = i
        while len(temp) < k:
            if i + k - 1 > len(strarr) - 1:
                return max(arr, default=0, key=len)
            else:
                temp.append(strarr[j])
                j += 1
        arr.append(''.join(temp))
    return max(arr, default=0 ,key=len)
    pass

print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(longest_consec([], 3))
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2))

