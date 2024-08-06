import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
vertex = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    vertex[u].append(v)
    vertex[v].append(u)

count = 0
def dfs(R):
    global count
    visited[R] = 1
    count += 1

    for i in vertex[R]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count - 1 if count > 0 else 0)
