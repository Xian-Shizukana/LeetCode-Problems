def separateDigits(nums:list[int]) -> list[int]:
    res = []

    for i in nums:
        if i > 9:
            temp = []
            while i != 0:
                digit = i % 10
                i //= 10
                temp.append(digit)   
            temp.reverse()
            res += temp
        else:
            res.append(i)

    return res

print(separateDigits([13,25,83,77]))
