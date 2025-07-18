def majorityElement(nums: list[int]) -> int:

    # Boyer-Moore Majority Vote Algorithm

    candidate = None
    counter = 0

    for i in nums:
        if counter == 0:
            candidate = i
        if candidate == i:
            counter += 1
        else:
            counter -= 1

    return candidate

    ''' BEFORE VIEWING SOLUTION (WORKS)
    counter_dict = {}

    for i in nums:
        try:
            counter_dict[i] += 1
        except:
            counter_dict[i] = 1

    for key, val in counter_dict.items():
        if val > (len(nums) / 2):
            return key
    '''


print(majorityElement([2,2,1,1,1,2,2]))
