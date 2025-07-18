def checkIfPangram(sentence: str) -> bool:
    letter_dict = {}

    for i in sentence:
        key = str(i)

        if key not in letter_dict:
            letter_dict[key] = 1
        else:
            pass

    return (True if len(letter_dict) == 26 else False)

print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
