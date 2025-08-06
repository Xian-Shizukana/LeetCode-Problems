def searchInsert(nums:list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    if target > nums[r]:
        return r + 1
    if target < nums[l]:
        return 0
    
    while l <= r :
        # Pointer
        m = l + ((r - l) // 2)

        # If the pointer is the target, return the index
        if nums[m] == target:
            return m

        # Narrows down the search of the target
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1

    # If the loop breaks (l overtakes r), that means the target was not found.
    # This means the position of l is where the target should be inserted.
    return l

print(searchInsert([1,3,5,6], 5))
        


