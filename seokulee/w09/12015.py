import sys
from bisect import bisect_left


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = list()

for i in arr:
    k = bisect_left(dp, int(i))
    if k >= len(dp):
        dp.append(i)
    else:
        dp[k] = i

print(len(dp))
