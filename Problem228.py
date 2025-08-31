def summaryRanges(nums:list[int]) -> list[str]:
    res = []
    temp = []

    if not nums:
        return []

    for index, element in enumerate(nums):

        # Only applies to the first iteration
        if not temp:
            temp.append(element)
            continue

        # If the current element only increments by 1,
        # append it to the temp array
        if element == temp[-1] + 1:
            temp.append(element)
            continue

        # If the current element doesn't increment by 1,
        # append the temp array to the result array.
        # If the temp has only 1 element, append it as is.
        # Otherwise, transform it into a range.
        if len(temp) == 1:
            res.append(str(temp[0]))
        else:
            res.append(str(temp[0]) + "->" + str(temp[-1]))

        # Empties and appends the current element to the temp to
        # start a new range.
        temp = []
        temp.append(element)

    # Appends leftover temp to the result array.
    if len(temp) == 1:
        res.append(str(temp[0]))
    else:
        res.append(str(temp[0]) + "->" + str(temp[-1]))

    return res

print(summaryRanges([0,1,2,4,5,7]))






