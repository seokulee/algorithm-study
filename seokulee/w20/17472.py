import sys
from collections import deque

def ordering(y, x, order):
    q = deque()
    q.append((y, x))
    graph[y][x] = order
    visited[y][x] = True

    while q:
        i, j = q.popleft()
        for dy, dx in nd:
            ni, nj = i + dy, j + dx

            if ni < 0 or ni >= N or nj < 0 or nj >= M or not graph[ni][nj] or visited[ni][nj]:
                continue
            graph[ni][nj] = order
            visited[ni][nj] = True
            q.append((ni, nj))


def getDistance(y, x, l):
    q = deque()
    for idx in range(4):
        q.append((y, x, 0, nd[idx]))

    while q:
        i, j, cnt, nowDir = q.popleft()
        if graph[i][j] and graph[i][j] != l:
            if cnt > 2:
                edge.add((cnt - 1, l, graph[i][j]))
            continue
        ni, nj = i + nowDir[0], j + nowDir[1]

        if ni < 0 or ni >= N or nj < 0 or nj >= M or graph[ni][nj] == l:
            continue
        q.append((ni, nj, cnt + 1, nowDir))


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

nd = [(1, 0), (-1, 0), (0, 1), (0, -1)]

edge = set()

order = 1
for i in range(N):
    for j in range(M):
        if graph[i][j] and not visited[i][j]:
            ordering(i, j, order)
            order += 1
parent = [i for i in range(order)]


for i in range(N):
    for j in range(M):
        if graph[i][j]:
            visited = [[False] * M for _ in range(N)]
            getDistance(i, j, graph[i][j])
edge = list(edge)
edge.sort()


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    return x


def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX > rootY:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX


bridge = 0
answer = 0

for c, a, b in edge:
    if find(a) != find(b):
        bridge += 1
        union(a, b)
        answer += c


print(answer if answer != 0 and bridge == order - 2 else -1)
