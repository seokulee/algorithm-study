import sys
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
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

class God:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, God):
        return ((God.x - self.x) ** 2 + (God.y - self.y) ** 2) ** 0.5


N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N)]
gods = []
edges = []


for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    gods.append(God(X, Y))

for i in range(len(gods)):
    for j in range(i + 1, len(gods)):
        edges.append((gods[i].distance(gods[j]), i, j))
edges.sort()

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    union(X - 1, Y - 1)

answer = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(f'{answer:.2f}')
