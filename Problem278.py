def firstBadVersion(n: int) -> int:
    l = 1
    r = n
    m = l + ((r - l) // 2)

    while l < r:
        if not isBadVersion(m):
            l = m + 1
        else:
            r = m

        print(f"m : {m}, l: {l}")

        m = l + ((r - l) // 2)

    return l

