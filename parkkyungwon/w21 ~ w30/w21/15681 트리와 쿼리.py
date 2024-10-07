import sys



sys.setrecursionlimit(10**6)


def sol(n, root, edges):
    dp = [1] * (n+1)

    def dfs(parent, i):
        for j in edges[i]:
            if j == parent: continue

            dp[i] += dfs(i, j)

        return dp[i]

    dfs(0, root)

    return dp

readline = sys.stdin.readline
N, R, Q = map(int, readline().split())

edges = [[] for _ in range(N+1)]
for a, b in (map(int, readline().split()) for _ in range(N-1)):
    edges[a].append(b)
    edges[b].append(a)

dp = sol(N, R, edges)

print(*(dp[int(readline())] for _ in range(Q)), sep='\n')
