import sys



sys.setrecursionlimit(10**6+10)


def sol(edges):
    def dfs(parent, cur):
        c1, c2 = 0, 1

        for chi in edges[cur]:
            if chi == parent: continue

            c3, c4 = dfs(cur, chi)

            c1 += c4
            c2 += c3 if c3 < c4 else c4
        
        return c1, c2

    return min(dfs(0, 1))


readline = sys.stdin.readline
N = int(readline())

edges = [[] for _ in range(N+1)]
for a, b in (map(int, readline().split()) for _ in range(N-1)):
    edges[a].append(b)
    edges[b].append(a)

print(sol(edges))
