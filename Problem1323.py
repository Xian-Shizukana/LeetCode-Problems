def maximum69Number(num:int) -> int:
    s_num = str(num)
    digit = 0.3

    for i in range(len(s_num)):
        if s_num[i] == "6" or digit >= 3:
            digit *= 10

    return int(num + digit // 1)



print(maximum69Number(9996))
