import sys

# n, m = map(int, sys.stdin.readline().split())
# es = {i: {i} for i in range(n + 1)}

# for _ in range(m):
#     o, a, b = map(int, sys.stdin.readline().split())

#     if not o:
#         new_set = es[a].union(es[b])
#         for e in new_set:
#             es[e] = new_set
#     else:
#         print("YES" if es[a] is es[b] else "NO")

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

for _ in range(m):
    o, a, b = map(int, sys.stdin.readline().split())

    if o == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
