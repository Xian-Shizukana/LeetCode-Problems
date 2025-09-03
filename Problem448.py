def findDisappearedNumbers(nums:list[int]) -> list[int]:
    sett = set(nums)
    length = len(nums)
    res = []

    for num in range(1, length + 1):
        if num in sett:
            continue
        else:
            res.append(num)

    return res




print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
        
