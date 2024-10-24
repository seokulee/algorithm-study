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

        if ra == rb: return

        if self.dp[ra] < self.dp[rb]:
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra
        
        else:
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb


def sol(parties):
    uf = UnionFind(N + 1)

    if not parties[0]: return M

    for party in parties:
        if not party: continue

        a = party[0]
        for b in party[1:]:
            uf.union(a, b)

    count = 0    
    a = uf.find(parties[0][0])

    for party in parties[1:]:
        b = uf.find(party[0])

        if a != b: count += 1

    return count


readline = sys.stdin.readline
N, M = map(int, readline().split())
parties = [tuple(map(int, readline().split()[1:])) for _ in range(M+1)]

print(sol(parties))
