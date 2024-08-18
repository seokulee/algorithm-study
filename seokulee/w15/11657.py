import sys
INF = int(1e9)

def bf(start):
    dist[start] = 0

    for i in range(V):
        for u in range(1, V + 1):
            for v, weight in graph[u]:
                if dist[u] != INF and dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    if i == V - 1:
                        return True
    return False

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

isCycle = bf(1)

if isCycle:
    print(-1)
else:
    for i in range(2, V + 1):
        print(dist[i] if dist[i] != INF else -1)
