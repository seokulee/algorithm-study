import sys



sys.setrecursionlimit(10**5)


def sol(weights, edges):
    def dfs(parent, cur):
        c1, c2 = 0, weights[cur]

        for chi in edges[cur]:
            if chi == parent: continue

            c3, c4 = dfs(cur, chi)

            c1 += c3 if c3 > c4 else c4
            c2 += c3 
        
        return c1, c2

    return max(dfs(0, 1))


readline = sys.stdin.readline
N = int(readline())

weights = (0,) + tuple(map(int, readline().split()))

edges = [[] for _ in range(N+1)]
for a, b in (map(int, readline().split()) for _ in range(N-1)):
    edges[a].append(b)
    edges[b].append(a)

print(sol(weights, edges))
