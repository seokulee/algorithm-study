import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
dist = [0] * 100_001

def bfs(N):
    q = []
    heapq.heappush(q, (0, N))

    while q:
        d, x = heapq.heappop(q)

        if x == K:
            return d

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100_000 and dist[nx] == 0:
                if nx == 2*x and nx != 0:
                    dist[nx] = dist[x]
                    heapq.heappush(q, (d, nx))
                else:
                    dist[nx] = dist[x] + 1
                    heapq.heappush(q, (d + 1, nx))

print(bfs(N))
