import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
graph = [0] * 100001
prev = [-1] * 100001  # To reconstruct the path

def bfs(N):
    q = deque([N])
    graph[N] = 1  # Mark starting point

    while q:
        x = q.popleft()

        if x == K:
            path = []
            while x != -1:
                path.append(x)
                x = prev[x]
            path.reverse()
            return graph[K] - 1, path

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and not graph[nx]:
                graph[nx] = graph[x] + 1
                prev[nx] = x
                q.append(nx)

d, path = bfs(N)

print(d)
print(*path)
