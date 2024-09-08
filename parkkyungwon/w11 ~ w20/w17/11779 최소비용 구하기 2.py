import sys
import heapq



def sol(edge, n, start, end):
    path = [0] * (n+1)
    dp = [float('inf')] * (n+1)
    dp[start] = 0
    queue = [(0, start)]
    maxi = float('inf')

    # 다익스트라
    while queue:
        w, p = heapq.heappop(queue)

        if w >= maxi or w > dp[p]: continue

        for i in edge[p]:
            w2 = edge[p][i] + w

            if w2 < dp[i]:
                dp[i] = w2
                path[i] = p
                heapq.heappush(queue, (w2, i))

                if i == end: maxi = w2
    
    # 최단 경로 역추적
    i = end
    shor = []
    
    while i:
        shor.append(i)
        i = path[i]

    return dp[end], len(shor), shor[::-1]



readline = sys.stdin.readline
N = int(readline())
M = int(readline())
edge = tuple(dict() for _ in range(N+1))
for a, b, c in (map(int, readline().split()) for _ in range(M)):
    if c < edge[a].get(b, float('inf')):
        edge[a][b] = c

S, E = map(int, readline().split())

cost, leng, shortest_path = sol(edge, N, S, E)

print(cost)
print(leng)
print(*shortest_path)
