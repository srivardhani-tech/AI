import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def evaluate(board):
    # Check rows, columns, and diagonals to determine the score
    for row in board:
        if all(cell == "X" for cell in row):
            return -1  # Player X wins
        elif all(cell == "O" for cell in row):
            return 1  # Player O wins

    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return -1
        elif all(board[row][col] == "O" for row in range(3)):
            return 1

    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return -1
    elif all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return 1

    return 0  # It's a draw

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score != 0 or depth == 0 or is_board_full(board):
        return score

    if maximizing_player:
        max_eval = float("-inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            eval = minimax(board, depth - 1, False)
            max_eval = max(max_eval, eval)
            board[i][j] = " "
        return max_eval
    else:
        min_eval = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            eval = minimax(board, depth - 1, True)
            min_eval = min(min_eval, eval)
            board[i][j] = " "
        return min_eval

def find_best_move(board):
    best_val = float("-inf")
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        move_val = minimax(board, 3, False)  # You can adjust the depth of the search
        board[i][j] = " "

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = "X"

            if evaluate(board) == -1:
                print_board(board)
                print("Player X wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            print("Computer's turn:")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = "O"

            if evaluate(board) == 1:
                print_board(board)
                print("Player O wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
