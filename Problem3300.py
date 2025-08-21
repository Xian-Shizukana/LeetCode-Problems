def minElement(nums:list[int]) -> int:
    res = 100000
    
    for i in nums:
        temp = 0

        while i > 0:
            temp += i % 10
            i //= 10

        res = min(res, temp)
    
    return res

print(minElement([10,12,13,4]))
            
