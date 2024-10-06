import sys

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parents[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parents[rootX] = rootY
        else:
            parents[rootY] = rootX
            rank[rootX] += 1

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

parents = [i for i in range(N)]
rank = [0] * N 

for i in range(N):
    connection = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if connection[j]:
            union(i, j)
parents = [-1] + parents

plan = list(map(int, sys.stdin.readline().split()))
start = parents[plan[0]]
for i in range(1, M):
    if parents[plan[i]] != start:
        print("NO")
        break
else:
    print("YES")

