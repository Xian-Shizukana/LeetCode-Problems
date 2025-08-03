def findWords(words:list[str]) -> list[str]:
    first_row = {"q","w","e","r","t","y","u","i","o","p"}
    second_row = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
    third_row = {"z", "x", "c", "v", "b", "n", "m"}
    used_row = {}

    accepted_words = []

    for word in words:
        lower_word = word.lower()

        if lower_word[0] in first_row:
            used_row = first_row
        elif lower_word[0] in second_row:
            used_row = second_row
        else:
            used_row = third_row

        for char in lower_word[1::]:
            if char not in used_row:
                break
        else:
            accepted_words.append(word)

    return accepted_words

print(findWords(["Hello","Alaska","Dad","Peace"]))

