def print_solution(board):
    for row in board:
        print(' '.join(['Q' if col else '.' for col in row]))
    print()


def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_n_queens_util(board, col):
    if col == len(board):
        # All queens are placed successfully, print the solution
        print_solution(board)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place queen and recur for the next column
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens_util(board, col + 1)

            # If placing queen in the current position doesn't lead to a solution,
            # backtrack and remove the queen from the current position
            board[i][col] = 0


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0)


# Example usage for 8 queens on an 8x8 chessboard
solve_n_queens(8)
