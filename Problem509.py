def fib(n:int) -> int:
    prev = 0
    curr = 1

    if n == 1:
        return n

    for i in range(n-1):
        prev, curr = curr, prev + curr
    return curr

print(fib(4))
