def sol(arr):
    min_dp = next(arr)
    max_dp = min_dp.copy()

    for a in arr:
        left = max_dp[0] if max_dp[0] > max_dp[1] else max_dp[1]
        right = max_dp[1] if max_dp[1] > max_dp[2] else max_dp[2]
        mid = left if left > right else right

        max_dp[0] = left + a[0]
        max_dp[1] = mid + a[1]
        max_dp[2] = right + a[2]

        left = min_dp[0] if min_dp[0] < min_dp[1] else min_dp[1]
        right = min_dp[1] if min_dp[1] < min_dp[2] else min_dp[2]
        mid = left if left < right else right

        min_dp[0] = left + a[0]
        min_dp[1] = mid + a[1]
        min_dp[2] = right + a[2]
    
    return max(max_dp), min(min_dp)


readline = open(0).readline
N = int(readline())
arr = (list(map(int, readline().split())) for _ in range(N))

print(*sol(arr))
