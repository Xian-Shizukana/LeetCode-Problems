def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    ''' BEFORE VIEWING SOLUTION (WORKS)
    arr_length = len(s)
    for i in range(arr_length):
        s.insert(arr_length - (i+1), s.pop(0))
    '''


print(reverseString(["h","e","l","l","o"]))
