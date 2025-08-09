def isHappy(n:int) -> bool:
    prev_set = set()

    while True:
        
        # Getting the square of each digit
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n //= 10

        # The sum repeating means it's an endless cycle
        if sum in prev_set:
            return False

        # A sum of 1 will forever be 1, making it happy(?)
        if sum == 1:
            return True
        else:
            prev_set.add(sum)

        # The sum becomes the new number to square
        n = sum

print(isHappy(2))
