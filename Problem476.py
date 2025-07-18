def findComplement(num:int):
    complement = ""

    while (num != 0):
        if num & 1 == 1:
            complement += "0"
        else:
            complement += "1"
        num >>= 1

    return int(complement[::-1], 2)

print(findComplement(5))
