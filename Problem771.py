def numJewelsInStones(jewels:str, stones:str) -> int:
    jewels_dict = {}
    count = 0

    for char in jewels:
        jewels_dict[char] = 1   
    
    for char in stones:
        if char in jewels_dict:
            count += 1

    return count


print(numJewelsInStones("aA","aAAbbbb"))
