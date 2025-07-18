def reversewords(s:str) -> str:

    # Similar solution but with fewer allocations
    # due to Python's strings being immutable.
    # The previous solution changes the string 
    # with every iteration, allocating a new memory
    # for it every time.

    words = s.split()
    r_str = []

    for word in words[::-1]:
        r_str.append(word)

    return " ".join(r_str)

    ''' BEFORE VIEWING SOLUTION (WORKS)
    n = s.split()
    r_str = ""

    for word in n[::-1]:
        r_str += word + " "

    return r_str.strip()
    '''

print(reversewords("the sky is blue"))
