def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums_dict = {}
    intersection = []

    for i in nums1:
        if str(i) not in nums_dict:
            nums_dict[str(i)] = 1
        else:
            continue

    for i in nums2:
        if str(i) in nums_dict:
            nums_dict[str(i)] += 1

    for key in nums_dict:
        if nums_dict[key] >= 2:
            intersection.append(int(key))

    return intersection

print(intersection([1,2,2,1], [2,2]))

