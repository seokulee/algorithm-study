import sys
from heapq import heappop, heappush



def dijkstra(edges, s):
    dp = [None] * (N + 1)
    queue = [(0, s)]

    while queue:
        v, i = heappop(queue)

        if dp[i] != None: continue
        dp[i] = v

        for j in edges[i]:
            if dp[j] != None: continue

            heappush(queue, (edges[i][j] + v, j))

    return dp


def sol(edges, edges_r):
    return max(a + b for a, b in zip(dijkstra(edges, X)[1:], dijkstra(edges_r, X)[1:]))
    

readline = sys.stdin.readline
N, M, X = map(int, readline().split())

edges = [{} for _ in range(N+1)]
edges_r = [{} for _ in range(N+1)]
for i, j, v in (map(int, readline().split()) for _ in range(M)):
    edges[i][j] = v
    edges_r[j][i] = v

print(sol(edges, edges_r))
