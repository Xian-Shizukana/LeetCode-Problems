def countPoints(rings:str) -> int:
    ring_dict = {}
    count = 0

    for i in range(1, len(rings), 2):
        rod = rings[i]
        ring = rings[i-1]

        if rod in ring_dict:
            ring_dict[rod] += [ring]
        else:
            ring_dict[rod] = [ring]

    for key in ring_dict:
        ring_dict[key] = set(ring_dict[key])
        if len(ring_dict[key]) == 3:
            count += 1

    return count



    print(ring_dict)

print(countPoints("B0R0G0R9R0B0G0"))




