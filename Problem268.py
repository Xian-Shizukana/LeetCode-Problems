def missingNumber(nums:list[int]) -> int:
    ans = len(nums)

    for i in range(len(nums)):
        ans += i - nums[i]

    return ans

    ''' BEFORE VIEWING SOLUTION (WORKS)
    nums.sort(reverse=True)

    for i in range(len(nums)):
        if nums[-i - 1] == i:
            continue
        else:
            print("Missing Number Found:")
            return i

    return nums[0] + 1
    '''

print(missingNumber([0,1]))
