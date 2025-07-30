def restoreString(s:str, indices: list[int]) -> str:
    shuffled_arr = [None] * len(s)
    count = 0

    for i in indices:
        shuffled_arr[i] = s[count]
        count +=1

    return "".join(shuffled_arr)

print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))

