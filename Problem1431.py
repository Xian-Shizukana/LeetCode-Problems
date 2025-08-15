def kidsWithCandies(candies:list[int], extraCandies:int) -> list[bool]:
    max = 0
    greatest_array = []

    for i in candies:
        if i > max:
            max = i

    for i in candies:
        if i + extraCandies >= max:
            greatest_array.append(True)
        else:
            greatest_array.append(False)

    return greatest_array

print(kidsWithCandies([2,3,5,1,3], 3))
