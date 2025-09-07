def sumZero(n:int) -> list[int]:
    res = []

    for i in range(1, n):
        res.append(i)

    res.append(-sum(res))

    return res

print(sumZero(10))

