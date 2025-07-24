def findRelativeRanks(score:list[int]) -> list[str]:
    rank_dict = {}
    rank_arr = [None] * len(score)
    count = 1

    for index, element in enumerate(score):
        rank_dict[index] = element

    for i in sorted(rank_dict.items(), key=lambda x: x[1], reverse=True):
        # lambda makes it sort by the dictionary's value (x[1])
        # i[0] is the key of the value

        if count == 1:
            rank_arr[i[0]] = "Gold Medal"
        elif count == 2:
            rank_arr[i[0]] = "Silver Medal"
        elif count == 3:
            rank_arr[i[0]] = "Bronze Medal"
        else:
            rank_arr[i[0]] = str(count)
        count += 1

    return rank_arr


print(findRelativeRanks([10,3,8,9,4]))
