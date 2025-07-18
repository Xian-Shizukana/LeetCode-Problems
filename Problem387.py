def firstUniqChar(s:str) -> int:
    char_dict = {}

    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for unique in char_dict.keys():
        if char_dict[unique] == 1:
            return s.index(unique)
    
    return -1


print(firstUniqChar("leetcode"))

