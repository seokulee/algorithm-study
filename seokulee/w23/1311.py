import sys

N = int(sys.stdin.readline().rstrip())
job = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

INF = 10 ** 9
dp = [INF] * (1 << N)
dp[0] = 0

bit_counts = [0] * (1 << N)
for i in range(1, 1 << N):
    bit_counts[i] = bit_counts[i >> 1] + (i & 1)


for bitmask in range(1 << N):
    for task in range(N):
        if not (bitmask & (1 << task)):
            next_bitmask = bitmask | (1 << task)
            dp[next_bitmask] = min(dp[next_bitmask], dp[bitmask] + job[bit_counts[bitmask]][task])


print(dp[(1 << N) - 1])
