def arraySign(nums:list[int]) -> int:
    neg_count = 0

    for i in nums:
        if i == 0:
            return 0
        if i < 0:
            neg_count += 1

    if neg_count % 2 == 1:
        return -1
    else:
        return 1

print(arraySign([-1,-2,-3,-4,3,2,1]))


