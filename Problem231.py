def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n-1)) == 0

    ''' BEFORE VIEWING SOLUTION (WORKS)
    if n == 1:
        return True
    elif n % 2 == 1:
        return False

    for i in range(0, 32):
        if n == 2**i:
            return True
        elif n < 2**i:
            return False
    '''
    
print(isPowerOfTwo(2))
