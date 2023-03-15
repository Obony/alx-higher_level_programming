#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        result = []
        for i in roman_string:
            if i == 'I':
                result.append(1)
            elif i == 'V':
                result.append(5)
            elif i == 'X':
                result.append(10)
            elif i == 'L':
                result.append(50)
            elif i == 'C':
                result.append(100)
            elif i == 'D':
                result.append(500)
            elif i == 'M':
                result.append(1000)

        for i in range(len(result)):
            if i != len(result) - 1:
                if result[i] < result[i + 1]:
                    result[i] = -result[i]
        return sum(result)
    else:
        return 0
