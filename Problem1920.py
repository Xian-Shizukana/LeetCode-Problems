def buildArray(nums:list[int]) -> list[int]:
    ans = []

    for i in range(0, len(nums)):
        ans.append(nums[nums[i]])

    return ans

print(buildArray([0,2,1,5,3,4]))
