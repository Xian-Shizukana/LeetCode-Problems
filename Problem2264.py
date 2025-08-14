def largestGoodInteger(num:str) -> str:
    count = 0
    curr_num = num[0]
    max_num = ""

    for digit in num:
        if digit == curr_num:
            count += 1
        else:
            curr_num = digit
            count = 1

        if count == 3:
            if max_num:
                max_num = str(max(int(max_num), int(digit)))
            else:
                max_num = digit

    return max_num * 3

