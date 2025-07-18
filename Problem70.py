
def climbStairs(n: int) -> int:
    last_value = 0
    value = 1
    for i in range(n):
        value = value + last_value
        last_value = value - last_value
    return value

print(climbStairs(4))
