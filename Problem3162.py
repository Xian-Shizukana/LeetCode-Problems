def numberofPairs(nums1:list[int], nums2: list[int], k:int) -> int:
    count = 0

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            nums_2 = nums2[j] * k

            if nums1[i] % nums_2 == 0:
                count += 1

    return count

print(numberofPairs([1,3,4],[1,3,4], 1))
