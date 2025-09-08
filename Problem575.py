def distributeCandies(candyType:list[int]) -> int:

    uniqueCandies = set(candyType)
    return min(len(candyType) // 2, len(uniqueCandies))

    """ BEFORE READING SOLUTION (WORKS)
    res = set()
    maxCandies = len(candyType) // 2

    candyType.sort()

    for i in candyType:
        if len(res) == maxCandies:
            break

        res.add(i)

    return len(res)
    """

print(distributeCandies([1,1,2,3]))


