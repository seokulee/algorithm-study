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

# Kruskal
V, E = map(int, sys.stdin.readline().split())
edges = []
parent = [i for i in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort()

answer = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)
