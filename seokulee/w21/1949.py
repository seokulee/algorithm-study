import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(currentNode, parent):
    dp[currentNode][0] = 0
    dp[currentNode][1] = population[currentNode]

    for child in graph[currentNode]:
        if child != parent:
            dfs(child, currentNode)

            dp[currentNode][0] += max(dp[child][0], dp[child][1])
            dp[currentNode][1] += dp[child][0]

N = int(input())
population = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(N + 1)]

dfs(1, -1)

print(max(dp[1][0], dp[1][1]))
