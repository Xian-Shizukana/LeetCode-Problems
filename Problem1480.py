def runningSum(nums:list[int]) -> list[int]:
    sum = 0
    sum_array = []

    for i in nums:
        sum += i
        sum_array.append(sum)

    return sum_array

print(runningSum([1,2,3,4]))
