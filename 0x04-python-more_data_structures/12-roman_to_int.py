#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        num = 0
        i = 0
        tmp = ''
        length = len(roman_string)
        dic = {"IV": 4, "IX": 9, "XL": 40, "LC": 90, "CD": 400, "CM": 900,
               'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i < length:
            if i + 1 < length:
                tmp = roman_string[i]+roman_string[i+1]
            for key, value in dic.items():
                if key == tmp:
                    num += value
                    i += 1
                    break
                elif key == roman_string[i]:
                    num += value
                    tmp = ""
            i += 1
        return num
    return 0
