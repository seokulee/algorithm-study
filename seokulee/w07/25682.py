import sys


def solution():
    N, M, K = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().strip() for _ in range(N)]
    binary_board = [[1 if cell == 'B' else 0 for cell in row] for row in board]

    accum_b = [[0] * (M + 1) for _ in range(N + 1)]
    accum_w = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            cell = binary_board[i - 1][j - 1]
            bf_cell = (i + j) % 2  # bf
            wf_cell = (i + j + 1) % 2  # wf
            accum_b[i][j] = accum_b[i - 1][j] + accum_b[i][j - 1] - accum_b[i - 1][j - 1] + (cell ^ bf_cell)
            accum_w[i][j] = accum_w[i - 1][j] + accum_w[i][j - 1] - accum_w[i - 1][j - 1] + (cell ^ wf_cell)

    min_cost = sys.maxsize
    for i in range(N - K + 1):
        for j in range(M - K + 1):
            cost_b = accum_b[i + K][j + K] - accum_b[i][j + K] - accum_b[i + K][j] + accum_b[i][j]
            cost_w = accum_w[i + K][j + K] - accum_w[i][j + K] - accum_w[i + K][j] + accum_w[i][j]
            min_cost = min(min_cost, cost_b, cost_w)

    return min_cost


if __name__ == "__main__":
    print(solution())
