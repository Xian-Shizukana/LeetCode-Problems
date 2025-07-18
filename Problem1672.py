def maximumWealth(accounts: list[list[int]]) -> int:
    max = 0
    
    for i in range(len(accounts)):
        temp = 0
        for j in accounts[i]:
            temp += j
        if temp > max:
            max = temp

    return max

print(maximumWealth([[1,2,3],[3,2,1]]))
