def containsDuplicate(nums:list[int]) -> bool:
    prev_num = None
    for i in sorted(nums):
        current_num = i

        if prev_num == current_num:
            return True
        else:
            prev_num = i
    return False

print(containsDuplicate([1,2,3,1]))
