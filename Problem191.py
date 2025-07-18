def hammingWeight(n: int) -> int:
    n = bin(n)
    return n.count('1')

    ''' BEFORE VIEWING SOLUTION (WORKS)
    n = str(bin(n)[2:])
    counter = 0

    for char in n:
        if char == '1':
            counter += 1
    
    return counter
    '''

print(hammingWeight(128))
