import sys

def read_board():
    board = []
    for _ in range(9):
        row = list(map(int, sys.stdin.readline().split()))
        board.append(row)
    return board

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def valid(board, num, pos):
    # Check row
    if num in board[pos[0]]:
        return False

    # Check column
    if num in [board[i][pos[1]] for i in range(9)]:
        return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    if num in [board[box_y*3 + i][box_x*3 + j] for i in range(3) for j in range(3)]:
        return False

    return True

def solve(board):
    find = find_empty(board)
    if find[0] is None:
        return True

    row, col = find

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(*row)

B = read_board()
solve(B)
print_board(B)
