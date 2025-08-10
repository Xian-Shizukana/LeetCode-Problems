def searchRange(nums:list[int], target:int) -> list[int]:
    ans = []
    l = 0
    r = len(nums) - 1
    inArray = False
    
    while l <= r:
        m = l + ((r - l) // 2)

        if nums[m] == target:
            inArray = True
            break
        elif target < nums[m]:
            r = m - 1
        else:
            l = m + 1

    if not inArray:
        return [-1,-1]

    l = 0
    r = m

    while l < r:
        print(f"R: {r}, L: {l}, M: {m}")
        m = l + ((r - l) // 2)

        if nums[m] == target:
            r = m
        else:
            l = m + 1
    ans.append(l)

    l = m 
    r = len(nums) - 1

    while l < r:
        print(f"R: {r}, L: {l}, M: {m}")
        m = l + ((r - l) // 2 + ((r-l) % 2))

        if nums[m] == target:
            l = m
        else:
            r = m - 1
    ans.append(l)

    return ans

print(searchRange([5,7,7,8,8,10], 8))
