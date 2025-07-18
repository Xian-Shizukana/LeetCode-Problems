def convertToTitle(columnNumber: int) -> str:

    column_title = ""

    while columnNumber != 0:
        # Decrementing 'columnNumber' to match Excel's 1-based indexing
        # basically, there's no "Column 0"
        columnNumber -= 1
        unicode = (columnNumber % 26)

        column_title += chr(ord('A') + unicode)
        columnNumber //= 26
        

    return column_title[::-1]
    
print(convertToTitle(701))
