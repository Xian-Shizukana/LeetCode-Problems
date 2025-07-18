def hammingDistance(x:int, y:int) -> int:
    z = x ^ y
    
    count = 0
    while (z != 0):
        count += z & 1
        z >>= 1

    return count

print(hammingDistance(1,4))
