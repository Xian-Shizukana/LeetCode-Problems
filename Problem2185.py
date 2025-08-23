def prefixCount(words:list[str], pref: str) -> int:
    res = 0
    pref_length = len(pref)

    for i in words:
        if i[:pref_length] == pref:
            res += 1

    return res

print(prefixCount(["pay","attention","practice","attend"], "at"))
