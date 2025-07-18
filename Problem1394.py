def findLucky(arr:list[int]) -> int:
    arr_dict = {}
    lucky_arr = []

    for i in arr:
        if not i in arr_dict:
            arr_dict[i] = 1
        else:
            arr_dict[i] += 1

    for key, value in arr_dict.items():
        if key == value:
            lucky_arr.append(value)

    if not lucky_arr:
        return -1
    else:
        return max(lucky_arr)

print(findLucky([2,4]))
