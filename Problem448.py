def findDisappearedNumbers(nums:list[int]) -> list[int]:
    res = []

    for i in nums:
        index = abs(i) - 1

        if nums[index] > 0:
            nums[index] = -nums[index]

    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)

    return res
        

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
        
