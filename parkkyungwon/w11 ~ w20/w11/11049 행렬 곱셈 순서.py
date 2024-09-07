import sys



readline = sys.stdin.readline
T = int(readline())
arr = tuple(map(int, readline().split()))
arr += tuple(int(readline().split()[1]) for _ in range(T-1))

def sol(arr):
    L = len(arr)
    dp = [[0] * (L) for _ in range(L)]

    for leng in range(2, L):
        for s in range(L-leng):
            e = s + leng
            side = arr[s] * arr[e]
            s1 = s + 1
            dp[s][e] = dp[e][s] = min(side * a + b + c for a, b, c in zip(arr[s1:e], dp[s][s1:e], dp[e][s1:e]))
            
    return dp[0][-1]

print(sol(arr))
