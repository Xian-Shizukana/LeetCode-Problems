def isPerfectSquare(num:int) -> bool:
    least = 1
    greatest = num // 2

    while least <= greatest:
        guess = least + ((greatest - least) // 2)

        squared = guess ** 2

        if squared == num:
            return True
        elif squared < num:
            least = guess + 1
        else:
            greatest = guess - 1

    return False


print(isPerfectSquare(104976))
