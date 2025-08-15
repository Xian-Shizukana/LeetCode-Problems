def minOperations(nums:list[int], k:int) -> int:
    sum = 0

    for i in nums:
        sum += i

    return sum % k

print(minOperations([3,9,7], 5))
