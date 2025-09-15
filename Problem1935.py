def canBeTypedWords(text:str, brokenLetters: str) -> int:
    res = 0
    split_arr = text.split()

    for word in split_arr:
        for char in word:
            if char in brokenLetters:
                break
        else:
            res += 1

    return res

print(canBeTypedWords("hello world", "ad"))


