#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for char in roman_string:
        if char not in roman_numbers:
            return 0
        else:
            value = roman_numbers[char]
            result += value
    return result

