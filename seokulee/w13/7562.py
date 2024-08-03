import sys
from collections import deque

sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(current, target, I):
    if current == target:
        return 0

    visited = [[False] * I for _ in range(I)]
    q = deque()
    q.append((current[0], current[1], 0))
    visited[current[1]][current[0]] = True

    while q:
        x, y, count = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and not visited[ny][nx]:
                if (nx, ny) == target:
                    return count + 1

                visited[ny][nx] = True
                q.append((nx, ny, count + 1))

    return -1

for _ in range(T):
    I = int(sys.stdin.readline())
    current = tuple(map(int, sys.stdin.readline().rstrip().split()))
    target = tuple(map(int, sys.stdin.readline().rstrip().split()))

    result = bfs(current, target, I)
    print(result)
