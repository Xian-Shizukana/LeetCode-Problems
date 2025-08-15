def countPairs(nums:list[int], target:int) -> int:
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                count += 1
            else:
                continue

    return count

print(countPairs([-1,1,2,3,1], 2))
