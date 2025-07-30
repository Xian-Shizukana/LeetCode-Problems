def isAcronym(words:list[str], s:str) -> bool:

    s_arr = []

    for i in range(len(words)):
        s_arr.append(words[i][0])

    if "".join(s_arr) == s:
        return True
    else:
        return False

print(isAcronym(["alice","bob","charlie"], "abc"))

