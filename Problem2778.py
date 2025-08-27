def sumOfSquares(nums:list[int]) -> int:
    sum = 0
    nums_length = len(nums)

    for i in range(1, nums_length + 1):
        if nums_length % i == 0:
            sum += nums[i - 1] ** 2

    return sum

print(sumOfSquares([1,2,3,4]))
