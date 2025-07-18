class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        to_delete = []

        for index, element in enumerate(nums):
            if element == val:
                to_delete.append(index)
        to_delete.reverse()

        for index in to_delete:
            nums.pop(index)

        k = len(nums)
                
        return k

leet = Solution()

nums = [0,1,2,2,3,0,4,2]

leet.removeElement(nums, 2)

print(nums)
