from collections import defaultdict



def hungarian(arr):
    dp = [defaultdict(lambda: float('inf')) for _ in range(N)]
    dp[0][1] = 0

    for bitmask in range(1, 1 << N, 2):
        for i in range(N):
            if bitmask not in dp[i]: continue

            for x in range(N):
                bit = 1 << x

                if bitmask & bit or not arr[i][x]: continue

                bit |= bitmask

                if dp[x][bit] > (v := dp[i][bitmask] + arr[i][x]): dp[x][bit] = v
    
    x = (1 << N) - 1

    return min(dp[y][x] + arr[y][0] for y in range(N) if arr[y][0])


ss = open(0).read().splitlines()
N = int(ss[0])
arr = [list(map(int, s.split())) for s in ss[1:]]

del ss

print(hungarian(arr))
