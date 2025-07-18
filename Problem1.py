def twoSum(nums: list[int], target:int) -> list[int]:
    nums_dict = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [index, nums_dict[complement]]
        nums_dict[num] = index

    # Using a dictionary allows constant-time (O(1)) lookups for complements,
    # while using a list would require a linear-time (O(n)) search for each element.
    # This reduces the overall time complexity from O(n^2) to O(n).

print(twoSum([1,3,4,2], 6))
