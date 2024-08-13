import sys
import heapq



def sol(edges, n, s, g, h, candidates):
    # distance에 발견한 가장 작은 값을 저장
    def dijkstra(start):
        distance = [float('inf')] * (n+1)
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
    
    # 시작점에서 다른 점과의 거리, 중간점에서 다른 점과의 거리를 구함
    start_distances = dijkstra(s)
    mid_point = g if start_distances[g] > start_distances[h] else h
    start_mid_diff = start_distances[mid_point]
    middle_distances = dijkstra(mid_point)

    # 목적지 후보를 검사
    # 시작지점에서 목적지까지 거리, 중간지점에서 목적지까지 거리를 사용해서, 최단거리를 이용하는지 확인
    dests = []
    for i in candidates:
        if start_distances[i] != float('inf') and start_distances[i] == (start_mid_diff + middle_distances[i]):
            dests.append(i)

    dests.sort()

    return dests


readline = sys.stdin.readline
num_of_case = int(readline())
for _ in range(num_of_case):
    n, m, t = map(int, readline().split())
    s, g, h = map(int, readline().split())

    edges = {i: {} for i in range(n+1)}
    for a, b, d in (map(int, readline().split()) for _ in range(m)):
        edges[a][b] = d
        edges[b][a] = d

    candiates = tuple(int(readline()) for _ in range(t))

    print(*sol(edges, n, s, g, h, candiates))
    