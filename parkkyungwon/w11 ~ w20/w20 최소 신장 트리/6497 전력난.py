import sys


class UnionFind():
    def __init__(self, n):
        self.dp = [-1] * n

    def find(self, i):
        if self.dp[i] < 0: return i

        self.dp[i] = self.find(self.dp[i])

        return self.dp[i]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb: return False
        
        if self.dp[ra] < self.dp[rb]: 
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra
        else: 
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb
        
        return True

    def get_size(self, i):
        return -self.dp[self.find(i)]


def sol(uf, edges, L):
    cost = 0

    for x, y, z in edges:
        if uf.union(x, y): 
            cost += z

            if uf.get_size(0) == L: break
    
    return cost


readline = sys.stdin.readline
while 1:
    M, N = map(int, readline().split())

    if M == 0 and N == 0: break

    uf = UnionFind(M)
    edges = []
    total_cost = 0

    for _ in range(N):
        x, y, z = tuple(map(int, readline().split()))
        edges.append((x, y, z))
        total_cost += z
    
    edges.sort(key=lambda x: x[2])

    print(total_cost - sol(uf, edges, M))
