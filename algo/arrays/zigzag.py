def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    movingDown = True
    row = 0
    col = 0
    result = []
    while not (row < 0 or row > height or col < 0 or col > width):
        result.append(array[row][col])
        if movingDown:
            if col == 0 or row == height:
                movingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                movingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result

    # Write your code here.
