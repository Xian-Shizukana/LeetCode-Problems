def differenceOfSum(nums: list[int]) -> int:
    element_sum = 0
    digit_sum = 0

    for i in nums:
        element_sum += i

        if i > 9:
            temp = i

            while temp:
                digit_sum += temp % 10
                temp //= 10
        else:
            digit_sum += i

    return abs(element_sum - digit_sum)

print(differenceOfSum([1,15,6,3]))
