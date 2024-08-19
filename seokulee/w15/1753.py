import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dist = [float('inf')] * (V + 1)
q = []

def dijkstra(start):
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        w, u = heapq.heappop(q)

        print(u, w, dist[u])
        if dist[u] < w:
            continue

        for v, weight in graph[u]:
            if dist[v] > w + weight:
                dist[v] = w + weight
                heapq.heappush(q, (dist[v], v))

    return dist

for d in dijkstra(K)[1:]:
    print(d if d != float('inf') else 'INF')
