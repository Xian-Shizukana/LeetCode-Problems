def nextGreaterElement(nums1:list[int], nums2: list[int]) -> list[int]:
    ans = []

    for i in nums1:
        x = nums2.index(i)

        for j in nums2[x:]:
            if i < j:
                ans.append(j)
                break
        else:
            ans.append(-1)           

    return ans

print(nextGreaterElement([4,1,2],[1,3,4,2]))

