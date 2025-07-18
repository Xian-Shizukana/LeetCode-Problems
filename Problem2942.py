def findWordsContaining(words:list[str], x: str) -> list[int]:
    has_char = []

    for index, element in enumerate(words):
        if x in element:
            has_char.append(index)

    return has_char

print(findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))
