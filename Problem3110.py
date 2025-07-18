def scoreOfString(s: str) -> int:
    val_arr = []
    sum = 0

    for index, value in enumerate(s):
        if index == len(s) - 1:
            break
        minuend = ord(value)
        subtrahend = ord(s[index + 1])
        

        val_arr.append(abs(minuend - subtrahend))

    for i in val_arr:
        sum += i

    return sum

print(scoreOfString("hello"))
