#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        rs = roman_dict[roman_string[i]]
        if i > 0:
            if roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
                num += rs - 2 * roman_dict[roman_string[i - 1]]
        else:
            num += roman_dict[roman_string[i]]
    return num
