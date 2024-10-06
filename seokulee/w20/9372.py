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

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    parent = [i for i in range(N + 1)]

    answer = 0
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if find(a) != find(b):
            union(a, b)
            answer += 1

    print(answer)
