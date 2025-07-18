def reverseBits(n:int) -> int:
    res = 0

    for i in range(32):
        # Shifts bits to the left
        # Ex: 011 (2) << 1 -> 0110 (6)
        res = res << 1

        # Adds the least significant bit of n to res
        # Ex: 0111 & 1 -> 011(1) & 1 -> 1
        res += (n & 1)

        # Shifts bits to the right
        # Ex: 1011 >> 1 -> 0101
        n = n >> 1

    return res

    ''' BEFORE VIEWING SOLUTION (KINDA WORKS??)
    a = int(n[::-1], 2)
    return a
    '''

print(reverseBits('00000010100101000001111010011100'))
