def findClosest(x:int, y:int, z:int) -> int:
    
    person1_speed = abs(z - y)
    person2_speed = abs(z - x)

    if person1_speed > person2_speed:
        return 1
    elif person2_speed > person1_speed:
        return 2
    else:
        return 0

print(findClosest(2,5,6))
         
