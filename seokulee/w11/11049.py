import sys

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N):
    for j in range(N-i):
        x = j
        y = i+j
        dp[x][y] = float('inf')
        for k in range(x, y):
            dp[x][y] = min(dp[x][y], dp[x][k]+dp[k+1][y] + arr[x][0]*arr[k][1]*arr[y][1])

print(dp[0][N-1])
