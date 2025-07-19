def toGoatLatin(sentence:str) -> str:
    txt = sentence.split()
    goat_sentence = []
    count = 1

    for i in txt:
        if i[0] in ['a','e','i','o','u','A','E','I','O','U']:
            goat_sentence.append(i + "ma" + ("a" * count))
        else:
            temp = i[1:] + i[0] + "ma" + ("a" * count)
            goat_sentence.append(temp)
        count += 1

    return " ".join(goat_sentence)

print(toGoatLatin("I speak Goat Latin"))
           
