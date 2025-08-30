def groupAnagrams(strs:list[str]) -> list[list[str]]:
    anagram_dict = {}
    res = []

    for word in strs:
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]

    for key in anagram_dict:
        res.append(anagram_dict[key])

    return res

print(groupAnagrams([""]))

