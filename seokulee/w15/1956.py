import sys
INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())
graph = [[INF for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for m in range(1, V + 1):
    for s in range(1, V + 1):
        for e in range(1, V + 1):
            if s == e:
                graph[s][e] = 0
                continue
            graph[s][e] = min(graph[s][e], graph[s][m] + graph[m][e])

answer = INF
for s in range(1, V + 1):
    for m in range(1, V + 1):
        if s == m:
            continue
        answer = min(answer, graph[s][m] + graph[m][s])

print(answer if answer < INF else -1)
