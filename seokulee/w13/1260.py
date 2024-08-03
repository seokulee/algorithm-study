import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())
vertex = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
result_dfs = []
result_bfs = []

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    vertex[u].append(v)
    vertex[v].append(u)

def dfs(vertex, visited, R):
    visited[R] = True
    result_dfs.append(R)

    vertex[R].sort()
    for i in vertex[R]:
        if not visited[i]:
            dfs(vertex, visited, i)

q = deque()

def bfs(vertex, visited, R):
    q.append(R)
    visited[R] = True
    result_bfs.append(R)

    while q:
        u = q.popleft()
        vertex[u].sort()
        for v in vertex[u]:
            if not visited[v]:
                visited[v] = True
                result_bfs.append(v)
                q.append(v)

dfs(vertex, visited_dfs, R)
bfs(vertex, visited_bfs, R)

print(' '.join(map(str, result_dfs)))
print(' '.join(map(str, result_bfs)))
