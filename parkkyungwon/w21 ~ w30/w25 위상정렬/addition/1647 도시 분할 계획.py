import sys
from heapq import heappop, heapify



class UnionFind():
    def __init__(self, n):
        self.dp = [-1] * n

    def find(self, i):
        if self.dp[i] < 0: return i

        self.dp[i] = self.find(self.dp[i])

        return self.dp[i]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb: return

        if self.dp[ra] > self.dp[rb]:
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb
        else:
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra


def sol(roads):
    uf = UnionFind(N+1)
    total = 0

    for _ in range(N-2):
        while 1:
            w, a, b = heappop(roads)

            if uf.find(a) != uf.find(b): 
                uf.union(a, b)
                total += w
                break

    return total


readline = sys.stdin.readline
N, M = map(int, readline().split())

roads = [(w, a, b) for a, b, w in (map(int, readline().split()) for _ in range(M))]
heapify(roads)

print(sol(roads))
