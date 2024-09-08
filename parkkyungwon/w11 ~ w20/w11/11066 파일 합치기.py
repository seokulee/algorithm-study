import sys



def find(arr):
    L = len(arr)
    dp = [[0] * L for _ in range(L)]
    sums = [0] * (L + 1)

    for i in range(L):
        sums[i+1] = sums[i] + arr[i]

    for leng in range(1, L):
        for s in range(L - leng):
            e = s + leng
            dp[s][e] = float('inf')
            for m in range(leng):
                dp[s][e] = min(dp[s][e], dp[s][s+m] + dp[s+m+1][e] + sums[e+1] - sums[s])
            
    return dp[0][-1]


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    readline()
    arr = list(map(int, readline().split()))

    sys.stdout.write(str(find(arr)) + '\n')
