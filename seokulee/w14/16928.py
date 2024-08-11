import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
visited = [0] * 101
graph = {}

for _ in range(N + M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x] = y

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        x = queue.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx in graph:
                nx = graph[nx]
            if nx == 100:
                return visited[x]
            if 1 <= nx <= 100 and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)

print(bfs())
