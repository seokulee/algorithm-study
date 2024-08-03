import sys
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    visited[y][x] = True
    graph[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(ny, nx)



T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    count = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)
