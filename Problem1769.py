def minOperations(boxes:str) -> list[int]:
    operations_arr = []
    
    for index, element in enumerate(boxes):
        operations = 0

        for index2, element2 in enumerate(boxes):
            if element2 == "1":
             operations += abs(index - index2)

        operations_arr.append(operations)

    return operations_arr

print(minOperations("110"))
