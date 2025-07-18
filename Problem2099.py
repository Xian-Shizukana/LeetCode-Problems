def maxSubsequence(nums: list[int], k:int) -> list[int]:
    
    index_num = []
    ans = []

    for i, n in enumerate(nums):
        index_num.append((i, n))

    index_num.sort(reverse=True, key=lambda val: val[1])

    index_num = index_num[:k]

    index_num.sort(key=lambda val: val[0])

    return [n for i, n in index_num]

    ''' BEFORE VIEWING SOLUTION (WORKS)
    max_arr = []
    ans = []
    nums_arr = nums

    for i in range(k):
        num = max(nums_arr)
        index = nums_arr.index(num)
        
        max_arr.append((index, num))
        nums_arr.pop(index)
        nums_arr.insert(index, -100001)

    max_arr.sort()

    for index, element in max_arr:
        ans.append(element)

    return ans
    '''
            
print(maxSubsequence([-1,-2,3,4], 3))
