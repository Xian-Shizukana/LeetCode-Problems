def minimumAverage(nums: list[int]) -> float:
    res = float('inf')
    l = 0
    r = len(nums) - 1

    nums.sort()

    while l < r:
        res = min(res, (nums[l] + nums[r]) / 2)
        l += 1
        r -= 1

    return res

print(minimumAverage([7,8,3,4,15,13,4,1]))

