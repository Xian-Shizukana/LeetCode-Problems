def threeConsecutiveOdds(arr:list[int]) -> bool:
    count = 0

    for i in arr:
        if i % 2 == 1:
            count += 1
        else:
            count = 0

        if count == 3:
            return True
    return False

print(threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
