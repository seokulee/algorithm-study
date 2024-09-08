import sys



def sol(edges, n):
    distance = [float('inf')] * (n+1)
    distance[1] = 0

    for i in range(n):
        for a in range(1, n+1):
            if distance[a] == float('inf'):
                continue

            for b, w in edges[a]:
                w += distance[a]
                if w < distance[b]:
                    distance[b] = w
                    
                    # 시작 정점을 제외한 정점의 개수는 n-1이고
                    # n-1 번 이상 변화가 발생하면 cycle이 발생
                    if i == n-1:
                        return[-1]
        
    return map(lambda x: -1 if x == float('inf') else x, distance[2:])


readline = sys.stdin.readline
N, M = map(int, readline().split())

edges = tuple([] for i in range(N+1))
for a, b, d in (map(int, readline().split()) for _ in range(M)):
    edges[a].append((b, d))

print(*sol(edges, N), sep='\n')
