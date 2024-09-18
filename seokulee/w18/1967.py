import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

def dfs(node, distance):
    global max_distance, farthest_node
    visited[node] = True

    if distance > max_distance:
        max_distance = distance
        farthest_node = node

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, distance + weight)

V = int(sys.stdin.readline())
graph = defaultdict(list)

for i in range(1, V):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [False] * (V + 1)
max_distance = 0
farthest_node = 1
dfs(1, 0)

visited = [False] * (V + 1)
max_distance = 0
dfs(farthest_node, 0)

print(max_distance)
