def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    sorted_arr = sorted(nums1 + nums2)
    arr_length = len(sorted_arr)

    if arr_length == 1:
        return sorted_arr[0]

    if arr_length % 2 == 1:
        return sorted_arr[(arr_length // 2)]
    else:
        return ((sorted_arr[arr_length // 2] + sorted_arr[(arr_length // 2) - 1]) / 2)

print(findMedianSortedArrays([1,2], [3]))
