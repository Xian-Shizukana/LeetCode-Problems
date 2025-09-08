def getNoZeroIntegers(n:int) -> list[int]:
    for i in range(n):
        test = str(i) + str(n - i)

        if "0" in test:
            continue
        else:
            return [i, n - i]
        

print(getNoZeroIntegers(1010))
