import sys

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

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

result = 0
for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        result = i
        break

    union(a, b)

print(result)
