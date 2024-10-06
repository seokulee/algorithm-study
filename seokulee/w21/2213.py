import sys

sys.setrecursionlimit(10**6)

EXCLUDE = 0
INCLUDE = 1

def dfs(currentNode):
    visited[currentNode] = True

    for node in graph[currentNode]:
        if not visited[node]:
            dfs(node)

            if dp[node][EXCLUDE] >= dp[node][INCLUDE]:
                dp[currentNode][EXCLUDE] += dp[node][EXCLUDE]
                path[currentNode][EXCLUDE].extend(path[node][EXCLUDE])
            else:
                dp[currentNode][EXCLUDE] += dp[node][INCLUDE]
                path[currentNode][EXCLUDE].extend(path[node][INCLUDE])

            dp[currentNode][INCLUDE] += dp[node][EXCLUDE]
            path[currentNode][INCLUDE].extend(path[node][EXCLUDE])

    dp[currentNode][INCLUDE] += W[currentNode]

N = int(input())
W = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

dp = [[0, 0] for _ in range(N + 1)]
path = [[[], [i]] for i in range(N + 1)]

visited = [False] * (N + 1)

dfs(1)

if dp[1][INCLUDE] >= dp[1][EXCLUDE]:
    print(dp[1][INCLUDE])
    print(*sorted(path[1][INCLUDE]))
else:
    print(dp[1][EXCLUDE])
    print(*sorted(path[1][EXCLUDE]))
