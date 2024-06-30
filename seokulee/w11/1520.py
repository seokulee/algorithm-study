import sys

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    total = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and arr[x][y] > arr[nx][ny]:
            total += dfs(nx, ny)

    dp[x][y] = total

    return dp[x][y]

M, N = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(dfs(0, 0))
