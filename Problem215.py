def findKthLargest(nums:list[int], k:int) -> int:

    nums.sort()
    return nums[-k]

print(findKthLargest([3,2,1,5,6,4], 2))
