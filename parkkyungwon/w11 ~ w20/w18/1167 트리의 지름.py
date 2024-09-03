import sys



sys.setrecursionlimit(10**6)


def sol(edges):
    visited = [False] * (N+1)
    visited[1] = True
    maxi = 0

    def dfs(i):
        nonlocal maxi
        maxi2 = 0

        for j in edges[i]:
            if visited[j]: continue
            visited[j] = True

            child = dfs(j) + edges[i][j]
            a = child + maxi2

            if a > maxi: maxi = a
            if child > maxi2: maxi2 = child

        return maxi2
        
    dfs(1)

    return maxi


readline = sys.stdin.readline
N = int(readline())
edges = [{} for _ in range(N+1)]

for data in (tuple(map(int, readline().split())) for _ in range(N)):
    a = data[0]
    for i in range(1, len(data)-1, 2):
        edges[a][data[i]] = data[i+1]
        edges[data[i]][a] = data[i+1]

print(sol(edges))
