def findTheDifference(s:str, t:str) -> str:
    letter = 0

    for char in s:
        letter ^= ord(char)
    for char in t:
        letter ^= ord(char)

    return chr(letter)

print(findTheDifference("abcd", "abcde"))
