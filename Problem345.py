def reverseVowels(s:str) -> str:
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
    rev_arr = []
    res = []
    count = 0

    for char in s:
        if char in vowels:
            rev_arr.append(char)
        
    rev_arr.reverse()

    for char in s:
        if char in vowels:
            res.append(rev_arr[count])
            count +=1
        else:
            res.append(char)

    return "".join(res)

print(reverseVowels("IceCreAm"))
