def isPalindrome(x: int) -> bool:
    num = x
    reversed_num = 0

    if num < 0:
        return False

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    if reversed_num == x:
        return True
    return False

print(isPalindrome(10001))
