def findPermutationDifference(s:str, t:str) -> int:
    s_dict = {}
    t_dict = {}
    difference = 0

    for index, element in enumerate(s):
        s_dict[element] = index

    for index, element in enumerate(t):
        t_dict[element] = index
    for key, value in s_dict.items():
        difference += abs(s_dict[key] - t_dict[key])

    return difference

print(findPermutationDifference("abc","bac"))


