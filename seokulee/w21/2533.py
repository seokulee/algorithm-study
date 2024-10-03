import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, parent):
    dp[node][0] = 0
    dp[node][1] = 1

    for child in graph[node]:
        if child != parent:
            dfs(child, node)

            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])


N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    graph[U].append(V)
    graph[V].append(U)

dp = [[0, 0] for _ in range(N + 1)]
visited = [False] * (N + 1)

dfs(1, -1)

print(min(dp[1][0], dp[1][1]))
