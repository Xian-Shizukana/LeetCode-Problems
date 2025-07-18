def firstPalindrome(words:list[str]) -> str:
    for i in words:
        if i == i[::-1]:
            return i

    return ""

print(firstPalindrome(["abc","car","ada","racecar","cool"]))
