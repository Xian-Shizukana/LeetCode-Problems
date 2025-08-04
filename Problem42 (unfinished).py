def trap(height:list[int]) -> int:
    temp_height = height[0]
    temp_count = 0
    count = 0

    for i in height[1:]:
        if i >= temp_height:
            temp_height = i
            count += temp_count
        else:
            temp_count += (temp_height - i)


    return count

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        
