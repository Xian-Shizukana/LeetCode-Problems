def zeroFilledSubarray(nums:list[int]) -> int:
    count = 0
    temp_count = 1

    for i in nums:
        if i == 0:
            count += temp_count
            temp_count += 1
        else:
            temp_count = 1

    return count

print(zeroFilledSubarray([1,3,0,0,2,0,0,4]))
