def judgeCircle(moves:str) -> bool:
    distance = [0,0]

    for char in moves:
        if char == "U":
            distance[0] += 1
        elif char == "D":
            distance[0] -= 1
        elif char =="R":
            distance[1] += 1
        else:
            distance[1] -= 1
    return distance == [0,0]

print(judgeCircle("DDRR"))
