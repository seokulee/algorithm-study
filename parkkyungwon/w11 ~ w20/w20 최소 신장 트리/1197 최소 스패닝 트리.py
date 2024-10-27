import sys
import heapq


class UnionFind():
    def __init__(self, n):
        self.dp = [-1] * n

    def find(self, i):
        if self.dp[i] < 0: return i

        self.dp[i] = self.find(self.dp[i])

        return self.dp[i]

    def union(self, a, b):
        if a == b: return False

        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        
        if self.dp[ra] < self.dp[rb]: 
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra
        else: 
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb
        
        return True

def sol(heap, n):
    uf = UnionFind(n+1)
    total_cost = 0
    edge_count = n-1

    while 1:
        cost, a, b  = heapq.heappop(heap)

        if uf.union(a, b):
            total_cost += cost
            edge_count -= 1
            
            if not edge_count: break
    
    return total_cost


readline = sys.stdin.readline
N, M = map(int, readline().split())
heap = []

for _ in range(M): 
    a, b, cost = map(int, readline().split())
    heapq.heappush(heap, (cost, a, b))

print(sol(heap, N))
