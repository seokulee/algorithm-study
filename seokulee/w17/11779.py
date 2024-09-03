import sys
import heapq


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]


for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


S, E = map(int, sys.stdin.readline().split())


def dijkstra(S, E):
    dist = [float('inf')] * (N + 1)
    dist[S] = 0
    prev = [-1] * (N + 1)

    q = [(0, S)]

    while q:
        current_cost, base = heapq.heappop(q)

        if current_cost > dist[base]:
            continue

        for target, cost in graph[base]:
            new_cost = current_cost + cost
            if new_cost < dist[target]:
                dist[target] = new_cost
                prev[target] = base
                heapq.heappush(q, (new_cost, target))

    path = []
    cursor = E
    while cursor != -1:
        path.append(cursor)
        cursor = prev[cursor]

    return dist[E], path[::-1]


min_cost, path = dijkstra(S, E)


print(min_cost)
print(len(path))
print(*path)
