def canAliceWin(nums:list[int]) -> bool:
    single_sum = 0
    double_sum = 0

    for i in nums:
        if i < 10:
            single_sum += i
        else:
            double_sum += i

    if single_sum > double_sum or single_sum < double_sum:
        return True
    return False

print(canAliceWin([1,2,3,4,5,14]))
