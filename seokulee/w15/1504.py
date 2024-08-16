import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

stopover1, stopover2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    dist = [float("inf") for _ in range(V + 1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        w, u = heapq.heappop(q)

        if dist[u] < w:
            continue

        for v, weight in graph[u]:
            cost = w + weight

            if dist[v] > cost:
                dist[v] = cost;
                heapq.heappush(q, (cost, v))

    return dist

start_distance = dijkstra(1)
so1_distance = dijkstra(stopover1)
so2_distance = dijkstra(stopover2)

s12e = start_distance[stopover1] + so1_distance[stopover2] +so2_distance[V]
s21e = start_distance[stopover2] + so2_distance[stopover1] +so1_distance[V]

answer = min(s12e, s21e)
print(answer if answer < float('inf') else -1)

