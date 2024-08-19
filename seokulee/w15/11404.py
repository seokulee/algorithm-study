import sys
INF = int(1e9)

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = [[INF for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

# Using Floyd Warshall
# memory 31120kb
# time 644 ms

for m in range(1, V + 1):
    for s in range(1, V + 1):
        for e in range(1, V + 1):
            if s == e and graph[s][e]:
                graph[s][e] = 0
            graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

for y in range(1, V + 1):
    for x in range(1, V + 1):
        print(graph[y][x] if graph[y][x] != INF else 0, end=' ')
    print()

# Using dijkstra
# memory 42808kb
# time 1276 ms

# def dijkstra(start):
#     dist = [INF] * (V + 1)
#     dist[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))

#     while q:
#         w, u = heapq.heappop(q)

#         if dist[u] < w:
#             continue

#         for v, weight in graph[u]:
#             if dist[v] > w + weight:
#                 dist[v] = w + weight
#                 heapq.heappush(q, (dist[v], v))

#     return dist

# for i in range(1, V + 1):
#     result = dijkstra(i)[1:]
#     answer = ''
#     for n in result:
#         n = 0 if n == INF else n
#         answer += str(n) + ' '
#     print(answer)
