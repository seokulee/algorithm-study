import sys
sys.setrecursionlimit(10**6)

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
while True:
    m, n = map(int, sys.stdin.readline().split())
    if not m and not n:
        break
    
    parent = [i for i in range(m)]
    edges = []

    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        edges.append((z, x-1, y-1))
    edges.sort()

    answer = 0
    for edge in edges:
        z, x, y = edge
        if find(x) != find(y):
            union(x, y)
        else:
            answer += z


    print(answer)
