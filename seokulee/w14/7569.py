import sys
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    queue.append((i, j, k))

    while queue:
        x, y, z = queue.popleft()
        for k in range(6):
            nx, ny, nz = x + dx[k], y + dy[k], z + dz[k]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and tomato[nx][ny][nz] == 0:
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                queue.append((nx, ny, nz))



M, N, H = map(int, sys.stdin.readline().rstrip().split())
tomato = [[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)] for _ in range(H)]

bfs()

days = 0
for height in tomato:
    for row in height:
        if 0 in row:
            print(-1)
            exit()
        days = max(days, max(row))

print(days - 1)
