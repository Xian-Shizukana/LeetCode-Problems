def subarraySum(nums:list[int]) -> int:
    left = 0
    right = 0
    res = 0

    while right < len(nums):
        temp = 0
        left = max(0, right - nums[right])
        right += 1

        for i in range(left, right):
            temp += nums[i]

        res += temp
            

    return res

print(subarraySum([2,3,1]))

