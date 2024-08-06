import sys
sys.setrecursionlimit(10**6)

order = 1

def dfs(vertex, visited, R):
    global order
    visited[R] = order
    order += 1

    vertex[R].sort()
    for i in vertex[R]:
        if not visited[i]:
            dfs(vertex, visited, i)

N, M, R = map(int, sys.stdin.readline().split())
vertex = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    vertex[u].append(v)
    vertex[v].append(u)

dfs(vertex, visited, R)

for i in range(1, N+1):
    print(visited[i])
