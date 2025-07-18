def calPoints(operations:list[str]) -> int:
    points_arr = []
    sum = 0
    
    for i in operations:
        try:
            points_arr.append(int(i))
        except:
            match i:
                case "C":
                    points_arr.pop()
                case "D":
                    points_arr.append(points_arr[-1] * 2)
                case "+":
                    points_arr.append(points_arr[-1] + points_arr[-2])

    for i in points_arr:
        sum += i

    return sum

print(calPoints(["5","2","C","D","+"]))


