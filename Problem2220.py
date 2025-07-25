def minBitFlips(start:int, goal:int) -> int:
    xor = start ^ goal
    count = 0

    while xor != 0:
        if xor & 1 == 1:
            count += 1
        xor >>= 1

    return count

print(minBitFlips(10,7))
