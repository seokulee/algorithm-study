def sol(arr):
    dp = [float('inf')] * (1 << N)
    dp[0] = 0

    for mask in range(1 << N):
        i = bin(mask).count('1')

        for j in range(N):
            jb = 1 << j

            if not mask & jb:
                target = mask | jb
                v = dp[mask] + arr[i][j]

                if dp[target] > v: dp[target] = v

    return dp[-1]


ss = open(0).read().splitlines()
N = int(ss[0])

arr = [tuple(map(int, s.split())) for s in ss[1:]]
del ss

print(sol(arr))
