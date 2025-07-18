def triangleType(nums:list[int]) -> str:

    nums.sort()
    if nums[0] + nums[1] <= nums[2]:
        return "none"
    if nums[0] == nums[2]:
        return "equilateral"
    if nums[0] == nums[1] or nums[1] == nums[2]:
        return "isosceles"
    return "scalene"

    ''' BEFORE VIEWING SOLUTION (WORKS)
    if not nums[0] + nums[1] > nums[2] or not nums[1] + nums[2] > nums[0] or not nums[0] + nums[2] > nums[1]:
        return "none"

    for i in range(0,3):
        if nums.count(nums[i]) == 2:
            return "isosceles"
        elif nums.count(nums[i]) == 3:
            return "equilateral"

    return "scalene"
    '''

print(triangleType([3,4,5]))
