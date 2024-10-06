def floyd(n, edges):
    n += 1
    dp = [[100] * n for _ in range(n)]

    for a, b in edges:
        dp[a][b], dp[b][a] = 1, 1

    for k in range(1, n):
        for i in range(1, n):
            for j in range(i+1, n):
                w = dp[i][k] + dp[k][j]

                if dp[i][j] > w: 
                    dp[i][j], dp[j][i] = w, w
    
    return min((v, i) for i, v in enumerate(sum(d) for d in dp))[1]


ss = open(0).read().splitlines()
N = int(ss[0].split()[0])

ss = (map(int, s.split()) for s in ss[1:])

print(floyd(N, ss))
