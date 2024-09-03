import sys
import heapq



def sol(edges, v, iv1, iv2):
    # distance에 발견한 가장 작은 값을 저장
    def dijkstra(start):
        distance = [float('inf')] * (v+1)
        distance[start] = 0
        vertexes = []
        # vertexes에 추가할 땐, 거리, 정점, 통과해야하는 정점을 통과한 횟수 순서로 넣는다.
        heapq.heappush(vertexes, (0, start))

        while vertexes:
            w1, dest = heapq.heappop(vertexes)

            if w1 > distance[dest]:
                continue

            for neighbor, w2 in edges[dest].items():
                w2 += w1

                if w2 < distance[neighbor]:
                    heapq.heappush(vertexes, (w2, neighbor))
                    distance[neighbor] = w2
            
        return distance


    # 시작점이 1, iv1, v를 계산하고 답을 구한다.
    s, m, e = dijkstra(1), dijkstra(iv1), dijkstra(v)
    answer = min(s[iv1] + e[iv2], s[iv2] + e[iv1]) + m[iv2]
    answer = -1 if answer == float('inf') else answer

    return answer


readline = sys.stdin.readline
V, E = map(int, readline().split())
edges = tuple(dict() for _ in range(V+1))
for d1, d2, d3 in (map(int, readline().split()) for _ in range(E)):
    edges[d1][d2] = d3
    edges[d2][d1] = d3
iv1, iv2 = map(int, readline().split())
print(sol(edges, V, iv1, iv2))
