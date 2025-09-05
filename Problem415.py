def addStrings(num1: str, num2: str) -> str:    
    values_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }

    most = max(len(num1), len(num2)) + 1
    carry = 0
    res = []


    for i in range(1, most):

        # Checks whether or not either of the arrays have no more digits
        # to prevent an error.
        if i > len(num1):
            temp = values_dict[num2[-i]] + carry
        elif i > len(num2):
            temp = values_dict[num1[-i]] + carry
        else:
            temp = values_dict[num1[-i]] + values_dict[num2[-i]] + carry

        carry = temp // 10
        temp %= 10
        res.append(str(temp))

    # If there's a carry leftover (e.g. 999 + 1),
    # add it to the array.
    if carry:
        res.append(str(carry))

    res.reverse()

    return "".join(res)
            
print(addStrings("999", "1"))
