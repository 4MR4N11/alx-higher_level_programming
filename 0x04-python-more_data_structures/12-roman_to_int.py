#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        num = 0
        i = 0
        length = len(roman_string)
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i < length:
            if i+1 < length and dic[roman_string[i]] < dic[roman_string[i+1]]:
                num += dic[roman_string[i + 1]] - dic[roman_string[i]]
                i += 2
            else:
                num += dic[roman_string[i]]
                i += 1
        return num
    return 0
