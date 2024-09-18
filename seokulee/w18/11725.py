import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(p):
    for c in graph[p]:
        if not parents[c]:
            parents[c] = p
            dfs(c)

dfs(1)

print(*parents[2:], sep='\n')
