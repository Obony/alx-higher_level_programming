import sys

def is_valid(board, row, col):
    """Check if it is valid to place a queen at (row, col) on the board."""
    # Check if there is a queen in the same row or column
    for i in range(len(board)):
        if board[i][col] == 'Q' or board[row][i] == 'Q':
            return False
    # Check diagonals
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False
    return True

def solve_n_queens(n):
    """Solve the N queens problem and print all solutions."""
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        """Backtrack and try to place a queen in each column of the given row."""
        if row == n:
            # Found a solution, add it to the list of solutions
            solutions.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                # Place a queen and move to the next row
                board[row][col] = 'Q'
                backtrack(row + 1)
                # Remove the queen and try the next column
                board[row][col] = '.'

    backtrack(0)
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == '__main__':
    # Check if the program is called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_n_queens(n)

