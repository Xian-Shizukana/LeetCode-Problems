def reverseDegree(s:str) -> int:
    sum = 0

    for index, char in enumerate(s):
        sum += (26 - (ord(char) - 97)) * (index + 1)
    return sum

print(reverseDegree("abc"))

