def numberGame(nums: list[int]) -> list[int]:
    nums.sort()
    arr = []

    while nums:
        alice = nums.pop(0)
        bob = nums.pop(0)

        arr.append(bob)
        arr.append(alice)

    return arr

    ''' BEFORE VIEWING SOLUTION (WORKS)
    arr = []
    while True:
        alice = min(nums)
        nums[nums.index(alice)] = 101

        bob = min(nums)
        nums[nums.index(bob)] = 101
        
        if bob == 101:
            pass
        else:
            arr.append(bob)

        if alice == 101:
            pass
        else:
            arr.append(alice)

        if bob == 101 and alice == 101:
            return arr
    '''

print(numberGame([5,4,2,3]))
