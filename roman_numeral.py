def solution(roman):
    num_pair = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]

    roman_dictionary = {key: value for key, value in num_pair}
    
    sum = 0
    for i, char in enumerate(roman):
        if len(roman) > 1 and roman_dictionary[char] > roman_dictionary[roman[i-1]] and i > 0:
            sum -= roman_dictionary[roman[i-1]] * 2
        sum += roman_dictionary[char]
    return sum

print(solution('XIX'))
print(solution('IX'))
print(solution('IV'))
print(solution('MMVIII'))
print(solution('MDCLXVI'))
print(solution('CMLXIX'))