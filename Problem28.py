def strStr(haystack: str, needle: str) -> int:
    
    needle_length = len(needle)
    counter = 0

    for i in range(len(haystack)):
        if haystack[counter : needle_length + counter] == needle:
            return counter
        else:
            counter += 1
    return -1


print(strStr("leetcode", "leeto"))
