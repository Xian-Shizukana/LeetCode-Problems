def leftRightDifference(nums:list[int]) -> list[int]:
    left = 0
    right = 0
    difference_array = []

    for i in nums:
        right += i

    for i in range(len(nums)):
        right -= nums[i]
        difference = abs(right - left)
        difference_array.append(difference)
        left += nums[i]

    return difference_array

print(leftRightDifference([10,4,8,3]))
