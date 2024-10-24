import sys



def sol(arr):
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N+1)]
    dp[1][1][2] = 1

    for i in range(1, N+1):
        for j in range(1, N):
            if arr[i][j]: continue

            dp[i][j][2] += dp[i][j-1][2] + dp[i][j-1][1]
            dp[i][j][0] += dp[i-1][j][0] + dp[i-1][j][1]

            if not (arr[i-1][j] or arr[i][j-1]):
                dp[i][j][1] += sum(dp[i-1][j-1])
                
    return sum(dp[N][N-1])


readline = sys.stdin.readline
N = int(readline())

arr = [[0] * (N + 1)]
arr += [list(map(int, readline().split())) + [0] for _ in range(N)]

print(sol(arr))
        