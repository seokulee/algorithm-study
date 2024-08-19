import sys
import heapq

def dijkstra(start):
    dist = [int(1e9)] * (V + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        w, u = heapq.heappop(q)

        if dist[u] < w:
            continue

        for v, weight in graph[u]:
            if dist[v] > w + weight:
                dist[v] = w + weight
                heapq.heappush(q, (dist[v], v))

    return dist

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    V, E, D = map(int, sys.stdin.readline().split())
    S, G, H = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    candidates = []

    for _ in range(E):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    for _ in range(D):
        t = int(sys.stdin.readline().rstrip())
        candidates.append(t)

    distS = dijkstra(S)
    newS = G if distS[G] > distS[H] else H

    distNewS = dijkstra(newS)
    answer = []
    for d in candidates:
        if distS[newS] + distNewS[d] == distS[d]:
            answer.append(d)

    answer.sort()
    print(*answer)


