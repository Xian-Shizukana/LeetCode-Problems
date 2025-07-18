def xorOperation(n:int, start:int) -> int:
    xor_sum = 0

    for i in range(0, n):
        xor_sum ^= start + 2 * i

    return xor_sum

print(xorOperation(4,3))
