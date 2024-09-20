import sys
sys.setrecursionlimit(10**9)

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

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, star):
        return ((star.x - self.x) ** 2 + (star.y - self.y) ** 2) ** 0.5


N = int(sys.stdin.readline())
parent = [i for i in range(N + 1)]
stars = []
edges = []

for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    stars.append(Star(x, y))

for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        edges.append((stars[i].distance(stars[j]), i, j))
edges.sort()

answer = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)
