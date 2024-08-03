import sys
from collections import deque
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x):
    visited[y][x] = True
    q.append((y, x))

    while q:
        (u, v) = q.popleft()
        for i in range(4):
            nx = v + dx[i]
            ny = u + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if vertex[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    vertex[ny][nx] = vertex[u][v] + 1


N, M = map(int, sys.stdin.readline().split())
vertex = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
q = deque()

bfs(0, 0)
print(vertex[N-1][M-1])
