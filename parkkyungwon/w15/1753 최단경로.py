import sys
import heapq



def sol(data, v, k):
    edges = tuple([] for _ in range(v+1))
    for d1, d2, d3 in data:
        edges[d1].append((d3, d2))

    # weight에 발견한 가장 작은 값을 저장
    weight = [float('inf')] * (v+1)
    weight[k] = 0
    vertexes = []
    heapq.heappush(vertexes, (0, k))

    while vertexes:
        w1, dest = heapq.heappop(vertexes)

        if w1 > weight[dest]:
            continue

        for w2, neighbor in edges[dest]:
            w2 += w1

            if w2 < weight[neighbor]:
                heapq.heappush(vertexes, (w2, neighbor))
                weight[neighbor] = w2
            
    return map(lambda x: 'INF' if x == float('inf') else x, weight[1:])


readline = sys.stdin.readline
V, E = map(int, readline().split())
K = int(readline())
data = (map(int, readline().split()) for _ in range(E))
print(*sol(data, V, K), sep='\n')
