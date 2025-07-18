def findArray(pref:list[int]) -> list[int]:
    arr = []

    for i in range(len(pref)):
        if not arr:
            arr.append(pref[i])
            continue
        original = pref[i] ^ pref[i - 1]
        arr.append(original)

    return arr

print(findArray([5,2,0,3,1]))

