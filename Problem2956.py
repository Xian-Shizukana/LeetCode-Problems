def findIntersectionValues(nums1:list[int], nums2:list[int]) -> list[int]:
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    count1 = 0
    count2 = 0

    for i in nums1:
        if i in nums2_set:
            print(i)
            count1 += 1

    for i in nums2:
        if i in nums1_set:
            count2 += 1

    res = [count1, count2]
    return res

print(findIntersectionValues([2,3,2],[1,2]))
