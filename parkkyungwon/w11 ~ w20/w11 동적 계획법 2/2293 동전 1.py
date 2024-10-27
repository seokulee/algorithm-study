import sys



readline = sys.stdin.readline
n, k = map(int, readline().split())
coins = [int(readline()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1      

for coin in coins:
    for j in range(coin, k + 1):
        dp[j] += dp[j - coin]

print(dp[k])
