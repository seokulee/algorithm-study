import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0, 0, 1, 0))
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    while queue:
        # wall 쓰면 1
        x, y, cnt, wall = queue.popleft()

        if x == N - 1 and y == M - 1:
            return cnt

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][1] = 1
                    queue.append((nx, ny, cnt + 1, 1))
                elif board[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = 1
                    queue.append((nx, ny, cnt + 1, wall))

    return -1

print(bfs())
