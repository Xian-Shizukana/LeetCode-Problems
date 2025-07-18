def finalValueAfterOperations(operations: list[str]) -> int:
    counter = 0

    for operation in operations:
        match operation:
            case "--X" | "X--":
                counter -=1
            case "++X" | "X++":
                counter += 1

    return counter

print(finalValueAfterOperations(["--X","X++","X++"]))
