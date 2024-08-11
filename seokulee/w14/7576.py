import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))



M, N = map(int, sys.stdin.readline().rstrip().split())
tomato = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

bfs()

days = 0
for row in tomato:
    if 0 in row:
        print(-1)
        exit()
    days = max(days, max(row))

print(days - 1)
