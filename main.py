from pprint import pprint

MATRIX = 9  # Size of 2d matrix


# Print completed puzzle
def sudoku_printer(a):
    sudoku_solver(a)
    grid = []
    solved = []
    for i in range(MATRIX):
        for j in range(MATRIX):
            """Append numbers to rows"""
            solved.append(a[i][j])
            if len(solved) >= 9:
                """Append rows to grid"""
                grid.append(solved)
                solved = []

    pprint(grid)
    return grid


def solve(puzzle, row, col, num):
    """If we find same num in the same row or same column or in the specific
        3*3 matrix, ‘false’ will be returned."""
    # Check for same number in row
    for x in range(9):
        if puzzle[row][x] == num:
            return False

    # Check for same number in column
    for x in range(9):
        if puzzle[x][col] == num:
            return False

    # Check for same number matrix
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[i + start_row][j + start_col] == num:
                return False
    return True


def sudoku_solver(puzzle, *args, **kwargs):
    """return the solved puzzle as a 2d array of 9 x 9"""
    row = 0
    col = 0
    solved = False

    while not solved:
        """Check if we have reached the 8th row and 9th column and return true 
        to stop further backtracking."""
        if row == MATRIX - 1 and col == MATRIX:
            return True

        """Check if the column value becomes 9, then move to the next row and 
        column"""
        if col == MATRIX:
            row += 1
            col = 0

        """see if the current position of the grid has value greater than 0, 
        then we iterate for next column."""
        if puzzle[row][col] > 0:
            col += 1
            continue

        for num in range(1, MATRIX + 1):
            """Check if it is a safe guess,"""
            if solve(puzzle, row, col, num):
                """move to the next column and then 
                    assign num in current (row ,col) position of the grid."""
                puzzle[row][col] = num
                """check for next possibility with next column."""
                if sudoku_solver(puzzle, col=col + 1):
                    """continue until solved or incorrect"""
                    return True
            puzzle[row][col] = 0
        """If the assumption is wrong, discard the assigned num and go for the 
        next assumption with different num value"""
        return False


# Run program

# Zero represents empty
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

sudoku_printer(puzzle)
