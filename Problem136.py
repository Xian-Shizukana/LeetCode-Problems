def singleNumber(nums: list[int]) -> int:
    counter_dict = {}

    for i in nums:
        key = str(i)

        if not key in counter_dict:
            counter_dict[key] = 1
        else:
            counter_dict.pop(key, None)

    ans = counter_dict.keys()

    for key in ans:
        return int(key)

print(singleNumber([4,1,2,1,2]))

