import sys


def sol(items, edges):
    leng = N + 1
    inf = float('inf')
    dp = [[inf] * (leng) for _ in range(leng)]

    for i in range(leng):
        dp[i][i] = 0

    for i, j, v in edges:
        if dp[i][j] > v and v <= M: 
            dp[i][j], dp[j][i] = v, v

    for k in range(1, leng):
        for i in range(1, leng):
            for j in range(i+1, leng):
                if (v := dp[i][k] + dp[k][j]) < dp[i][j] and v <= M:
                    dp[i][j], dp[j][i] = v, v

    return max(sum(v for i, v in zip(d[1:], items) if i != inf) for d in dp[1:])


readline = sys.stdin.readline
N, M, R = map(int, readline().split())
items = tuple(map(int, readline().split()))
edges = (map(int, readline().split()) for _ in range(R))

print(sol(items, edges))