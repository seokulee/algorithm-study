import sys

N = int(sys.stdin.readline().rstrip())
count = 0

def min_operations_to_one(N: int) -> int:
    dp = [0] * (N + 1)
    path = [0] * (N + 1)
    path[1] = [1]

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        path[i] = path[i - 1] + [i]

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            path[i] = path[i // 2] + [i]

        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            path[i] = path[i // 3] + [i]

    print(dp[N])
    print(*path[N][::-1])

min_operations_to_one(N)
