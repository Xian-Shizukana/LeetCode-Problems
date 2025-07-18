def romantoInt(s: str) -> int:
    value = 0
    roman_arr = []
    for char in s:
        roman_arr.append(char)
    roman_arr.append("|")

    roman_dict = {
            "I": 1, "V": 5,"X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000,

            "IV": 4, "IX": 9, "XL": 40, "XC": 90,
            "CD": 400, "CM": 900
            }

    for index, numeral in enumerate(roman_arr):
        if numeral in ['V', 'L', 'D', 'M']:
            value += roman_dict[numeral]
            roman_arr[index] = None
        elif numeral in ['I', 'X', 'C']:
            if roman_arr[index + 1] in ['V', 'X', 'L', 'C', 'D', 'M'] and roman_dict[roman_arr[index]] < roman_dict[roman_arr[index + 1]]:
                subtraction = roman_arr[index] + roman_arr[index + 1]
                roman_arr[index] = None
                roman_arr[index + 1] = None
                value += roman_dict[subtraction]
            else:
                roman_arr[index] = None
                value += roman_dict[numeral]
        else:
            continue
                
    print(roman_arr)
    return value

print(romantoInt("MCMXCIV"))
