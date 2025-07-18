def numIdenticalPairs(nums: list[int]) -> int:
    counter = 0

    for index1, element1 in enumerate(nums):
        for index2, element2 in enumerate(nums):
            if element1 == element2 and index1 < index2:
                counter += 1

    return counter

print(numIdenticalPairs([1,2,3,1,1,3]))
