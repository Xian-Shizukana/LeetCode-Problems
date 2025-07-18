def plusOne(digits: list[int]) -> list[int]:
    digits[-1] = digits[-1] + 1
    while 10 in digits:
        x = digits.index(10)
        digits[x] = 0
        if x - 1 == -1:
            digits.insert(0, 1)
        else:
            digits[x-1] += 1
         
    return digits

print(plusOne([]))

