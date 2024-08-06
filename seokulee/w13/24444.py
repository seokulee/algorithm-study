import sys
from collections import deque
sys.setrecursionlimit(10**6)

order = 1
q = deque()

def bfs(vertex, visited, R):
    for v in range(N+1):
        if v != R:
            visited[v] = 0
    global order
    visited[R] = order
    order += 1

    q.append(R)

    while q:
        u = q.popleft()
        vertex[u].sort()
        for v in vertex[u]:
            if not visited[v]:
                visited[v] = order
                order += 1
                q.append(v)

N, M, R = map(int, sys.stdin.readline().split())
vertex = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    vertex[u].append(v)
    vertex[v].append(u)

bfs(vertex, visited, R)

for i in range(1, N+1):
    print(visited[i])
