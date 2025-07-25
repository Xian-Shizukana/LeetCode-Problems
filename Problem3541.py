def maxFreqSum(s:str) -> int:
    vowels_dict = {"a":0, "e":0, "i":0, "o":0, "u": 0}
    const_dict = {}
    const_max = 0

    for char in s:
        if char in vowels_dict:
            vowels_dict[char] += 1
        else:
            if char in const_dict:
                const_dict[char] += 1
            else:
                const_dict[char] = 1

    if const_dict:
        const_max = max(const_dict.values())
    vowel_max = max(vowels_dict.values())

    return const_max + vowel_max

print(maxFreqSum("successes"))
