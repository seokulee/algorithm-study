import sys
sys.setrecursionlimit(10**6)

COMPLEX = 0

N = int(sys.stdin.readline())
housemap = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

result = [0]

def dfs(x, y):
    global count
    visited[x][y] = True
    housemap[x][y] = 0
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if housemap[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if housemap[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            result[COMPLEX] += 1
            result.append(count)
            count = 0

result[1:] = sorted(result[1:])
print('\n'.join(map(str, result)))
