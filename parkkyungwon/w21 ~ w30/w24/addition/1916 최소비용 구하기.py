import heapq
import sys



def sol(start, end, edges):
    visited = [False] * len(edges)
    heap = [(0, start)]

    while 1:
        c, s = heapq.heappop(heap)

        if visited[s]: continue
        if s == end: return c

        for d in edges[s]:
            if visited[d]: continue

            heapq.heappush(heap, (edges[s][d] + c, d))

        visited[s] = True


readline = sys.stdin.readline
N = int(readline())
M = int(readline())

edges = [{} for _ in range(N+1)]
for _ in range(M):
    s, d, c = map(int, readline().split())

    if d not in edges[s] or edges[s][d] > c:
        edges[s][d] = c

start, end = map(int, readline().split())

print(sol(start, end, edges))
