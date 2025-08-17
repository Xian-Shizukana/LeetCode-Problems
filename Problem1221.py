def balancedStringSplit(s:str) -> int:
    count_res = 0
    count = 0

    for char in s:
        if char == "R":
            count += 1
        else:
            count -= 1

        if count == 0:
            count_res += 1

    return count_res

print(balancedStringSplit("RLRRLLRLRL"))
