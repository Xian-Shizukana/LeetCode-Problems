def toLowerCase(s:str) -> str:
    return s.lower()

    ''' lower()-less solution
    lower_str = ""

    for i in range(len(s)):
        if ord(s[i]) < 91 and ord(s[i]) > 64:
            lower_str += chr(ord(s[i]) + 32)
        else:
            lower_str += s[i]
    return lower_str
    '''

print(toLowerCase("ZZZZZZ"))
            
