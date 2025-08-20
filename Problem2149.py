def rearrangeArray(nums:list[int]) -> list[int]:
    pos_arr = []
    neg_arr = []
    res = []

    for i in nums:
        if i < 0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)

    for i in range(len(nums) // 2):
        res.append(pos_arr[i])
        res.append(neg_arr[i])

    return res

print(rearrangeArray([3,1,-2,-5,2,-4]))

