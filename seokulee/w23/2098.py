import sys

N = int(sys.stdin.readline().rstrip())
route = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

INF = 10 ** 9
dp = [[-1] * (1 << N) for _ in range(N)]

def DFS(now, visited):
    if visited == (1 << N) - 1:
        return route[now][0] if route[now][0] else INF

    if dp[now][visited] != -1:
        return dp[now][visited]

    dp[now][visited] = INF

    for next_city in range(1, N):
        if not route[now][next_city] or visited & (1 << next_city):
            continue

        dp[now][visited] = min(dp[now][visited], DFS(next_city, visited | (1 << next_city)) + route[now][next_city])

    return dp[now][visited]

print(DFS(0, 1))
