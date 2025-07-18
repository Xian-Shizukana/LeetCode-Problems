class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        duplicate_index = []

        for index, element in enumerate(nums):

            print(nums)
            print("Current Number: " + str(element))

            for d_index, d_element in enumerate(nums):
                print("     Comparing to " + str(d_element))

                if element == d_element and index != d_index:
                    duplicate_index.append(d_index)
                    print("          Removed Duplicate " + str(element))

        duplicate_index.reverse()
        print(duplicate_index)
        for i in duplicate_index:
            print(nums)
            del nums[i]

        k = len(nums)
        return k
    
# For Testing (not part of the solution)

leet = Solution()

nums = [1,1,2]

leet.removeDuplicates(nums)

print(nums)


            
        