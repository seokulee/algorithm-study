import sys



def find(arr):
    L = len(arr) - 1
    dp = [[0] * L for _ in range(L)]

    p = [[0] * (L+1) for _ in range(L+1)]
    for s in range(L):
        for e in range(s+1, L+1):
            p[s][e] = arr[s] * arr[e]

    for leng in range(1, L):
        for s in range(L - leng):
            e = s + leng
            dp[s][e] = float('inf')
            for m in range(s, e):
                cost = p[s][e+1] * arr[m+1] + dp[s][m] + dp[m+1][e]
                if dp[s][e] > cost:
                    dp[s][e] = cost
            
    return dp[0][-1]


readline = sys.stdin.readline
T = int(readline())
arr = tuple(map(int, readline().split()))
arr += tuple(int(readline().split()[1]) for _ in range(T-1))

print(find(arr))
