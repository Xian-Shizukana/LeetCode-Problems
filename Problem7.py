def reverse(x:int) -> int:
    reversed_num = 0
    y = abs(x)

    while y != 0:
        digit = y % 10

        # While accepted in Leetcode, the if statement is
        # not accurate as it only accepts until 2,147,483,647
        # even though negative numbers can go until | -2,147,483,648 |
        if reversed_num * 10 + digit > 2**31 - 1:
            return 0
        reversed_num = reversed_num * 10 + digit
        y //= 10

    if x < 0:
        reversed_num *= -1

    return reversed_num 

print(reverse(-2147483640))
