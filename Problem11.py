def maxArea(height: list[int]) -> int:

    # This solution was coded after looking
    # at existing solutions and hints

    max_area = 0
    left = 0
    right = len(height) - 1

    while left <= right:
        max_area = max(max_area, 
                       min(height[left], height[right]) * abs(left - right))

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))



