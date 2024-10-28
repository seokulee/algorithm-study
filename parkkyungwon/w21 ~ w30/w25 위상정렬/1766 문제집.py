import sys
from heapq import heappush, heappop



def sol(edges, levels):
    heap = []
    for i, v in enumerate(levels):
        if v: continue

        heappush(heap, i)

    answer = []

    while heap:
        i = heappop(heap)
        answer.append(i)

        for j in edges[i]:
            levels[j] -= 1

            if not levels[j]: heappush(heap, j)
    
    return answer


readline = sys.stdin.readline
N, M = map(int, readline().split())

levels = [0] * (N+1)
levels[0] = -1
edges = [[] for _ in range(N+1)]

for a, b in (map(int, readline().split()) for _ in range(M)):
    edges[a].append(b)
    levels[b] += 1

print(*sol(edges, levels))
