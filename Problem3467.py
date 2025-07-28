def transformArray(nums:list[int]) -> list[int]:
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[i] = 0
        else:
            nums[i] = 1

    return sorted(nums)

print(transformArray([4,3,2,1]))
