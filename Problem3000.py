def areaOfMaxDiagonal(dimensions:list[int]) -> int:
    greatest_index = None
    greatest_diagonal = float('-inf')
    greatest_area = float('inf')

    for i in range(len(dimensions)):
        d_length = dimensions[i][0]
        d_width = dimensions[i][1]

        diagonal = (d_length ** 2 + d_width ** 2) ** 0.5

        # If the diagonal is the same as the current greatest,
        # get the area of the rectangle with the largest area.
        if greatest_diagonal == diagonal:
            prev_area = greatest_area
            curr_area = dimensions[i][0] * dimensions[i][1]
            
            greatest_area = max(prev_area, curr_area)
            continue

        # If the diagonal is larger than the current greatest,
        # get its area.
        if max(greatest_diagonal, diagonal) == diagonal:
            greatest_diagonal = diagonal
            greatest_index = i

            greatest_area = dimensions[greatest_index][0] * dimensions[greatest_index][1]

    return greatest_area

print(areaOfMaxDiagonal([[4,7],[8,9],[5,3],[6,10],[2,9],[3,10],[2,2],[5,8],[5,10],[5,6],[8,9],[10,7],[8,9],[3,7],[2,6],[5,1],[7,4],[1,10],[1,7],[6,9],[3,3],[4,6],[8,2],[10,6],[7,9],[9,2],[1,2],[3,8],[10,2],[4,1],[9,7],[10,3],[6,9],[9,8],[7,7],[5,7],[5,4],[6,5],[1,8],[2,3],[7,10],[3,9],[5,7],[2,4],[5,6],[9,5],[8,8],[8,10],[6,8],[5,1],[10,8],[7,4],[2,1],[2,7],[10,3],[2,5],[7,6],[10,5],[10,9],[5,7],[10,6],[4,3],[10,4],[1,5],[8,9],[3,1],[2,5],[9,10],[6,6],[5,10],[10,2],[6,10],[1,1],[8,6],[1,7],[6,3],[9,3],[1,4],[1,1],[10,4],[7,9],[4,5],[2,8],[7,9],[7,3],[4,9],[2,8],[4,6],[9,1],[8,4],[2,4],[7,8],[3,5],[7,6],[8,6],[4,7],[25,60],[39,52],[16,63],[33,56]]))


