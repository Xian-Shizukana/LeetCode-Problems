def pivotArray(nums: list[int], pivot:int) -> list[int]:
    lesser_array = []
    same_array = []
    greater_array = []

    for i in nums:
        if i < pivot:
            lesser_array.append(i)
        elif i > pivot:
            greater_array.append(i)
        else:
            same_array.append(i)

    return lesser_array + same_array + greater_array

print(pivotArray([9,12,5,10,14,3,10], 10))
