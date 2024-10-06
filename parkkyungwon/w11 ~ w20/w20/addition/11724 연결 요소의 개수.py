def uf(n, edges):
    dp = [-1] * (n+1)

    def union(a, b):
        ra, rb = find(a), find(b)

        if ra == rb: return

        if dp[ra] > dp[rb]:
            dp[ra] += dp[rb]
            dp[rb] = ra
        else:
            dp[rb] += dp[ra]
            dp[ra] = rb
    
    def find(i):
        if dp[i] < 0: return i

        dp[i] = find(dp[i])
        return dp[i]
    
    for e in edges:
        a, b = map(int, e.split())
        union(a, b)

    return sum(map(lambda x: x < 0, dp)) - 1

ss = open(0).read().splitlines()
N = int(ss[0].split()[0])

print(uf(N, ss[1:]))
