def largestAltitude(gain:list[int]) -> int:
    res = 0
    temp = 0

    for i in gain:
        temp += i

        res = max(res, temp)

    return res

print(largestAltitude([-5,1,5,0,-7]))

