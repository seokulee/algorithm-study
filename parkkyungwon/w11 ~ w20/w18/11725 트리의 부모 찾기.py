import sys



sys.setrecursionlimit(10**6)


def sol():
    dp = [0] * (N+1)
    dp[1] = 1

    def dfs(i):
        for j in edges[i]:
            if not dp[j]: 
                dp[j] = i
                dfs(j)
    
    dfs(1)
    
    return dp[2:]


readline = sys.stdin.readline
N = int(readline())
edges = [[] for _ in range(N+1)]

for a, b in (map(int, readline().split()) for _ in range(N-1)):
    edges[a].append(b)
    edges[b].append(a)

print(*sol(), sep='\n')
