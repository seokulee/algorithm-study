import sys
input = sys.stdin.read

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        parents[rootY] = x
        visited[rootX] += visited[rootY]


T = int(sys.stdin.readline())
for _ in range(T):
    F = int(sys.stdin.readline())
    parents = {}
    visited = {}

    for _ in range(F):
        a, b = map(str, sys.stdin.readline().split())

        if a not in parents:
            parents[a] = a
            visited[a] = 1
        if b not in parents:
            parents[b] = b
            visited[b] = 1

        union(a, b)
        print(visited[find(a)])
