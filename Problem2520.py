def countDigits(num:int) -> int:
    num_str = str(num)
    counter = 0

    for char in num_str:
        if num % int(char) == 0:
            counter += 1

    return counter

print(countDigits(121))
