import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
cost = [[float('inf')] * (N + 1) for _ in range(N + 1)]
path = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    cost[i][i] = 0
    path[i][i] = [0]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    cost[a][b] = min(cost[a][b], c)
    path[a][b] = [a, b]


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]
                path[i][j] = path[i][k] + path[k][j][1:]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(cost[i][j] if cost[i][j] != float('inf') else 0, end=' ')
    print()


for i in range(1, N + 1):
    for j in range(1, N + 1):
        if len(path[i][j]) > 1:
            print(len(path[i][j]), *path[i][j])
        else:
            print(0)
