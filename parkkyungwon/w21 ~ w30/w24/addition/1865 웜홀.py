import sys



def sol(n, edges):
    leng = n+1
    dp = [0] * (leng)
    flags = [True] * (leng)

    for _ in range(n-1):
        for i in range(1, leng):
            if not flags[i]: continue

            flags[i] = False

            for j in edges[i]:
                v = dp[i] + edges[i][j]

                if dp[j] > v:
                    dp[j] = v
                    flags[j] = True
    
    return 'YES' if any(flags[1:]) else 'NO'


readline = sys.stdin.readline
INF = float('inf')
T = int(readline())

for _ in range(T):
    n, m, w = map(int, readline().split())

    edges = [{} for _ in range(n+1)]

    for _ in range(m):
        i, j, v = map(int, readline().split())
        if j in edges[i] and edges[i][j] < v: continue
        edges[i][j], edges[j][i] = v, v

    for _ in range(w):
        i, j, v = map(int, readline().split())
        if j in edges[i] and edges[i][j] < -v: continue
        edges[i][j] = -v
    
    print(sol(n, edges))
